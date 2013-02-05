# Current Roadmap #

[TOC]

# openchange-2.5 PRECOG #

Forthcoming `openchange-2.5` release is a key step in OpenChange
development. It aims at providing the technology required for
openchange-3.0 API changes and associated features development.

Note that the roadmap is not frozen and intermediate version may be
released upon completion of important features.

<br>

## OpenChange Features ##

<br>

### Mailbox folders translation ###

Upon first user connection or when MAPI client updates its codepage,
folder names of the user's mailbox should be updated to reflect the
new chosen language.

## OpenChange Engineering ##

<br>

### mapirops IDL compiler ###

mapirops is a compiler that builds a stack designed to pack and unpack
MAPI operations (rops) and MAPI content. This technology is the core
of OpenChange networking and is a candidate for replacing the existing
MAPI buffering implementation relying on Samba. The mapirops compiler
aims at providing a similar approach but with different outcomes.

First it makes use of its own description language while implementing
a grammar similar to Samba IDL files and in particular to the existing
OpenChange MAPI IDL. Secondly, it implements a specific set of
(compatible) keywords and primitive types chosen for this OpenChange
language offering an easy migration path and reduces the overall
effort.

Finally the compiler is responsible for generating code that
automatically build and process MAPI buffers. The immediate benefit in
having MAPI content as a buffer is the introduction of a semantic and
physical distinction between content and RPC transport. This offers an
immediate solution working around existing NDR limitations with MAPI,
building a dedicated logging channel, limiting the number of
dependencies and finally making the core networking design cleaner.

### logging channels ###

The objective of the new logging channel implementation is to separate
Samba logging from OpenChange one and provides separate channels
depending on the level of severity (message, warn and error) through
syslog. This development should also lead in a small guide on
OpenChange logging for developers. The new implementation should be
compliant with the requirements of production systems.

### build system migration to waf ###

OpenChange will migrate from autoconf/automake to waf build system
which should improve compilation speed and enable OpenChange to
compile individual parts of OpenChange for components releases
purposes.

<br/>

# openchange-3.0 OBSERVER #

No public information is yet available for 3.0 OBSERVER release of
openchange.
