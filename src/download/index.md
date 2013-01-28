# Download #

[TOC]

## Introduction ##

Users looking for nightly builds packages of OpenChange, Samba4, SOGo,
and openchange-sogo backend can use the repositories from Inverse to
download latest binaries packages.

## Red Hat Enterprise Linux v5 or V6 ##

If you use Red Hat Entreprise Linux 5 (or an equivalent distribution
like CentOS 5), you can install the nightly builds by creating a new
yum configuration file (such as `/etc/yum.repos.d/SOGo.repo`) with the
following content:

### RHEL v5 ###

    [sogo-nightly-rhel5]
    name=Inverse SOGo nightly-build Repository
    baseurl=http://inverse.ca/downloads/SOGo/RHEL5/nightly/$basearch
    gpgcheck=0

### RHEL v6 ###

    [sogo-nightly-rhel6]
    name=Inverse SOGo nightly-build Repository
    baseurl=http://inverse.ca/downloads/SOGo/RHEL6/nightly/$basearch
    gpgcheck=0


Some of the dependencies are provided by RPMForge. Before installing
the packages, install the following package to add RPMForge to your
yum repositories:
[http://dag.wieers.com/rpm/packages/rpmforge-release/](http://dag.wieers.com/rpm/packages/rpmforge-release/)


When you are ready to install OpenChange and its dependencies, run:

    yum clean all && yum makecache
    yum install samba4                  \
                openchange              \
                sogo-openchange-backend \
                openchange-ocsmanager   \
                openchange-rpcproxy     \
                sogo                    

## Debian 6.0 (*Squeeze*) and Ubuntu 12.04 (*Precise Pangolin*) ##

### Debian Squeeze and old Samba ###

Debian Squeeze ships an older version of some libraries required by
Samba 4. In order to workaround this, users of this distribution will
have to use the `squeeze-backports` repository.

To do so, create `/etc/apt/sources.list.d/backports.list`:

    deb http://backports.debian.org/debian-backports squeeze-backports main

Then install the dependencies on Debian Squeeze, do:

    apt-get update
    apt-get install -t squeeze-backports libwbclient-dev   \
                       samba-common smbclient libsmbclient \
                       libsmbclient-dev

To install the packages under Debian *Lenny*, add to your apt source
list (`/etc/apt/sources.list`):

    deb http://inverse.ca/debian lenny lenny

If you prefer using the nightly builds, simply use instead:

    deb http://inverse.ca/debian-nightly lenny lenny

Then, do:

    apt-get update
    apt-get install sogo
    apt-get install samba4
    apt-get install openchangeserver      \
                    sogo-openchange       \
                    openchangeproxy       \
                    openchange-ocsmanager \
                    openchange-rpcproxy

For Debian Squeeze, simply use *squeeze* instead of *lenny*. For
Debian Wheezy, simply use *wheezy* instead of *lenny*.

### Signed packages ###

Since 2011-07-14, the builds are signed.  In order to verify their
signature, our GPG public key has to be added into apt keyring. To do
so, run the following commands:

    sudo apt-key adv --keyserver keys.gnupg.net --recv-key 0x810273C4
    sudo apt-get update

From that point, apt-get should not complain about package signatures anymore.