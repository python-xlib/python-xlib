#!/usr/bin/env python
#
# examples/run_examples.py -- run some examples.
#
# GUI Application automation and testing library
# Copyright (C) 2016 Intel Corporation
# Copyright (C) 2012 Michael Herrmann
# Copyright (C) 2010 Mark Mc Mahon
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

import subprocess
import unittest

from subprocess import call

class TestExamples(unittest.TestCase):
	def test_eventthread(self):
		self.assertEqual(subprocess.call("examples/eventthread.py"), 0)

	def test_get_selection(self):
		self.assertEqual(subprocess.call(["./get_selection.py", "PRIMARY"]), 0)
		self.assertEqual(subprocess.call(["./get_selection", "SECONDARY"]), 0)
		self.assertEqual(subprocess.call(["./get_selection.py", "CLIPBOARD"]), 0)

	def test_profilex(self):
		self.assertEqual(subprocess.call(["./profilex.py", "profilex_output"]), 0)
		subprocess.call(["rm", "./profilex_output"])

	def test_record_demo(self):
		self.assertEqual(subprocess.call("./record_demo.py"), 0)

	def test_security(self):
		self.assertEqual(subprocess.call(["./security.py", "--generate"]), 0)
		self.assertEqual(subprocess.call(["./security.py", "--revoke"]), 0)

	def test_xfixes(self):
		self.assertEqual(subprocess.call("./xfixes.py"), 0)

	def test_xlsatoms(self):
		self.assertEqual(subprocess.call("./xlsatoms.py"), 0)

if __name__ == '__main__':
    unittest.main()


