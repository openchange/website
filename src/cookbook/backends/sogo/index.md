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

    $ sudo apt-get install gnustep-make gnustep-base-runtime devscripts     \
    debhelper libgnustep-base-dev gobjc libxml2-dev libldap2-dev libssl-dev \
    zlib1g-dev libmysqlclient-dev libmemcached-dev memcached libpq-dev      \
    libcurl4-openssl-dev

<br/>
## Source code ##

As the local user, checkout the latest SOGo sources:

    $ git clone git://github.com/inverse-inc/sope
    $ git clone git://github.com/inverse-inc/sogo

<br/>
### Install SOPE ###

SOPE has to be installed first since SOGo depends on it:

    $ cd sope
    $ ./configure --with-gnustep --enable-debug --enable-strip
    $ make
    $ sudo make install

<br/>
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

<br/>
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

<br/>
## Give root access to user's GNUstep environment ##

Assuming your local user is named openchange, we will create a symlink
to openchange's GNUstep environment for root. Since samba is run as a
privileged user, so will the sogo code called from OpenChange
server. SOGo backend and server are relying on the same configuration
and so need to be accessible both from openchange and root user:

    # ln -s ~openchange/GNUstep /root/

<br/>
# Next: Configuring SOGo Web UI #

Your core SOGo installation is completed! Proceed to [SOGo Web UI
setup](webui.html).
