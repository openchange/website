[TOC]

# MAPIStore Table #

A MAPIStore Table object allows the visualisation of a folder's contents as a
table. Each row in the table represents a child of the parent folder, and the
columns represent the different properties of the children. When a table is
opened, the table type is specified, so only children of a certain kind are
taken into account (e.g. subfolders, messages...).
The MAPIStore Table object implements different methods to display the
information contained in the rows and to set the properties that are displayed.

## Row count ##

The `count` attribute of a MAPIStore Table object can be accessed directly, and
contains the number of rows in the table.

        >>> msg_tbl = my_fld.open_table(mapistore.MESSAGE_TABLE)
        >>> print msg_tbl.count

Is equivalent to

        >>> print my_fld.get_child_count(mapistore.MESSAGE_TABLE)

## Set columns ##

The `set_columns` method sets the properties that each column represents. The
method takes a list of property names (as *strings*) or tags (as *integers*)
and updates the columns of the table.

        >>> fld_tbl.set_columns(['PidTagLastModificationTime', 0x67480014])

## Rows ##

A single row can be retrieved through the `get_row` method, which takes as an
argument the row number and returns a dictionary with the format `{'property':
value}`. It is also possible to access the `rows` attribute, an iterator that 
allows looping over the rows.

        >>> for r in fld_tbl.rows:
        >>>     print r

Is equivalent to

        >>> for i in range(0, fld_tbl.count):
        >>>     print fld_tbl.get_row(i)

# Next: MAPIStore Attchments #

The next section describes the [MAPIStore Attachment](mapistoreatt.html) implementation.
