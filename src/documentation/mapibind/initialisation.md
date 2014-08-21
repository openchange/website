[TOC]

# Ititialisation and parameter setting#

<br/>

## The `initialize` method ##

The initialisation of the *MAPIStore* context `mstore_ctx` is carried out in a different method from the `new` one. This way, MAPIStore can be initialised with non-default parameters by calling the `set_parm` method.

        static PyObject *py_MAPIStore_initialize(PyMAPIStoreObject *self, PyObject *args)

This method initialises the *Openchange* LDB trying to use MySQL as backend (if it fails, it uses the default backend), and then it initialises *MAPIStore*. The method takes an optional argument, `path`, used to specify the location of the backend providers. If no argument is provided, `NULL` is passed to the `mapistore_init` function and the default path is set.

<br/>

## Setting the parameters ##

This method allows Python to modify the parameters stored in the *loadparm* context.

        static PyObject *py_MAPIStore_set_parm(PyMAPIStoreObject *self, PyObject *args)

It takes two arguments, `option` and `value`, and sets the value in an option of the *loadparm* context.

<br/>

## Listing the parameters ##

The fields in the *loadparm* context and their values can be listed (depending on the access permits) by calling the `dump` function, which takes no arguments.

        static PyObject *py_MAPIStore_dump(PyMAPIStoreObject *self, PyObject *args)

# Next: Next Chapter #

Proceed to to the [Next Chapter](next.html).
