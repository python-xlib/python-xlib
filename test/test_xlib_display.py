#!/usr/bin/env python

import sys
import os
import unittest
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Xlib.display
import Xlib.protocol.display


class TestXlibDisplay(unittest.TestCase):
    def setUp(self):
        # Create authority file.

        self.authfile = os.path.join(os.getenv("HOME"), ".Xauthority")
        self.cookie = "926e3f51b3540ca0d54bf2725c1af2b6" #subprocess.check_output(["`ps -ef | md5sum | cut -f 1 -d " "`"])
        os.system("xauth -f {} add :99.0 MIT-MAGIC-COOKIE-1 {}".format(self.authfile, self.cookie))
        self.display = Xlib.display.Display(":99.0")

    def test_display_instance(self):
        print "1"
        self.assertIsInstance(self.display, Xlib.display.Display)

    def test_default_display_name(self):
        print "2"
        self.assertEqual(self.display.get_display_name(), ":99.0")

    def test_default_screen_number(self):
        self.assertEqual(self.display.get_default_screen(), 0)

    def test_returns_no_events(self):
        self.assertEqual(self.display.pending_events(), 0)

    def test_pointer_mapping_is_list(self):
        self.assertIsInstance(self.display.get_pointer_mapping(), list)

    def test_set_get_pointer_mapping(self):
        length = len(self.display.get_pointer_mapping())
        self.display.set_pointer_mapping([0] * length)
        self.assertEqual(self.display.get_pointer_mapping(), [0] * length)

    def tearDown(self):
        os.remove(self.authfile)


if __name__ == '__main__':
    unittest.main()
