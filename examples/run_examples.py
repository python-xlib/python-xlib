#!/usr/bin/env python
#
# examples/run_examples.py -- run some examples.
#
#    Copyright (C) 2016 Svetlana Filicheva
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

# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os
import subprocess
import unittest

examples_folder = os.path.abspath(os.path.dirname(__file__)) + "/"

def run_example(path):
    """ Returns returncode of example """
    cmd = "{0} {1}".format(sys.executable, path)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = proc.communicate()
    if proc.returncode:
        print(res[1].decode())
    return proc.returncode

class TestExamples(unittest.TestCase):
    """ Run some of examples """

# TODO
#     def test_eventthread(self):
#         """ Run eventthread.py -- Tests multithreaded event handling """
#         self.assertEqual(run_example(examples_folder + "eventthread.py"), 0)

    def test_get_selection(self):
        """ Run get_selection.py -- demonstrate getting selections """
        self.assertEqual(run_example(examples_folder + "get_selection.py PRIMARY"), 0)
        self.assertEqual(run_example(examples_folder + "get_selection.py SECONDARY"), 0)
        self.assertEqual(run_example(examples_folder + "get_selection.py CLIPBOARD"), 0)

    def test_profilex(self):
        """ Run profilex.py -- program to generate profiling data """
        self.assertEqual(run_example(examples_folder + "profilex.py " + examples_folder + "profilex_output"), 0)
        subprocess.call(["rm", examples_folder + "profilex_output"])

# TODO
#     def test_record_demo(self):
#         """ Run record_demo.py -- demonstrate record extension """
#         self.assertEqual(run_example(examples_folder + "record_demo.py"), 0)

    def test_security(self):
        """ Run security.py -- demonstrate the SECURITY extension """
        self.assertEqual(run_example(examples_folder + "security.py --generate"), 0)
        self.assertEqual(run_example(examples_folder + "security.py --revoke"), 0)

    def test_xfixes(self):
        """ Run xfixes.py -- demonstrate the XFIXES extension """
        self.assertEqual(run_example(examples_folder + "xfixes.py"), 0)

# TODO
#     def test_xlsatoms(self):
#         """ Run xlsatoms.py -- show list atoms on X server """
#         self.assertEqual(run_example(examples_folder + "xlsatoms.py"), 0)


if __name__ == '__main__':
    unittest.main()
