# Debian 6.0 (*Squeeze*) and Ubuntu 12.04 (*Precise Pangolin*) #

Users looking for nightly builds packages of OpenChange, Samba4, SOGo,
and openchange-sogo backend can use the repositories kindly made
available by Inverse to download latest binaries packages.

## Debian Squeeze and old Samba ##

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

## Signed packages ##

Since 2011-07-14, the builds are signed.  In order to verify their
signature, Inverse GPG public key has to be added into apt keyring. To do
so, run the following commands:

    sudo apt-key adv --keyserver keys.gnupg.net --recv-key 0x810273C4
    sudo apt-get update

From that point, apt-get should not complain about package signatures
anymore