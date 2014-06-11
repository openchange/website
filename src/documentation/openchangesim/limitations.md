# Limitations #

[TOC]

## Packed MAPI calls ##

Outlook is using packed MAPI calls in some circumstances to save
bandwidth and limit the number of network transactions. These packed
calls are generally generated when a transaction deals with the same
object and when all operations are subsequently related one to each
other. OpenChange implements a 1 MAPI call / 1 packet transaction
model. Offering the ability to move from the existing model to the
Outlook default one is however doable within a very reasonable amount
of time and few more API calls.

## Thread support for concurrent flows ##

OpenChange client side libraries are able to deal with concurrent
connections and its model is compliant with threaded application. A
pending patch is available on the list and requires a review before
integration. This feature is required to efficiently generate any
number of parallel MAPI data flows within a given authenticated user
context.

## Cached mode and FXICS implementation ##

When Outlook is configured with cached mode enabled, it retrieves
email and updates its local PST/OST files using FXICS. It is a Fast
Transfer Buffer used in Incremental Synchronization Changes. Depending
if clients are using online mode (which is preferable for security and
in critical environment) or use cached mode for better local
performances, this scenario may be of interest. This part of the
Exchange protocol is the last OpenChange doesn’t yet implement.