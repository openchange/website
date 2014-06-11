# Configuration file DTD #

[TOC]

The configuration file format defined below is a draft and is not the definitive version.

OpenChangeSim configuration file is divided into 2 different sections,
including Main section which is root-level:

1. **Main**: with global configuration parameters for openchangesim tool
2. **servers**: describes the list of Exchange server openchangesim can work with
3. **scenarios**: describes the scenarios openchangesim can use

# General Syntax #

The configuration file(s) of OpenChangeSim are processed sequentially.

## Blocks ##

Blocks are used to describe a particular set of properties attached to
configuration elements. Elements are referenced as keywords and can be
of type **`server`** or **`scenario`**. A block starts with the
element type's keyword followed by a block enclosed with brackets and
ending with a semi-colon. The content of the block is a list of
variables.


        KEYWORD { ... };

## Comments ##

OCSIM files can contain comments embedded in normal C-style comment
markers. That is, a comment starts with a combination of `/` followed by
`*`, and ends with combination of `*` followed by `/`.

Anything contained with in comment markers is ignored by
OpenChangeSim, and is only for the convenience of human readers.


        /* This is a comment */


# Servers section #

This section describes the different Exchange server openchangesim can connect to.
Servers are described within a `server` block

        server {
                   name               = EXCHANGE;
                   version            = 2010;
                   address            = xxx.xxx.xxx.xxx;
                   domain             = DOMAIN;
                   realm              = REALM;
                   generic_user       = user;
                   generic_user_range = 1-1000;
                   generic_password   = "SecretPassword";
                   ip_range           = 172.16.10.1 - 172.16.40.254;
        };


## name parameter ##

Define the server section name and is used on command-line to specify
the server to use.

## version parameter ##

Specify the remote Exchange server version. Possible values for this
parameter are 2010, 2007, 2003 and 2000.  

2010, 2007, 2003 will automatically enable libmapi use of
`EcDoConnectEx`/`EcDoRpcExt2` (0xA/0xB) opnums while 2000 will
fallback to `EcDoConnect`/`EcDoRpc` (0x0/0x2).

## address parameter ##

Specify the IP address of the remote Exchange server. In future
version, usage of FQDN will be provided to enable KRB5 encryption over
ExchangeRPC pipes.

## domain parameter ##

Specify the Windows domain the remote server belongs to

## realm parameter ##

Specify the realm of the remote server

## generic_user parameter ##

Specify a username that will be used as template base for profile
creation.

## generic_user_range parameter ##

Specify the range and the number of profiles to be created/used. The
range number will be concatenated to the `generic_user` parameter to
create the Exchange account username. For example, if the
`generic_user` is `user` and the range is 1-100, then user accounts
with username `user1` to `user100` will be created.

## generic_password parameter ##

Specify the password to use for all users. OpenChangeSim assumes
accounts have been created with the same password.

## ip_range parameter ##

Specify the IP range to use for MAPI profiles. Each MAPI profile will
be assigned a unique IP address from the range. If the IP range is
smaller than the generic_user_range parameter's range, openchangesim
will display an error.

# Scenarios section #

This section describes the different parameters a scenario can use to
customize its behavior.  Servers are described within a `scenario`
block:

        scenario {
	           name         =       "sendmail";
	           repeat       =       4;

	           case {
                        name            =       "utf8 case";
                        inline_utf8     =       "Hello world, this is a very special case";
                        attachment      =       "/path/to/attachment_1";
	           };

	           case {
                        file_html       =       "/tmp/html_body.html";
                        attachment      =       "/path_to_attachment_2";
                        attachment      =       "/path_to_attachment_3";
	           };
        };


A scenario describes an action that will be executed by each unique
client. The action is described using a set of generic parameters
(that applies to any scenario) and a set of cases with custom
parameters (that are specific to a given scenario).

* By generic scenario, we understand `fetchmail` and `sendmail`.
* However only the `sendmail` scenario makes use of cases for the moment.

A scenario is described with 2 main parameters:

* **name**: identify the module name. Possible values for name are:
** fetchmail
** sendmail
* **repeat**: defines the number of times this scenario should be
    replayed for each unique client.

Cases are describing a particular way to play the scenario. The syntax
of a case is the case keyword followed by a block (enclosed with
brackets) and ending with the semi-colon termination character. Within
the case block, you can specify parameters (described below) that are
specific to each scenario.

You can add as many cases as you want. All of them will be
sequentially played within one sendmail scenario instance.

It is important to understand that **if you decribe n cases, then
sendmail will be run repeat * n times** and the user will receive
`repeat` number of mails for each case.


The current DTD let you customize the message body and the number of
attachments for the sendmail scenario.

The body can be defined differently:

## Inline body ##

The body of the message is fetched from the configuration file

* **inline_utf8**: a UNICODE plaintext body will be used for the case
    message:

        inline_utf8 = "Hello world";

* **inline_html**: an HTML body content will be used for the case
    message:

        inline_html = "<body bgcolor=\"yellow\"><h1>Example h1 title</h1></body>";


## File body ##

The body of the message is stored within an external file

* **file_utf8**: Retrieve the content of the file pointed by the
    file_utf8 directive and sends its content as a plaintext UNICODE
    body message

        file_utf8 = "/path/to/utf8_file.txt";


* **file_html**: Retrieve the content of the file pointed by the
    file_html directive and sends its content as an HTML body message.

        file_html = "/path/to/html_file.html";

Finally, you can control the attachment through the attachment directive.

## Attachments ##

You can specify as many attachment as you want for each
scenario. There is neither restriction on the file type nor on its
size. Be however aware that the sendmail scenario will fail if the
size of the specified attachment exceeds Exchange server limitations.

To specify attachments, you need to use the attachment keyword
followed by the equal sign, then the path to the attachment file and
finally a semi-colon termination character.

        attachment = "/path/to/attachment_1.jpg";

You can add as many attachment as needed:


        attachment = "/path/to/attachment_1.jpg";
        attachment = "/path/to/attachment_2.png";
        attachment = "/path/to/attachment_3.docx";
        attachment = "/path/to/attachment_4.pdf";
        attachment = "/path/to/attachment_5.zip";
        attachment = "/path/to/attachment_6.tar.gz";
