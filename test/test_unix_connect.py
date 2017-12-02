#!/usr/bin/env python
# -*- coding: utf-8 -*

from functools import partial
import socket
import sys
import unittest

from mock import patch

from Xlib.support import unix_connect
from Xlib.error import DisplayConnectionError, DisplayNameError


@unittest.skipUnless(sys.platform.startswith('linux'), 'Linux specific tests')
class TestUnixConnect(unittest.TestCase):

    def test_get_display(self):
        # Valid cases.
        for display, expected in (
            # Implicit Unix socket connections.
            (':0.1', (None, '', 0, 1)),
            (':4', (None, '', 4, 0)),
            # Implicit TCP connections.
            ('foo:1.2', (None, 'foo', 1, 2)),
            ('bar:5', (None, 'bar', 5, 0)),
            # Explicit Unix socket connections.
            ('unix/foo:4.3', ('unix', 'foo', 4, 3)),
            ('unix/:66', ('unix', '', 66, 0)),
            # Explicit TCP connections.
            ('tcp/foo:11.1', ('tcp', 'foo', 11, 1)),
            ('tcp/bar:66.6', ('tcp', 'bar', 66, 6)),
            ('tcp/unix:54.3', ('tcp', 'unix', 54, 3)),
            # Special case: `unix:0.0` is equivalent to `:0.0`.
            ('unix:99.5', (None, 'unix', 99, 5)),
            ('unix:42', (None, 'unix', 42, 0)),
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

    def test_get_socket(self):
        class FakeSocket(object):
            def fileno(self):
                return 42
        calls = []
        def _get_socket(socket_type, raises, *params):
            calls.append(('_get_%s_socket' % socket_type,) + params)
            if raises:
                raise socket.error()
            return FakeSocket()
        def path_exists(returns, path):
            calls.append(('os.path.exists', path))
            return returns
        def fcntl(*args):
            calls.append(('fcntl',) + args)
        for params, allow_unix, unix_addr_exists, allow_tcp, expect_connection_error, expected_calls in (
            # Successful explicit TCP socket connection.
            (('tcp/host:6', None, 'host', 6), False, False, True, False, [
                ('_get_tcp_socket', 'host', 6),
            ]),
            # Failed explicit TCP socket connection.
            (('tcp/host:6', None, 'host', 6), False, False, False, True, [
                ('_get_tcp_socket', 'host', 6),
            ]),
            # Successful implicit TCP socket connection.
            (('host:5', None, 'host', 5), False, False, True, False, [
                ('_get_tcp_socket', 'host', 5),
            ]),
            # Failed implicit TCP socket connection.
            (('host:5', None, 'host', 5), False, False, False, True, [
                ('_get_tcp_socket', 'host', 5),
            ]),
            # Successful explicit Unix socket connection.
            (('unix/name:0', 'unix', 'name', 0), True, True, False, False, [
                ('os.path.exists', '/tmp/.X11-unix/X0'),
                ('_get_unix_socket', '/tmp/.X11-unix/X0'),
            ]),
            # Failed explicit Unix socket connection.
            (('unix/name:0', 'unix', 'name', 0), False, True, False, True, [
                ('os.path.exists', '/tmp/.X11-unix/X0'),
                ('_get_unix_socket', '/tmp/.X11-unix/X0'),
            ]),
            # Successful explicit Unix socket connection, variant.
            (('unix:0', None, 'unix', 0), True, True, False, False, [
                ('os.path.exists', '/tmp/.X11-unix/X0'),
                ('_get_unix_socket', '/tmp/.X11-unix/X0'),
            ]),
            # Failed explicit Unix socket connection, variant.
            (('unix:0', None, 'unix', 0), False, True, False, True, [
                ('os.path.exists', '/tmp/.X11-unix/X0'),
                ('_get_unix_socket', '/tmp/.X11-unix/X0'),
            ]),
            # Successful implicit Unix socket connection.
            ((':4', None, '', 4), True, True, False, False, [
                ('os.path.exists', '/tmp/.X11-unix/X4'),
                ('_get_unix_socket', '/tmp/.X11-unix/X4'),
            ]),
            # Successful implicit Unix socket connection, abstract address.
            ((':3', None, '', 3), True, False, False, False, [
                ('os.path.exists', '/tmp/.X11-unix/X3'),
                ('_get_unix_socket', '\0/tmp/.X11-unix/X3'),
            ]),
            # Failed implicit Unix socket connection, successful fallback on TCP.
            ((':2', None, '', 2), False, False, True, False, [
                ('os.path.exists', '/tmp/.X11-unix/X2'),
                ('_get_unix_socket', '\0/tmp/.X11-unix/X2'),
                ('_get_tcp_socket', '', 2),
            ]),
            # Failed implicit Unix socket connection, failed fallback on TCP.
            ((':1', None, '', 1), False, False, False, True, [
                ('os.path.exists', '/tmp/.X11-unix/X1'),
                ('_get_unix_socket', '\0/tmp/.X11-unix/X1'),
                ('_get_tcp_socket', '', 1),
            ]),
        ):
            with \
                    patch('Xlib.support.unix_connect._get_unix_socket',
                       partial(_get_socket, 'unix', not allow_unix)), \
                    patch('Xlib.support.unix_connect._get_tcp_socket',
                          partial(_get_socket, 'tcp', not allow_tcp)), \
                    patch('os.path.exists',
                          partial(path_exists, unix_addr_exists)), \
                    patch('fcntl.fcntl', fcntl):
                del calls[:]
                if expect_connection_error:
                    with self.assertRaises(DisplayConnectionError):
                        unix_connect.get_socket(*params)
                else:
                    s = unix_connect.get_socket(*params)
                    self.assertIsInstance(s, FakeSocket)
                    expected_calls.append(('fcntl', 42,
                                           unix_connect.F_SETFD,
                                           unix_connect.FD_CLOEXEC))
                self.assertEqual(calls, expected_calls)


if __name__ == '__main__':
    unittest.main()
