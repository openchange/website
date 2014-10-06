[TOC]

# MAPIStore Attachment #

The attachments of a message have their own class in the MAPIstore Python bindings.
Each attachment in a message has an associated identifier.
In oppsition to FMIDs, they are represented by a 32-bit unsigned integer (instead of a 64-bit one), and they aren't unique to the entire system (attachments of different messages can have the same ID).
Furthermore, the IDs of the attachments in a message are consecutive and start on 0.

## Properties ##

Attachments have properties as well, and these can be displayed by calling the `get_properties` method, which works the same way as in MAPIStore folders or messages.

        >>> prop_dict = my_fld.get_properties(['PidTagAttachFilename', 0x0E210003])
        >>> prop_dict
        {'0x36e9000b': False, 'PidTagDisplayName': 'foo'}

