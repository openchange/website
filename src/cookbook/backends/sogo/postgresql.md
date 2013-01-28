# Postgresql Setup #

[TOC]

## Install the dependencies ##

    $ sudo apt-get install postgresql

## Create database and schema ##

Create the database user and schema using the following commands (as superuser)

    # su - postgres
    $ createuser --no-superuser --no-createdb --no-createrole --encrypted --pwprompt openchange
    Enter password for new role: 
    Enter it again: 
    $ createdb -O openchange openchange

## Adjust permissions ##

Adjust the access rights to the database. To do so, modify the
configuration file `/etc/postgresql/9.1/main/pg_hba.conf` in order to
add the following line at the very beginning of the file:

    host     precog     precog    127.0.0.1/32     md5

# Next: Configuring OpenLDAP #

Process to [OpenLDAP setup](openldap.html).