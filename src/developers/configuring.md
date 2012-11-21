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

### Set PYTHONPATH environment variable ###

You will need to adjust your `PYTHONPATH` variable accordingly to the
common installation prefix you chose for openchange and samba. 

If your prefix is `/usr/local/samba` and your python version is 2.7,
then your openchange and samba python modules will have been installed
into `/usr/local/samba/lib/python-2.7/site-packages/` directory.

    PYTHONPATH=$PYTHONPATH:/usr/local/samba/lib/python-2.7/site-packages

## Configure Samba4 ##

<br/>

### Provision the Server ###

Provision Samba4 server as a domain controller:

    $ sudo PYTHONPATH=$PYTHONPATH /usr/local/samba/bin/samba-tool domain provision \
      --realm=oc.local --domain=OC --adminpass='openchange1!' --server-role='dc'

### Create new user ###

By default the Administrator account is setup, we'll just have to
extend it in OpenChange. However we need to create other users. To
perform this task, use the following command:


    $ sudo PYTHONPATH=$PYTHONPATH /usr/local/samba/bin/samba-tool user add JohnDoe openchange
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

## Configure OpenChange ##

<br/>

### Provision Active Directory with OpenChange schema ###

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

### Create openchangedb database ###

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

### Create OpenChange users ###

    $ sudo PYTHONPATH=$PYTHONPATH ./setup/openchange_newuser --create JohnDoe
    [+] User JohnDoe extended and enabled

Perform the same steps for the Administrator user:

    $ sudo PYTHONPATH=$PYTHONPATH ./setup/openchange_newuser --create Administrator
    [+] User Administrator extended and enabled
