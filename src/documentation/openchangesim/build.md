# Build the Source #

[TOC]

## Dependencies ##

OpenChangeSim depends on:

* libmapi: OpenChange client libraries, 
* Samba DCERPC libraries (installed as part of libmapi package)
* libtalloc
* libpopt
* flex/bison

## Compile the software ##

        $ ./bin/waf configure build

If you have all the requirements installed but still encounter
configure issue similar to:

        Checking for talloc 2.0.7                 : not found

It probably means you need to adjust `PKG_CONFIG_PATH` environment
variable. Assuming you have followed OpenChange cookbook and installed
OpenChange and Samba within `/usr/local/samba@ prefix`:

        $ export PKG_CONFIG_PATH=/usr/local/samba/lib/pkgconfig:$PKG_CONFIG_PATH
        $ ./bin/waf configure build

## Sample compilation output ##

        $ ./bin/waf distclean configure build
        'distclean' finished successfully (0.006s)
        Setting top to                           : /home/ocsim/openchangesim 
        Setting out to                           : /home/ocsim/openchangesim/build 
        Checking for 'gcc' (c compiler)          : /usr/bin/gcc 
        Checking for header sys/types.h          : yes 
        Checking for header sys/mman.h           : yes 
        Checking for header sys/stat.h           : yes 
        Checking for header sys/ioctl.h          : yes 
        Checking for header syslog.h             : yes 
        Checking for header stdio.h              : yes 
        Checking for header stdlib.h             : yes 
        Checking for header stdbool.h            : yes 
        Checking for header stdarg.h             : yes 
        Checking for header unistd.h             : yes 
        Checking for header stdarg.h             : yes 
        Checking for header signal.h             : yes 
        Checking for header net/if.h             : yes 
        Checking for header linux/if_tun.h       : yes 
        Checking for type uint8_t                : yes 
        Checking for type uint16_t               : yes 
        Checking for type uint32_t               : yes 
        Checking for type uint64_t               : yes 
        Checking for type bool                   : yes 
        Checking for function memcpy             : yes 
        Checking for function memset             : yes 
        Checking for function openlog            : yes 
        Checking for function syslog             : yes 
        Checking for function closelog           : yes 
        Checking for program bison               : /usr/bin/bison 
        Checking for program flex                : /usr/bin/flex 
        Checking for program pkg-config          : /usr/bin/pkg-config 
        Checking for pkg-config version >= '0.20' : yes 
        Checking for talloc 2.0.7                 : yes 
        Checking for libpopt 1.16                 : yes 
        Checking for libmapi 2.0                  : yes 
        'configure' finished successfully (1.127s)
        Waf: Entering directory `/home/ocsim/openchangesim/build'
        ./script/mkversion.sh: 'build/version.h' created for OpenChangeSim ("1.0 (PLUGJUNE)")
        [ 1/16] flex: src/configuration.l -> build/src/configuration.lex.c
        [ 2/16] bison: src/configuration.y -> build/src/configuration.tab.c build/src/configuration.tab.h
        [ 3/16] c: build/src/configuration.lex.c -> build/src/configuration.lex.c.1.o
        [ 4/16] c: src/modules/module_cleanup.c -> build/src/modules/module_cleanup.c.1.o
        [ 5/16] c: src/modules/module_fetchmail.c -> build/src/modules/module_fetchmail.c.1.o
        [ 6/16] c: src/openchangesim_public.c -> build/src/openchangesim_public.c.1.o
        [ 7/16] c: src/configuration_api.c -> build/src/configuration_api.c.1.o
        [ 8/16] c: src/openchangesim_modules.c -> build/src/openchangesim_modules.c.1.o
        [ 9/16] c: src/openchangesim.c -> build/src/openchangesim.c.1.o
        [10/16] c: src/openchangesim_logs.c -> build/src/openchangesim_logs.c.1.o
        [11/16] c: src/configuration_dump.c -> build/src/configuration_dump.c.1.o
        [12/16] c: src/openchangesim_interface.c -> build/src/openchangesim_interface.c.1.o
        [13/16] c: src/openchangesim_fork.c -> build/src/openchangesim_fork.c.1.o
        [14/16] c: src/modules/module_sendmail.c -> build/src/modules/module_sendmail.c.1.o
        [15/16] c: build/src/configuration.tab.c -> build/src/configuration.tab.c.1.o
        [16/16] cprogram: build/src/configuration_api.c.1.o build/src/configuration_dump.c.1.o build/src/openchangesim_public.c.1.o build/src/openchangesim_interface.c.1.o build/src/openchangesim_modules.c.1.o build/src/openchangesim_fork.c.1.o build/src/openchangesim_logs.c.1.o build/src/openchangesim.c.1.o build/src/modules/module_fetchmail.c.1.o build/src/modules/module_sendmail.c.1.o build/src/modules/module_cleanup.c.1.o build/src/configuration.lex.c.1.o build/src/configuration.tab.c.1.o -> build/openchangesim
        Waf: Leaving directory `/home/ocsim/openchangesim/build'
        'build' finished successfully (0.830s)


        $ ./build/openchangesim --version
        Version 1.0 (PLUGJUNE)

        $ ./build/openchangesim --help
        Usage: openchangesim [OPTION...]
          -f, --database=STRING       set the profile database path
          -d, --debuglevel=STRING     set debug level
              --dump-data             dump hexadecimal data
          -V, --version               Print version 
          -c, --config=STRING         Specify configuration file
              --confcheck             Check/Validate configuration
              --confdump              Dump configuration
              --server-list           List available servers
              --server=STRING         Select server to use for openchangesim

         Help options:
          -?, --help                  Show this help message
              --usage                 Display brief usage message

# Next: HowTo Setup Logging System #

The next section will show you how to configure syslog and [setup the
logging system](logging.html).