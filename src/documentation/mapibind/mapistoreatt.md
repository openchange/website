[TOC]

# MAPIStore Attachment #

The attachments of a message have their own class in the MAPIstore Python
bindings. Each attachment in a message has an associated identifier. In
oppsition to FMIDs, they are represented by a 32-bit unsigned integer (instead
of a 64-bit one), and they aren't unique to the entire system (attachments of
different messages can have the same ID). Furthermore, the IDs of the
attachments in a message are consecutive and start on 0.

## Properties ##

Attachments have properties as well, and these can be set and displayed by
calling the `set_properties` and `get_properties` methods, which work the same
way as in MAPIStore folders or messages.

        >>> my_att.set_properties({'PidTagAttachFilename': 'foo.txt'})
        >>> prop_dict = my_att.get_properties(['PidTagAttachFilename'])
        >>> prop_dict
        {'PidTagAttachFilename': 'foo.txt'}
