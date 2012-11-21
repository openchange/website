# Building the Source #

[TOC]

## Building Samba4 ##

Once the environment is set, use the samba target to build and install
samba4. This requires internet access from the host since it either
fetches the source code tarball from the samba web site or GIT
repository. These commands can be run as normal user with sudo
access. The current code in trunk works with latest release and should
also work with latest git revisions unless specified otherwise.

### Use latest Samba4 release ###

    $ make samba
    $ sudo ldconfig

### Use latest Samba4 GIT revision ###

    $ make samba-git
    $ sudo ldconfig

At this stage, we have a working Samba4 environment. 

## Building OpenChange ##

<br/>

### Configure OpenChange ###

Launch the configure script in openchange directory:

    $ ./autogen.sh
    $ ./configure --prefix=/usr/local/samba

You should have an output similar to the following:

    ===============================================================
    OpenChange Configuration (Please review)

           * OpenChange Libraries:
             - libmapi (C library):     yes
                      Thread support:   yes (pthread)
             - libmapi++ (C++ library): yes
             - libmapiadmin:            yes
             - libocpf:                 yes

           * OpenChange Server:
             - mapiproxy:               yes

           * OpenChange mapistore backends:
             - backends dependencies goes here

           * OpenChange Tools:
             - openchangeclient:        yes
             - mapiprofile:             yes
             - openchangepfadmin:       yes
             - exchange2mbox:           yes
             - exchange2ical:           yes
             - mapitest:                yes
             - openchangemapidump:      yes
             - schemaIDGUID:            yes

           * subunit format (mapitest): no

           * OpenChange Documentation:  yes

           * Coverage Tests:            no

           * OpenChange Bindings:
             - Python:                  no
             - Qt4:                     no

           * Installation prefix:       /usr/local/samba

    ===============================================================

### Compile OpenChange ###

Compile and install OpenChange

    $ make
    $ sudo make install
    $ sudo ldconfig


## Next: Configure the Server ##

Your minimal build environment is now ready! Proceed to [Configuring
the Server](/developers/configuring.html)