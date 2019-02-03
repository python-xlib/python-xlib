#!/usr/bin/python
#    Copyright (C) 2011 Arun Balasubramanian <med.diagnostix@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA


'''
xlsatoms - list atoms on X server (see man xlsatoms)
sample program using python Xlib that mimics the standard xlsatoms utility
additional capability is to match against regular expressions for atoms

'''

# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import re
from Xlib import display, error
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d","--display",dest="display",help="This option specifies the X server to which to connect",metavar="dpy",default=":0.0")
parser.add_option("-n","--name",dest="name",help="This option specifies the name of an atom to list.  If the atom does  not  exist,  a  message  will  be printed on the standard error.",metavar="string",default=None)
parser.add_option("-m","--match",dest="match_re",help="This option specifies a regular expression to match against name of an atom to list.  If the atom does  not  exist,  a  message  will  be printed on the standard error.",metavar="reg-exp",default=None)
parser.add_option("-f","--format",dest="format",help="This  option  specifies a printf-style string used to list each atom <value,name> pair, printed in  that  order  (value  is  an unsigned  long  and  name is a char *).  Xlsatoms will supply a newline at the end of each line.  The default is %ld\\t%s.",metavar="string",default="%ld\t%s")
parser.add_option("-r","--range",dest="range",help="This option specifies the range of atom values  to  check.   If low  is not given, a value of 1 assumed.  If high is not given, xlsatoms will stop at the first undefined atom at or above low.",metavar="[low]-[high]",default="1-")

(options, args) = parser.parse_args()

low = 1
high = 1
ec = error.CatchError(error.BadAtom)
d = display.Display(options.display)

def print_atom(print_format,atom,value):
	print(print_format%(atom,value))

def list_atoms(d,re_obj,low,high):
	while(low <= high):
		try:
			val = d.get_atom_name(low)
			if (re_obj == None) :
				print_atom(options.format,low,val)
			elif re_obj.match(val) != None:
				print_atom(options.format,low,val)
			low += 1
		except:
			sys.exit(0)

if options.name != None:
	try:
		atom = d.intern_atom(options.name)
		val = d.get_atom_name(atom)
		print_atom(options.format,atom,val)
	except:
		sys.stderr.write('xlsatoms:  no atom named "%s" on server "%s"'%(options.name,options.display))
		sys.stderr.write("\n")
		sys.exit(1)
	sys.exit(0)

rangeVals = options.range.split("-")
if rangeVals[0] != "":
	low = long(rangeVals[0])

if rangeVals[1] != "":
	high = long(rangeVals[1])
else:
	high = sys.maxint

if options.match_re != None:
	re_obj = re.compile(options.match_re)
else:
	re_obj = None

list_atoms(d,re_obj,low,high)
