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

## Provisioning the sample backend ##

Provisioning the sample backend yet require manual operations on the
mysql backend. Fortunately they ar enot very complex and just require
a small set of queries to be executed.

The objective is to create a "SampleFolder" underneath INBOX powered
by the `sample://` backend for the user **julien**.

### Identify the mailbox  and organization identifiers ###

        $ mysql -u openchange -h localhost -p
        mysql> use openchange;
        mysql> select id,ou_id from mailboxes where name="julien";
        +----+-------+
        | id | ou_id |
        +----+-------+
        |  3 |     1 |
        +----+-------+
        1 row in set (0.01 sec)

* mailbox_id = 3
* ou_id = 1

### Identify the parent folder ID ###

Using the mailbox_id retrieved in the previous query:

        mysql> select id from folders where SystemIdx=12 AND mailbox_id=3;
        +----+
        | id |
        +----+
        | 66 |
        +----+
        1 row in set (0.00 sec)


### Inserting the new folder in the table ###

We now have:

* ou_id =  1
* mailbox_id = 3
* parent_folder_id = 66

All other parameters are hardcoded and should not be changed unless you know *exactly* what you are doing.

       mysql> insert into folders (ou_id,folder_id,folder_class,mailbox_id,parent_folder_id,FolderType,SystemIdx,MAPIStoreURI) 
           -> values (1, 1002855686318587905, "system", 3, 66, 1, -1, "sample://deadbeef0000001/");
      
Then retrieve the ID of the created row

       mysql> select MAX(id) from folders;
       +---------+
       | MAX(id) |
       +---------+
       |      86 |
       +---------+

### Customizing folder attributes ###

Using the ID of the created folder, we can now customize the folder name, class and content count

        mysql> insert into folders_properties (folder_id, name, value) values (86, "PidTagDisplayName", "SampleFolder");
        mysql> insert into folders_properties (folder_id, name, value) values (86, "PidTagContainerClass", "IPF.Note");
        mysql> insert into folders_properties (folder_id, name, value) values (86, "PidTagFolderChildCount", "1");

### Index the sample folder and message ###

The sample backend comes with a sample folder and message. It is required to index it into the `mapistore_indexing` table to make it available to Outlook:

        mysql> insert into mapistore_indexing (username, fmid, url, soft_deleted) values ("julien", 1002843665241997313, "sample://deadbeef0000001/dead10010000001/", 0);


## Restart Outlook in Online Mode ##

1. Edit the profile of the user
2. Untick ***Enabled Cached Mode***
3. Click `More Settings` button, go in `Security` tab and tick ***Always prompt for logon credentials***
4. Restart Outlook

You should now have a `SampleFolder` folder showing up in the
hierarchy. This folder should hold a sample folder DEAD-0001 and a
sample message with an attachment.