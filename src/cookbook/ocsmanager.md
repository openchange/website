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

If you want to tune **autodiscover** settings to match your configuration,
edit the following keys:

* `[autodiscover]`
    * internal_networks: set it if you want to prioritise RPC/Proxy settings
      when you are outside the office. The network addresses are in
      CIDR format and separated by commas, for
      instance: `internal_networks = 192.168.2.0/24, 10.2.0.0/16`
* `[autodiscover:rpcproxy]`
    * enabled: it is a pre-requisite to have RPC/Proxy service
      configured.
    * external_hostname: if we want to set it statically since by
      default it is guessed from the client request. Most of the
      times this is happening when your RPC/Proxy is hosted by other host.
    * ssl: If your RPC/Proxy is configured to use SSL. Make sure the
      presented SSL certificate's common name matches the hostname the
      client is asking for.

Take into account, the commented key values are the default values
when the option is not present.

## Start ocsmanager ##

    $ sudo PYTHONPATH=$PYTHONPATH paster serve /etc/ocsmanager/ocsmanager.ini --pid-file /var/run/ocsmanager.pid --log-file /var/log/ocsmanager.log
    $ sudo service apache2 restart
