#!/usr/bin/env python

import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Xlib.protocol.display
import Xlib.protocol.rq


class TestResourceClasses(unittest.TestCase):
    """get_resource_class on a bare protocol display.

    The resource class table is populated by Xlib.display.Display
    (xobject layer).  A display opened at the protocol level, as the
    examples do, has no such table; lookups must fall back to the
    default so resource-typed reply fields decode to raw XIDs
    instead of raising AttributeError (issue #281).
    """

    def setUp(self):
        self.disp = Xlib.protocol.display.Display.__new__(
            Xlib.protocol.display.Display)

    def test_missing_table_returns_default(self):
        self.assertIsNone(self.disp.get_resource_class('window'))
        self.assertIs(self.disp.get_resource_class('window', int), int)

    def test_populated_table_lookup(self):
        class FakeWindow(object):
            pass

        self.disp.resource_classes = {'window': FakeWindow}
        self.assertIs(self.disp.get_resource_class('window'), FakeWindow)
        self.assertIsNone(self.disp.get_resource_class('pixmap'))

    def test_resource_field_decodes_to_xid(self):
        field = Xlib.protocol.rq.Window('wnd')
        xid = 0x034000fc
        self.assertEqual(field.parse_value(xid, self.disp), xid)


if __name__ == '__main__':
    unittest.main()
