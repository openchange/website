[TOC]

# MAPIStore Context #

The objects of this class are children of a MAPIStore object and represent a 
MAPIStore context, a root folder (e.g. Inbox, Calendar or Notes) of a Mailbox
associated to a particular backend.

## Opening the root folder ##

A context can be seen as the root folder of a particular backend. The 
`open_folder` method returns this root folder as a MAPIStore folder object.

        >>> my_root_fld = my_ctx.open()

# Next: MAPIStore Contexts #

The methods implemented by the MAPIStore Folder object can be found in the 
[MAPIStore Folder](mapistorefld.html) section.
