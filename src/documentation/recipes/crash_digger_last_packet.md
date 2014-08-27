# How to extract the last packet before a crash #

[TOC]

## Purpose and Scope ##

When an OpenChange developer investigates a crash, it starts with a
gdb session. This session is generally initiated using data from a
crash report, therefore it is a memory footprint of a process at the
moment it crashed.

In most cases, it is possible to fix the root cause of an issue by
studying its consequences, in other words the actual crash. The
general process implies the following steps: digging into data
structures to find the defect, then rewind the hierarchy of calls
until the starting point is found and finally fix the root cause.

In other cases, an overview of the context in which the crash occured
can help the developer moving forward and the analysis to be more
precise. This is where the recovery of the last DCERPC network packet,
just before the crash occured can be very useful.

The following recipe explains how to extract this network information
for the core dump and reinterpret it locally to be meaningful.

## The procedure ##

The procedure implies 3 steps:

1. find a frame where we can access the network packet in memory
2. extract this packet from memory into a file
3. Parse and dump this network packet locally using ndrdump

## Finding the network packet ##

The DCERPC packet is available and embedded within the
`dce_call_state` structure inside a `ndr_pull` data structure. This
latest structure has a pointer on an array of bytes which represents
the DCERPC packet along with a data_size integer field which gives the
size of the packet.

The first step is therefore to find a valid reference to the
`dcesrv_call_state` structure. If the code has been compiled with
optimization, you may encounter some references to `<optimized_out>`
in some frames. You would therefore have to move up within the stack
to find an previous reference.

In general, the first visible and direct reference to this information
is within the frame where `dcesrv_request` is called. In Samba,
`dcesrv_call_state` are generally named `dce_call` or `call`. In the
example below, it is the frame `#17`.

    [...]
    #12 0x00007fa02b45bfbb in EcDoRpc_process_transaction (mem_ctx=mem_ctx@entry=0x7fa04c33b1d0, emsmdbp_ctx=emsmdbp_ctx@entry=0x7fa04c33b6d0, mapi_request=0x7fa04c3401e0)
        at mapiproxy/servers/default/emsmdb/dcesrv_exchange_emsmdb.c:806
    #13 0x00007fa02b45ce2d in dcesrv_EcDoRpcExt2 (r=0x7fa04d66ef40, mem_ctx=0x7fa04c33b1d0, dce_call=<optimized out>) at mapiproxy/servers/default/emsmdb/dcesrv_exchange_emsmdb.c:1759
    #14 dcesrv_exchange_emsmdb_dispatch (dce_call=<optimized out>, mem_ctx=0x7fa04c33b1d0, r=0x7fa04d66ef40, mapiproxy=<optimized out>) at mapiproxy/servers/default/emsmdb/dcesrv_exchange_emsmdb.c:1920
    #15 0x00007fa02cd10634 in mapiproxy_server_dispatch (dce_call=dce_call@entry=0x7fa04c33b1d0, mem_ctx=mem_ctx@entry=0x7fa04c33b1d0, r=r@entry=0x7fa04d66ef40, mapiproxy=mapiproxy@entry=0x7fff887716d0)
        at mapiproxy/libmapiproxy/dcesrv_mapiproxy_server.c:57
    #16 0x00007fa02cf4df95 in mapiproxy_op_dispatch (dce_call=0x7fa04c33b1d0, mem_ctx=0x7fa04c33b1d0, r=0x7fa04d66ef40) at mapiproxy/dcesrv_mapiproxy.c:504
    #17 0x00007fa03a2562b0 in dcesrv_request (call=0x7fa04c33b1d0) at ../source4/rpc_server/dcerpc_server.c:967
    #18 dcesrv_process_ncacn_packet (dce_conn=dce_conn@entry=0x7fa04c90e730, pkt=<optimized out>, blob=...) at ../source4/rpc_server/dcerpc_server.c:1112
    #19 0x00007fa03a257081 in dcesrv_read_fragment_done (subreq=0x0) at ../source4/rpc_server/dcerpc_server.c:1539
    [...]

We can move to the frame #17 by using the `frame` command in gdb:

    (gdb) frame 17
    #17 0x00007fa03a2562b0 in dcesrv_request (call=0x7fa04c33b1d0) at ../source4/rpc_server/dcerpc_server.c:967
    967	    in ../source4/rpc_server/dcerpc_server.c


## Save the network packet into a file ##

Now we have found the frame where a valid reference where the
information we are looking for is available, we can dump it from
memory into a file. The gdb program has a **dump binary memory**
command designed for this purpose. The format of this command is:

    dump binary memory <outfile> <start_addr> <end_addr>

In our case:
* start_addr is the address where the array of bytes starts: `call->ndr_pull->data`
* end_addr is the address where the array of bytes ends: `(call->ndr_pull->data + call->ndr_pull->data_size)`

In summary to dump the network packet into a file, we run:

    (gdb) dump binary memory /tmp/pkt_in call->ndr_pull->data (call->ndr_pull->data + call->ndr_pull->data_size)


## Parse and dump the packet ##

The file generated with the previous call is what we call a ndrdump
file, which can be parsed and dumped using the ndrdump tool from
samba4 binary suite and the following command:

    $ ndrdump -l libmapi.so exchange_emsmdb 0xb in /tmp/pkt_in

This tool takes the following argument:
1. `-l libmapi.so` to tell ndrdump to load a DSO
2. `exchange_emsmdb` to specify the dcerpc endpoint
3. `0xb` to specify the RPC operation number (here EcDoRpcExt2)
4. `in` to specify the direction (here from client to server)
5.  `/tmp/pkt_in` the file to process

The command produces the following dump:

    0.     $ ndrdump -l libmapi.so exchange_emsmdb 0xb in /tmp/pkt_in
    1.     pull returned NT_STATUS_OK
    2.         0xb: struct EcDoRpcExt2
    3.             in: struct EcDoRpcExt2
    4.                 handle                   : *
    5.                     handle: struct policy_handle
    6.                         handle_type              : 0x00000001 (1)
    7.                         uuid                     : 48a9ebbb-c167-4afc-bf3c-e2dbbb59f394
    8.                 pulFlags                 : *
    9.                     pulFlags                 : 0x00000000 (0)
    10.                mapi_request: struct mapi2k7_request
    11.                    header: struct RPC_HEADER_EXT
    12.                        Version                  : 0x0000 (0)
    13.                        Flags                    : 0x0005 (5)
    14.                               1: RHEF_Compressed          
    15.                               0: RHEF_XorMagic            
    16.                               1: RHEF_Last                
    17.                        Size                     : 0x0045 (69)
    18.                        SizeActual               : 0x0047 (71)
    19.                    mapi_request             : *
    20.                        mapi_len                 : 0x00000047 (71)
    21.                        length                   : 0x0033 (51)
    22.                            mapi_request: struct EcDoRpc_MAPI_REQ
    23.                                opnum                    : 0x01 (1)
    24.                                logon_id                 : 0x00 (0)
    25.                                handle_idx               : 0x00 (0)
    26.                                u                        : union EcDoRpc_MAPI_REQ_UNION(case 1)
    27.                                mapi_Release: struct Release_req
    28.                            mapi_request: struct EcDoRpc_MAPI_REQ
    29.                                opnum                    : 0x01 (1)
    30.                                logon_id                 : 0x00 (0)
    31.                                handle_idx               : 0x01 (1)
    32.                                u                        : union EcDoRpc_MAPI_REQ_UNION(case 1)
    33.                                mapi_Release: struct Release_req
    34.                            mapi_request: struct EcDoRpc_MAPI_REQ
    35.                                opnum                    : 0x02 (2)
    36.                                logon_id                 : 0x00 (0)
    37.                                handle_idx               : 0x02 (2)
    38.                                u                        : union EcDoRpc_MAPI_REQ_UNION(case 2)
    39.                                mapi_OpenFolder: struct OpenFolder_req
    40.                                    handle_idx               : 0x03 (3)
    41.                                    folder_id                : 0x4a04010000000001 (5333388958225137665)
    42.                                    OpenModeFlags            : OpenModeFlags_Folder (0)
    43.                            mapi_request: struct EcDoRpc_MAPI_REQ
    44.                                opnum                    : 0x04 (4)
    45.                                logon_id                 : 0x00 (0)
    46.                                handle_idx               : 0x03 (3)
    47.                                u                        : union EcDoRpc_MAPI_REQ_UNION(case 4)
    48.                                mapi_GetHierarchyTable: struct GetHierarchyTable_req
    49.                                    handle_idx               : 0x04 (4)
    50.                                    TableFlags               : 0x00 (0)
    51.                                           0: TableFlags_Associated    
    52.                                           0: TableFlags_Depth         
    53.                                           0: TableFlags_DeferredErrors
    54.                                           0: TableFlags_NoNotifications
    55.                                           0: TableFlags_SoftDeletes   
    56.                                           0: TableFlags_UseUnicode    
    57.                                           0: TableFlags_SuppressNotifications
    58.                            mapi_request: struct EcDoRpc_MAPI_REQ
    59.                                opnum                    : 0x12 (18)
    60.                                logon_id                 : 0x00 (0)
    61.                                handle_idx               : 0x04 (4)
    62.                                u                        : union EcDoRpc_MAPI_REQ_UNION(case 18)
    63.                                mapi_SetColumns: struct SetColumns_req
    64.                                    SetColumnsFlags          : SetColumns_TBL_SYNC (0)
    65.                                    prop_count               : 0x0003 (3)
    66.                                    properties: ARRAY(3)
    67.                                        properties               : PidTagFolderId (0x67480014)
    68.                                        properties               : PidTagSubfolders (0x360A000B)
    69.                                        properties               : PidTagContainerClass (0x3613001F)
    70.                            mapi_request: struct EcDoRpc_MAPI_REQ
    71.                                opnum                    : 0x15 (21)
    72.                                logon_id                 : 0x00 (0)
    73.                                handle_idx               : 0x04 (4)
    74.                                u                        : union EcDoRpc_MAPI_REQ_UNION(case 21)
    75.                                mapi_QueryRows: struct QueryRows_req
    76.                                    QueryRowsFlags           : TBL_ADVANCE (0)
    77.                                    ForwardRead              : 0x01 (1)
    78.                                    RowCount                 : 0x1000 (4096)
    79.                            mapi_request             : (handles) number=5
    80.                                handle                   : 0x00000008 (8)
    81.                                handle                   : 0x00000004 (4)
    82.                                handle                   : 0x00000001 (1)
    83.                                handle                   : 0xffffffff (4294967295)
    84.                                handle                   : 0xffffffff (4294967295)
    85.                    cbIn                     : 0x0000004d (77)
    86.                    pcbOut                   : *
    87.                        pcbOut                   : 0x00008007 (32775)
    88.                    rgbAuxIn                 : DATA_BLOB length=0
    89.                    cbAuxIn                  : 0x00000000 (0)
    90.                    pcbAuxOut                : *
    91.                        pcbAuxOut                : 0x00000088 (136)
    92.    dump OK
    93.

## Summary ##

1. Start a gdb session
2. Find a reference to a `dcesrv_call_state` structure
3. Extract the packet using `dump memory <outfile> <start_addr> <end_addr>`
4. Run ndrdump to dump the packet
