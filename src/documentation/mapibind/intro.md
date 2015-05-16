[TOC]

# Introduction #

<br/>
## Purpose and Scope ##

The MAPIStore Python bindings aim to provide a way to access and test the 
[MAPIStore C library](../programming/mapistore_python/concepts.html) using 
Python. 

## Source Code & Installation ##

MAPIStore is the *SAL* (Storage Abstraction Layer) of the OpenChange project, 
which is placed on <https://github.com/openchange/openchange>. The source 
code of the bindings can be found at

        /path/to/openchange/pyopenchange/mapistore

After [initialising the environment][initialising] and [downloading the source][downloading],
the MAPIStore Python Bindings can be installed by [building the source regularly][building],
but changing the configure command:

        CFLAGS='-g -O0' LDFLAGS=-Wl,--as-needed ./configure  --prefix=/usr --mandir=/usr/share/man -- enable-pyopenchange --with-modulesdir=/usr/lib/x86_64-linux-gnu/openchange --libdir=/usr/lib/x86_64-linux-gnu; sed -i -e 's/site-packages/dist-packages/' config.mk

[initialising]: http://openchange.org/cookbook/initializing.html
[downloading]: http://openchange.org/cookbook/downloading.html
[building]: http://openchange.org/cookbook/building.html


## Useful background ##

The following links can provide useful background to understand the MAPIStore 
bindings.

  *  The [MAPIStore 1.0 Development guide][devguide].
  *  [Extending and Embedding the Python Interpreter][extending] and 
      [How to write a Python Extension][howtowrite].
  *  The [talloc Tutorial][tutorial].

[devguide]: http://tracker.openchange.org/projects/openchange/wiki/MAPIStore_10_Development_Guide
[extending]: https://docs.python.org/2/extending/index.html
[howtowrite]: http://starship.python.net/crew/arcege/extwriting/pyext.html
[tutorial]: https://talloc.samba.org/talloc/doc/html/libtalloc__tutorial.html

It is also strongly recommended to take a look to the MAPIStore source code,
located at

        /path/to/openchange/mapiproxy/libmapistore

# Next: Type Definition #

Proceed to [MAPIStore Object](mapistoreobj.html).
