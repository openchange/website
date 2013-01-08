# HowTo Setup OpenChange Client #

[TOC]

## Create a Profile Store ##

The MAPI library requires a profile database and a profile in that
database before it can be used. The default location for the profile
database is `$HOME/.openchange/profiles.ldb` but you can define a
specific path using mapiprofile parameters:

1. To create a MAPI profile database stored at the default location:

        $ mapiprofile --newdb

2. To create a MAPI profile database at custom location:

        $ mapiprofile --database=/tmp/profiles.ldb

OpenChange tools assumes the MAPI profile database is stored in the
default location. If you specified a custom location, you must specify
the **`--database`** parameter whenever you use command line tools.

## Create a MAPI Profile ##

<br/>

### mapiprofile command line parameters ###

Creating MAPI profiles require a set of mandatory parameters described below:

Parameter    | Description
------------ | -----------
`--profile`  | the profile name used to identify the profile in the profiles database
`--username` | the username used for authentication on the Exchange server
`--password` | the password used for authenticating the user on the Exchange server
`--domain`   | the Windows domain your Exchange server belongs to
`--realm`    | the Windows realm your Exchange server belongs to
`--address`  | the Exchange server address. Can either be an IP address or a fully qualified domain name
`--create`   | the mapiprofile operation to execute

### Kerberos or NTLMv2 authentication ###

If your Windows domain is configured to use Kerberos for
authentication, mapiprofile can also use it but it has some
requirements:

1. Your workstation needs to be configured to use Kerberos

2. You **must specify a Fully qualified domain name in place of the IP
address for the `--address` parameter**

OpenChange will fallback to NTLMv2 if the intended authentication
mechanism doesn't work properly.

### Exchange below or equal 2007 ###


    $ mapiprofile --profile=testuser            \
                  --username=testuser           \
                  --password=openchange         \
                  --domain=EXCHANGE07           \
                  --realm=EXCHANGE07.LOCAL      \ 
                  --address=10.254.0.102        \
                  --create
    Profile testuser completed and added to database /home/testuser/.openchange/profiles.ldb


### Exchange 2010 specific ###

Exchange 2010 requires RPC communications to be encrypted. mapiprofile
enables this behavior through the **`--encrypt`** parameter:

    $ mapiprofile --encrypt                     \
                  --profile=testuser            \
                  --username=testuser           \
                  --password=openchange         \
                  --domain=EXCHANGE10           \
                  --realm=EXCHANGE10.LOCAL      \
                  --address=10.254.0.1          \
                  --create
    Profile testuser completed and added to database /home/testuser/.openchange/profiles.ldb


## Set the default profile ##

You can always specify the profile to use through **`--profile`**
openchange tools command line parameters. However openchange tools are
designed to work with a default profile and it is therefore convenient
to set your profile as the default one.

Assuming your profile is named testuser, you can set it as the default
profile using the **`--default`** parameter as exposed in the example
below:

    $ mapiprofile --profile=testuser --default
    Profile testuser is now set the default one

## Test the profile ##

<br/>

### List profiles and lookup default one ###

    $ mapiprofile --list
    We have 1 profiles in the database:
        Profile = testuser [default]

### Dump MAPI profile ###

    $ mapiprofile --profile=testuser --dump
    Profile: testuser
            username       == testuser
            password       == openchange
            mailbox        == /o=First Organization/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=Test User
            workstation    == test
            domain         == EXCHANGE10
            server         == 10.254.0.101

## Test openchangeclient application ##

You can now use your MAPI profile with OpenChange command
applications. For example:

1. List mailbox folders:

        $ openchangeclient --mailbox
        + Mailbox - Test User
        |---+ Calendar        :                      (Total: 0 / Unread: 0 - Container class: IPF.Appointment) [FID: 0x27d19e0000003c7c]
        |---+ Contacts        :                      (Total: 0 / Unread: 0 - Container class: IPF.Contact) [FID: 0x28d19e0000003c7c]
        |---+ Conversation Action Settings :         (Total: 0 / Unread: 0 - Container class: IPF.Configuration) [FID: 0x5bd19e0000003c7c]
        |---+ Deleted Items   :                      (Total: 0 / Unread: 0 - Container class: IPF.Note) [FID: 0x21d19e0000003c7c]
        |---+ Drafts          :                      (Total: 0 / Unread: 0 - Container class: IPF.Note) [FID: 0x29d19e0000003c7c]
        |---+ Inbox           :                      (Total: 0 / Unread: 0 - Container class: IPF.Note) [FID: 0x1ed19e0000003c7c]
        |---+ Journal         :                      (Total: 0 / Unread: 0 - Container class: IPF.Journal) [FID: 0x2ad19e0000003c7c]
        |---+ Junk E-Mail     :                      (Total: 0 / Unread: 0 - Container class: IPF.Note) [FID: 0x57d19e0000003c7c]
        |---+ Notes           :                      (Total: 0 / Unread: 0 - Container class: IPF.StickyNote) [FID: 0x2bd19e0000003c7c]
        |---+ Outbox          :                      (Total: 0 / Unread: 0 - Container class: IPF.Note) [FID: 0x1fd19e0000003c7c]
        |---+ Sent Items      :                      (Total: 0 / Unread: 0 - Container class: IPF.Note) [FID: 0x20d19e0000003c7c]
        |---+ Tasks           :                      (Total: 0 / Unread: 0 - Container class: IPF.Task) [FID: 0x2cd19e0000003c7c]

2. Fetch emails:

        $ openchangeclient --fetchmail
        MAILBOX (0 messages)
