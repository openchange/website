# Howto Setup an OpenChange developer environment in Zentyal #

[TOC]

## Purpose and Scope ##

This document describes how to setup a developer environment of
OpenChange on a configured Zentyal server and to leverage an already
configured system to run latest master git revision.

The version of Zentyal server deployed in this document is a 4.0 daily
build. The distribution was configured to run as an OpenChange server
and is fully functional.

The development branch selected for this documentation is
`jkerihuel/mapistore_python` which is also the branch where the
Python-C MAPIStore gateway work is happening and where you can test
the sample backend.

<div class="alert"> <p>You MUST create the OpenChange user and log
into its mailbox once with Outlook prior following this guide.</p>
</div>

## Get OpenChange ##

### Install dependencies ###

        sudo apt-get install build-essential autoconf automake ccache pkg-config python python-dev \
        libacl1-dev git flex bison docbook-xsl xsltproc libpopt-dev libical-dev libmagic-dev       \
        libboost-thread-dev zlib1g-dev libmysqlclient-dev samba-dev libtevent-dev python-dateutil

### Fetch OpenChange code  ###

        git clone https://github.com/openchange/openchange
        cd openchange
        git fetch origin
        git checkout --track origin/jkerihuel/mapistore-python-DEMO


### Compile and Install OpenChange ###

The main difference with the cookbook is the `configure` part which
installs openchange in different prefixes depending on the component.

        ./autogen.sh

        LDFLAGS=-Wl,--as-needed ./configure  --prefix=/usr --mandir=/usr/share/man                 \
        --with-modulesdir=/usr/lib/x86_64-linux-gnu/openchange --libdir=/usr/lib/x86_64-linux-gnu; \
        sed -i -e 's/site-packages/dist-packages/' config.mk

        make
        sudo make install

        sudo ldconfig
        sudo cp mapiproxy/libmapistore/backends/python/sample.py /usr/lib/python2.7/dist-packages/openchange/backends/
        sudo service zentyal samba restart

## Get SOGo ##

The mapistore-python-DEMO (and mapistore-python) branches are using an
updated version of the mapistore library ABI and require to compile a
specific version.

### Install dependencies ###

        sudo apt-get install gnustep-make gnustep-base-runtime devscripts       \
        debhelper libgnustep-base-dev gobjc libxml2-dev libldap2-dev libssl-dev \
        zlib1g-dev libmysqlclient-dev libmemcached-dev memcached libpq-dev      \
        libcurl4-openssl-dev libsbjson-dev libwbxml2-dev libsope-dev

### Fetch SOGo code ###

        git clone https://github.com/Zentyal/sogo
        cd sogo
        git fetch origin
        git checkout --track origin/jkerihuel/mapistore-python

### Compile and Install SOGo ###

        ./configure --enable-debug --disable-strip --prefix=/usr/System
        make
        sudo make install

## Feature of the sample backend ##

The sample backend is provisioned with static and fake data and only
provide a volatile state, effective as long as the server is running.

The set of data the backend provide are:

### SampleMail ###

This is a mail folder with one email item. This email item has an
attachment which content is set to:

      <html><head></head><h1>Attach me</h1></body></html>

The SampleMail folder also holds a subfolder named DEAD-1001

### SampleCalendar ###

This is a calendar folder with:

1. one floating single-instance appointment which starts at current
time (server) and ends one hour later. If the event does not show up
in the day view or if the date sounds incorrect, ensure the date is
properly synchronized.

## Provisioning the sample backend ##

The sample backend comes with an embedded setup script to manage
provisioning and deprovisioning of backend data into openchange
database.

      sudo python ./mapiproxy/libmapistore/backends/python/sample.py --help
      Usage: sample.py [options]

      Options:
        -h, --help            show this help message and exit
        --status              Status of sample backend for specified user
        --provision           Provision sample backend for specified user
        --deprovision         Deprovision sample backend for specified user
        --username=USERNAME   User mailbox to update
      
        Samba Common Options:
          -s FILE, --configfile=FILE
                              Configuration file
          -d DEBUGLEVEL, --debuglevel=DEBUGLEVEL
                              debug level
          --option=OPTION     set smb.conf option from command line
          --realm=REALM       set the realm name

If you are using Zentyal, `/etc/samba/openchange.conf` is not world
readable and require root privileges.

### The status command ###

This command gives you the status of the `sample://` backend for
specified user. If the backend has been provisioned, the status will
output the list of sample folders along with their identifier.

      sudo python /usr/lib/python2.7/dist-packages/openchange/backends/sample.py -d0 --status --username=julien
      [PYTHON]: sample backend class __init__
      [INFO] Sample backend is provisioned for user julien the following folders:
	      * SampleMail                               (sample://deadbeef0000001/)
	      * SampleCalendar                           (sample://cacabeef0000001/)

If the user has not been provisioned, the tool will output something similar to:

      [PYTHON]: sample backend class __init__
      [INFO] Sample backend is not provisioned for user julien

### The provision command ###

This command will index all the root folder of the sample backend into
openchange database for the specified user:

      sudo python /usr/lib/python2.7/dist-packages/openchange/backends/sample.py -d0 --provision --username=julien
      [PYTHON]: sample backend class __init__
      [PYTHON]: sample backend.list_contexts(): username = julien
      [PYTHON]: sample backend.create_context: uri = sample://deadbeef0000001/
      [PYTHON]: sample context class __init__
      [PYTHON]: sample context.get_root_folder
      [PYTHON]: sample folder.__init__(fid=1002855686318587905)
      [PYTHON]: sample folder.get_properties()
      None
      [PYTHON]: sample backend.create_context: uri = sample://cacabeef0000001/
      [PYTHON]: sample context class __init__
      [PYTHON]: sample context.get_root_folder
      [PYTHON]: sample folder.__init__(fid=913293867166466049)
      [PYTHON]: sample folder.get_properties()
      None
      [DONE]

If openchange database has already been provisioned for the specified
user and you still issue this command, an output similar to the one
below will be displayed:

      [PYTHON]: sample backend class __init__
      [WARN] Sample backend is already provisioned for user julien

### The deprovision command ###

This command will remove any references to the sample backend into the
openchange database for the specified user. In addition to this
behavior, every sample backend messages and folders of **every** user
will be deleted from the indexing database:

      sudo python /usr/lib/python2.7/dist-packages/openchange/backends/sample.py -d0 --deprovision --username=julien
      [PYTHON]: sample backend class __init__
      [DONE]

If the account has already been deprovisioned for the specified user
and you still issue this command, an output similar to the one below
will be displayed:

      [PYTHON]: sample backend class __init__
      [WARN] Sample backend is not provisioned for user julien


## Restart Outlook in Online Mode ##

1. Edit the profile of the user
2. Untick ***Enabled Cached Mode***
3. Click `More Settings` button, go in `Security` tab and tick ***Always prompt for logon credentials***
4. Restart Outlook

You should now have a `SampleFolder` folder showing up in the
hierarchy. This folder should hold a sample folder DEAD-0001 and a
sample message with an attachment.