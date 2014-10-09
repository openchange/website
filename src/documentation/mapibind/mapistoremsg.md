[TOC]

# MAPIStore Message #

The MAPIStore Message object represents a message. It implements several methods
to display and modify its properties.

## URI ##

The MAPIStore Message object has an attribute that contains its URI.

        >>> my_uri = my_msg.uri()
        >>> print my_uri

## Message Data ##

The `get_data` method takes no arguments and returns the message data stored in
a dictionary. The entries in the dictionary are the following:

 - `Subject prefix`: *String* with the subject prefix
 - `Normalized priefix`: *String* with the normalized subject
 - `Recipient columns`: *List of strings* containing the available properties
     for the recipients, each one represented by either its property tag name
     (e.g. 'PidTagSmtpAddress') or its property tag value in hexadecimal (e.g.
     '`0x39FE001F`')
 - `Recipient count`: *Integer* with the number of recipients
 - `Recipient data`: *List of dictionaries* with the data of each recipient. The
     entries contain the available properties' names/tags and values, plus the
     recipient's username (as a *string*) and it's type (as a *long integer*)
 
## Properties ##

The properties of a message can be retrieved through the `get_properties`
method. The method takes a list containing the requested properties (either the
name of the property or the property tag) and returns a dictionary. Each entry
in the dictionary contains the property name (if available) or the property tag
as key and the property value as value. If the input entry is empty, all the
available properties are listed.

        >>> prop_dict = my_msg.get_properties([0x1000001F, 'PidTagDisplayName'])
        >>> prop_dict
        {'0x36e9000a': 'Not Found', 'PidTagDisplayName': 'foomsg'}

If an error is found when retrieving the data of a property, the entry in the
dictionary is formed by its associated error tag (replacing the last 16 bits by
`0x000A`) as the key and the MAPIStore error as the value.

The properties of a message can be modified by using the `set_properties`
method, which takes a dictionary with the same format as the output of
`get_properties`.

        >>> my_fld.set_properties({'PidTagDisplayName': 'FOOMSG'})
        >>> prop_dict = my_fld.get_properties('PidTagDisplayName'])
        >>> prop_dict
        {'PidTagDisplayName': 'FOOMSG'}

## Save messages ##

The `save` method commits the changes made to a message in MAPIStore.

        >>> my_msg = my_fld.create_message(mapistore.CREATE_GENERIC)
        >>> my_msg.set_properties({'PidTagSubject': 'mymsg', 'PidTagNormalizedSubject': 'mymsg', 'PidTagBody': 'Hello, World!'})
        >>> my_msg.save()


## Attachments ##

A MAPIstore Message object can handle its attachments and iterate over them (see
the [MAPIStore Attachment](mapistoreatt.html) section). The `create_attachment`
method, which takes no arguments, creates an attachment for the message and
returns a MAPIStore message object. In a similar way, an attachment can be
opened by calling the `open_attachment` method, which takes an integer with the
attachment number as an argument. The MAPIStore Message object has an attribute
from which the number of attachments can be read.

        >>> print my_msg.attachment_count
        1L
        >>> existing_att = my_msg.open_attachment(0)
        >>> new_att = my_msg.create_attachment()
        >>> print my_msg.attachment_count
        2L

## Get attachment table ##

Attachments' properties can be visualised through a table by calling the
`get_attachment_table` method, which returns a MAPIStore Table object with
these properties.

        >>> att_tbl = my_msg.open_attachment_table(mapistore.MESSAGE_TABLE)

# Next: MAPIStore Tables #

The section describes the [MAPIStore Table](mapistoretbl.html) implementation:.
