# OCSManager #

[TOC]

## Introduction ##

OCSManager is a set of services like

* HTTP Autodiscover: auto configuration of Outlook clients using *New
  account* wizard.
* EWS: partial implementation of Exchange Web Services.
    * Out Of Office
    * Free/Busy information

## Dependencies ##

OCSManager is implemented with pylons and can be run with python-paste.

    $ sudo apt-get install python-paste python-pastedeploy python-pastescript python-pylons python-mako python-mysqldb

We also need apache2

    $ sudo apt-get install apache2
    $ sudo a2enmod proxy

<div class="alert"><p>
HTTP Autodiscover needs SSL certificates with a common name autodiscover.<em>yourdomain.com</em>.
</p></div>

## Installation ##

This will install the python package `ocsmanager`

    $ sudo make ocsmanager-install
    $ sudo make pyopenchange-install

## Configuration ##

    $ sudo mkdir /etc/ocsmanager
    $ sudo cp mapiproxy/services/ocsmanager/ocsmanager.ini /etc/ocsmanager/
    $ sudo cp mapiproxy/services/ocsmanager/ocsmanager-apache.conf /etc/apache2/conf.d/ocsmanager.conf

Now we need to edit `/etc/ocsmanager/ocsmanager.ini` and change, at least, the following keys according to our environment:

* mapistore_root: probably you need `/usr/local/samba/private`
* mapistore_data: probably you need
  `/usr/local/samba/private/mapistore`

Take into account, along the file the commented key values are the
default values when the option is not present.

### AutoDiscovery ###

The autodiscovery service can be adjusted.

If you want to tune **autodiscover** settings to match your configuration,
edit the following keys:

* `[autodiscover]`

    * internal_networks: This setting is useful if you want to adjust
      settings for users that need to access OpenChange using Outlook
      Anywhere. The default configuration of the autodiscovery service
      assumes the Internet to be the internal network and therefore
      always give priority to MAPI/RPC over Outlook Anywhere. When
      this parameter is defined, specified networks will have MAPI/RPC
      prioritized over Outlook Anywhere while the non specified ones
      will have RPC over HTTP specified over MAPI/RPC. To set this
      parameter, specify network addresses using their CIDR format and
      separate them with commas. For example: `internal_networks =
      192.168.2.0/24, 10.2.0.0/16`

* `[autodiscover:rpcproxy]`
    * enabled: it is a requirement to have RPC/Proxy service
      configured.
    * external_hostname: if we want to set it statically since by
      default it is guessed from the client request. Most of the
      times this is happening when your RPC/Proxy is hosted by other host.
    * ssl: If your RPC/Proxy is configured to use SSL. Make sure the
      presented SSL certificate's common name matches the hostname the
      client is asking for.


### Out of Office ###

The Out of Office service sets the reply automatically sent to your
contacts when you receive an email. This reply is stored on the IMAP
server using SIEVE language. Two backends are provided to manage this
sieve script. Either `file` to write it directly on the file system or
`managesieve` to store it using *ManageSieve* protocol (when dealing
with remote IMAP services). The following options are available for
each backend:

* `[outofoffice:file]`

    * sieve_script_path: The path where the sieve script is
      stored. The value is expanded from the user, domain or full user
      variables.
    * sieve_script_path_mkdir: This option creates the directory
      hierarchy if it doesn't exist yet.

* `[outofoffice:managesieve]`

    * server: the server IP or hostname where the ManageSieve server
      is listening.
    * ssl: if it uses STARTTLS or not.
    * secret: it is required to have a master password to get into
      every account or having a configuration where the password is
      not required, for instance, validate a connection based on the
      source IP address.

## Start ocsmanager ##

    $ sudo PYTHONPATH=$PYTHONPATH paster serve /etc/ocsmanager/ocsmanager.ini --pid-file /var/run/ocsmanager.pid --log-file /var/log/ocsmanager.log
    $ sudo service apache2 restart

# Next: Setting the Backends #

OpenChange server up and running! It is now time to choose, install
and configure backends and their dependencies. Proceed to [deploying
the backends](/cookbook/backends/index.html)