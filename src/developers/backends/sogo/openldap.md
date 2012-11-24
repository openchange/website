# OpenLDAP Setup #

[TOC]

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

# Next: Configuring Dovecot #

Proceed to [Dovecot setup](dovecot.html).