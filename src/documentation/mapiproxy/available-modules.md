<div style="float: right; width: 45%;margin-left:2em;">
<img src="/images/mapiproxy/mapiproxy.png" alt="MAPIProxy Logo"/>
</div>

# Available Modules #

[TOC]

## Downgrade Module ##

The **downgrade** module implements the `EcDoConnect`/`EcDoRpc`
negotiation as described in the Technical concepts section. It ensures
Outlook will not send compressed information or use functions other
than EcDoRpc for EMSMDB transport. In order to use the downgrade
module, edit smb.conf and add `downgrade` to `dcerpc_mapiproxy:modules`.

    dcerpc_mapiproxy:modules = downgrade

<br/>

## Pack Module ##
<br>
<div class="alert"> 
Note that this module only works with an infrastructure using two or
more instances of MAPIProxy as described
in Figure 1 </div>

The **pack** module implements routines designed to manipulate and
factorize MAPI content between different MAPIProxy instances. It also
offers a developer overview on how to manipulate mapi requests. Last
but not least, it provides data which can next be used by subsequent
MAPIProxy modules for example to compress or encrypt this proxypack
blob.

* First, MAPIProxy extracts and removes specific MAPI calls from the
request, pack them within the proxypack MAPI call data blob, prefix
them with their real offset in the array of mapi requests and finally
append this custom call at the end of the mapi requests array (Figure
4). <br/>![MPM Pack](/images/mapiproxy/mpm_pack_pack.png "Pack process")<br/><br/>

* Final MAPIProxy hop will seek the mapi requests array looking for
the proxypack call. If found, it unpacks MAPI data and restore these
calls at their initial location within the mapi requests array (Figure
6). <br/>![MPM UNpack](/images/mapiproxy/mpm_pack_unpack.png "Unpack process")


This module has two configuration options:

Option | Description
------ | -----------
**mpm_pack:opnums** | This option takes a list of MAPI calls to pack into the proxypack data blob. It can take one or more MAPI opnums, each of them separated with a comma.
**mpm_pack:lasthop** | This options takes either `true` or `false`.the lasthop option defines whether this is a MAPIProxy directly connected to Outlook/Exchange or yet another proxy inserted within the MAPIProxy chain of hops. If this MAPIProxy instance is not a last hop, then it will skip the pack/unpack operations and forward the request to the next one.

    mpm_pack:opnums = 0x70,0x75,0x76,0x77,0xa
    mpm_pack:lasthop = true

In order to use the `pack` module, edit `smb.conf` and add `pack` to
`dcerpc_mapiproxy:modules`.

    dcerpc_mapiproxy:modules = downgrade,pack


## Cache Module ##

The **cache** module implements a cache mechanism for
streams related to messages or attachments. This module reduces
communication latency between MAPI clients (using `online` mode)
and Exchange. When configured with online mode, MAPI clients retrieve
data from Exchange each time they access a message and don't have any
offline storage mechanisms enabled - data are downloaded and stored
within a `temporary files` folder. This module also offers a
preliminary synchronization mechanism which can be used to transfer
files between different MAPIProxy instances and use different
protocols than MAPI for data transfer (such as `rsync` or `wget`).

The cache module is designed to cover different cases:

### Scenario 1: Replay attachments ###

This scenario only requires a single MAPIProxy instance and requires a
single configuration option:

    mpm_cache:path = /tmp/cache

![MPM Cache case 1](/images/mapiproxy/mpm_cache_case_one.png "Figure 8. Replay stream scenario")

1. **Outlook reads a stream for the first time**:<br/> MAPIProxy
monitors the Outlook-Exchange traffic and store the attachment on the
local filesystem. </li>

2. **Outlook requests this stream again**:<br/> MAPIProxy looks over
its cache, find the requested stream and directly communicate with
Outlook without forwarding requests to the remote server.


### Scenario 2: Read stream ahead ###

This scenario requires two MAPIProxy instances and requires different configuration options for local and remote MAPIProxy:

* **local MAPIProxy smb.conf sample**:

        mpm_cache:path = /tmp/cache
        mpm_cache:ahead = false
        mpm_cache:sync = true
        mpm_cache:sync_cmd = /usr/bin/rsync -z mapiproxy@192.168.102.2:__FILE__  __FILE__

* **remote MAPIProxy smb.conf sample**:

        mpm_cache:path = /tmp/cache
        mpm_cache:ahead = true
        mpm_cache:sync = false


![MPM Cache Case 2](/images/mapiproxy/mpm_cache_case_two.png "Figure
 9. Read ahead scenario with synchronization mechanism")

**This scenario uses 2 MAPIProxy instances**. We call <i>remote MAPIProxy</i>, the MAPIProxy instance connected to the Exchange server network and <i>local MAPIProxy</i> the instance connected to the MAPI clients network:

1. **Outlook wants to read an attachment for the first time**:<br/>
The remote MAPIProxy monitors the first ReadStream request and read
the full stream ahead on its own and stores it on its local
filesystem.

2. **remote MAPIProxy replies to local MAPIProxy and local MAPIProxy
runs the synchronization mechanism.** The current implementation
provides a fork/execve/waitpid process which allows to run any command
with parameters. When local MAPIProxy finishes to store the file
locally through the synchronization mechanism, it marks the stream as
being cached.

3. **local MAPIProxy plays the attachment back to the client
from cache**.

The module monitors `OpenMessage`, `OpenAttach`, `OpenStream`,
`ReadStream` and `Release` MAPI calls and stores streams on the local
filesystem with indexation in a TDB database. Note that the module
doesn't yet provide semantics needed to remove entries from the TDB
database.


This module has different configuration options and modes:

* **mpm_cache:path**<br/> This option takes the full path to an
    existing folder on the filesystem. This folder will be the storage
    root path for the cache module and will hold the TDB store, a
    folder hierarchy and stream files.

        mpm_cache:path = /tmp/cache

* **mpm_cache:ahead**<br/> This option takes a boolean value (true or
    false) and defines whether the ahead mechanism should be enabled
    or not. This mode should only be enabled on the remote MAPIProxy
    instance. It can be enabled on local MAPIProxy instance, however
    there won't be any benefit but Outlook unexpectedly falling in
    some time out mode and close the connection.

        mpm_cache:ahead = true


* **mpm_cache:sync**<br/> This option takes a boolean value (true or
false) and defines whether the synchronization mechanism should be
enabled or not. This mode only makes sense on the local MAPIProxy
instance and **mpm_cache:sync_cmd** must also be configured.

        mpm_cache:sync = true

* **mpm_cache:sync_cmd**<br/> aThis option takes the command line to
execute for the synchronization process. A preliminary substitution
variable mechanism is available but should be improved over time. For
the moment, the cache module only provides **__FILE__** which will be
substituted by the full path to the cached file. The synchronization
process currently assumes local and remote MAPIProxy instances have
the same storage path (<i>mpm_cache:path</i>).

        mpm_cache:sync_cmd = /usr/bin/rsync -z mapiproxy@192.168.102.2:__FILE__  __FILE__

In order to use the cache module, edit smb.conf and add <i>cache</i>
to <i>dcerpc_mapiproxy:modules</i>.

    dcerpc_mapiproxy:modules = downgrade,cache

<br/>

### Notes ###


* While the cache module implements a preliminary <i>session</i>
mechanism (multiple clients support), this mode is currently only
implemented up to 50%. Multiple clients will work for files already
cached, but will cause unexpected behaviors while synchronizing a
remote file at the same moment from different session. This bug should
be fixed when the streaming and lock mechanism will be
implemented.

* The synchronization mechanism is experimental and we have
deliberately changed the storage path permissions from 0700 to 0777
for trivial setup. File permissions will become parametric smb.conf
options in the future.
