# General Concepts #

[TOC]

# What is MAPIStore #

MAPIStore is the Software Abstraction Layer (SAL) storage component
for OpenChange server. It is the component used by OpenChange Server
to push/get information (messages, folders) to/from storage
backends. It is designed as a library called within OpenChange Server
and it accesses backends compiled as dynamic shared object (DSO) or
interpreted as Python scripts and loaded when mapistore is
initialized.

The main objective of mapistore is to provide an interface layer with
a common set of atomic functions (operations) used to trigger and
dispatch data and commands to the appropriate backend. MAPIStore
relies on a backend mechanism specifically designed to transparently
handle some of the MAPI semantics required by any Exchange compatible
server.

The initial idea was to provide to OpenChange a highly customizable
storage backend mechanism which would fit in any situation and any
environments. One of the greatest limitation we have found with
existing groupware is the storage layer which is generally limited to
a single solution, service or format and is neither scalable nor
modifiable when user requirements evolve upon time.

MAPIStore solves this problem and go beyond classical limitations. It
is not a revolutionary concept, but the way openchange uses it makes
the whole difference and offer administrators an innovative way to
customize storage.

MAPIStore allows you to:

* use a different backend for any top-folder
* transparently move/copy data across backends
* develop new backends quickly
* access all the different backends through an unique API

For example (assuming all associated backends were developed) a user
could have the following storage organization for his mailbox:

* Mails stored using an IMAP backend (Cyrus-IMAP or dovecot)
* Calendar items stored in CalDAV or pushed in Google calendar
* Sent emails and archives/backup stored in a compression backend
* Tasks stored in a MySQL database
* Notes stored on the filesystem

Information can be completely decentralized, stored on one of several
servers and still be accessible transparently from OpenChange server.


# MAPIStore architecture overview #

<br/>

## URI and Scope ##

__A URI is the key (and only) element mapistore and calling applications
rely on in order to access and perform operation on a specific
backend.__

It is made of a prefixing namespace followed by data specific to the
backend:


### namespace

This is the __unique identifier__ associated to your backend. It is
the combination of your backend's name followed by __://__. If you
write a backend named _sample_, the namespace would therefore be:

        sample://


### backend's specific data

This is a set of data that doesn't have any meaning for the calling
application but is relevant for the backend. While the format of this
data is completely specific to your backend, backends generally set
information such as username, password or folder name within the
destination system the backend manages.

## Contexts ##

A Microsoft Exchange user mailbox is represented as a top folder (the
mailbox name) holding root (sub) folders (Inbox, Outbox, Calendar,
Contacts, Notes, Tasks etc.). In MAPIStore, we consider that we
shouldn't have to use the same backend for everything. We should be
able to use a backend for Inbox, another for Calendar and so on.

This is where the notion of mapistore context steps in. __A context is
a sandbox created by a backend__ when you access root folder. For
every operation you perform on this root folder or any data within
this folder, the same created context will be used. For example, if we
want to open a specific message in _/Inbox/Holidays/_, we will:

1. Create a context for Inbox when we open the folder
2. Open the Holidays folder using the Inbox context
3. Access the message using the Inbox context

If the backend attached to my Inbox points to an IMAP server, all the
operation performed on Inbox and subfolders will be propagated to this
IMAP server. In this case, creating a context would mean:

1. Open a connection on the IMAP server
2. Open the Inbox folder
3. Keep the connection opened and save parameters this IMAP backend
needs to access/interact with physical (folder, message) or virtual
(tables) elements stored within this Inbox folder.
