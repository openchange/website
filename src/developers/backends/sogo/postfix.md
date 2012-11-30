# Postfix setup #

[TOC]

## Barebone Postfix server ##

This will pull in postfix along with postfix-ldap, simply select Local
only for local mail only or use Internet site otherwise.

When it comes to enter the system mail name, make sure to select the
FQDN that will match your AD configuration. In our case, we will use
oc.local for the DOMAIN and REALM, so our System mail name is:
**precog.oc.local**.

    $ sudo apt-get install postfix postfix-ldap

## Edit Postfix configuration file ##

If you chose *Local Site* setup, postfix won't bind on all
interfaces. You will need to update the `inet_interfaces` parameter
and change it from `loopback-only` to `all` in
`/etc/postfix/main.cf` file.

We also need to remove `default_transport` and `relay_transport`
default values and replace them with expected dovecot deliver
values. Our final `main.cf` file should looks like the dump
below. Also note that we have adjusted the `virtual_alias_maps`
parameter detailed later.

    smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)
    biff = no
    append_dot_mydomain = no
    readme_directory = no

    # TLS parameters
    smtpd_tls_cert_file = /etc/ssl/certs/ssl-cert-snakeoil.pem
    smtpd_tls_key_file = /etc/ssl/private/ssl-cert-snakeoil.key
    smtpd_use_tls = yes
    smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
    smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

    # See /usr/share/doc/postfix/TLS_README.gz in the postfix-doc package for
    # information on enabling SSL in the smtp client.

    myhostname = precog.oc.local
    alias_maps = hash:/etc/aliases
    alias_database = hash:/etc/aliases
    myorigin = /etc/mailname
    mydestination = precog.oc.local, localhost.oc.local, localhost
    relayhost = 
    mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
    mailbox_size_limit = 0
    recipient_delimiter = +
    inet_interfaces = all 
    relay_transport = ldap:/etc/postfix/people.ldap  
    smtpd_sasl_auth_enable = no
    smtpd_sasl_type = cyrus
    smtpd_sasl_path = smtpd
    smtpd_sasl_authenticated_header = no
    smtpd_sasl_security_options = noanonymous
    smtpd_sasl_local_domain = 
    broken_sasl_auth_clients = no
    smtpd_recipient_restrictions = permit_mynetworks, reject_unauth_destination
    smtpd_sender_restrictions = 
    mailbox_command = 
    smtp_use_tls = no
    smtpd_tls_received_header = no
    smtpd_tls_mandatory_protocols = SSLv3, TLSv1
    smtpd_tls_mandatory_ciphers = medium
    smtpd_tls_auth_only = no
    tls_random_source = dev:/dev/urandom
    
    dovecot_destination_recipient_limit = 1
    virtual_mailbox_domains = oc.local
    virtual_transport = dovecot

## Setting up LDAP configuration ##

We now create the `/etc/postfix/people.ldap` file:

    version = 3
    server_host = localhost
    server_port = 3389
    timeout = 60
    search_base = ou=users,dc=oc,dc=local
    query_filter = (mail=%s)
    result_attribute = uid
    bind = yes
    bind_dn = cn=admin,dc=oc,dc=local
    bind_pw = openchange
    debuglevel = 2

## Setting up delivery method ##

Finally we edit `/etc/postfix/master.cf` and add a dovecot deliver
line:

    dovecot    unix -       n       n       -       -       pipe
       flags=DRhu user=vmail:vmail argv=/usr/lib/dovecot/deliver -d ${user}

## Restart postfix service ##

    # service postfix restart

## Testing messaging services ##

You can either configure your messaging client or you can use the SOGo
web UI. For the purpose of this guide, we will assume that you
followed it thoroughly and followed the [web UI configuration page](webui.html).
<br>

### Run sogod ###

If not already enabled, run `sogod` in one terminal as normal user:

    $ sogod
<br>

### Login onto Web UI ###

- Open a browser and navigate to `${IP_ADDRESS}/SOGo/`.
- Enter your user credentials, here: `JohnDoe`/`JohnDoe` and click
  `Connect` button.
<br>

### Write and Send an email ###

- Click on `Write` button and wait for the popup window to show up
- Starts writing JohnDoe as your `To` recipient and it should
  autocomplete to `JohnDoe Account <JohnDoe@oc.local>`
- Specify a subject, write some contents in the body, then click `Send` button.
<br>

### Test email reception ###

- Click on `Get Mail` button
- Refresh folder if new message doesn't display

<br><br>

# Conclusion #

If you went through all these steps successfully, Congratulations! 

You now have a fully working SOGo installation that OpenChange can use
as a storage backend.