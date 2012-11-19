# Current Roadmap #

[TOC]

# openchange-1.5 VOYAGER #

Forthcoming `openchange-1.5` release is a key step in OpenChange
development. It will achieve and maintain current client and server
code but will also provide the background required for openchange-2.0
API changes and associated features development.

<br/>

## libmapirops ##

This library packs and unpacks MAPI Rops and MAPI data. This will
replace the MAPI NDR IDL auto-generated code, with a hand-written
stack reviewed using Microsoft Exchange Protocols specifications and
coupled to unit testing and documentation

## Unit testing ##

This new release will provide a set of API level unit tests for
libmapirops to ensure full API stability and compliance to
specifications. subunit and check will be used for this task.

## Documentation ##

Doxygen documentation for libmapirops will extensive coverage of each
function, enum or data structure.

## Waf build system ##

OpenChange will migrate from autoconf/automake to waf build system
which should improve compilation speed and enable OpenChange to
compile individual parts of OpenChange for components releases
purposes.

## Branches Merge ##

Pending changes from other branches will be reviewed and merged within
master to offer the higher level of compatibility with projects
depending on OpenChange to provide Exchange compatibility.

<br/>

# openchange-2.0 OBSERVER #

No public information is yet available for 2.0 OBSERVER release of
openchange.
