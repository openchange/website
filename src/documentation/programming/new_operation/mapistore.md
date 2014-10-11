[TOC]

# MAPIStore Library #

The MAPIStore Library is in charge of the communication with the storage
backends, and it's called both by the OpenChange Server code and by the
MAPIStore Python Bindings in order to push/pop information in/from them.

## mapistore_interface.c ##

In *mapiproxy/libmapistore/mapistore_interface.c*:

We create the function `mapistore_message_delete_attachment`, which takes as
arguments the MAPIStore context and the context ID, from which it accesses the
backend context. The function returns the error status provided by the function
`mapistore_backend_message_delete_attachment`. This function takes as arguments
the backend context and the other two arguments, the message object and the
attachment ID.

    _PUBLIC_ enum mapistore_error mapistore_message_delete_attachment(struct mapistore_context *mstore_ctx, uint32_t context_id,
                                                                      void *message, uint32_t aid)
    {
            struct backend_context  *backend_ctx;

            /* Sanity checks */
            MAPISTORE_SANITY_CHECKS(mstore_ctx, NULL);

            /* Step 1. Search the context */
            backend_ctx = mapistore_backend_lookup(mstore_ctx->context_list, context_id);
            MAPISTORE_RETVAL_IF(!backend_ctx, MAPISTORE_ERR_INVALID_PARAMETER, NULL);

            /* Step 2. Call backend operation */
            return mapistore_backend_message_delete_attachment(backend_ctx, message, aid);
    }

The function must be defined as well in *mapiproxy/libmapistore/mapistore.h*.

## mapistore_backend.c ##

In *mapiproxy/libmapistore/mapistore_backend.c*:

The function `mapistore_backend_message_delete_attachment` is the one in charge
of calling the backend, and returns the MAPIStore status returned by it.

    enum mapistore_error mapistore_backend_message_delete_attachment(struct backend_context *bctx, void *message, uint32_t aid)
    {
            return bctx->backend->message.delete_attachment(message, aid);
    }

The structure `mapistore_backend`, in *mapiproxy/libmapistore/mapistore.h*,
must contain the declaration of the delete_attachment function in its `message`
attribute.

## mapistore_backend_defaults.c ##

In *mapiproxy/libmapistore/mapistore_backend_defaults.c*:

We can create a function that returns `MAPISTORE_ERR_NOT_IMPLEMENTED` for when
the backend doesn't have this operation implemented.

    static enum mapistore_error mapistore_op_defaults_delete_attachment(void *message_object,
                                                                        uint32_t aid)
    {
            DEBUG(3, ("[%s:%d] MAPISTORE defaults - MAPISTORE_ERR_NOT_IMPLEMENTED\n", __FUNCTION__, __LINE__));
            return MAPISTORE_ERR_NOT_IMPLEMENTED;
    }

The default behaviour must be set in `mapistore_backend_init_defaults`, in the same file:

        backend->message.delete_attachment = mapistore_op_defaults_delete_attachment;

*NOTE: the default behaviour needs to be set by the different backends when
    they are initialised, The SOGo backend, for instance, doesn't do this, and
    calling `delete_attachment` produces a segmentation fault.

# Next Section: Sample Backend #

The [next section](backend.html) describes the implementation of the operation in the Sample Backend.
