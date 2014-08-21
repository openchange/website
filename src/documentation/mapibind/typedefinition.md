[TOC]

# Type Definition #

<br/>

## Initialisation Function ##

The `initmapistore` function initialises the type and adds it to the module dictionary, allowing us to create MAPIStore instances in Python by calling its class.

        >>> from openchange import mapistore
        >>> mapi = mapistore.MAPIStore([<syspath>])

<br/>

## Data attributes ##

The *MAPIStoreObject* type has four data attributes: a *talloc* context and two contexts hanging off it: a *loadparm* context and a *MAPIStore* context. It has an additional attribute that definies de debug level of the methods, and which can be set directly from python.

        typedef struct {
          PyObject_HEAD
          TALLOC_CTX                    *mem_ctx;
          loadparm_context              *lp_ctx;
          struct mapistore_context      *mstore_ctx;
          int                           debuglevel;
        } PyMAPIStoreObject;

There are also three global variables. `datetime_module` and `datetime_datetime_class` are set during the initialisation of the type, while `ocdb_context` is set during the initialisation of the *Openchange* LDB.

        typedef struct {
        PyObject                        *datetime_module;
        PyObject                        *datetime_datetime_class;
        struct openchangedb_context     *ocdb_ctx;
        } PyMAPIStoreGlobals;

- - -

> *Explain the two first global variables a bit more*

> *The *structs* are defined in a header file. In the existing bindings' header file `PyAPI_DATA(PyTypeObject) PyMAPIStore` appears, and I haven't found clear information about what this does.

- - -



<br/>

## `New` Method ##

This method is responsible of creating objects of the type with the default initial parameters. 

        static PyObject *py_MAPIStore_new(PyTypeObject *type, PyObject *args, PyObject *kwargs)

When a new PyMAPIStore object is created in Python, this method is executed. It basically returns an object with an initialised *talloc* context, a *loadparm* context initialised to the default values and an empty *MAPIStore* context. It takes an optional argument, `syspath`, that specifies the route to the `sam.conf` file.

<br/>

## Destructor ##

The deallocation method frees/releases the attributes in the type by calling their respective destructors. Then, it calls `PyObject_Del` to free the object's memory.

        static void MAPIStore_dealloc(PyObject *_self)
<br/>

# Next: Initialisation #

Proceed to [Initialisation](initialisation.html)
