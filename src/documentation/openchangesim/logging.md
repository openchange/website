# HowTo Setup Logging System #

[TOC]

OpenChangeSim is using rsyslogd as its logging system. Instructions
below help you setting up rsyslog to redirect openchangesim output in
a specific file.

## Ubuntu Configuration ##

To enable openchangesim logs, you need to edit
*`/etc/rsyslog.d/50-default.conf`*

* **Step 1**: We don't want openchangesim logs to end in
   `/var/log/messages`, so we need to add `openchangesim.none` to the
   exception:

        *.=info;*.=notice;*.=warn;\
                auth,authpriv.none;\
                cron,daemon.none;\
                openchangesim.none;\
                mail,news.none          -/var/log/messages

* **Step 2**: OpenChangeSim logs needs to be redirected to a specific
   log file. Add the following lines to `/etc/rsyslog.conf`:

        # OpenChangesim
        if $programname == 'openchangesim' then -/var/log/openchangesim.log

* **Step 3**: Save `rsyslogd.conf` and restart the service:

        $ sudo /etc/init.d/rsyslog restart
        Shutting down system logger:                               [  OK  ]
        Starting system logger:                                    [  OK  ]

## Fedora Configuration ##

To enable openchangesim logs, you need to edit **`/etc/rsyslogd.conf`**:

* **Step 1**: We don't want openchangesim logs to end in `/var/log/messages`, so we need to add *openchangesim.none* to the exception:

        # Log anything (except mail) of level info or higher.
        # Don't log private authentication messages!
        *.info;mail.none;openchangesim.none;authpriv.none;cron.none                /var/log/messages

* **Step 2**: OpenChangeSim logs needs to be redirected to a specific log file. Add the following lines to `rsyslog.conf`:

        # OpenChangesim
        if $programname == 'openchangesim' then -/var/log/openchangesim.log

* **Step 3**: Save `rsyslogd.conf` and restart the service:

        $ sudo /etc/init.d/rsyslog restart
        Shutting down system logger:                               [  OK  ]
        Starting system logger:                                    [  OK  ]

## openchangesim.log sample output

        # tail -f /var/log/openchangesim.log
        Sep  9 13:26:33 mapiproxy openchangesim[1968]: sendmail: 192.168.0.191 "scenario case 1": 10 seconds 600209 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1955]: sendmail: 192.168.0.178 "scenario case 1": 11 seconds 199173 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1960]: sendmail: 192.168.0.183 "scenario case 1": 11 seconds 62624 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1925]: sendmail: 192.168.0.150 "scenario case 1": 5 seconds 148577 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1965]: sendmail: 192.168.0.188 "scenario case 1": 10 seconds 701219 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1919]: sendmail: 192.168.0.144 "scenario case 1": 5 seconds 115201 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1929]: sendmail: 192.168.0.154 "scenario case 1": 3 seconds 875085 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1928]: sendmail: 192.168.0.153 "scenario case 1": 3 seconds 521680 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1933]: sendmail: 192.168.0.157 "scenario case 1": 3 seconds 522270 microseconds
        Sep  9 13:26:33 mapiproxy openchangesim[1930]: sendmail: 192.168.0.155 "scenario case 1": 3 seconds 664552 microseconds

The log file stores the following information as described below:

        [date][workstation][process_name][process_pid]: scenario: client IP address "scenario_case": time

The relevant parameters for further log analysis are:
* the scenario
* the ip address
* the scenario_case
* the time

# Next: HowTo Use OpenChangeSim #

You are now ready to [use OpenChangeSim](usage.html)