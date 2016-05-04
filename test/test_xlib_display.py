#!/usr/bin/env python

import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Xlib.display
import Xlib.protocol.display


class TestXlibDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Xlib.display.Display(":99.0")

    def test_display_instance(self):
        print "1"
        self.assertIsInstance(self.display, Xlib.display.Display)

    def test_default_DisplayName(self):
        print "2"
        self.assertEqual(self.display.get_display_name(), ":99.0")

    def test_default_screenNumber(self):
        self.assertEqual(self.display.get_default_screen(), 0)

    def test_returns_no_events(self):
        self.assertEqual(self.display.pending_events(), 0)

    def test_pointer_mapping_is_list(self):
        self.assertIsInstance(self.display.get_pointer_mapping(), list)

    def test_set_get_pointer_mapping(self):
        length = len(self.display.get_pointer_mapping())
        self.display.set_pointer_mapping([0] * length)
        self.assertEqual(self.display.get_pointer_mapping(), [0] * length)


if __name__ == '__main__':
    unittest.main()
