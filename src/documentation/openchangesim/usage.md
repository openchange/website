# HowTo Use OpenChangeSim

[TOC]

In this guide, we assume you have followed [HowTo Setup Logging System](logging.html).

# Setting up the Exchange server #

OpenChangeSim assumes that your Exchange server is configured to use a
generic naming for username and a single common password for all the
accounts.

Furthermore, openchangesim PLUGJUNE is assuming all the mailboxes are
stored on the same Exchange server.

A powershell script for Exchange 2007 is available in the script
folder of the openchangesim repository:
[CreateMailbox.ps1](https://github.com/openchange/openchangesim/blob/master/script/CreateMailbox.ps1)

* Open CreateMailbox.ps1 and update `$user`, `$fqdn`, `$database`,
  `$ou`, `$i` and `$end` variables to match the Exchange server
  configuration.
* Run the script in a powershell console on the Exchange server
* Enter the generic password you want to use for all accounts when
  prompted

You should now have `n` Exchange users available on the server. For
example, user1 to user999 if your `$i,$end range` is `1,1000`.

# Setting up the environment #

The configuration is stored by default in
`$HOME/.openchange/openchangesim/` and mainly stores 2 files:

* `$HOME/.openchange/openchangesim/profiles.ldb`: The profile database
  automatically created by OpenChangeSim

* `$HOME/.openchange/openchangesim/openchangesim.conf`: The main
  configuration file

        $ mkdir -p ~/.openchange/openchangesim
        $ touch ~/.openchange/openchangesim/openchangesim.conf


# Creating the configuration file #

Create or open with your favorite editor the file
`~/.openchange/openchangesim/openchangesim.conf`

## Add a server section block ##

The configuration requires at least one server section as [described
here](dtd.html#servers-section).

A sample server section is available below. Update it to reflect your
server configuration.

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

The configuration above specifies that the server EXCHANGE with IP
address `xxx.xxx.xxx.xxx` have accounts for `user1` up to `user999`
all with the same password `SecretPassword`.  A unique IP address from
the `172.16.10.1 - 172.16.40.254` IP pool will be allocated to each
client.

## Add scenario section blocks ##

Finally you can control and customize the different scenario
available. The detailed list of available options and parameters for
scenario is [available here](dtd.html#scenarios-section).

Sample scenarios are provided below:

        scenario {
               name         =       "sendmail";
               repeat       =       100;

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

        scenario {
               name         =       "fetchmail";
               repeat       =       100;
        };


In the above example, we define 2 scenarios:
* sendmail
* fetchmail

For the sendmail scenario, we define that we want each client to run
it 100 times. For each *run*, the sendmail scenario will execute *the
utf8 case* and *case 1* (default if name parameter is missing for a
case):

* The utf8 case specifies that we want to send an email with an utf8 body
  specified inline and with an attachment stored on the filesystem at
  `/path/to/attachment_1`.

* The second case specifies we want to send an email with an HTML body
  which contents is stored on the file system at
  `/tmp/html_body.html`. Furthermore we also want to attach two files
  to this e-mail: `/path_to_atachment_2` and `/path_to_attachment_3`.

For the fetchmail scenario, we define that we want each client to run
it 100 times.

# OpenChangeSim command-line parameters #

        $ ./bin/openchangesim --help
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

## confcheck option ##

Before running openchangesim, you need to ensure your configuration
file is OK. The `--confcheck` option will process the configuration
file and report whether it is OK or not.

        $ ./bin/openchangesim --confcheck
        [*] Configuration file OK

        $ mv ~/.openchange /tmp/
        $ ./bin/openchangesim --confcheck
        Invalid Filename: /home/jkerihuel/.openchange/openchangesim/openchangesim.conf
        [WARN] Configuration file not OK!

If your configuration file has an incorrect syntax, confcheck will
detect it and provide information on how to fix it. For example, I
deliberately removed a `;` for a variable in a scenario case:

        ./bin/openchangesim --confcheck
        syntax error, unexpected EBRACE, expecting SEMICOLON: 39
        Error in configuration file
        [WARN] Configuration file not OK!

## confdump option ##

The `--confdump`option will parse the configuration file and dumps it
on stdout. This option is mainly for debugging purposes and to ensure
all parameters were retrieved and mapped properly.

For example if I have the following configuration file:

        server {
                   name               = WINDOWS;
                   version            = 2010;
                   address            = 192.168.0.250;
                   domain             = EXCHANGE2007;
                   realm              = EXCHANGE2007.LOCAL;
                   generic_user       = user;
                   generic_user_range = 1-99;
                   generic_password   = "^!OpenChange";
                   ip_range           = 192.168.0.121 - 192.168.0.222;
        };

        server {
                  name                    = EXCHANGE2003;
                  version                 = 2003;
                  address                 = 192.168.102.236;
                  domain                  = OPENCHANGE2003;
                  realm                   = OPENCHANGE2003.LOCAL;
                  generic_user            = user;
                  generic_user_range      = 1-4;
                  generic_password        = "^!OpenChange";
                  ip_range                = 192.168.0.121 - 192.168.0.124 ;
       };

       scenario {
                  name         =       "sendmail";
                  repeat       =       4;

                  case {
                        name            =       "utf8 case";
                        inline_utf8     =       "Hello world, this is a very special case";
                        attachment      =       "/home/openchangesim/Pictures/plugfest.png";
                  };

                  case {
                        file_html       =       "/tmp/html_body.html";
                        attachment      =       "/home/openchangesim/Pictures/redmond.jpg";
                        attachment      =       "/home/openchangesim/Pictures/test.png";
                  };
        };

        scenario {
                  name          =        "fetchmail";
                  repeat        =        2;
        };

`confdump` will process and display it:

        ./bin/openchangesim --confdump
        server {
               EXCHANGE2003 {
                    version                = 2003
                    address                = 192.168.102.236
                    domain                 = OPENCHANGE2003
                    realm                  = OPENCHANGE2003.LOCAL
                    generic user           = user
                    generic user range     = from 1 to 4
                    generic password       = ^!OpenChange
               }

               WINDOWS {
                    version                = 2010
                    address                = 192.168.0.250
                    domain                 = EXCHANGE2007
                    realm                  = EXCHANGE2007.LOCAL
                    generic user           = user
                    generic user range     = from 1 to 99
                    generic password       = ^!OpenChange
              }

         }
         scenario fetchmail {
               repeat                = 2

         }
         scenario sendmail {
               repeat                = 4

               case "utf8 case" {
                    body                   = INLINE UTF8
                    content = Hello world, this is a very special case
                    attachments            = 1
                    attachment             = /home/openchangesim/Pictures/plugfest.png
               };

               case "scenario case 1" {
                    body                   = HTML FILE
                    filename               = /tmp/html_body.html
                    attachments            = 2
                    attachment             = /home/jkerihuel/Pictures/redmond.jpg
                    attachment             = /home/jkerihuel/Pictures/test.png
               };

        }


## server-list option ##

The `--server-list` option gives you a quick overview of the available
servers and the number of users they are configured to use.

        $ ./bin/openchangesim --server-list
        Available servers:
               * EXCHANGE2003 (4 users)
               * WINDOWS (99 users)

### server option ###

The `--server` option is the main parameter openchangesim relies on
and is used to specify the server to use.

        $ sudo ./bin/openchangesim --server=WINDOWS


# Running OpenChangeSim #

OpenChangeSim creates virtual interfaces on startup and **requires root
privileges to run**.

To run openchangesim, just specify the `--server` parameter on the
command line:

        $ sudo ./bin/openchangesim --server=WINDOWS
        [*] Initializing modules
               [*] fetchmail           : Module loaded
               [*] sendmail            : Module loaded
        [*] 98 User profiles ready

On startup, openchangesim will check for the profile database,
ensuring all profiles exist, otherwise will create it and insert
missing profiles. The profile creation process is a 2 steps procedure:

* Contact the Exchange server and perform the MAPI profile creation
  tasks similar to Outlook *new account wizard* process.
* From this initial profile, duplicate the profile in the database for
  all other users

OpenChangeSim is next running the scenario:
* For each user, openchangesim forks and create a child process
* Each forked instance runs the scenario and cases accordingly to
  configuration file parameters
* When thee child process finishes running scenarios, the child process exits


# OpenChangeSim Logs #

OpenChangeSim is applying a per case scenario log approach. Each time
a mail is sent (through a sendmail case), a new line is added to
`/var/log/openchangesim.log`. Further information on OpenChangeSim
logs is available in the [HowTo Setup Logging System](logging.html) section.

# Next: Configuration file DTD #

Learn about the [configuration file DTD](dtd.html).