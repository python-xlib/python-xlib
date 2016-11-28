#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import unittest

from Xlib.support import unix_connect
from Xlib.error import DisplayNameError


@unittest.skipUnless(sys.platform.startswith('linux'), 'Linux specific tests')
class TestUnixConnect(unittest.TestCase):

     def test_get_display(self):
         # Valid cases.
         for display, expected in (
             # Implicit Unix socket connections.
             (':0.1', ('', 0, 1)),
             (':4', ('', 4, 0)),
             # Implicit TCP connections.
             ('foo:1.2', ('foo', 1, 2)),
             ('bar:5', ('bar', 5, 0)),
             # Explicit Unix socket connections.
             ('unix/foo:4.3', ('', 4, 3)),
             ('unix/:66', ('', 66, 0)),
             # Explicit TCP connections.
             ('tcp/foo:11.1', ('foo', 11, 1)),
             ('tcp/bar:66.6', ('bar', 66, 6)),
             ('tcp/unix:54.3', ('unix', 54, 3)),
             # Special case: `unix:0.0` is equivalent to `:0.0`.
             ('unix:99.5', ('', 99, 5)),
             ('unix:42', ('', 42, 0)),
         ):
             result = unix_connect.get_display(display)
             self.assertEqual(result, (display,) + expected)
         # Invalid cases.
         for display in (
             # No display number.
             '',
             ':',
             'foo',
             'bar:',
             # Bad screen number.
             ':48.',
             ':47.f',
             # Bad hostname.
             u'fòó:0',
             u'tcp/bàr:1',
             u'unix/fòóbàr:2',
             # Bad protocol.
             'udp/foo:0'
             # With explicit TCP connections, hostname must be set.
             'tcp/:0',
         ):
             with self.assertRaises(DisplayNameError):
                 unix_connect.get_display(display)


if __name__ == '__main__':
    unittest.main()
