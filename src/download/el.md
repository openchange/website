# Red Hat Enterprise Linux v5 or V6 #

Users looking for nightly builds packages of OpenChange, Samba4, SOGo,
and openchange-sogo backend can use the repositories kindly made
available by Inverse to download latest binaries packages.

If you use Red Hat Entreprise Linux 5 (or an equivalent distribution
like CentOS 5), you can install the nightly builds by creating a new
yum configuration file (such as `/etc/yum.repos.d/SOGo.repo`) with the
following content:

## RHEL v5 ##

    [sogo-nightly-rhel5]
    name=Inverse SOGo nightly-build Repository
    baseurl=http://inverse.ca/downloads/SOGo/RHEL5/nightly/$basearch
    gpgcheck=0

## RHEL v6 ##

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