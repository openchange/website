[TOC]

# Openchange Server #

In \[MS-OXROPS\] we can see that:

- The `RopDeleteAttachment` operation has an ID (`RopId`) equal to 0x24.
- It takes as arguments the handle index of the message that calls the operation
    (`InputHandleIndex`) and the attachment ID (`AttachmentID`).
- It returns nothing but the status of the operation.

## dcesrv_exchange_emsmdb.c ##

In *mapiproxy/servers/default/emsmdb/dcesrv_exchange_emsmdb.c*:

When OpenChange receives the request of an operation, it calls
`EcDoRpc_process_transaction`. This function has an inner switch-case that
detects and performs the requested operation by checking the `RopId` field of
the request.

We have to include the `RopId` of this operation in the switch but, instead
of using the numeric ID, 0x24, we can use the global definition
`op_MAPI_DeleteAttach` present in *gen_ndr/exchange.h*.

      case op_MAPI_DeleteAttach: /* 0x24 */
              retval = EcDoRpc_RopDeleteAttach(mem_ctx, emsmdbp_ctx,
                                              &(mapi_request->mapi_req[i]),
                                              &(mapi_response->mapi_repl[idx]),
                                              mapi_response->handles, &size);
              break;

## oxcmsg.h ##

In *mapiproxy/servers/default/emsmdb/oxcmsg.c*:

We have to implement then the function called in the switch,
`EcDoRpc_RopDeleteAttach`. which receives two pointers to the structures with
the request and the response data and a pointer to the MAPI handles, and
returns by reference the response data and the response size. We will also have
to define it in *dcesrv_exchange_emsmdb.h*, in the same folder.

The function calls the MAPIStore library function `mapistore_message_delete_attachment`, 
which requires the message object and the attachment ID. These arguments can be
obtained from the handle index in the request and the MAPI handle array. The
result of this function will determine the error_code attribute of the response
structure.

Since the response operation returns just the status of the operation, the size
is the default response size, defined in *mapiproxy/libmapiserver/libmapiserver_oxcmsg.c*
as `SIZE_DFLT_MAPI_RESPONSE`. However, and following the convention, all the
operations have a function in that file that returns the response size.

    _PUBLIC_ uint16_t libmapiserver_RopDeleteAttach_size(struct EcDoRpc_MAPI_REPL *response)
    {
            return SIZE_DFLT_MAPI_RESPONSE;
    }


# Next: MAPIStore Library ##

The [next section](mapistore.html) describes the implementation of the operation in the MAPIStore Library.
