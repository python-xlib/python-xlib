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
    if struct.unpack('BB', struct.pack('H', 0x0100))[0] != 1:
        sys.stderr.write('Big-endian tests, skipping on this system.\n')
        sys.exit(0)



class TestKeymapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'type': 255,
            'data': [138, 211, 213, 249, 149, 215, 230, 178, 219, 143, 133, 215, 245, 229, 255, 204, 136, 141, 238, 209, 187, 135, 217, 167, 133, 195, 245, 184, 134, 178, 236],
            }
        self.evt_bin_0 = '\xff\x8a\xd3\xd5' '\xf9\x95\xd7\xe6' \
            '\xb2\xdb\x8f\x85' '\xd7\xf5\xe5\xff' \
            '\xcc\x88\x8d\xee' '\xd1\xbb\x87\xd9' \
            '\xa7\x85\xc3\xf5' '\xb8\x86\xb2\xec'


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
            'height': 49582,
            'sequence_number': 27271,
            'type': 184,
            'x': 62946,
            'y': 50538,
            'window': 623716066,
            'width': 21339,
            'count': 36331,
            }
        self.evt_bin_0 = '\xb8\x00\x6a\x87' '\x25\x2d\x26\xe2' \
            '\xf5\xe2\xc5\x6a' '\x53\x5b\xc1\xae' \
            '\x8d\xeb\x00\x00' '\x00\x00\x00\x00' \
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
            'height': 34920,
            'sequence_number': 23281,
            'type': 172,
            'drawable': 735100327,
            'x': 13695,
            'y': 28822,
            'major_event': 183,
            'count': 62976,
            'width': 58911,
            'minor_event': 49173,
            }
        self.evt_bin_0 = '\xac\x00\x5a\xf1' '\x2b\xd0\xbd\xa7' \
            '\x35\x7f\x70\x96' '\xe6\x1f\x88\x68' \
            '\xc0\x15\xf6\x00' '\xb7\x00\x00\x00' \
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
            'sequence_number': 24105,
            'major_event': 237,
            'type': 240,
            'window': 1907711419,
            'minor_event': 22763,
            }
        self.evt_bin_0 = '\xf0\x00\x5e\x29' '\x71\xb5\x5d\xbb' \
            '\x58\xeb\xed\x00' '\x00\x00\x00\x00' \
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
            'state': 187,
            'sequence_number': 46586,
            'type': 135,
            'window': 522025642,
            }
        self.evt_bin_0 = '\x87\x00\xb5\xfa' '\x1f\x1d\x7a\xaa' \
            '\xbb\x00\x00\x00' '\x00\x00\x00\x00' \
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
            'height': 62345,
            'sequence_number': 54477,
            'type': 151,
            'border_width': 16718,
            'x': -21616,
            'y': -23606,
            'override': 1,
            'parent': 573359010,
            'window': 477813132,
            'width': 10293,
            }
        self.evt_bin_0 = '\x97\x00\xd4\xcd' '\x22\x2c\xc3\xa2' \
            '\x1c\x7a\xd9\x8c' '\xab\x90\xa3\xca' \
            '\x28\x35\xf3\x89' '\x41\x4e\x01\x00' \
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
            'sequence_number': 47821,
            'event': 450592933,
            'type': 181,
            'window': 1847295084,
            }
        self.evt_bin_0 = '\xb5\x00\xba\xcd' '\x1a\xdb\x80\xa5' \
            '\x6e\x1b\x7c\x6c' '\x00\x00\x00\x00' \
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
            'from_configure': 0,
            'sequence_number': 59521,
            'event': 215982689,
            'type': 130,
            'window': 511126656,
            }
        self.evt_bin_0 = '\x82\x00\xe8\x81' '\x0c\xdf\xa2\x61' \
            '\x1e\x77\x2c\x80' '\x00\x00\x00\x00' \
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
            'sequence_number': 8913,
            'event': 57885184,
            'type': 245,
            'window': 520206415,
            'override': 0,
            }
        self.evt_bin_0 = '\xf5\x00\x22\xd1' '\x03\x73\x42\x00' \
            '\x1f\x01\xb8\x4f' '\x00\x00\x00\x00' \
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
            'parent': 515013776,
            'sequence_number': 4750,
            'type': 137,
            'window': 1344718970,
            }
        self.evt_bin_0 = '\x89\x00\x12\x8e' '\x1e\xb2\x7c\x90' \
            '\x50\x26\xc8\x7a' '\x00\x00\x00\x00' \
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
            'sequence_number': 13962,
            'event': 1725821076,
            'type': 215,
            'override': 1,
            'x': -24019,
            'y': -9521,
            'parent': 1306130067,
            'window': 1141785517,
            }
        self.evt_bin_0 = '\xd7\x00\x36\x8a' '\x66\xdd\xf0\x94' \
            '\x44\x0e\x43\xad' '\x4d\xd9\xf6\x93' \
            '\xa2\x2d\xda\xcf' '\x01\x00\x00\x00' \
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
            'height': 22676,
            'sequence_number': 63610,
            'event': 807934531,
            'type': 213,
            'border_width': 1080,
            'x': -29787,
            'y': -29137,
            'override': 1,
            'above_sibling': 732901015,
            'window': 495512755,
            'width': 50590,
            }
        self.evt_bin_0 = '\xd5\x00\xf8\x7a' '\x30\x28\x1a\x43' \
            '\x1d\x88\xec\xb3' '\x2b\xaf\x2e\x97' \
            '\x8b\xa5\x8e\x2f' '\xc5\x9e\x58\x94' \
            '\x04\x38\x01\x00' '\x00\x00\x00\x00'


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
            'sequence_number': 476,
            'value_mask': 23711,
            'type': 192,
            'border_width': 61245,
            'x': -18519,
            'y': -25818,
            'window': 116002273,
            'width': 25394,
            'height': 49095,
            'sibling': 1107734662,
            'stack_mode': 221,
            'parent': 305623440,
            }
        self.evt_bin_0 = '\xc0\xdd\x01\xdc' '\x12\x37\x71\x90' \
            '\x06\xea\x0d\xe1' '\x42\x06\xb0\x86' \
            '\xb7\xa9\x9b\x26' '\x63\x32\xbf\xc7' \
            '\xef\x3d\x5c\x9f' '\x00\x00\x00\x00'


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
            'sequence_number': 3556,
            'event': 1678614807,
            'type': 177,
            'window': 262092179,
            'x': -29735,
            'y': -10538,
            }
        self.evt_bin_0 = '\xb1\x00\x0d\xe4' '\x64\x0d\xa1\x17' \
            '\x0f\x9f\x35\x93' '\x8b\xd9\xd6\xd6' \
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
            'height': 1220,
            'sequence_number': 15881,
            'type': 152,
            'window': 1307693775,
            'width': 56632,
            }
        self.evt_bin_0 = '\x98\x00\x3e\x09' '\x4d\xf1\xd2\xcf' \
            '\xdd\x38\x04\xc4' '\x00\x00\x00\x00' \
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
            'atom': 890909209,
            'sequence_number': 32269,
            'time': 1866968150,
            'type': 199,
            'state': 132,
            'window': 1328191351,
            }
        self.evt_bin_0 = '\xc7\x00\x7e\x0d' '\x4f\x2a\x97\x77' \
            '\x35\x1a\x32\x19' '\x6f\x47\xac\x56' \
            '\x84\x00\x00\x00' '\x00\x00\x00\x00' \
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
            'time': 1125695406,
            'sequence_number': 21836,
            'atom': 1124598722,
            'type': 252,
            'window': 1553920847,
            }
        self.evt_bin_0 = '\xfc\x00\x55\x4c' '\x43\x18\xbf\xae' \
            '\x5c\x9e\xf3\x4f' '\x43\x08\x03\xc2' \
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
            'sequence_number': 6923,
            'type': 242,
            'property': 887305180,
            'owner': 1039823940,
            'time': 1209072537,
            'target': 487869453,
            'selection': 1246795803,
            'requestor': 1274632508,
            }
        self.evt_bin_0 = '\xf2\x00\x1b\x0b' '\x48\x10\xfb\x99' \
            '\x3d\xfa\x74\x44' '\x4b\xf9\x59\x3c' \
            '\x4a\x50\x98\x1b' '\x1d\x14\x4c\x0d' \
            '\x34\xe3\x33\xdc' '\x00\x00\x00\x00'


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
            'sequence_number': 4125,
            'type': 139,
            'property': 663510710,
            'time': 904889514,
            'target': 1962029134,
            'selection': 1615988927,
            'requestor': 1772961059,
            }
        self.evt_bin_0 = '\x8b\x00\x10\x1d' '\x35\xef\x84\xaa' \
            '\x69\xad\x3d\x23' '\x60\x52\x08\xbf' \
            '\x74\xf2\x30\x4e' '\x27\x8c\x5e\xb6' \
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
            'state': 191,
            'sequence_number': 8912,
            'colormap': 842531669,
            'type': 136,
            'window': 993201034,
            'new': 1,
            }
        self.evt_bin_0 = '\x88\x00\x22\xd0' '\x3b\x33\x0b\x8a' \
            '\x32\x38\x03\x55' '\x01\xbf\x00\x00' \
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
            'sequence_number': 50515,
            'data': (8, '01234567890123456789'),
            'type': 227,
            'client_type': 238514940,
            'window': 859552707,
            }
        self.evt_bin_0 = '\xe3\x08\xc5\x53' '\x33\x3b\xbb\xc3' \
            '\x0e\x37\x72\xfc' '\x30\x31\x32\x33' \
            '\x34\x35\x36\x37' '\x38\x39\x30\x31' \
            '\x32\x33\x34\x35' '\x36\x37\x38\x39'

        self.evt_args_1 = {
            'sequence_number': 9163,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'type': 192,
            'client_type': 71083170,
            'window': 2104973875,
            }
        self.evt_bin_1 = '\xc0\x10\x23\xcb' '\x7d\x77\x5a\x33' \
            '\x04\x3c\xa4\xa2' '\x00\x01\x00\x02' \
            '\x00\x03\x00\x04' '\x00\x05\x00\x06' \
            '\x00\x07\x00\x08' '\x00\x09\x00\x0a'

        self.evt_args_2 = {
            'sequence_number': 1512,
            'data': (32, [1, 2, 3, 4, 5]),
            'type': 213,
            'client_type': 140121241,
            'window': 612709138,
            }
        self.evt_bin_2 = '\xd5\x20\x05\xe8' '\x24\x85\x33\x12' \
            '\x08\x5a\x14\x99' '\x00\x00\x00\x01' \
            '\x00\x00\x00\x02' '\x00\x00\x00\x03' \
            '\x00\x00\x00\x04' '\x00\x00\x00\x05'


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
            'sequence_number': 21990,
            'count': 161,
            'request': 220,
            'type': 216,
            'first_keycode': 192,
            }
        self.evt_bin_0 = '\xd8\x00\x55\xe6' '\xdc\xc0\xa1\x00' \
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
