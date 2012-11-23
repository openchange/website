# Initializing a build environment #

The "Getting Started" section describes how to set up your local work
environment. To build the OpenChange source files, you will need to
use Linux.

[TOC]

# Dependencies #

Installing OpenChange and Samba4 from sources requires several
dependencies. You may already have installed some (or all of them) as
part of previous development. However this guide has been written
using fresh installed (and often minimal) Linux
distributions. Installing the list of packages described below ensures
your environment is compliant with OpenChange requirements.

## Ubuntu ##

<br/>
The instructions have been updated and tested with `12.04.1 LTS`.
<br/>

### Compilation tools ###

    $ sudo apt-get install build-essential autoconf ccache pkg-config python python-dev libacl1-dev
    $ sudo apt-get install git flex bison docbook-xsl xsltproc

### OpenChange dependencies ###

    $ sudo apt-get install libpopt-dev libical-dev libmagic-dev libboost-thread-dev zlib1g-dev

### OpenChange documentation tools ###

    $ sudo apt-get install doxygen

## Fedora ##

<br/>

### Compilation Tools ###

    # yum groupinstall "Development Tools" "Legacy Software Development" 
    # yum install ccache python-devel git-all docbook-style-xsl perl-ExtUtils-MakeMaker libacl-devel

### OpenChange dependencies ###

    # yum install popt-devel libical-devel sqlite-devel file-devel boost-thread

### Set environment variable to make boost-thread work ###

    export BOOST_LIB_SUFFIX="-mt" 

**Note**: You may wish to set the `BOOST_LIB_SUFFIX` environment
  variable in your startup scripts (e.g. `~/.bashrc`) instead of
  hand-adding it each time you want to build.

# Setting up a Linux build environment #

OpenChange installs OpenChange and Samba4 binaries and libraries in
non-standard locations, mostly to avoid any potential conflicts with
Samba3 installation which may come by default with the system. While
this is not a requirement for current install, we will anyway set this
up. This requires telling the system and dynamic linker about these
location:

    # Teach ld.so about the non standard location of samba4 libraries
    $ echo '/usr/local/samba/lib' | sudo tee /etc/ld.so.conf.d/samba4.conf
    # update PKG_CONFIG_PATH and PYTHONPATH
    $ echo 'PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/samba/lib/pkgconfig; export PKG_CONFIG_PATH' | sudo tee /etc/profile.d/samba4-env-build.sh
    $ echo 'PYTHONPATH=$PYTHONPATH:/usr/local/samba/lib/python2.7/site-packages;export PYTHONPATH' | sudo tee -a /etc/profile.d/samba4-env-build.sh
    $ . /etc/profile.d/samba4-env-build.sh

# Next: Download the source #

Your build environment is good to go! Proceed to [downloading the source](/developers/downloading.html)
