# BackendObject #

[TOC]

It is the root class of a backend and the first one to be
instantiated. It is used to initialize and register the backend into
mapistore, list and create contexts and create mailbox root folders.

## Class Attributes ##

BackendObject requires 3 attributes to be defined for every backend in
order to initialize and register properly:

        class BackendObject(object):
            name = "sample"
            description = "Quick description of the backend"
            namespace = "sample://"

### name attribute ###

This attribute specifies the name of the backend. It is a unique
identifier among the list of backends.

### description ###

This attribute provides a brief description of the backend. While it
is required, an empty string can be specified.

### namespace ###

This attribute specifies the namespace of the backend used when
building a URI and is used to find the appropriate backend associated
to a URI. It is therefore a unique identifier among the list of backends.


## \_\_init\_\_ method ##

This function is called automatically to initialize the backend but is
Python specific. The execution of this function is therefore not
triggered by any specific code from mapistore but the import of the
module.

## init method ##

This function is __called once in the lifetime of the OpenChange
server process__ and is used to initialize global settings to the
backend. The init function can for example be used instantiate a
container (LXC, docker) or a virtual machine.

If your backend does not require any specific initialization, you just
have to return MAPISTORE_SUCCESS.

        def init(self):
            """ Initialize sample backend
            """
            print '[PYTHON]: backend.init: init()'
            return 0

## create_context method ##