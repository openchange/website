# Dovecot Setup #

[TOC]

This setup will install and use dovecot with LDAP authentication
enabled and deliver support.

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

## Adjust `dovecot.message` permissions ##

This will be required so that postfix can use dovecot delivery method.

    # chown vmail:mail /var/log/dovecot.message

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

# Next: Configuring Postfix #

Proceed to [Postfix setup](postfix.html).