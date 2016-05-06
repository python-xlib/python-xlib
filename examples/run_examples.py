#!/usr/bin/python
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

from subprocess import Popen
from subprocess import PIPE
from subprocess import call

def run(name):
	proc = Popen("./" + name, shell=True, stdout=PIPE, stderr=PIPE)
	return proc.wait()

class TestExamples(unittest.TestCase):
	def testEventthread(self):
		self.assertEqual(run("eventthread.py"), 0)

	def testProfilex(self):
		self.assertEqual(run("./profilex.py profilex_output"), 0)
		subprocess.call(["rm", "./profilex_output"])


if __name__ == '__main__':
    unittest.main()


