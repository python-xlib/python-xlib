import os
import struct
import sys
import tempfile
import unittest

from Xlib import xauth, error


def _entry(family, addr, num, name, data):
    out = struct.pack('>H', family)
    for field in (addr, num, name, data):
        out += struct.pack('>H', len(field)) + field
    return out


def _write_xauth(entries):
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'wb') as fp:
            fp.write(b''.join(entries))
        return xauth.Xauthority(path)
    finally:
        os.unlink(path)


class TestXauthority(unittest.TestCase):
    def test_family_wild_matches_any_family_and_address(self):
        # Mutter/XWayland writes FamilyWild entries with an empty display
        # number; they are meant to match every family, address and
        # display. See https://github.com/python-xlib/python-xlib/issues/294
        au = _write_xauth([
            _entry(xauth.FamilyWild, b'whatever', b'',
                   b'MIT-MAGIC-COOKIE-1', b'cookie'),
        ])
        name, data = au.get_best_auth(xauth.FamilyLocal, b'other-host', 0)
        self.assertEqual(name, b'MIT-MAGIC-COOKIE-1')
        self.assertEqual(data, b'cookie')

    def test_family_wild_empty_num_only(self):
        au = _write_xauth([
            _entry(xauth.FamilyWild, b'host', b'',
                   b'MIT-MAGIC-COOKIE-1', b'cookie'),
        ])
        name, data = au.get_best_auth(xauth.FamilyInternet,
                                      b'\x7f\x00\x00\x01', 42)
        self.assertEqual(data, b'cookie')

    def test_no_match_still_raises(self):
        au = _write_xauth([
            _entry(xauth.FamilyLocal, b'other-host', b'1',
                   b'MIT-MAGIC-COOKIE-1', b'cookie'),
        ])
        self.assertRaises(error.XNoAuthError, au.get_best_auth,
                          xauth.FamilyLocal, b'my-host', 0)

    def test_exact_match_unchanged(self):
        au = _write_xauth([
            _entry(xauth.FamilyLocal, b'my-host', b'0',
                   b'MIT-MAGIC-COOKIE-1', b'cookie'),
        ])
        name, data = au.get_best_auth(xauth.FamilyLocal, b'my-host', 0)
        self.assertEqual(data, b'cookie')


if __name__ == '__main__':
    unittest.main()
