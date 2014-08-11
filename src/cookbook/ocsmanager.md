# OCSManager #

[TOC]

## Introduction ##

OCSManager is a set of services like

* HTTP Autodiscover: auto configuration of outlook clients.
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
HTTP Autodiscover needs ssl certificates with a common name autodiscover.<em>yourdomain.com</em>.
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
* mapistore_data: probably you need `/usr/local/samba/private/mapistore`

## Start ocsmanager ##

    $ sudo PYTHONPATH=$PYTHONPATH paster serve /etc/ocsmanager/ocsmanager.ini --pid-file /var/run/ocsmanager.pid --log-file /var/log/ocsmanager.log
    $ sudo service apache2 restart
