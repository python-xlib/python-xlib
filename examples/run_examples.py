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

import subprocess, unittest
from subprocess import Popen, PIPE, call

class TestExamples(unittest.TestCase):
	def testEventthread(self):
		subprocess.check_output("./eventthread.py")

	def testGetSelection(self):
		subprocess.check_output(["./get_selection.py", "PRIMARY"])
		subprocess.check_output(["./get_selection.py", "SECONDARY"])
		subprocess.check_output(["./get_selection.py", "CLIPBOARD"])

	def testProfilex(self):
		subprocess.check_output(["./profilex.py", "profilex_output"])
		subprocess.call(["rm", "./profilex_output"])

	def testRecordDemo(self):
		subprocess.check_output("./record_demo.py")

	def testSecurity(self):
		subprocess.check_output(["./security.py", "--generate"])
		subprocess.check_output(["./security.py", "--revoke"])

	def testXfixes(self):
		subprocess.check_output("./xfixes.py")

	def testXlsatoms(self):
		subprocess.check_output("./xlsatoms.py")

if __name__ == '__main__':
    unittest.main()


