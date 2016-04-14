#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Xlib.display
import Xlib.protocol.display
import unittest


class TestXlibDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Xlib.display.Display()

    def testDefaultDisplayName(self):
        print "Cool"
        print self.display.get_default_screen()
        self.assertEqual(self.display.get_display_name(), ":0")

    def testDefaultScreenNumber(self):
        print self.display.get_default_screen()
        self.assertEqual(self.display.get_default_screen(), 0)



if __name__ == '__main__':
    unittest.main()
