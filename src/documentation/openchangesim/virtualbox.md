# HowTo Configure VirtualBox #

## Introduction ##

VirtualBox - among other virtualization system - is working pretty
well for openchangesim purposes. However it requires a few
modifications on Microsoft Windows operating systems in order to
manage properly hundreds or thousands or concurrent MAPI
communications. The following instructions apply for VirtualBox
(3.2.8), are probably valid for anterior versions and may probably
remain valid unless this bug is fixed.

## Problematic ##

If your virtual machine is using a bridged interface directly linked
to a physical interface, then openchangesim will probably fail running
with 10 concurrent users. One potential reason is that the VirtualBox
bridge code fail to handle all the incoming traffic from physical
interface, leading in some IP stack overflow which prevent from any
further communication to the virtual host. The following instructions
intend to fix this issue.

## Creating a MAC bridge Miniport ##

What we will do is put our physical interface within a MAC bridge and
use this bridge as the bridged interface our virtual machine needs to
rely on.

To create a MAC bridge Miniport:

1. Click on `Start > Control Panel` and select network interfaces
2. Right click on the network interface you used along with the virtual
  bridged interface
3. Select the `Bridge Connections` option in the menu
4. After few moments, Network Bridge should be created and activated by
  Windows
5. Check for IPv4 options on this new interface and check if it has an
  IPv4 address assigned

## Using the MAC bridge Miniport in VirtualBox ##

In VirtualBox, shutdown the virtual machine, then:

1. Select the virtual machine in the GUI
2. Click on Settings
3. Select Network in the left menu
4. Look within the tabs for your bridged interface (generally Adapter
1 or Adapter 2)
5. In the Adapter pane, use the drop-down list associated to the Name
item and select MAC bridge Miniport
6. Valid your choice by clicking on OK
7. Start the virtual machine again

Your virtual machine should now work properly and able to handle
hundreds of simultaneous communications.