<div style="float: right; width: 45%;margin-left:2em;">
<img src="/images/mapiproxy/mapiproxy.png" alt="MAPIProxy Logo"/>
</div>

# Frequently Asked Questions #

[TOC]

<br/><br/>

## The action could not be completed ##

![MAPIProxy Error 001](/images/mapiproxy/mapiproxy_error_001.png "Figure 13. Outlook error: The action could not be completed")

If you have followed the [5-Minute Configuration](install-config.html)
instructions and the above error message box (Figure 13) is displayed
each time you click the `Check Name` button, then you need to:

* Click on **More Settings**
* Open the security Tab
* Tick the **Always prompt for username and password** checkbox in the
  User Configuration section (Figure 14)

<br>

![MAPIProxy fix 001](/images/mapiproxy/mapiproxy_error_001_fix.png "Figure 14. Resolution: Always prompt for username and password")

Next time you click on `Check Name`, Outlook will prompt for username
and password. A similar credentials dialog will be displayed each time
Outlook is launched.

<br/><br/>

## Profile creation goes fine, but Outlook can't open your default e-mail folders ##

The profile was properly created using the mail applet from the
configuration panel (or using Outlook wizard). However when I launch
Outlook, I keep having the following error message:

![MAPIProxy error 002](/images/mapiproxy/mapiproxy_error_002.png "Figure 15. Outlook error: Unable to Open your default e-mail folders")

This probably means Outlook is unable to lookup the resolved name of your MAPIProxy/samba4 server. You can either:


1. Make your Windows workstation points to a domain name server able to resolve MAPIProxy fully qualified name. See the [Samba4 internal DNS setup](/developers/configuring.html#configuration-1-samba4-with-internal-dns-server) for a fix.

2. Open `C:\WINDOWS\system32\etc\drivers\hosts` file and add an entry for mapiproxy. For example if I have `mapiproxy.openchange.local` pointing at `192.168.102.2`, then hosts file should hold the following line:<pre><code>192.168.102.2 mapiproxy.openchange.local mapiproxy</code></pre>

<br/><br/>

## Does MAPIProxy need to be domain controller? ##

No it doesn't. 

MAPIProxy works fine as a member server of a Windows domain. However,
since delegated credentials and forwarded kerberos credentials don't
yet work, you'll need to force samba to rely on the local SAM
database. To force this behavior, add to smb.conf within the global
section:


	server role               = member server
	aux_methods:member server = sam

<br/><br/>

## Generating Samba's private keys takes infinite time ##

For some configuration, the private keys generation process at Samba
startup can be very long. In case private keys are not generated
within a couple of minutes, it is suggested to recompile Samba with
gnutls disabled as in the example below:

	$ ./configure.developer --enable-debug --disable-gnutls
	$ gmake idl_full
	$ gmake
	$ sudo gmake install

<br/><br/>

## On Ubuntu `make samba-git` exits with `gmake: not found` ##

On Ubuntu, I have the following output while trying to install samba4
from OpenChange sources:

	To build Samba, run /usr/bin/make
	Step2: Compile Samba4 (IDL)
	./script/installsamba4.sh: 332: gmake: not found
	Step3: Compile Samba4 (Source)
	./script/installsamba4.sh: 332: gmake: not found
	Error in Step3 (error code 127)

gmake is make on Ubuntu. Creating the following symbolic link will fix the issue:

	$ sudo ln -s /usr/bin/make /usr/bin/gmake

