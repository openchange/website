[TOC]

# MAPIStore Message #

The MAPIStore Message object represents a message. It implements seveal methods to display and modify its properties.

## URI ##

The `get_uri` method returns a string containing the URI of a message.

        >>> my_uri = my_msg.get_uri()
        >>> print my_uri

## Properties ##

The properties of a message can be retrieved through the `get_properties` method. The method takes a list containing the requested properties (either the name of the property or the property tag) and returns a dictionary.
Each entry in the dictionary contains the property name (if available) or the property tag as key and the property value as value.
If the input entry is empty, all the available properties are listed.

        >>> prop_dict = my_msg.get_properties([0x1000001F, 'PidTagDisplayName'])
        >>> prop_dict
        {'0x36e9000a': 'Not Found', 'PidTagDisplayName': 'foomsg'}

If an error is found when retrieving the data of a property, the entry in the dictionary is formed by its associated error tag (replacing the last 16 bits by `0x000A`) as the key and the MAPIStore error as the value.

The properties of a message can be modified by using the `set_properties` method, which takes a dictionary with the same format as the output of `get_properties`.

        >>> my_fld.set_properties({'PidTagDisplayName': 'FOOMSG'})
        >>> prop_dict = my_fld.get_properties('PidTagDisplayName'])
        >>> prop_dict
        {'PidTagDisplayName': 'FOOMSG'}

# Next: Next Section #

You can now proceed to the [next](next.html) section.

