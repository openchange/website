# Howto Setup OpenChange Server on CentOS 6.5 #

[TOC]

## Purpose and Scope ##

A while ago, I promised some instructions on building OpenChange on CentOS.

- Two approaches have been tried. Firstly, install openchange on top of
CentOS samba4 packages and secondly install openchange/samba4 from
scratch in a minimal environment.

- The first approach (install openchange on top of samba4 packaged for
CentOS) has been a failure. It was caused by missing libraries in the
devel RPM packages preventing OpenChange server from compiling properly.
The best solution shall probably to inspect the RPM spec files and
include missing libraries but I did not have time for this.

- The second approach (install samba4/openchange couple from scratch)
has been a success and the following section only focuses on different
instruction/requirements needed to get it working.

- This HowTo only focuses on samba4/openchange deployment. If you have
been building SOGo on CentOS and want to contribute to openchange
documentation, send your pull requests to openchange/website.git
repository on GitHub. Any help you can provide in making CentOS users
life easier with OpenChange will be welcomed!


## Environment ##

For this test, I have been deploying CentOS 6.5 on a x86_64
architecture. The distribution was set as a minimal server.


## Instructions ##


### Install Samba4 requirements ###

        yum install git autoconf automake gcc python-devel popt-devel libacl-devel

### Patch OpenChange samba4 build script ###

<div class="alert"><p>This problematic has been fixed in OpenChange
version GIT and versions released after March 2014.</p></div>

When OpenChange build script defines pythondir, it computes the result
of `sysconfig.get_python_lib()` function and defines platform_specific as
False. However, it sounds like Samba4 python bindings are installed in a
patform_specific location. If prefix is `/usr/local/samba`, then bindings
on CentOS will be installed in
`/usr/local/samba/lib64/python2.6/site-packages` while the scripts expects
them to be in `/usr/local/samba/lib/python2.6/site-packages`. The
following command will fix samba4 compilation.

         $ sed s/get_python_lib\(0,0/get_python_lib\(1,0/g -i script/installsamba4.sh


### Install Samba ###

         $ make samba


### Update dynamic linker ###

Update ld with non-standard path where we installed samba:

         # echo '/usr/local/samba/lib' > /etc/ld.so.conf.d/samba4.conf
         # echo '/usr/local/samba/lib64' >> /etc/ld.so.conf.d/samba4.conf
         # ldconfig

### Install OpenChange requirements ###

         # yum install flex bison zlib-devel file-devel libical-devel


Any other instructions from the cookbook should apply here - OpenChange
compilation, server configuration etc.

