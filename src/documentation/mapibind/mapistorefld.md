[TOC]

# MAPIStore Folder #

This object represents a folder and implements several methods to display its information and open, create, move and delete  messages and subfolders.

## URI ##

The `get_uri` method returns a string containing the URI of a folder.

        >>> my_uri = my_fld.get_uri()
        >>> print my_uri

## Properties ##

The properties of a folder can be retrieved through the `get_properties` method. The method takes a list containing the requested properties (either the name of the property or the property tag) and returns a dictionary.
Each entry in the dictionary contains the property name (if available) or the property tag as key and the property value as value.
If the input entry is empty, all the available properties are listed.

        >>> prop_dict = my_fld.get_properties([0x36e9000b, 'PidTagDisplayName'])
        >>> prop_dict
        {'0x36e9000b': False, 'PidTagDisplayName': 'foo'}

If an error is found when retrieving the data of a property, the entry in the dictionary is formed by its associated error tag (replacing the last 16 bits by `0x000A`) as the key and the MAPIStore error as the value.

The properties of a folder can be modified by using the `set_properties` method, which takes a dictionary with the same format as the output of `get_properties`.

        >>> my_fld.set_properties({'PidTagDisplayName': 'FOO'})
        >>> prop_dict = my_fld.get_properties([0x36e9000b, 'PidTagDisplayName'])
        >>> prop_dict
        {'0x36e9000b': False, 'PidTagDisplayName': 'FOO'}
 
## Child Count ##

The number children of a folder can be accessed by calling the `get_child_count` method. A flag argument specifies the kind of children taken into account:

 - `FOLDER_TABLE` returns the number of *child folders*.
 - `MESSAGE_TABLE` returns the number of *child messages*.
 - `MAPISTORE_FAI_TABLE` returns the number of *associated messages*.
 - `MAPISTORE_RULE_TABLE` returns the number of *child rule tables*.
 - `MAPISTORE_ATTACHMENT_TABLE` returns the number of *child attachment tables*.
 - `MAPISTORE_PERMISSIONS_TABLE` returns the number of *child permissions tables*.

        >>> fld_child_count = my_fld.get_child_count(mapistore.FOLDER_TABLE)
        >>> msg_child_count = my_fld.get_child_count(mapistore.MESSAGE_TABLE)
        >>> at_table_child_count = my_fld.get_child_count(mapistore.MAPISTORE_ATTACHMENT_TABLE)

## Child Folders  ##

It is possible to handle the child folders by calling the `get_child_folders` method, which returns an iterable object.

        >>> it_fld = my_fld.get_child_folders()
        >>> for f in it_fld:
        >>>     f_name = f.get_properties(['PidTagDisplayName'])['PidTagDisplayName'] 
        >>>     f_uri = f.get_uri() 
        >>>     print 'FOLDER NAME: ' + f_name
        >>>     print 'URI: ' + f_uri
        >>>     print
 
The child folders can be looped over through the returned object, and the implemented operations can be performed on them.

## Open, create and destroy subfolders ##

Subfolders can be created by calling the `create_folder` method, which takes a string with the name of the folder as an argument.
Optionally, a string with a description of the folder and a flag with the type of folder (`FOLDER_GENERIC`, by default, or `FOLDER_SEARCH`) can be passed to the method.
The function creates the new folder in the backend and returns a MAPIStore Folder object that allows us to handle the new folder.

        >>> new_subfld = my_fld.create_folder('foo', 'foo desc', mapistore.FOLDER_GENERIC)

If there are existing subfolders, they can be opened by using the `open_folder` method, which takes a string containing the subfolder's URI as an argument. It returns a MAPIStore folder object with the parameters of the subfolder.

        >>> existing_subfld = my_fld.open_folder('example://existing_fld_uri')

The `delete` method deletes a folder in MAPIStore. The method takes a flag as an optional argument, which specifies the way subfolders and child messages are handled:

 - `DEL_MESSAGES` deletes the messages (both generic and associated) contained in the folder.
 - `DEL_FOLDERS` deletes the subfolders in the folder.
 - `DEL_ALL`, which is equivalent to `DEL_MESSAGES | DEL_FOLDERS`, deletes all the messages and subfolders.

The default behaviour is to raise an error if the folder contains any messages or folders. If a flag is provided, the children of the specified type don't raise the error. 

        >>> new_subfld.delete(mapistore.DEL_ALL)
        >>> del new_subfld

*NOTE: The `delete` method does not destroy the Python folder object, so the user remains responsible of that.*

## Move and copy folders ##

The `move_folder` and `copy_folder` methods allow messages to be moved and copied through folders, respectively. Both take as arguments the target folder object and the name of the new folder.
An extra argument can be passed `copy_folder`, a flag that to request a recursive (`RECURSIVE`, by default) or non-recursive (`NON_RECURSIVE`) copy.
Neither method returns a MAPIStore Folder object, so the `open_folder` method needs to be used in order to get one.

        >>> my_fld.move_folder(my_other_fld, 'MOVED')
        >>> moved_fld = my_other_fld.open_folder('example://URI_of_MOVED/')
        >>> moved_fld.copy_folder(my_fld, 'COPIED_BACK', mapistore.RECURSIVE)

*NOTE: As in `delete`, `move_folder` doesn't destroy the Python folder object.*

## Child Messages ##

In a similar way to `get_child_messages`, the child messages can be handled and iterated over by calling `get_child_messages`.

        >>> it_msg = my_fld.get_child_messages()
        >>> for m in it_msg:
        >>>     m_uri = m.get_uri()
        >>>     print `URI: ` + m_uri

*NOTE: When using the iterator returned by `get_child_messages`, the messages are opened in read-only mode.*

## Open, create and destroy messages ##

If a folder contains messages, the parent folder can open and destroy them by using the `open_message` and `delete_message` methods, respectively.
Both of them take the message's URI as an argument (this way, a MAPIStore Message object doesn't need to be created in order to destroy a folder).

        >>> my_msg = my_fld.open_message('example://URI_of_msg1', mapistore.OPEN_WRITE)
        >>> my_fld.delete_message('example://URI_of_msg2', mapistore.PERMANENT_DELETE)

Messages can be opened in read-only mode or in read-and-write mode. An optional argument in `open_message` specifies the permissions of the message object (`OPEN_READ`, by default, or `OPEN_WRITE`).
If the backend implements soft deletion, a flag can be passed to `delete_message` to specify the type of deletion (`PERMANENT_DELETE`, by default, or `SOFT_DELETE`).

## Move and copy messages #

A parent folder can copy and move several messages at a time. Both `copy_messages` and `move_messages` methods take a list of URIs and a target MAPIStore Folder object, and performs the copy/move operation between the parent and the target folder.

        >>> my_fld.move_messages(['example://URI_of_msg1', 'example://URI_of_msg2'], my_other_fld)
        >>> my_other_fld.copy_messages(['example://URI_of_msg1_copy', 'example://URI_of_msg2_copy'], my_fld)

# Next: MAPIStore Messages #

The next section covers the [MAPIStore Message](mapistoremsg.html) implementation.
