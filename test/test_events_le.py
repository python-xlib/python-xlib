#!/usr/bin/env python

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from Xlib.protocol import request, rq, event
import Xlib.protocol.event

import struct
import array

if sys.version_info[0] >= 3:
    def _ordb(i):
        """Integer representation of a byte indexed from a byte string - Py3"""
        return i
else:
    def _ordb(c):
        """Integer representation of a byte indexed from a byte string - Py2"""
        return ord(c)

class CmpArray(object):
    def __init__(self, *args, **kws):
        self.array = array.array(*args, **kws)

    def __len__(self):
        return len(self.array)

    def __getitem__(self, key):
        if isinstance(key, slice):
            x = key.start
            y = key.stop
            return list(self.array[x:y])
        else:
            return self.array[key]

    def __getattr__(self, attr):
        return getattr(self.array, attr)

    def __lt__(self, other):
        return self.array.tolist() < other

    def __gt__(self, other):
        return self.array.tolist() > other

    def __eq__(self, other):
        return self.array.tolist() == other

rq.array = CmpArray

def tohex(bin):
    bin = ''.join(map(lambda c: '\\x%02x' % _ordb(c), bin))

    bins = []
    for i in range(0, len(bin), 16):
        bins.append(bin[i:i+16])

    bins2 = []
    for i in range(0, len(bins), 2):
        try:
            bins2.append("'%s' '%s'" % (bins[i], bins[i + 1]))
        except IndexError:
            bins2.append("'%s'" % bins[i])

    return ' \\\n            '.join(bins2)

class DummyDisplay:
    def get_resource_class(self, x):
        return None

    event_classes = Xlib.protocol.event.event_class
dummy_display = DummyDisplay()


def check_endian():
    if struct.unpack('BB', struct.pack('H', 0x0100))[0] != 0:
        sys.stderr.write('Little-endian tests, skipping on this system.\n')
        sys.exit(0)



class TestKeymapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'type': 173,
            'data': [130, 181, 177, 244, 167, 144, 216, 185, 228, 220, 254, 130, 239, 213, 142, 240, 233, 248, 161, 238, 160, 205, 212, 205, 166, 156, 241, 169, 198, 147, 144],
            }
        self.evt_bin_0 = b'\xad\x82\xb5\xb1' b'\xf4\xa7\x90\xd8' \
            b'\xb9\xe4\xdc\xfe' b'\x82\xef\xd5\x8e' \
            b'\xf0\xe9\xf8\xa1' b'\xee\xa0\xcd\xd4' \
            b'\xcd\xa6\x9c\xf1' b'\xa9\xc6\x93\x90'


    def testPack0(self):
        bin = event.KeymapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.KeymapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestExpose(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'count': 31063,
            'width': 57024,
            'window': 1993119152,
            'y': 29154,
            'x': 15652,
            'type': 192,
            'sequence_number': 45668,
            'height': 29709,
            }
        self.evt_bin_0 = b'\xc0\x00\x64\xb2' b'\xb0\x95\xcc\x76' \
            b'\x24\x3d\xe2\x71' b'\xc0\xde\x0d\x74' \
            b'\x57\x79\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.Expose._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.Expose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGraphicsExpose(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'count': 7002,
            'width': 21650,
            'major_event': 238,
            'minor_event': 44368,
            'y': 2412,
            'x': 50041,
            'drawable': 950531249,
            'type': 138,
            'sequence_number': 9516,
            'height': 10465,
            }
        self.evt_bin_0 = b'\x8a\x00\x2c\x25' b'\xb1\xf4\xa7\x38' \
            b'\x79\xc3\x6c\x09' b'\x92\x54\xe1\x28' \
            b'\x50\xad\x5a\x1b' b'\xee\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.GraphicsExpose._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.GraphicsExpose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestNoExpose(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'minor_event': 49058,
            'window': 1389793826,
            'type': 198,
            'major_event': 149,
            'sequence_number': 51301,
            }
        self.evt_bin_0 = b'\xc6\x00\x65\xc8' b'\x22\x92\xd6\x52' \
            b'\xa2\xbf\x95\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.NoExpose._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.NoExpose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestVisibilityNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 848538738,
            'type': 233,
            'state': 239,
            'sequence_number': 38248,
            }
        self.evt_bin_0 = b'\xe9\x00\x68\x95' b'\x72\xac\x93\x32' \
            b'\xef\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.VisibilityNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.VisibilityNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCreateNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'width': 24559,
            'window': 1328254552,
            'parent': 112487253,
            'override': 0,
            'y': -31372,
            'x': -13676,
            'border_width': 32812,
            'type': 230,
            'sequence_number': 14268,
            'height': 8803,
            }
        self.evt_bin_0 = b'\xe6\x00\xbc\x37' b'\x55\x6b\xb4\x06' \
            b'\x58\x8e\x2b\x4f' b'\x94\xca\x74\x85' \
            b'\xef\x5f\x63\x22' b'\x2c\x80\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.CreateNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.CreateNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestDestroyNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 1384567865,
            'type': 183,
            'event': 1596763581,
            'sequence_number': 37839,
            }
        self.evt_bin_0 = b'\xb7\x00\xcf\x93' b'\xbd\xad\x2c\x5f' \
            b'\x39\xd4\x86\x52' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.DestroyNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.DestroyNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUnmapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 1267184116,
            'type': 192,
            'event': 913541146,
            'sequence_number': 55135,
            'from_configure': 0,
            }
        self.evt_bin_0 = b'\xc0\x00\x5f\xd7' b'\x1a\x88\x73\x36' \
            b'\xf4\xb1\x87\x4b' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.UnmapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.UnmapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestMapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'override': 0,
            'window': 2002432488,
            'type': 216,
            'event': 1566597012,
            'sequence_number': 8920,
            }
        self.evt_bin_0 = b'\xd8\x00\xd8\x22' b'\x94\x5f\x60\x5d' \
            b'\xe8\xb1\x5a\x77' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.MapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestMapRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 1740270413,
            'type': 242,
            'parent': 1188866605,
            'sequence_number': 6729,
            }
        self.evt_bin_0 = b'\xf2\x00\x49\x1a' b'\x2d\xaa\xdc\x46' \
            b'\x4d\x6b\xba\x67' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MapRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.MapRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestReparentNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'override': 0,
            'window': 918878719,
            'parent': 1046822430,
            'y': -10755,
            'x': -11814,
            'type': 185,
            'event': 1344092894,
            'sequence_number': 31034,
            }
        self.evt_bin_0 = b'\xb9\x00\x3a\x79' b'\xde\x3a\x1d\x50' \
            b'\xff\xf9\xc4\x36' b'\x1e\x3e\x65\x3e' \
            b'\xda\xd1\xfd\xd5' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ReparentNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ReparentNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestConfigureNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'y': -32583,
            'above_sibling': 1143940649,
            'height': 44365,
            'width': 24191,
            'window': 1699527401,
            'override': 1,
            'x': -23713,
            'border_width': 51797,
            'type': 191,
            'event': 2102634753,
            'sequence_number': 21818,
            }
        self.evt_bin_0 = b'\xbf\x00\x3a\x55' b'\x01\xa9\x53\x7d' \
            b'\xe9\xba\x4c\x65' b'\x29\x26\x2f\x44' \
            b'\x5f\xa3\xb9\x80' b'\x7f\x5e\x4d\xad' \
            b'\x55\xca\x01\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ConfigureNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ConfigureNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestConfigureRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'parent': 1484835068,
            'width': 46666,
            'value_mask': 41755,
            'stack_mode': 155,
            'height': 27280,
            'sibling': 1153557246,
            'window': 549283037,
            'y': -1019,
            'x': -11524,
            'border_width': 41299,
            'type': 140,
            'sequence_number': 48820,
            }
        self.evt_bin_0 = b'\x8c\x9b\xb4\xbe' b'\xfc\xc8\x80\x58' \
            b'\xdd\x64\xbd\x20' b'\xfe\xe2\xc1\x44' \
            b'\xfc\xd2\x05\xfc' b'\x4a\xb6\x90\x6a' \
            b'\x53\xa1\x1b\xa3' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ConfigureRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ConfigureRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGravityNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 1471159096,
            'y': -26841,
            'x': -10882,
            'type': 191,
            'event': 860169186,
            'sequence_number': 48472,
            }
        self.evt_bin_0 = b'\xbf\x00\x58\xbd' b'\xe2\x23\x45\x33' \
            b'\x38\x1b\xb0\x57' b'\x7e\xd5\x27\x97' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.GravityNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.GravityNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestResizeRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'width': 8842,
            'window': 995086195,
            'type': 139,
            'sequence_number': 9443,
            'height': 58942,
            }
        self.evt_bin_0 = b'\x8b\x00\xe3\x24' b'\x73\xcf\x4f\x3b' \
            b'\x8a\x22\x3e\xe6' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ResizeRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ResizeRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPropertyNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 1763395006,
            'time': 936540618,
            'atom': 47197280,
            'type': 205,
            'state': 241,
            'sequence_number': 47586,
            }
        self.evt_bin_0 = b'\xcd\x00\xe2\xb9' b'\xbe\x45\x1b\x69' \
            b'\x60\x2c\xd0\x02' b'\xca\x79\xd2\x37' \
            b'\xf1\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.PropertyNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.PropertyNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSelectionClear(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 336291153,
            'atom': 256452607,
            'type': 232,
            'sequence_number': 26660,
            'time': 1732839301,
            }
        self.evt_bin_0 = b'\xe8\x00\x24\x68' b'\x85\x07\x49\x67' \
            b'\x51\x65\x0b\x14' b'\xff\x27\x49\x0f' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionClear._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.SelectionClear._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSelectionRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'requestor': 264947265,
            'selection': 1535909824,
            'target': 607705863,
            'time': 1423586793,
            'owner': 764886771,
            'property': 1148098854,
            'type': 147,
            'sequence_number': 20571,
            }
        self.evt_bin_0 = b'\x93\x00\x5b\x50' b'\xe9\x35\xda\x54' \
            b'\xf3\x3e\x97\x2d' b'\x41\xc6\xca\x0f' \
            b'\xc0\x1f\x8c\x5b' b'\x07\xdb\x38\x24' \
            b'\x26\x99\x6e\x44' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.SelectionRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSelectionNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'requestor': 971528625,
            'selection': 327380230,
            'target': 1874329297,
            'time': 1022248107,
            'property': 1791820478,
            'type': 133,
            'sequence_number': 30741,
            }
        self.evt_bin_0 = b'\x85\x00\x15\x78' b'\xab\x44\xee\x3c' \
            b'\xb1\x59\xe8\x39' b'\x06\x6d\x83\x13' \
            b'\xd1\xfe\xb7\x6f' b'\xbe\x02\xcd\x6a' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.SelectionNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestColormapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'window': 1353796539,
            'colormap': 659729309,
            'new': 1,
            'type': 211,
            'state': 168,
            'sequence_number': 8684,
            }
        self.evt_bin_0 = b'\xd3\x00\xec\x21' b'\xbb\x4b\xb1\x50' \
            b'\x9d\xab\x52\x27' b'\x01\xa8\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ColormapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ColormapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestClientMessage(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'type': 237,
            'window': 1804643202,
            'client_type': 455293257,
            'data': (8, '01234567890123456789'),
            'sequence_number': 14854,
            }
        self.evt_bin_0 = b'\xed\x08\x06\x3a' b'\x82\xab\x90\x6b' \
            b'\x49\x39\x23\x1b' b'\x30\x31\x32\x33' \
            b'\x34\x35\x36\x37' b'\x38\x39\x30\x31' \
            b'\x32\x33\x34\x35' b'\x36\x37\x38\x39'

        self.evt_args_1 = {
            'type': 160,
            'window': 948875838,
            'client_type': 212297388,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'sequence_number': 28171,
            }
        self.evt_bin_1 = b'\xa0\x10\x0b\x6e' b'\x3e\xb2\x8e\x38' \
            b'\xac\x66\xa7\x0c' b'\x01\x00\x02\x00' \
            b'\x03\x00\x04\x00' b'\x05\x00\x06\x00' \
            b'\x07\x00\x08\x00' b'\x09\x00\x0a\x00'

        self.evt_args_2 = {
            'type': 243,
            'window': 581929030,
            'client_type': 966878718,
            'data': (32, [1, 2, 3, 4, 5]),
            'sequence_number': 63569,
            }
        self.evt_bin_2 = b'\xf3\x20\x51\xf8' b'\x46\x88\xaf\x22' \
            b'\xfe\x65\xa1\x39' b'\x01\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x04\x00\x00\x00' b'\x05\x00\x00\x00'


    def testPack0(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPack1(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_1)
        try:
            assert bin == self.evt_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack1(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_1
        except AssertionError:
            raise AssertionError(args)

    def testPack2(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_2)
        try:
            assert bin == self.evt_bin_2
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack2(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_2, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_2
        except AssertionError:
            raise AssertionError(args)


class TestMappingNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'first_keycode': 246,
            'request': 189,
            'type': 198,
            'count': 201,
            'sequence_number': 32665,
            }
        self.evt_bin_0 = b'\xc6\x00\x99\x7f' b'\xbd\xf6\xc9\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MappingNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.MappingNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


if __name__ == "__main__":
    check_endian()
    unittest.main()
