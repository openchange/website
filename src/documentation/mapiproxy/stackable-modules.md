<div style="float: right; width: 35%;margin-left:2em;">
<img src="/images/mapiproxy/mapiproxy.png" alt="MAPIProxy Logo"/>
</div>

# Stackable Modules #

[TOC]

## General Overview ##

The MAPIProxy stackable modules system provides implementers a
development framework to add new features. This stackable mechanism
allows developers to write modules with a very specific scope of 
which modifications will transparently be relayed to the next module
until it is finally pushed by MAPIProxy to
the next hop (Figure 3.).

!["MPM Stack"](/images/mapiproxy/mpm_stack.png "Figure 3. MAPIProxy module stack and EcDoRpc interaction")

With this system, developers can focus their effort on ExchangeRPC
traffic - or any other protocol samba supports - interception,
modification, analysis and avoid spending time on implementing a new
endpoint server. Furthermore it provides an easier way for
implementers to divide the work in smaller units and develop each of
them in a separated module.
<br/>

MAPIProxy modules are dynamic shared objects with an entry point and a
limited set of hooks. These modules have to be installed in the
`dcerpc_mapiproxy` folder within the samba4 modules directory
(e.g. _/usr/local/samba/modules_). MAPIProxy modules specified
in the Samba configuration file (smb.conf) will be loaded into MAPIProxy
at runtime and interact with each other in the same order they were
defined:

	dcerpc_mapiproxy:modules = downgrade,dummy

All MAPIProxy modules will be registered but only those specified on
the **`dcerpc_mapiproxy:modules`** parametric option line
will be added to the chained list of effective modules.
<br/><br/>


## Module entry point ##

MAPIProxy modules must have an entry point function named
**`samba_init_module`**. This function needs to set general
information about the module, specify the module's hooks and finally
call the **`mapiproxy_module_register`** function to
register itself in the MAPIProxy module subsystem.

    0.     NTSTATUS samba_init_module(void)
    1.     {
    2.     	struct mapiproxy_module	module;
    3.     	NTSTATUS		ret;
    4.     
    5.     	/* Fill in our name */
    6.     	module.name        = "sample";
    7.     	module.description = "A sample module";
    8.     	module.endpoint    = "any";
    9.     
    10.    	/* Fill in all the operations */
    11.    	module.init     = sample_init;
    12.    	module.push     = sample_push;
    13.    	module.ndr_pull = sample_ndr_pull;
    14.    	module.pull     = sample_pull;
    15.    	module.dispatch = NULL;
    16.    	module.unbind   = NULL;
    17.    
    18.    	/* Register ourselves with the MAPIPROXY subsytem */
    19.    	ret = mapiproxy_module_register(&module);
    20.    	if (!NT_STATUS_IS_OK(ret)) {
    21.    		DEBUG(0, ("Failed to register 'sample' mapiproxy module!\n"));
    22.    		return ret;
    23.    	}
    24.    
    25.    	return ret;
    26.    }


Module structure field | Description
---------------------- | -----------
**module.name ** | This is the module name. This name will be used by `dcerpc_mapiproxy:modules` in `smb.conf` to load the module
**module.description** | This field lets developers specify a brief module description for information purpose only.
** module.endpoint ** | This field defines the interface which this module is designed to work with. The primary objective is to avoid calling the module hooks if the module doesn't have any impact on the requests or replies. For example, a module only interacting with the EcDoRpc function should define `exchange_emsmdb`.<br> In the meantime, it can happen that a module requires to interact with more than a single interface. In such case, use the '**any**' keyword which will call the modules functions with any endpoints proxied by MAPIProxy.

<br/><br/>

## Module Hooks ##

MAPIProxy offers a set of hooks which modules can implement to
modify/change/alter client to server MAPI traffic. The figure below
shows how and when hooks are called during a request/response
lifetime.

!["MAPIProxy Hook Life Cycle"](/images/mapiproxy/mapiproxy_hook_life.png "Figure 4. Usage of MAPIProxy Hooks during a request/response life time")

<br/>

Hook name | Description
--------- | -----------
**init** | This is the initialization function for the module which is only called once - when the module is loaded. It is generally used to retrieve `smb.conf` parametric options for the module and initialize some global structures
**pull** | This is the function called when MAPIProxy receives a MAPI request. The request has already been extracted and its information filled into MAPI structures
**push** | This is the function called when MAPIProxy receive a MAPI response. The response has already been extracted and its information filled into MAPI structures.
**dispatch** | Similarly to the MAPIProxy top-level dispatch function, it is used to dispatch the information. This function is called after the `pull` but before the `push`. Moreover it is called before the request is forward to the remote endpoint.
**ndr_pull** | This is the function called before data from a request is extracted from the NDR blob.
**ndr_push** | This is the function called before data from a response is extracted from the NDR blob.
**unbind** | This is the function called when the connection closes. It can be used to free data associated to a given session and stored within a module global list.

<br/><br/>

## mapiproxy structure ##

MAPIProxy uses a structure modules can modify in their dispatch
routine and which impact on the general MAPIProxy behavior.

![MAPIProxy Structure](/images/mapiproxy/mapiproxy_struct.png "Figure
 5. overview of mapiproxy structure variables scope")

* **norelay**: This boolean variable can be used by modules to tell
MAPIProxy not to relay the incoming **request** to the remote server
through `dcerpc_ndr_request()` but directly jump to the push
(response) MAPIProxy code. This variable is for example in use within
the cache module when we read stream from the local filesystem and
play it back to MAPI clients.

* **ahead**: This boolean variable can be used by modules to tell
MAPIProxy not to relay the incoming **response** to the client through
the `push` and `dcerpc_ndr_request` routine but loop over
the dispatch routine. This variable is for example in use within the
cache module when we want to read a stream ahead from Exchange server
to the remote MAPIProxy instance.
