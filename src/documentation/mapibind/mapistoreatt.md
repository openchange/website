[TOC]

# MAPIStore Attachment #

The attachments of a message have their own class in the MAPIstore Python
bindings. Each attachment in a message has an associated identifier. In
oppsition to FMIDs, they are represented by a 32-bit unsigned integer (instead
of a 64-bit one), and they aren't unique to the entire system (attachments of
different messages can have the same ID) but to their parent message.
Furthermore, the IDs of the attachments created in a message are consecutive,
starting from 0. The IDs aren't reused, so the deletion of attachments can
alter this order.

## Attachment ID ##

The MAPIStore Attachment object has an attribute that contains its AID.

        >>> my_aid = my_att.aid
        >>> print my_aid

## Properties ##

Attachments have properties as well, and these can be set and displayed by
calling the `set_properties` and `get_properties` methods, which work the same
way as in MAPIStore folders or messages.

        >>> my_att.set_properties({'PidTagAttachFilename': 'foo.txt'})
        >>> prop_dict = my_att.get_properties(['PidTagAttachFilename'])
        >>> prop_dict
        {'PidTagAttachFilename': 'foo.txt'}

## Save ##

Saving attachments works the same way as message saving: the `save` method
commits the changes made in an existing attachment and updates the parent
message information when the attachment has been created.

        >>> my_att = my_msg.create_attachment()
        >>> my_msg.attachment_count
        0L
        >>> my_att.save()
        >>> my_msg.attachment_count
        1L
