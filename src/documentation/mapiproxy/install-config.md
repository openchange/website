<div style="float: right; width: 45%;margin-left:2em;">
<img src="/images/mapiproxy/mapiproxy.png" alt="MAPIProxy Logo"/>
</div>

[TOC]

# Installation #

Instructions on how to build mapiproxy from sources are the same than
the [OpenChange server installation guide](/cookbook/initiliazing.html) ones.

This document only outlines relevant changes between server and proxy
mode configuration.

# 5-Minute Configuration #

This 5-Minute configuration will help you set up a minimal MAPIProxy
using specified credentials and relaying traffic from Outlook clients
to a remote Exchange server. This configuration will be performed in
three steps.

## Provision Samba ##

Provision Samba as [described
here](/cookbook/configuring.html#provision_the_server). 
<br><br>
If you don't have DNS resolution and your realm can't be resolved,
samba will be unable to authenticate the user in its user
database. You must specify a realm which MAPI clients and MAPIProxy
can resolve. If everything works fine, the provisioning script will
have created all the databases, populated the AD (Active Directory)
and generated a valid smb.conf file.

## Add a user account ##

In this configuration, we'll set the same credentials both for the
user in the windows domain and on the Samba4 server. Note that it is
not required to set the same password for a user both on Samba and
exchange server side. This is for convenience purpose only. 

Let say there is already a user named `JohnDoe` with its password set
to `openchange2!` on the Exchange server, we will create the user with
the `samba-tool` command as [exposed
here](http://www.openchange.org/cookbook/configuring.html#create-new-user).

## Configure MAPIProxy options ##

In this final step, we only need to customize a small set of parameters.

Option | Description
------ | -----------
dcerpc endpoint servers  | MUST include epmapper and mapiproxy separated with comma.
dcerpc_mapiproxy:binding | This is the binding string used to connect to the remote Exchange server. The format of this string is: `transport:address[flags]`. In the example below, we'll be using the TCP over IP transport, connect on `192.168.1.1` and add the `print` flag so MAPI packets get dissected on samba stdout (or logfile).
dcerpc_mapiproxy:username | Specify the username of the specified credentials account that we will be using to connect to the remote Exchange server.
dcerpc_mapiproxy:password | Specify the password of the specified credentials account we will be using to connect to the remote Exchange server.
dcerpc_mapiproxy:domain | The Windows domain the remote Exchange server belongs to.
dcerpc_mapiproxy:interfaces | In our case, we want to relay the whole ExchangeRPC traffic, so we need to load both the EMSMDB and NSP interface. In the meantime, people interested in NSPI proxy only would only have to load the exchange_nsp interface.
dcerpc_mapiproxy:modules | MAPIProxy provides a stackable modular system which primary objective is to provide developers an API for modules development. In our case we want to activate the `downgrade` module responsible for the EcDoConnect/EcDoRpc EMSMDB RPC functions negotiation.

## MAPIProxy smb.conf configuration ##

Add the following lines within the `[global]` section of `smb.conf`
file:

    ### Configuration required by mapiproxy ###

    dcesrv:assoc group checking = false
    dcerpc endpoint servers = epmapper, mapiproxy

    dcerpc_mapiproxy:binding = ncacn_ip_tcp:192.168.1.1[print]
    dcerpc_mapiproxy:username = JohnDoe
    dcerpc_mapiproxy:password = openchange2!
    dcerpc_mapiproxy:domain = EXCHANGE
    dcerpc_mapiproxy:interfaces = exchange_emsmdb, exchange_nsp, exchange_ds_rfr
    dcerpc_mapiproxy:modules = downgrade
    ### Configuration required by mapiproxy ###


We are now ready to run samba:

    # samba -d5 -i -M single

If everything works properly, the following lines should be displayed
in samba output:

    DCERPC endpoint server 'exchange_emsmdb' registered
    DCERPC endpoint server 'exchange_nsp' registered
    DCERPC endpoint server 'exchange_ds_rfr' registered
    DCERPC endpoint server 'mapiproxy' registered
    dcesrv_interface_register: interface 'epmapper' registered on endpoint 'ncacn_np:[\pipe\epmapper]'
    dcesrv_interface_register: interface 'epmapper' registered on endpoint 'ncacn_ip_tcp:[135]'
    dcesrv_interface_register: interface 'epmapper' registered on endpoint 'ncalrpc:[EPMAPPER]'
    MAPIPROXY module 'downgrade' registered
    MAPIPROXY module 'downgrade' loaded
    mapiproxy_module_load 'downgrade' (Downgrade EMSMDB protocol version EcDoConnect/EcDoRpc)
    dcesrv_interface_register: interface 'exchange_emsmdb' registered on endpoint 'ncacn_np:[\pipe\lsass]'
    dcesrv_interface_register: interface 'exchange_emsmdb' registered on endpoint 'ncacn_np:[\pipe\protected_storage]'
    dcesrv_interface_register: interface 'exchange_emsmdb' registered on endpoint 'ncacn_ip_tcp:'
    dcesrv_interface_register: interface 'exchange_nsp' registered on endpoint 'ncacn_np:[\pipe\lsass]'
    dcesrv_interface_register: interface 'exchange_nsp' registered on endpoint 'ncacn_np:[\pipe\protected_storage]'
    dcesrv_interface_register: interface 'exchange_nsp' registered on endpoint 'ncacn_ip_tcp:[]'
    dcesrv_interface_register: interface 'exchange_ds_rfr' registered on endpoint 'ncacn_np:[\pipe\lsass]'
    dcesrv_interface_register: interface 'exchange_ds_rfr' registered on endpoint 'ncacn_np:[\pipe\protected_storage]'
    dcesrv_interface_register: interface 'exchange_ds_rfr' registered on endpoint 'ncacn_ip_tcp:[]'

**You should now be able to configure Outlook to use an Exchange account with the proxy IP address and run Outlook seamlessly (both online or cached exchange mode).**

# Next: Technical Concepts #

The next section introduces most important MAPIProxy [technical
concepts](tech-concepts.html).
