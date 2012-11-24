# SOGo Web UI Setup #

[TOC]

## Dependencies ##

Install the dependencies needed to run SOGo Web UI:

    $ sudo apt-get install apache2

## Configure SOGo Apache configuration ##

Copy `SOGo.conf` template from your `sogo/Apache/` source directory
into `/etc/apache2/conf.d/` folder.

    # cp ~openchange/sogo/Apache/SOGo.conf /etc/apache2/conf.d/SOGo.conf

Edit `/etc/apache2/conf.d/SOGo.conf`:

+ Replace path to GNUstep from `/usr/lib` to `/usr/local/lib` for all
occurrences.
+ Change `yourhostname` to your IP address and change from `https` to
`http` for `RequestHeader` fields:

<pre><code>RequestHeader set "x-webobjects-server-name" "192.168.102.48" 
RequestHeader set "x-webobjects-server-url" "http://192.168.102.48"</code></pre> 

## Enabling Apache modules ##

Turn `a2enmod` and restart `apache`:

    # a2enmod proxy
    # a2enmod proxy_http
    # a2enmod proxy_html
    # a2enmod headers
    # a2enmod rewrite

    # service apache2 restart


# Next: Configuring Postgresql #

Process to [Postgresql setup](postgresql.html).
