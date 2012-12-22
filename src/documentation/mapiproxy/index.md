<div style="float: right; width: 45%;margin-left:2em;">
<img src="/images/mapiproxy/mapiproxy.png" alt="MAPIProxy Logo"/>
</div>

# Introduction #

<br/>

## Purpose and Scope ##

MAPIProxy is an endpoint server for Samba4 which proxies ExchangeRPC
traffic from MAPI clients (Outlook, openchangeclient, etc.) to
Microsoft Exchange Server (and back). It can either act as a
transparent proxy, for hacking, monitoring or debugging purposes or
modify traffic on the fly and so provide new features. It is primarily
developed for - but not limited to - third-party implementors looking
for a development framework they can use for MAPI acceleration
purposes.

This project is originally based on `dcerpc_remote.c` code from Stefan
Metzemacher (Samba4 trunk) and is released under GPLv3 or later
license. It creates a dynamic shared object file which is loaded into
samba and uses the Samba configuration file (smb.conf) to set common
options.

<br/>

## General overview ##

![MAPIProxy overview](/images/mapiproxy/mapiproxy_overview.png "Figure 1. General MAPIProxy network overview")

The MAPIProxy traffic can be divided into 3 different parts as described in the figure above:

1. **clients to MAPIProxy**: <br/> The origin of a client connect does not  have much importance: it can either be an incoming connection from a real MAPI client, a connection relayed from another third-party proxy or another MAPIProxy instance. MAPIProxy runs as an endpoint server registered when samba starts. When the Samba4 endpoint mapper receives an incoming connection asking for one of the ExchangeRPC endpoints: NSPI (Name Service Provider Interface - Address Book) or EMSMDB (Exchange Message Store), the endpoint mapper redirects ExchangeRPC traffic to MAPIProxy which will pull, push and dispatch MAPI operations.

2. **MAPIProxy to MAPIProxy**:<br/>The main objective of MAPIProxy is not to directly connect to the remote message server, but rather to relay some kind of modified MAPI traffic to the next MAPIProxy hop. This configuration can be used to add a compression layer between MAPIProxy instances, or to send specific third-party vendor information. However, a proxied connection directly from a MAPI client to an Exchange server (i.e. <i>client-MAPIProxy-server</i> is possible and such a configuration could be used for many other purposes.

3. **MAPIProxy to server**:<br/>This last node is responsible for restoring MAPI contents and pushing it to the real Exchange server.

## Bugs and Limitations ##

If you find bugs, limitations or have features you would like to see included in MAPIProxy, please register on the <a href="http://tracker.openchange.org">OpenChange Tracker System</a> and create new tickets.

# Next: Installation & Configuration #

Proceed to [Installation & Configuration](install-config.html)
