<div style="float: right; width: 35%;margin-left:2em;">
<img src="/images/mapiproxy/mapiproxy.png" alt="MAPIProxy Logo"/>
</div>

# Technical Concepts #

[TOC]

## NSPI Bindings Replacement ##

When Outlook sets up an Exchange account using either the mail applet
from the configuration panel or the account editor within Outlook, it
uses the NSPI protocol (Name Service Provider Interface, effectively
the address book provider). In this case, NSPI is used to resolve the
Exchange username and fetch from Exchange server all information
needed by Outlook to initiate direct connection to the EMSMDB pipe
(effectively the message store) the next time it connects to the
server.<br>

At some point of the profile's creation process, Outlook queries
Exchange for some specific connection information using the
**`NspiGetProps (0x9)` RPC operation**. More specifically, when
Outlook requests for the **`PR_EMS_AB_NETWORK_ADDRESS`** MAPI
property, Exchange returns a list **binding strings**. Outlook next
stores these binding strings at some location - associated to the
Outlook profile - in the windows registry and uses them for future
connections.<br>

Outlook can also rely on other information returned by NSPI functions
and connect to the real Exchange server rather than MAPIProxy. Such
case occurs when Outlook is able to resolve the exchange server using
its hostname. This reference to the original Exchange server can be
found when Outlook requests for the **`PR_EMS_AB_HOME_MDB`** MAPI
property during the **`NspiQueryRows (0x3)`** RPC operation. MAPIProxy
replaces the Exchange server name with its own netbios name and
forward the reply to the client.<br/>

In the meantime, this information is next used by Outlook to query a
minimal entry ID for a distinguished name using this server
name. MAPIProxy needs to substitute the server name in the inbound
request string with the original exchange one.<br>

MAPIProxy needs to avoid Outlook clients being aware of this remote
server address and trying to communicate directly with the remote server
instead of using the proxy. In order to do this, MAPIProxy alters the
Outlook-Exchange MAPI traffic and replaces these binding strings with
the MAPIProxy FQDN and netbios name.

<br/>

## NSPI Referral Replacement ##

The Address Book Name Service Provider Interface (NSPI) Referral
Service is a service used by Outlook to retrieve the name of an NSPI
server. No NSPI connection should be initiated without first querying
for the correct NSPI server. In this case, RFR returns the fully
qualified domain name of the real Exchange server and starts using it
if available. <br>

MAPIProxy needs to avoid Outlook clients being aware of this server
address and trying to communicate directly with the remote server
instead of using the proxy. In order to do this, MAPIProxy alters the
Outlook-Exchange MAPI traffic and replaces the server DN returned by
**`RfrGetNewDSA (0x0)` RPC operation** with the MAPIProxy realm as
specified in smb.conf.

<br/>

## Force EMSMDB Protocol Version ##

When Outlook starts and presumably calls `MapiLogonEx`, it first opens
a connection to the Exchange server on the NSPI pipe, then on the
EMSMDB pipe. Under Outlook 2003, the very first EMSMDB RPC call
Outlook makes can be considered as a kind of * protocol version
negotiation *. Depending on which version of Outlook is used, and how
the Exchange server replies to the EMSMDB connect request, Outlook
will either keep using the same pool of RPC calls or
downgrade.<br>

For example Outlook 2003 (default behavior) tests if the remote server
supports the 2 new EMSMDB calls (`EcDoConnectEx`/`EcDoRpcExt2`)
introduced in Exchange 2003. If Exchange replies to the `EcDoConnectEx`
request with a dcerpc_fault, it means the server does not support the
RPC operation, presumably has a version before 2003, and Outlook needs
to downgrade its version in order to communicate with the server:

* `EcDoConnectEx` (0xa) call:
    * On success, Outlook will use `EcDoRpcExt2` (0xb) to handle MAPI traffic
    * On failure (`dcerpc_fault`: `nca_op_rng_error`), Outlook calls `EcDoConnect` (0x0) and use `EcDoRpc` (0x2) to handle MAPI traffic

If MAPIProxy runs in an environment with Outlook clients and Exchange
servers using a version above 2003, a last step is required to
successfully use Outlook. The `EcDoConnect` RPC reply returns the
Exchange server version (as an array of 3 short integers). When
Outlook detects this particular server version, it automatically
closes the connection and keep requesting indefinitely for
`EcDoConnectEx`. To deal with this, MAPIProxy modifies the EcDoConnect
reply sent by Exchange and replaces the server version with a one
equal to that sent by Exchange 2000.<br>

In the meantime, if we reproduce this test with Outlook 2000 which
doesn't support these 2 new RPC calls, Outlook will directly call
`EcDoConnect`.<br>

The main difference between the `EcDoConnectEx`/`EcDoRpcExt2`
operations and the `EcDoConnect`/`EcDoRpc` operations is that the
former use both `XOR 0xA5` obfuscation and `LZ77` compression/Direct2
encoding; while the latter only use the `XOR` obfuscation to handle
MAPI content.  If MAPIProxy wants to act as an intelligent proxy (for
example, to be able to analyze MAPI content on the fly, compress MAPI
data etc), receiving non compressed MAPI traffic would probably
improve the overall process.

Below is a list of Exchange/Outlook pairs and the EMSMDB connect
function they will use by default:

Exchange version | Outlook version | EMSMDB connect function
---------------- | --------------- | ------------------------
5.5  | any         | `EcDoConnect` (0x0)
2003 | 2000        | `EcDoConnect` (0x0)
2007 | 2000        | `EcDoConnect` (0x0)<br/>Microsoft officially says it is unsupported
2003 | 2003 - 2007 | `EcDoConnectEx` (0xA)
2007 | 2003        | `EcDoConnectEx` (0xA)
2007 | 2007        | `EcDoConnectEx` (0xA)


MAPIProxy reproduces the Exchange 2000 behavior and prevents Outlook
from communicating with the Exchange server using the
`EcDoConnectEx`/`EcDoRpcExt2` as described in Figure 2 below. When
Outlook sends an EcDoConnectEx request, MAPIProxy does not relay the
request to the remote Exchange server and immediately returns a
dcerpc_fault to Outlook. Outlook, assuming the server doesn't support
this call uses EcDoConnect instead. From this call, MAPIProxy relay
the information to Exchange.

![MAPIProxy emsmdb graph](/images/mapiproxy/mapiproxy_emsmdb_graph.png
 "Figure 2. MAPIProxy behavior on Outlook EMSMDB connection")

From the Exchange side, the server will analyze this EcDoConnect
request as a call sent by Outlook 2000 or below version. Exchange
works fine using this protocol version unless Exchange 2007 SP1 which
appears to introduce client version restrictions <i>by default</i>. In
the meantime, existing tests demonstrate similar restrictions would
apply to Outlook 2003 connection (without MAPIProxy) and prevent
Outlook version before 2007 connecting to Exchange 2007. Further
information and solution is available at the following addresses:
 
* [Earlier Outlook clients cant connect to Exchange 2007
  Server](http://support.microsoft.com/kb/555851)
* [Exchange 12 and Public
  Folders](http://msexchangeteam.com/archive/2006/02/20/419994.aspx)

## OpenChange IDL File ##

IDL stands for Interface Definition Language and OpenChange uses this
format to describe ExchangeRPC communications. This file is processed
by pidl (Perl IDL compiler provided by Samba4) which turns this
protocol description into C-code dealing with the push, pull and print
operations.

# Next: Stackable Modules #

Next section introduces the [stackable modules](stackable-modules.html)