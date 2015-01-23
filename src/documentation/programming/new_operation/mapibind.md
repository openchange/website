[TOC]

# MAPIStore Python Bindings #

The [MAPIStore Python Bindings][mapibind] allow the user to access the MAPIStore
Library from a Python script, instead of through the OpenChange Server.
Therefore, they are a powerful tool in order to test the new implemented
function.

[mapibind]: http://openchange.org/documentation/mapibind/intro.html

## message.c ##

In *pyopenchange/mapistore/message.c*:

We add the function `py_MAPIStoreMessage_delete_attachment` to the message
class methods. The method takes as an argument the attachment ID (the message
object is obtained internally), calls the `mapistore_message_delete_attachment`
function and returns nothing, raising the proper exceptions if an error
happens.

It is also necessary to expose the method to Python by adding it in
`mapistore_message_methods`.

    { "delete_attachment", (PyCFunction)py_MAPIStoreMessage_delete_attachment, METH_VARARGS|METH_KEYWORDS },

