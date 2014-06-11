# HowTo Use the Mailbox Creation Script #

The [Exchange mailbox creation
script](https://github.com/openchange/openchangesim/blob/master/script/createmailbox.ps1)
we provide in the script folder of the openchangesim repository and is
designed to work with PowerShell with Exchange 2007.

## Requirements ##

CreateMail.ps1 requires to have Exchange Administration Powershell modules installed:

* For Exchange 2007: 

        Add-PSSnapin Microsoft.Exchange.Management.PowerShell.Admin

* For Exchange 2010: 

        Add-PSSnapin Microsoft.Exchange.Management.PowerShell.E2010 

## Configuration ##

Before you run the script, make sure you have edited parameters properly:

* **user**: the generic username template to use
* **fqdn**: the REALM of your Exchange server
* **database**: the location of the Mailbox database
* **ou**: the Organizational Unit
* **$i** and **$end**: the start and end range numbers to append to
    the user generic username template.

## Run the script ##

1. From a Windows powershell, execute the script.
2. You will be prompted for a **password**. This is the generic
  password we will use for all our new Exchange user accounts.
3. Wait until it finishes. Normally the operation shouldn't take longer
  than a few seconds even for hundreds of users
4. You are now ready to run openchangesim.