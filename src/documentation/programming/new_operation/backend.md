[TOC]

# Sample Backend #

The operation can be implemented in any backend supported by MAPIStore, and the
MAPIStore Library will call each backend's context depending on where we are
performing the operation.

In this guide, the operation will only be implemented in the
[Sample Python Backend][sample].

[sample]: http://openchange.org/documentation/programming/mapistore_python/index.html

## mapistore_python.c ##

In *mapiproxy/libmapistore/mapistore_python.c*:

The function in `mapistore_backend.c` will call the
`mapistore_python_message_delete_attachment` function in the Python-C gateway,
This function uses the Python-C API function [`PyObject_CallMethod`][callme] to
access *sample.py*, the script where the structures and methods of the backend
are. The value returned by the method is its error code, which is returned back
to MAPIStore.

[callme]: https://docs.python.org/2/c-api/object.html#c.PyObject_CallMethod

This function must be included as well in `mapistore_python_load_backend`,
located in the same file. This way, when the backend is intialised, the
`delete_attachment` function is set to `mapistore_python_message_delete_attachment`.

        backend.message.delete_attachment = mapistore_python_message_delete_attachment;

## sample.py ##

In *mapiproxy/libmapistore/backends/python/sample.py*:

We include the `delete_attachment` method in the `MessageObject` class.


    def delete_attachment(self, attach_id):
        print '[PYTHON]: %s message.delete_attachment %d' % (self.name, attach_id)

        attachments = [self.basedict["attachments"].pop(i) for i, att in enumerate(self.basedict["attachments"]) if att["attachid"] == attach_id]
        if len(attachments) == 0:
            return 17

        [self.basedict["attachment_cache"].remove(att) for att in self.basedict["attachment_cache"] if att["attachid"] == attach_id]
        return 0

In the Sample Python Backend, a Message object is a dictionary with an
`"attachments"` entry, which has as a value a list with the attachments. Each
one is, at the same time, a dictionary which has an `"attachid"` entry, a value
that identifies it uniquely across the message.

The message has an `attachment_cache` entry as well. When an attachment is
opened, the object that is returned is a copy of the attachment, and it's
stored in the cache. Therefore, if we want to delete a message, we have to
remove the object from both the attachment list and the cache.

*NOTE: Outlook looks for the Python Sample backend in
    `/usr/lib/python2.7/dist-packages/openchange/backends/`, so the file
    *sample.py* must be updated there before trying Outlook to perform this
    operation.*

# Next: MAPIStore Python Bindings ##

You can now proceed to the implementation of the operation in the
[MAPIStore Python Bindings](mapibind.html).
