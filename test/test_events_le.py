#!/usr/bin/env python

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import string
import unittest
from Xlib.protocol import request, rq, event
import Xlib.protocol.event

import struct
import array

class CmpArray:
    def __init__(self, *args, **kws):
        self.array = apply(array.array, args, kws)

    def __len__(self):
        return len(self.array)

    def __getslice__(self, x, y):
        return list(self.array[x:y])

    def __getattr__(self, attr):
        return getattr(self.array, attr)

    def __cmp__(self, other):
        return cmp(self.array.tolist(), other)

rq.array = CmpArray

def tohex(bin):
    bin = string.join(map(lambda c: '\\x%02x' % ord(c), bin), '')

    bins = []
    for i in range(0, len(bin), 16):
        bins.append(bin[i:i+16])

    bins2 = []
    for i in range(0, len(bins), 2):
        try:
            bins2.append("'%s' '%s'" % (bins[i], bins[i + 1]))
        except IndexError:
            bins2.append("'%s'" % bins[i])

    return string.join(bins2, ' \\\n            ')

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
        self.evt_bin_0 = '\xad\x82\xb5\xb1' '\xf4\xa7\x90\xd8' \
            '\xb9\xe4\xdc\xfe' '\x82\xef\xd5\x8e' \
            '\xf0\xe9\xf8\xa1' '\xee\xa0\xcd\xd4' \
            '\xcd\xa6\x9c\xf1' '\xa9\xc6\x93\x90'


    def testPack0(self):
        bin = apply(event.KeymapNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xc0\x00\x64\xb2' '\xb0\x95\xcc\x76' \
            '\x24\x3d\xe2\x71' '\xc0\xde\x0d\x74' \
            '\x57\x79\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.Expose._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\x8a\x00\x2c\x25' '\xb1\xf4\xa7\x38' \
            '\x79\xc3\x6c\x09' '\x92\x54\xe1\x28' \
            '\x50\xad\x5a\x1b' '\xee\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.GraphicsExpose._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xc6\x00\x65\xc8' '\x22\x92\xd6\x52' \
            '\xa2\xbf\x95\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.NoExpose._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xe9\x00\x68\x95' '\x72\xac\x93\x32' \
            '\xef\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.VisibilityNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xe6\x00\xbc\x37' '\x55\x6b\xb4\x06' \
            '\x58\x8e\x2b\x4f' '\x94\xca\x74\x85' \
            '\xef\x5f\x63\x22' '\x2c\x80\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.CreateNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xb7\x00\xcf\x93' '\xbd\xad\x2c\x5f' \
            '\x39\xd4\x86\x52' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.DestroyNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xc0\x00\x5f\xd7' '\x1a\x88\x73\x36' \
            '\xf4\xb1\x87\x4b' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.UnmapNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xd8\x00\xd8\x22' '\x94\x5f\x60\x5d' \
            '\xe8\xb1\x5a\x77' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.MapNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xf2\x00\x49\x1a' '\x2d\xaa\xdc\x46' \
            '\x4d\x6b\xba\x67' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.MapRequest._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xb9\x00\x3a\x79' '\xde\x3a\x1d\x50' \
            '\xff\xf9\xc4\x36' '\x1e\x3e\x65\x3e' \
            '\xda\xd1\xfd\xd5' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.ReparentNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xbf\x00\x3a\x55' '\x01\xa9\x53\x7d' \
            '\xe9\xba\x4c\x65' '\x29\x26\x2f\x44' \
            '\x5f\xa3\xb9\x80' '\x7f\x5e\x4d\xad' \
            '\x55\xca\x01\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.ConfigureNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\x8c\x9b\xb4\xbe' '\xfc\xc8\x80\x58' \
            '\xdd\x64\xbd\x20' '\xfe\xe2\xc1\x44' \
            '\xfc\xd2\x05\xfc' '\x4a\xb6\x90\x6a' \
            '\x53\xa1\x1b\xa3' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.ConfigureRequest._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xbf\x00\x58\xbd' '\xe2\x23\x45\x33' \
            '\x38\x1b\xb0\x57' '\x7e\xd5\x27\x97' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.GravityNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\x8b\x00\xe3\x24' '\x73\xcf\x4f\x3b' \
            '\x8a\x22\x3e\xe6' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.ResizeRequest._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xcd\x00\xe2\xb9' '\xbe\x45\x1b\x69' \
            '\x60\x2c\xd0\x02' '\xca\x79\xd2\x37' \
            '\xf1\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.PropertyNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xe8\x00\x24\x68' '\x85\x07\x49\x67' \
            '\x51\x65\x0b\x14' '\xff\x27\x49\x0f' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.SelectionClear._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\x93\x00\x5b\x50' '\xe9\x35\xda\x54' \
            '\xf3\x3e\x97\x2d' '\x41\xc6\xca\x0f' \
            '\xc0\x1f\x8c\x5b' '\x07\xdb\x38\x24' \
            '\x26\x99\x6e\x44' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.SelectionRequest._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\x85\x00\x15\x78' '\xab\x44\xee\x3c' \
            '\xb1\x59\xe8\x39' '\x06\x6d\x83\x13' \
            '\xd1\xfe\xb7\x6f' '\xbe\x02\xcd\x6a' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.SelectionNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xd3\x00\xec\x21' '\xbb\x4b\xb1\x50' \
            '\x9d\xab\x52\x27' '\x01\xa8\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.ColormapNotify._fields.to_binary, (), self.evt_args_0)
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
        self.evt_bin_0 = '\xed\x08\x06\x3a' '\x82\xab\x90\x6b' \
            '\x49\x39\x23\x1b' '\x30\x31\x32\x33' \
            '\x34\x35\x36\x37' '\x38\x39\x30\x31' \
            '\x32\x33\x34\x35' '\x36\x37\x38\x39'

        self.evt_args_1 = {
            'type': 160,
            'window': 948875838,
            'client_type': 212297388,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'sequence_number': 28171,
            }
        self.evt_bin_1 = '\xa0\x10\x0b\x6e' '\x3e\xb2\x8e\x38' \
            '\xac\x66\xa7\x0c' '\x01\x00\x02\x00' \
            '\x03\x00\x04\x00' '\x05\x00\x06\x00' \
            '\x07\x00\x08\x00' '\x09\x00\x0a\x00'

        self.evt_args_2 = {
            'type': 243,
            'window': 581929030,
            'client_type': 966878718,
            'data': (32, [1, 2, 3, 4, 5]),
            'sequence_number': 63569,
            }
        self.evt_bin_2 = '\xf3\x20\x51\xf8' '\x46\x88\xaf\x22' \
            '\xfe\x65\xa1\x39' '\x01\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x04\x00\x00\x00' '\x05\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.ClientMessage._fields.to_binary, (), self.evt_args_0)
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
        bin = apply(event.ClientMessage._fields.to_binary, (), self.evt_args_1)
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
        bin = apply(event.ClientMessage._fields.to_binary, (), self.evt_args_2)
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
        self.evt_bin_0 = '\xc6\x00\x99\x7f' '\xbd\xf6\xc9\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPack0(self):
        bin = apply(event.MappingNotify._fields.to_binary, (), self.evt_args_0)
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
