# SOGo Backend Setup #

[TOC]

## Dependencies ##

Install the dependencies needed to build SOGo as superuser:

    $ sudo apt-get install monotone gnustep-make gnustep-base-runtime devscripts \
    debhelper libgnustep-base-dev gobjc libxml2-dev libldap2-dev libssl-dev      \
    zlib1g-dev libmysqlclient-dev libmemcached-dev memcached libpq-dev           \
    libcurl4-openssl-dev

This will pull in postfix, simply select Local only for local mail
only or use Internet site with smarthost if you want to relay mail
through another smtp server. For the purpose of this guide, we will
set it as Local site and configuration Postfix as our SMTP server.

When it comes to enter the system mail name, make sure to select the
FQDN that will match your AD configuration. In our case, we will use
OC for the DOMAIN and oc.local for the REALM, so our System mail name is:
precog.oc.local.


## Source code ##

As the local user, checkout the latest SOGo sources:

    $ git clone git://github.com/inverse-inc/sope
    $ git clone git://github.com/inverse-inc/sogo

### Install SOPE ###

SOPE has to be installed first since SOGo depends on it:

    $ cd sope
    $ ./configure --with-gnustep --enable-debug --enable-strip
    $ make
    $ sudo make install

### Install SOGo ###

<br/>

#### Compile and install SOGo ####

    $ cd sogo
    $ ./configure --enable-debug --disable-strip
    $ make
    $ sudo make install

#### Install SOGo OpenChange plugin ####

    $ cd sogo/OpenChange
    $ make
    $ sudo PKG_CONFIG_PATH=$PKG_CONFIG_PATH make install

## Additional Configuration ##

Run under the user account that will run SOGo server (in our case the
openchange user):

    $ defaults write sogod SOGoTimeZone "Europe/Paris" 
    $ defaults write sogod SOGoProfileURL "postgresql://openchange:openchange@localhost/openchange/sogo_user_profile" 
    $ defaults write sogod OCSFolderInfoURL "postgresql://openchange:openchange@localhost/openchange/sogo_folder_info" 
    $ defaults write sogod OCSSessionsFolderURL "postgresql://openchange:openchange@localhost/openchange/sogo_sessions_folder" 
    $ defaults write sogod SOGoUserSources '({CNFieldName = cn; IDFieldName = uid; UIDFieldName = uid; IMAPHostFieldName =; 
    baseDN = "ou=users,dc=oc,dc=local"; bindDN = "uid=Administrator,ou=users,dc=oc,dc=local"; bindPassword = Administrator; 
    canAuthenticate = YES; displayName = "Shared Addresses"; hostname = "localhost"; id = public; isAddressBook = YES; port = 3389;})'
    $ defaults write sogod WONoDetach YES
    $ defaults write sogod WOLogFile -
    $ defaults write sogod WOPidFile /tmp/sogo.pid

## Give root access to user's GNUstep environment ##

Assuming your local user is named openchange, we will create a symlink
to openchange's GNUstep environment for root. Since samba is run as a
privileged user, so will the sogo code called from OpenChange
server. SOGo backend and server are relying on the same configuration
and so need to be accessible both from openchange and root user:

    # ln -s ~openchange/GNUstep /root/

<br/>
# Postgresql Setup #
<br/>
## Install the dependencies ##

    $ sudo apt-get install postgresql

## Create database and schema ##

Create the database user and schema using the following commands (as superuser)

    # su - postgres
    $ createuser --no-superuser --no-createdb --no-createrole --encrypted --pwprompt openchange
    Enter password for new role: 
    Enter it again: 
    $ createdb -O openchange openchange

## Adjust permissions ##

Adjust the access rights to the database. To do so, modify the
configuration file `/etc/postgresql/9.1/main/pg_hba.conf` in order to
add the following line at the very beginning of the file:

    host     precog     precog    127.0.0.1/32     md5


<br/>
# OpenLDAP Setup #
<br/>

## Install dependencies ##

    $ sudo apt-get install -y slapd ldap-utils
    (Specify openchange as password when asked)

In previous Ubuntu releases (10.04 and below), it was required to
provision the schema (cosine, nis, inetorgperson) and the
backend. Starting with 11.04 Natty, these steps are not mandatory
anymore.


## Provision the frontend ##

Create a file named frontend.ldif:

    dn: ou=users,dc=oc,dc=local
    objectClass: organizationalUnit
    ou: users

    dn: ou=groups,dc=oc,dc=local
    objectClass: organizationalUnit
    ou: groups

Provision the server with the following command as a superuser:

    # ldapadd -x -D cn=admin,dc=oc,dc=local -W -f frontend.ldif
    Enter LDAP Password: 
    adding new entry "ou=users,dc=oc,dc=local"

    adding new entry "ou=groups,dc=oc,dc=local"


## Create additional users ##

Create a file named johndoe.ldif:

    dn: uid=JohnDoe,ou=users,dc=oc,dc=local
    objectClass: top
    objectClass: inetOrgPerson
    objectClass: person
    objectClass: organizationalPerson
    objectClass: posixAccount
    uid: JohnDoe
    cn: JohnDoe Account
    uidNumber: 5000
    gidNumber: 5000
    mail: JohnDoe@oc.local
    sn: JohnDoe
    givenName: JohnDoe
    homeDirectory: /var/mail

Provision the server with this file and set the password to JohnDoe as a superuser:

    # ldapadd -f johndoe.ldif -x -w openchange -D cn=admin,dc=oc,dc=local
    adding new entry "uid=JohnDoe,ou=users,dc=oc,dc=local"
    # ldappasswd -h localhost -x -w openchange -D cn=admin,dc=oc,dc=local uid=JohnDoe,ou=users,dc=oc,dc=local -s JohnDoe

## Create other accounts (Administrator etc.) ##

Follow the same steps than previous section and replace JohnDoe
occurrences with Administrator or any other account name you want to
create.


## Change default LDAP port ##

Finally we need to change default LDAP service port. Samba4 provides
its own LDAP service running on `tcp/389` and if `slapd` service
remains unchanged, it will result in `NT_ALREADY_ASSOCIATED_PORT`
error raised and prevent from using Kerberos service.

In `/etc/default/slapd` file, change `SLAPD_SERVICES` to:

    SLAPD_SERVICES="ldap://localhost:3389 ldapi:///" 

## Restart LDAP server ##

Restart the server to apply changes and ensure it now listens on port `3389/tcp`:

    $ sudo service slapd restart
    * Stopping OpenLDAP slapd                                               [ OK ] 
    * Starting OpenLDAP slapd                                               [ OK ] 

    $ sudo netstat -anp | grep 3389
    tcp        0      0 127.0.0.1:3389          0.0.0.0:*               LISTEN      30795/slapd

<br/>
# Dovecot Setup #

This setup will install and use dovecot with LDAP authentication enabled and deliver support.

## Install dependencies ##

    $ sudo apt-get install dovecot-common dovecot-imapd dovecot-dev dovecot-ldap

## Configure Dovecot ##

Edit `/etc/dovecot/local.conf` to match the following configuration:

    disable_plaintext_auth = no
    log_path = /var/log/dovecot.message
    log_timestamp = "%Y-%m-%d %H:%M:%S " 
    mail_location = maildir:/var/mail/%u
    mail_privileged_group = mail
    passdb {
      args = /etc/dovecot/dovecot-ldap.conf
      driver = ldap
    }
    passdb {
      driver = pam
    }
    protocols = imap
    service auth {
      unix_listener auth-master {
        group = vmail
        mode = 0600
        user = vmail
      }
      unix_listener auth-userdb {
        user = vmail
      }
      user = root
    }
    ssl_cert = </etc/ssl/certs/dovecot.pem
    ssl_key = </etc/ssl/private/dovecot.pem
    userdb {
      args = /etc/dovecot/dovecot-ldap.conf
      driver = ldap
    }
    userdb {
      driver = passwd
    }
    protocol lda {
      hostname = oc.local
      log_path = /var/log/dovecot.message
      postmaster_address = postmaster@oc.local
    }

    protocol pop3 {
      pop3_uidl_format = %08Xu%08Xv
    }

## Configure dovecot LDAP ##

Edit `/etc/dovecot/dovecot-ldap.conf` and match the following configuration:

    uris = ldap://localhost:3389
    dn = cn=admin,dc=oc,dc=local
    dnpass = openchange
    tls = no
    ldap_version = 3
    base = dc=oc,dc=local
    scope = subtree
    user_attrs = homeDirectory=home,uidNumber=uid,gidNumber=gid
    user_filter = (uid=%u)
    pass_attrs = uid=user,userPassword=password
    pass_filter = (uid=%u)

It is also recommended to adjust `DEBUG_LOGIN` variable to 2 and
ensure everything is setup and working properly before resetting it to
0.

    DEBUG_LOGIN=2

## Create the virtual user ##

    # groupadd –g 5000 vmail
    # useradd –m –u 5000 –g 5000 –s /bin/bash –d /var/mail vmail
    # adduser vmail mail
    Adding user `vmail' to group `mail' ...
    Adding user vmail to group mail
    Done.
    # chown -R vmail:vmail /var/mail

## Create maildir directories for LDAP users

    # cd /var/mail
    # mkdir johndoe
    # mkdir -p johndoe/Drafts johndoe/Sent johndoe/Trash
    # ln -s johndoe JohnDoe
    # ln -s johndoe johndoe@oc.local
    # ln -s johndoe JohnDoe@oc.local
    # chown -R vmail:vmail *

## Restart server and test setup ##

    $ sudo service dovecot restart
    dovecot stop/waiting
    dovecot start/running, process 1773

    $ telnet localhost 143
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    * OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE STARTTLS AUTH=PLAIN] Dovecot ready.
    1 LOGIN JohnDoe JohnDoe
    1 OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS MULTIAPPEND UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS] Logged in
    ^]
    
    telnet> quit
    Connection closed.

# Postfix setup #

This will pull in postfix along with postfix-ldap, simply select Local
only for local mail only or use Internet site with smarthost if you
want to relay mail through another smtp server. For the purpose of
this guide, we will set it as Local site and configuration Postfix as
our SMTP server.

When it comes to enter the system mail name, make sure to select the
FQDN that will match your AD configuration. In our case, we will use
oc.local for the DOMAIN and REALM, so our System mail name is:
**precog.oc.local**.

    $ sudo apt-get install postfix-ldap dovecot-postfix

