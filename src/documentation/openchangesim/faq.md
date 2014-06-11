# Frequently Asked Questions #

[TOC]

## How to manually remove tap interfaces? ##

If openchangesim fails for a reason to delete tap interfaces, you can
run as root the bash script below.

Assuming you have 99 tap interfaces created (from `tap0` to `tap98`):

        # for i in `seq 0 98`; do tunctl -d tap$i; done