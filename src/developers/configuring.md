# Configuring the Server #

[TOC]

## Introduction ##

For the purpose of this documentation, arbitrary domain (`OC`) and
realm (`OC.LOCAL`) and passwords (`adminpass` and `user password`)
have been chosen. Feel free to adjust values to match your
requirements.

However, when configuring the domain name during OS installation, it
is very important **NOT** to choose a realm which length is more or
equal to 15 characters. This is a limit on Windows domain side which
may result in connectivity issues.

## Set PYTHONPATH environment variable ##

You will need to adjust your `PYTHONPATH` variable accordingly to your
python version and to the common installation prefix you chose for
openchange and samba.

If your prefix is `/usr/local/samba` and your python version is `2.7`,
then your openchange and samba python modules will have been installed
into `/usr/local/samba/lib/python2.7/site-packages/` directory.

    PYTHONPATH=$PYTHONPATH:/usr/local/samba/lib/python2.7/site-packages

<br>
# Configure Samba4 #

<br>

OpenChange can be used with different Samba4 setups depending on
infrastructure needs and availability. You can either use the Samba4
internal DNS server or use bind9 with `DLZ` is supported and enabled.

<div class="alert"> <p>If you are unsure or don't know what it means,
follow the internal DNS server setup subsection below.</p> </div>

## Configuration 1: Samba4 with internal DNS server ##
<br>
### Provision the Server ###

Provision Samba4 server as a domain controller.

    $ sudo PYTHONPATH=$PYTHONPATH /usr/local/samba/bin/samba-tool domain provision \
      --realm=oc.local --domain=OC --adminpass='openchange1!' --server-role='dc'

### Create new user ###

By default the Administrator account is setup, we'll just have to
extend it in OpenChange. However we need to create other users. To
perform this task, use the following command:


    $ sudo PYTHONPATH=$PYTHONPATH /usr/local/samba/bin/samba-tool user add JohnDoe 'openchange2!'
    User 'JohnDoe' created successfully

### Edit Samba configuration ###

For OpenChange server to run properly, we need to edit Samba
`smb.conf` configuration file. In this guide, `smb.conf` is located at
`/usr/local/samba/etc/smb.conf`.

Add the following lines within the `[global]` section of the file:

	### Configuration required by OpenChange server ###
	dcerpc endpoint servers = epmapper, mapiproxy
	dcerpc_mapiproxy:server = true
	dcerpc_mapiproxy:interfaces = exchange_emsmdb, exchange_nsp, exchange_ds_rfr
	### Configuration required by OpenChange server ###


### Configure DNS server ###

As of early September 2012, Samba4 internal DNS server is fully
functional, for both GSS-TSIG-signed and unsigned updates.

To enable the internal DNS server, edit your `smb.conf` file and add
**dnsserver** to the list of `dcerpc endpoint servers`:

    dcerpc endpoint servers = epmapper, mapiproxy, dnsserver

<br>
## Configuration 2: Samba4 with Bind9 DNS server ##

We assume here that you already have a named server installed and
running properly with DLZ support enabled. If not, you can still
generate DNS zone flat files for your bind9 server.

### Provision the Server ###

Provision Samba4 as a domain controller with bind9 DLZ support.

    $ sudo PYTHONPATH=$PYTHONPATH /usr/local/samba/bin/samba-tool domain provision \
      --realm=oc.local --domain=OC --adminpass='openchange1!' --server-role='dc'   \
      --dna-backend=BIND9_DLZ

### Setup apparmor ###

You first need to create or edit `/etc/apparmor.d/usr.sbin.named` file
as priviledged user, then add the following Samba4 records to the file
- assumng your installation prefix is `/usr/local/samba/`

     /usr/local/samba/lib/bind9/dlz_bind9.so mr,
     /usr/local/samba/private/dns/sam.ldb.d/** k,
     /usr/local/samba/private/dns/** kw,
     /usr/local/samba/private/** rw,
     /usr/local/samba/modules/ldb/* m,
     /usr/local/samba/lib/** mr,
     /usr/local/samba/** r,

### Setup Bind9 folder permissions ###

    $ sudo chown -R root:bind /usr/local/samba/private/
    $ sudo chown bind:bind /usr/local/samba/private/dns
    $ sudo chgrp bind /usr/local/samba/private/dns.keytab
    $ sudo chmod g+x /usr/local/samba/private/dns.keytab
    $ sudo chmod 755 /usr/local/samba/private/dns

### Edit Bind9 configuration ###
<br>
#### named.conf ####

Edit `/etc/bind/named.conf` and append at the end of the file:

    include "/usr/local/samba/private/named.conf";

#### named.conf.options ####

Edit `/etc/bind/named.conf.options` and add to the options:

    tkey-gssapi-keytab "/usr/local/samba/private/dns.keytab";

### Restart services ###

Restart apparmor, then bind9:

    $ sudo /etc/init.d/apparmor restart
    $ sudo /etc/init.d/bind9 restart


<br>
# Configure OpenChange #

<br/>

## Provision Active Directory with OpenChange schema ##

From master trunk directory run:

    $ sudo PYTHONPATH=$PYTHONPATH ./setup/openchange_provision
    NOTE: This operation can take several minutes
    [+] Step 1: Register Exchange OIDs
    [+] Step 2: Add Exchange attributes to Samba schema
    [+] Step 3: Add Exchange auxiliary classes to Samba schema
    [+] Step 4: Add Exchange objectCategory to Samba schema
    [+] Step 5: Add Exchange containers to Samba schema
    [+] Step 6: Add Exchange *sub* containers to Samba schema
    [+] Step 7: Add Exchange CfgProtocol subcontainers to Samba schema
    [+] Step 8: Add Exchange mailGateway subcontainers to Samba schema
    [+] Step 9: Add Exchange classes to Samba schema
    [+] Step 10: Add possSuperior attributes to Exchange classes
    [+] Step 11: Extend existing Samba classes and attributes
    [+] Step 12: Exchange Samba with Exchange configuration objects
    [+] Step 13: Finalize Exchange configuration objects
    [SUCCESS] Done!

## Create openchangedb database ##

OpenChange indexes user mailbox folder hierarchy within a dedicated
database different from Samba4 active directory. Provision this
database with following command:

    $ sudo PYTHONPATH=$PYTHONPATH ./setup/openchange_provision --openchangedb
    Setting up openchange db
    Adding root DSE
    [+] Public Folders
    ===================
	    * Public Folder Root                      : 0x0100000000000001 (72057594037927937)
	    * IPM_SUBTREE                             : 0x0200000000000001 (144115188075855873)
	    * NON_IPM_SUBTREE                         : 0x0300000000000001 (216172782113783809)
	    * EFORMS REGISTRY                         : 0x0400000000000001 (288230376151711745)
	    * OFFLINE ADDRESS BOOK                    : 0x0500000000000001 (360287970189639681)
	    * /o=First Organization/cn=addrlists/cn=oabs/cn=Default Offline Address Book: 0x0600000000000001 (432345564227567617)
	    * SCHEDULE+ FREE BUSY                     : 0x0700000000000001 (504403158265495553)
	    * EX:/o=first organization/ou=first administrative group: 0x0800000000000001 (576460752303423489)
	    * Events Root                             : 0x0900000000000001 (648518346341351425)

## Create OpenChange users ##

    $ sudo PYTHONPATH=$PYTHONPATH ./setup/openchange_newuser --create JohnDoe
    [+] User JohnDoe extended and enabled

Perform the same steps for the Administrator user:

    $ sudo PYTHONPATH=$PYTHONPATH ./setup/openchange_newuser --create Administrator
    [+] User Administrator extended and enabled

# Testing server connectivity #

At this stage you have a working but limited OpenChange server. In
fact we have not yet configured any backend, so we can't access one's
user mailbox. However, it is already possible to test server's
connectivity, MAPI profile creation and ensure setup is OK and
working.

## Starting Samba server ##

In one terminal, execute samba daemon to run interactively and within
a single process

    $ sudo PYTHONPATH=$PYTHONPATH /usr/local/samba/sbin/samba -d3 -i -M single

The sample output of this command is [available
here](/developers/configuration/output-samba-4.0.0-rc5.html).

If OpenChange started correctly, the following content should be
available in your server's output:

    42.    DCERPC endpoint server 'epmapper' registered

    [...]

    57.    DCERPC endpoint server 'dnsserver' registered
    58.    DCERPC endpoint server 'exchange_emsmdb' registered
    59.    DCERPC endpoint server 'exchange_nsp' registered
    60.    DCERPC endpoint server 'exchange_ds_rfr' registered
    61.    DCERPC endpoint server 'mapiproxy' registered

    [...]

    66.    MAPIPROXY server 'exchange_ds_rfr' registered
    67.    MAPIPROXY server 'exchange_nsp' registered
    68.    MAPIPROXY server 'exchange_emsmdb' registered
    69.    MAPIPROXY server mode enabled
    70.    MAPIPROXY proxy mode disabled
    71.    mapiproxy_server_load 'exchange_nsp' (OpenChange NSPI server)
    72.    dcesrv_exchange_nsp_init
    73.    mapiproxy_server_load 'exchange_emsmdb' (OpenChange EMSMDB server)
    74.    mapiproxy_server_load 'exchange_ds_rfr' (OpenChange RFR server)

## Setting up DNS resolution ##

On your Linux machine, adjust your `resolv.conf` file to point to
Samba4 internal DNS server:

    $ cat /etc/resolv.conf
    search oc.local
    nameserver 192.168.102.48

In current example:

Variable | Value
-------- | -----
`realm`  | `oc.local`
`domain` | `OC`
`IP`     | `192.168.102.48`

While **samba is running**, ensure DNS resolution is working properly
by running nslookup commands:

First on chosen `realm`:

    $ nslookup oc.local
    Server:             192.168.102.48
    Address:            192.168.102.48#53

    Name:   oc.local
    Address: 192.168.102.48

Next on server's hostname:

    $ nslookup precog
    Server:             192.168.102.48
    Address:            192.168.102.48#53

    Name:   precog.oc.local
    Address: 192.168.102.48


## Setting up mapiprofile ##

<br/>

### Creating the profile ###

`mapiprofile` is a command line tool designed to provide
administrative support for OpenChange MAPI profiles. 

A profile in this context represents a single user's connection to a
server. It can be thought of as a user's account information stored on
the client side. Most OpenChange utilities make use of the profile
information stored in the local profile database, often by referring
to the name of the profile.

We are now creating a MAPI profile for `JohnDoe` user. `mapiprofile`
requires several arguments to be set up to start creating a profile:

Command       | Description
------------- | -----------
`--create`    | MAPI profile creation operation
`-P testing`  | Create a profile named *testing*
`-S`          | Make this profile the default one
`-I`	      | Specify openchange server IP address
`--domain`    | Specify openchange domain
`--realm`     | Specify openchange realm
`--username`  | Specify OpenChange username
`--password`  | Specify OpenChange user's password


    $ /usr/local/samba/bin/mapiprofile --create -P testing -S   \
    -I 192.168.102.48 --domain=OC --realm=oc.local              \
    --username=JohnDoe --password='openchange2!' 
    Profile default completed and added to database /home/openchange/.openchange/profiles.ldb
    Profile default is now set the default one

The server side output matching the command above is [available here](/developers/configuration/output-openchangeserver-profile.html).

### Listing profiles ###

The profile is now available within mapiprofile's list:

    $ /usr/local/samba/bin/mapiprofile --list
    We have 1 profile in the database:
	  Profile = testing [default]

### Dumping profiles ###

Profile information can be dumped using the command below:

    $ /usr/local/samba/bin/mapiprofile --dump -P testing
    Profile: testing
	exchange server == exchange 2000
	encryption      == no
	username        == JohnDoe
	password        == openchange2!
	mailbox         == /o=First Organization/ou=First Administrative Group/cn=Recipients/cn=JohnDoe
	workstation     == precog
	domain          == OC
	server          == 192.168.102.48

# Next: Setting the Backends #

OpenChange server up and running! It is now time to choose, install
and configure backends and their dependencies. Proceed to [deploying
the backends](/developers/backends/index.html)
