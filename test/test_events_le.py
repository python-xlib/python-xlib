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
            'type': 186,
            'data': [165, 253, 213, 175, 197, 174, 235, 241, 132, 130, 197, 157, 194, 140, 236, 206, 159, 165, 149, 171, 171, 204, 253, 164, 141, 173, 190, 230, 133, 204, 180],
            }
        self.evt_bin_0 = '\xba\xa5\xfd\xd5' '\xaf\xc5\xae\xeb' \
            '\xf1\x84\x82\xc5' '\x9d\xc2\x8c\xec' \
            '\xce\x9f\xa5\x95' '\xab\xab\xcc\xfd' \
            '\xa4\x8d\xad\xbe' '\xe6\x85\xcc\xb4'


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
            'height': 57457,
            'sequence_number': 43449,
            'type': 197,
            'x': 39873,
            'y': 36255,
            'window': 2026743979,
            'width': 44271,
            'count': 33251,
            }
        self.evt_bin_0 = '\xc5\x00\xb9\xa9' '\xab\xa8\xcd\x78' \
            '\xc1\x9b\x9f\x8d' '\xef\xac\x71\xe0' \
            '\xe3\x81\x00\x00' '\x00\x00\x00\x00' \
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
            'height': 5890,
            'sequence_number': 45710,
            'type': 229,
            'drawable': 509134898,
            'x': 47429,
            'y': 4032,
            'major_event': 255,
            'count': 19526,
            'width': 26463,
            'minor_event': 6877,
            }
        self.evt_bin_0 = '\xe5\x00\x8e\xb2' '\x32\xc8\x58\x1e' \
            '\x45\xb9\xc0\x0f' '\x5f\x67\x02\x17' \
            '\xdd\x1a\x46\x4c' '\xff\x00\x00\x00' \
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
            'sequence_number': 33494,
            'major_event': 214,
            'type': 201,
            'window': 1850880805,
            'minor_event': 52658,
            }
        self.evt_bin_0 = '\xc9\x00\xd6\x82' '\x25\x33\x52\x6e' \
            '\xb2\xcd\xd6\x00' '\x00\x00\x00\x00' \
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
            'state': 192,
            'sequence_number': 17401,
            'type': 221,
            'window': 2046433634,
            }
        self.evt_bin_0 = '\xdd\x00\xf9\x43' '\x62\x19\xfa\x79' \
            '\xc0\x00\x00\x00' '\x00\x00\x00\x00' \
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
            'height': 16744,
            'sequence_number': 18590,
            'type': 185,
            'border_width': 21365,
            'x': -15988,
            'y': -16181,
            'override': 0,
            'parent': 633561251,
            'window': 943449734,
            'width': 53147,
            }
        self.evt_bin_0 = '\xb9\x00\x9e\x48' '\xa3\x60\xc3\x25' \
            '\x86\xe6\x3b\x38' '\x8c\xc1\xcb\xc0' \
            '\x9b\xcf\x68\x41' '\x75\x53\x00\x00' \
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
            'sequence_number': 1876,
            'event': 1071958935,
            'type': 196,
            'window': 2007819931,
            }
        self.evt_bin_0 = '\xc4\x00\x54\x07' '\x97\xcb\xe4\x3f' \
            '\x9b\xe6\xac\x77' '\x00\x00\x00\x00' \
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
            'from_configure': 1,
            'sequence_number': 21657,
            'event': 1231045924,
            'type': 155,
            'window': 1767649953,
            }
        self.evt_bin_0 = '\x9b\x00\x99\x54' '\x24\x45\x60\x49' \
            '\xa1\x32\x5c\x69' '\x01\x00\x00\x00' \
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
            'sequence_number': 57255,
            'event': 1950231896,
            'type': 209,
            'window': 1876096300,
            'override': 0,
            }
        self.evt_bin_0 = '\xd1\x00\xa7\xdf' '\x58\x2d\x3e\x74' \
            '\x2c\xf5\xd2\x6f' '\x00\x00\x00\x00' \
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
            'parent': 1412864960,
            'sequence_number': 3631,
            'type': 140,
            'window': 909987208,
            }
        self.evt_bin_0 = '\x8c\x00\x2f\x0e' '\xc0\x9b\x36\x54' \
            '\x88\x4d\x3d\x36' '\x00\x00\x00\x00' \
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
            'sequence_number': 8846,
            'event': 154719893,
            'type': 203,
            'override': 0,
            'x': -7695,
            'y': -16870,
            'parent': 434073314,
            'window': 1908206096,
            }
        self.evt_bin_0 = '\xcb\x00\x8e\x22' '\x95\xd6\x38\x09' \
            '\x10\xea\xbc\x71' '\xe2\x6e\xdf\x19' \
            '\xf1\xe1\x1a\xbe' '\x00\x00\x00\x00' \
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
            'height': 21833,
            'sequence_number': 43966,
            'event': 1058232245,
            'type': 209,
            'border_width': 24372,
            'x': -29423,
            'y': -24830,
            'override': 1,
            'above_sibling': 143009970,
            'window': 1313929058,
            'width': 8146,
            }
        self.evt_bin_0 = '\xd1\x00\xbe\xab' '\xb5\x57\x13\x3f' \
            '\x62\xf7\x50\x4e' '\xb2\x28\x86\x08' \
            '\x11\x8d\x02\x9f' '\xd2\x1f\x49\x55' \
            '\x34\x5f\x01\x00' '\x00\x00\x00\x00'


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
            'sequence_number': 50651,
            'value_mask': 29375,
            'type': 176,
            'border_width': 18503,
            'x': -25928,
            'y': -15243,
            'window': 1060859268,
            'width': 14856,
            'height': 63131,
            'sibling': 282352008,
            'stack_mode': 146,
            'parent': 929791867,
            }
        self.evt_bin_0 = '\xb0\x92\xdb\xc5' '\x7b\x7f\x6b\x37' \
            '\x84\x6d\x3b\x3f' '\x88\x59\xd4\x10' \
            '\xb8\x9a\x75\xc4' '\x08\x3a\x9b\xf6' \
            '\x47\x48\xbf\x72' '\x00\x00\x00\x00'


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
            'sequence_number': 7983,
            'event': 196785485,
            'type': 147,
            'window': 1932944214,
            'x': -1592,
            'y': -6080,
            }
        self.evt_bin_0 = '\x93\x00\x2f\x1f' '\x4d\xb5\xba\x0b' \
            '\x56\x63\x36\x73' '\xc8\xf9\x40\xe8' \
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
            'height': 9912,
            'sequence_number': 44998,
            'type': 131,
            'window': 1301144144,
            'width': 29687,
            }
        self.evt_bin_0 = '\x83\x00\xc6\xaf' '\x50\xe2\x8d\x4d' \
            '\xf7\x73\xb8\x26' '\x00\x00\x00\x00' \
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
            'atom': 1495377327,
            'sequence_number': 1751,
            'time': 1695557742,
            'type': 139,
            'state': 163,
            'window': 1112748504,
            }
        self.evt_bin_0 = '\x8b\x00\xd7\x06' '\xd8\x31\x53\x42' \
            '\xaf\xa5\x21\x59' '\x6e\x28\x10\x65' \
            '\xa3\x00\x00\x00' '\x00\x00\x00\x00' \
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
            'time': 1437358133,
            'sequence_number': 60498,
            'atom': 1873249900,
            'type': 138,
            'window': 1733318162,
            }
        self.evt_bin_0 = '\x8a\x00\x52\xec' '\x35\x58\xac\x55' \
            '\x12\x56\x50\x67' '\x6c\x86\xa7\x6f' \
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
            'sequence_number': 36984,
            'type': 211,
            'property': 983580162,
            'owner': 177882841,
            'time': 1526056960,
            'target': 1426934685,
            'selection': 1822659914,
            'requestor': 2139818089,
            }
        self.evt_bin_0 = '\xd3\x00\x78\x90' '\x00\xc8\xf5\x5a' \
            '\xd9\x46\x9a\x0a' '\x69\x08\x8b\x7f' \
            '\x4a\x95\xa3\x6c' '\x9d\x4b\x0d\x55' \
            '\x02\x3e\xa0\x3a' '\x00\x00\x00\x00'


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
            'sequence_number': 33180,
            'type': 134,
            'property': 921665219,
            'time': 2051752575,
            'target': 430622250,
            'selection': 1613640904,
            'requestor': 2117848699,
            }
        self.evt_bin_0 = '\x86\x00\x9c\x81' '\x7f\x42\x4b\x7a' \
            '\x7b\xce\x3b\x7e' '\xc8\x34\x2e\x60' \
            '\x2a\xc6\xaa\x19' '\xc3\x7e\xef\x36' \
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
            'state': 160,
            'sequence_number': 50674,
            'colormap': 1988387051,
            'type': 198,
            'window': 1445764713,
            'new': 1,
            }
        self.evt_bin_0 = '\xc6\x00\xf2\xc5' '\x69\x9e\x2c\x56' \
            '\xeb\x60\x84\x76' '\x01\xa0\x00\x00' \
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
            'sequence_number': 51883,
            'data': (8, '01234567890123456789'),
            'type': 223,
            'client_type': 926681334,
            'window': 1737261199,
            }
        self.evt_bin_0 = '\xdf\x08\xab\xca' '\x8f\x80\x8c\x67' \
            '\xf6\x08\x3c\x37' '\x30\x31\x32\x33' \
            '\x34\x35\x36\x37' '\x38\x39\x30\x31' \
            '\x32\x33\x34\x35' '\x36\x37\x38\x39'

        self.evt_args_1 = {
            'sequence_number': 47465,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'type': 136,
            'client_type': 125979976,
            'window': 1615259319,
            }
        self.evt_bin_1 = '\x88\x10\x69\xb9' '\xb7\xe6\x46\x60' \
            '\x48\x4d\x82\x07' '\x01\x00\x02\x00' \
            '\x03\x00\x04\x00' '\x05\x00\x06\x00' \
            '\x07\x00\x08\x00' '\x09\x00\x0a\x00'

        self.evt_args_2 = {
            'sequence_number': 54021,
            'data': (32, [1, 2, 3, 4, 5]),
            'type': 184,
            'client_type': 1714086272,
            'window': 1276109555,
            }
        self.evt_bin_2 = '\xb8\x20\x05\xd3' '\xf3\xe2\x0f\x4c' \
            '\x80\xe1\x2a\x66' '\x01\x00\x00\x00' \
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
            'sequence_number': 1565,
            'count': 221,
            'request': 209,
            'type': 182,
            'first_keycode': 179,
            }
        self.evt_bin_0 = '\xb6\x00\x1d\x06' '\xd1\xb3\xdd\x00' \
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
