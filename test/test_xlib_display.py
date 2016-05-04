#!/usr/bin/env python

import sys
import os
import unittest
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Xlib.display
import Xlib.error
import Xlib.protocol.display


class TestXlibDisplay(unittest.TestCase):
    def setUp(self):
        # Create authority file.
        self.authfile = os.path.join(os.getenv("HOME"), ".Xauthority")
        self.cookie = "926e3f51b3540ca0d54bf2725c1af2b6"
        os.system("xauth -f {0} add :99.0 MIT-MAGIC-COOKIE-1 {1}".format(self.authfile, self.cookie))
        self.display = Xlib.display.Display(":99.0")

    def test_display_instance(self):
        self.assertTrue(isinstance(self.display, Xlib.display.Display))

    def test_default_display_name(self):
        self.assertEqual(self.display.get_display_name(), ":99.0")

    def test_default_screen_number(self):
        self.assertEqual(self.display.get_default_screen(), 0)

    def test_returns_no_events(self):
        self.assertEqual(self.display.pending_events(), 0)

    def test_pointer_mapping_is_list(self):
        self.assertTrue(isinstance(self.display.get_pointer_mapping(), list))

    def test_set_get_pointer_mapping(self):
        length = len(self.display.get_pointer_mapping())
        self.display.set_pointer_mapping([0] * length)
        self.assertEqual(self.display.get_pointer_mapping(), [0] * length)

    def test_can_close_display(self):
        self.display.close()
        self.assertEqual(str(self.display.display.socket_error), "Display connection closed by client")

    def test_can_close_display_and_check_for_error(self):
        self.display.close()
        with self.assertRaises(Xlib.error.ConnectionClosedError, None) as e:
            self.display.flush()


    def tearDown(self):
        os.remove(self.authfile)


if __name__ == '__main__':
    unittest.main()
