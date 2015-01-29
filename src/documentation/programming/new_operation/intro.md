# HowTo Implement a New Operation in OpenChange #

[TOC]

# Purpose and Scope #

This document provides a guide on how to implement a new operation in
OpenChange, and it aims to serve both as a cookbook and as a way to gain
insight into the different components of OpenChange.

## Overview of the task ##

Not all the operations implemented in the Exchange protocols are mapped into
OpenChange. This guide takes one of these operations, `RopDeleteAttachment`,
and lists the neccesary steps for implementing it in OpenChange. The operation
belongs to the Message Object Protocol and performs the deletion of an
attachment.

The [Microsoft Developer Network][msdn] site contains two documents where more 
information about this operation can be found:  \[MS-OXCMSG\] and  \[MS-OXROPS\].

[msdn]: http://msdn.microsoft.com/en-us/library/cc307725(v=EXCHG.80).aspx

The operation needs to be implemented in several components of OpenChange:

- OpenChange Server - Called by Outlook when the user requests the operation.
- MAPIStore Library - Called by the OpenChange Server code in order to interact
    with the storage backend.
- MAPIStore backend (in this case, the [Python Sample Backend][sample])
- Additionally, the [MAPIStore Python Bindings][mapibind] will include a method
    that maps this operation into Python.

[sample]: http://openchange.org/documentation/programming/mapistore_python/index.html
[mapibind]: http://openchange.org/documentation/mapibind/intro.html

## Setting up the environment ##

The necessary environment can be set up by following the guide [Howto Setup an
OpenChange developer environment in Zentyal][deven]. The MAPIStore Python
Bindings can be enabled by specifying the `--enable-pyopenchange` flag when 
running the configure script in OpenChange.

[deven]: http://openchange.org/documentation/howto/zentyal_developer.html

# Next: OpenChange Server ##

You can now proceed to the [OpenChange Server](server.html) implementation.
