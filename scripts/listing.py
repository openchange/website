#!/usr/bin/python
# OpenChange website scripts collection
# Create a listing with line numbering
#
# Copyright (C) Julien Kerihuel <j.kerihuel@openchange.org> 2012
#   
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import optparse
import os,sys

parser = optparse.OptionParser("%prog --file=LISTING [options]")
parser.add_option("--file", type="string", metavar="LISTING", help="set input listing to convert")
opts,args = parser.parse_args()
if len(args) != 0:
    parser.print_usage()
    sys.exit(1)

if not opts.file:
    parser.print_usage()
    sys.exit(1)

counter = 0
for line in open(opts.file, 'r'):
    number = "%d." % counter
    newline = "    %-6s %s" % (number, line)
    sys.stdout.write(newline)
    counter += 1
