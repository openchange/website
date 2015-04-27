# SOGo Backend Setup #

[TOC]

<div class="alert">
<p>This guide has been written for Ubuntu 12.04.1 LTS. </p>
</div>

## What is SOGo? ##
<br/>
<img border="0" width="96" height="96" style="border: 0pt none; margin: -5px 5px 5px; float: left;" alt="" src="/images/icon_sogo.png" />

SOGo is a groupware server with a focus on scalability and open
standards. SOGo is released under the GNU GPL/LGPL v2 and above.

SOGo provides a rich AJAX-based Web interface and supports multiple
native clients through the use of standard protocols such as `CalDAV`,
`CardDAV` and `GroupDAV`.

Further information available on [SOGo website &raquo;](http://www.sogo.nu).

<div style="clear:both"></div>
<br/>

## Dependencies ##

Install the dependencies needed to build SOGo as superuser:

    sudo apt-get install gnustep-make gnustep-base-runtime devscripts       \
    debhelper libgnustep-base-dev gobjc libxml2-dev libldap2-dev libssl-dev \
    zlib1g-dev libmysqlclient-dev libmemcached-dev memcached libpq-dev      \
    libcurl4-openssl-dev libsbjson-dev libwbxml2-dev

<br/>
## Source code ##

As the local user, checkout the latest SOGo sources:

    git clone git://github.com/inverse-inc/sope
    git clone git://github.com/inverse-inc/sogo

<br/>
### Install SOPE ###

SOPE has to be installed first since SOGo depends on it:

    cd sope
    ./configure --with-gnustep --enable-debug --enable-strip
    make
    sudo make install

<br/>
### Install SOGo ###

<br/>

#### Compile and install SOGo ####

    cd sogo
    ./configure --enable-debug --disable-strip
    make
    sudo make install

#### Install SOGo OpenChange plugin ####

    cd sogo/OpenChange
    make
    sudo PKG_CONFIG_PATH=$PKG_CONFIG_PATH make install

<br/>

## SOGo Configuration ##

This configuration assumes that you have a sogo user created in Samba
which password is _NuzIgtKovyva04in8l02_. This user does not have any
specific attributes and can be created with a regular `samba-tool`
command.

    sudo PYTHONPATH=$PYTHONPATH samba-tool user add sogo 'NuzIgtKovyva04in8l02'
    User 'sogo' created successfully.

The following guide also assume you have followed the cookbook and
your domain is setup to oc.lan. If you have changed this in earlier
part of the configuration, do not forget to update further
configuration bits accordingly.

Adjust the following commands to your environment where relevant and
run them under the user account that will run SOGo server (in our case
the openchange user):

Edit `/etc/sogo/sogo.conf`:

### General parameters ###

    WOPort = 20000;
    WOLogFile = /var/log/sogo/sogo.log;
    WOPidFile = /var/run/sogo/sogo.pid;
    SOGoTimeZone "Europe/Paris"
    SOGoMailDomain = oc.lan;
    SOGoPasswordChangeEnabled = NO;
    SOGoLanguage = English;

### Mail preferences ###

    SOGoAppointmentSendEmailNotifications = YES;
    SOGoACLsSendEMailNotifications = NO;

### Database configuration ###

    SOGoProfileURL "mysql://openchange:openchange@localhost/openchange/sogo_user_profile"
    OCSFolderInfoURL "mysql://openchange:openchange@localhost/openchange/sogo_folder_info"
    OCSSessionsFolderURL "mysql://openchange:openchange@localhost/openchange/sogo_sessions_folder"

### Common IMAP and SMTP configuration ###

    SOGoForceExternalLoginWithEmail = YES;

### IMAP server configuration ###

    NGImap4ConnectionStringSeparator = ".";
    SOGoIMAPAclConformsToIMAPExt = NO;
    SOGoMailSpoolPath = /var/spool/sogo;
    SOGoIMAPServer = 127.0.0.1:143;
    SOGoSieveServer = sieve://127.0.0.1:4190;
    SOGoDraftsFolderName = Drafts;
    SOGoSentFolderName = Sent;
    SOGoTrashFolderName = Trash;
    SOGoMailShowSubscribedFoldersOnly = NO;

### SMTP server configuration ###

    SOGoMailingMechanism = smtp;
    SOGoSMTPServer = 127.0.0.1:25;

### Sieve configuration ###

    SOGoVacationEnabled = YES;
    SOGoSieveScriptsEnabled = YES;
    SOGoForwardEnabled = YES;

### LDAP authentication ###

We are going to use Samba4 Active Directory directly.

    SOGoUserSources =  (
        {
            id = sambaLogin;
            displayName = "SambaLogin";
            canAuthenticate = YES;
            type = ldap;
            CNFieldName = cn;
            IDFieldName = cn;
            UIDFieldName = sAMAccountName;
            hostname = "ldap://127.0.0.1";
            baseDN = "CN=Users,DC=oc,DC=lan";
            bindDN = "CN=sogo,CN=Users,DC=oc,DC=lan";
            bindPassword = "NuzIgtKovyva04in8l02";
            bindFields = (sAMAccountName);
        },
        {
            id = sambaShared;
            displayName = "Shared Addressbook";
            canAuthenticate = NO;
            isAddressBook = YES;
            type = ldap;
            CNFieldName = cn;
            IDFieldName = mail;
            UIDFieldName = mail;
            hostname = "ldap://127.0.0.1";
            baseDN = "DC=oc,DC=lan";
            bindDN = "CN=sogo,CN=Users,DC=oc,DC=lan";
            bindPassword = "NuzIgtKovyva04in8l02";
            filter = "((NOT isCriticalSystemObject='TRUE') AND (mail=\'*\') AND (NOT objectClass=contact))";
        },
        {
            id = sambaContacts;
            displayName = "Shared Contacts";
            canAuthenticate = NO;
            isAddressBook = YES;
            type = ldap;
            CNFieldName = cn;
            IDFieldName = mail;
            UIDFieldName = mail;
            hostname = "ldap://127.0.0.1";
            baseDN = "DC=oc,DC=lan";
            bindDN = "CN=sogo,CN=Users,DC=oc,DC=lan";
            bindPassword = "NuzIgtKovyva04in8l02";
            filter = "((((objectClass=person) AND (objectClass=contact) AND ((uidNumber>=2000) OR (mail='*')))
                     AND (NOT isCriticalSystemObject='TRUE') AND (NOT showInAdvancedViewOnly='TRUE') AND (NOT uid=Guest))
                     OR (((objectClass=group) AND (gidNumber>=2000)) AND (NOT isCriticalSystemObject='TRUE') AND (NOT showInAdvancedViewOnly='TRUE')))";
            mapping = {
                displayname = ("cn");
            };
        }
    );


### Debug options ###

    GCSFolderDebugEnabled = NO;
    GCSFolderStoreDebugEnabled = NO;
    LDAPDebugEnabled = NO;
    MySQL4DebugEnabled = NO;
    NGImap4DisableIMAP4Pooling = NO;
    OCSFolderManagerSQLDebugEnabled = NO;
    PGDebugEnabled = NO;
    SOGoDebugRequests = NO;
    SOGoMailKeepDraftsAfterSend = NO;
    SOGoUIxDebugEnabled = NO;
    SoDebugObjectTraversal = NO;
    SoSecurityManagerDebugEnabled = NO;
    WODontZipResponse = NO;
    WODebugZipResponse = NO;

<br/>
## Give root access to user's GNUstep environment ##

We will create a symlink to openchange's GNUstep environment for root. 
Since samba is run as a privileged user, so will the sogo code called 
from OpenChange server. SOGo backend and server are relying on the same
configuration and so need to be accessible both from openchange and root 
user:

    ln -s ~/GNUstep /root/

<br/>
# Next: Configuring SOGo Web UI #

Your core SOGo installation is completed! Proceed to [SOGo Web UI
setup](webui.html).
