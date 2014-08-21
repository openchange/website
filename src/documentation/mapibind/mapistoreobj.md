[TOC]

# MAPIStore Object #

This object defines a set of methods with which the general MAPIStore and Openchange parameters are set.

## Object creation ##

By creating a MAPIStore object, the default parameters are loaded. The constructor takes an optional parameter, `syspath`, that specifies the route to the `smb.conf` file.


        >>> from openchange import mapistore
        >>> mstore = mapistore.MAPIStore([/path/to/smb.conf])

## MAPIStore Initialisation ##

The MAPIStore initialisation is carried out in a different method, `initialisation`, which initialises the Samba database, the Openchange database and MAPIStore. It sets afterwards the connection information for a particular user (which makes the MAPIStore object user-dependent), so the function takes a string with the user name as an argument.

*NOTE: The files needed to initialise the Openchange database are located in a private path, so Python should be called by a root user in order to fully use the MAPIStore Python bindings.*

        >>> mstore.initialize('user1')

## Parameter Display & Modification ##

The parameters of the MAPIStore object can be printed by calling the `dump` method. The `set_parm` method can change the value of these parameters. The arguments taken by `set_parm` are two strings: the modified parameter and its new value.

        >>> mstore.dump()
        >>> mstore.set_parm('option1', 'value')

One of the parameters displayed by dump is `log_level`, exposed to Python as an attribute of the MAPIStore object named `debuglevel`. Its value is an integer number that acts as a threshold for the verbosity of certain functions.
In the example, this parameter could be set the following way:

        >>> mstore.debuglevel = 3

## Backend & Capabilities List ##

A MAPIStore object can display the available backends for its user and the contexts (root folders) that can be opened for each backend. This is achieved by calling the `list_backends` and `capabilites` methods, respectively.

        >>> mstore.list_backends()
        >>> mstore.capabilities()

The return value of `list_backends` is a list with the available backends, while `capabilities` returns a list of dictionaries, one for each available backend. Each dictionary has four entries with properties of a context: the name, the URI, the role and the main folder.

## Adding a Context ##

In order to add a new context, a context URI is provided. If this URI is not known beforehand, it can be found by calling `capabilities`. On success, the `add_context` method returns the URI's MAPIStore context as a Python object. 

        >>> my_ctx = mstore.add_context('my_uri')

# Next: MAPIStore Contexts #

The methods implemented by the MAPIStore Context object can be found in the [Next section](mapistorectx.html)
