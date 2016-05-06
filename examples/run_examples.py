#!/usr/bin/python
#
# examples/run_examples.py -- run some examples.
#
#	Copyright (C) 2008 David Bronke <whitelynx@gmail.com>
#	Copyright (C) 2002 Peter Liljenberg <petli@ctrl-c.liu.se>
#
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import subprocess
from subprocess import Popen, PIPE, call

def run(name):
	proc = Popen("./" + name, shell=True, stdout=PIPE, stderr=PIPE)
	
	if proc.wait() == 0:
		print(name + " ..... ok")
		return True
	else:
		print(name + " ..... fail")
		return False

def run_with_args(name, args):
	for arg in args:
		proc = Popen("./" + name + " " + arg, shell=True, stdout=PIPE, stderr=PIPE)
		if proc.wait() != 0:
			print(name + " ..... fail")
			return False
	
	print(name + " ..... ok")
	return True

n = 0
n_ok = 0
	 
if run("eventthread.py"): n_ok += 1
n += 1

if run_with_args("get_selection.py", ["PRIMARY", "SECONDARY", "CLIPBOARD"]): n_ok += 1
n += 1

if run_with_args("profilex.py", ["profilex_output"]): n_ok += 1
subprocess.call(["rm", "./profilex_output"])
n += 1

if run("record_demo.py"): n_ok += 1
n += 1

if run_with_args("security.py", ["--generate", "--revoke"]): n_ok += 1
n += 1

if run("xfixes.py"): n_ok += 1
n += 1

if run("xlsatoms.py"): n_ok += 1
n += 1

print("\n--------------------------------------------------")
print("Run: " + str(n))
print("Success: " + str(n_ok))


