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



class TestCreateWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 8017,
            'window_class': 0,
            'border_width': 26096,
            'visual': 27534831,
            'x': -28091,
            'y': -29791,
            'parent': 1931287363,
            'attrs': {'backing_pixel': 1636335129, 'cursor': 1539745537, 'background_pixmap': 1319334920, 'border_pixmap': 865648768, 'backing_planes': 88009460, 'win_gravity': 0, 'backing_store': 0, 'event_mask': 1604514590, 'save_under': 0, 'background_pixel': 215391800, 'colormap': 2039891007, 'border_pixel': 910242230, 'bit_gravity': 1, 'do_not_propagate_mask': 1541988605, 'override_redirect': 0},
            'wid': 1518857223,
            'depth': 213,
            'width': 15396,
            }
        self.req_bin_0 = '\x01\xd5\x00\x17' '\x5a\x87\xec\x07' \
            '\x73\x1d\x1b\x43' '\x92\x45\x8b\xa1' \
            '\x3c\x24\x1f\x51' '\x65\xf0\x00\x00' \
            '\x01\xa4\x25\xef' '\x00\x00\x7f\xff' \
            '\x4e\xa3\x74\x08' '\x0c\xd6\x9e\x38' \
            '\x33\x98\xc0\x80' '\x36\x41\x31\xb6' \
            '\x01\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x05\x3e\xea\xf4' \
            '\x61\x88\x7e\x19' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x5f\xa2\xf3\x1e' \
            '\x5b\xe8\xe0\xfd' '\x79\x96\x44\x3f' \
            '\x5b\xc6\xa7\x01'


    def testPackRequest0(self):
	bin = apply(request.CreateWindow._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CreateWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeWindowAttributes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 493630976,
            'attrs': {'backing_pixel': 1526297547, 'cursor': 1900655715, 'background_pixmap': 1900827120, 'border_pixmap': 1555500281, 'backing_planes': 1744890268, 'win_gravity': 3, 'backing_store': 2, 'event_mask': 901533631, 'save_under': 0, 'background_pixel': 1743143905, 'colormap': 684397188, 'border_pixel': 1616380377, 'bit_gravity': 5, 'do_not_propagate_mask': 648986533, 'override_redirect': 1},
            }
        self.req_bin_0 = '\x02\x00\x00\x12' '\x1d\x6c\x36\x00' \
            '\x00\x00\x7f\xff' '\x71\x4c\x51\xf0' \
            '\x67\xe6\x43\xe1' '\x5c\xb7\x0c\xf9' \
            '\x60\x58\x01\xd9' '\x05\x00\x00\x00' \
            '\x03\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x68\x00\xe9\x9c' '\x5a\xf9\x73\xcb' \
            '\x01\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x35\xbc\x4f\xbf' '\x26\xae\xbf\xa5' \
            '\x28\xcb\x12\x84' '\x71\x49\xb4\x63'


    def testPackRequest0(self):
	bin = apply(request.ChangeWindowAttributes._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeWindowAttributes._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetWindowAttributes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 2129386044,
            }
        self.req_bin_0 = '\x03\x00\x00\x02' '\x7e\xeb\xda\x3c'

        self.reply_args_0 = {
            'sequence_number': 684,
            'backing_pixel': 1215988101,
            'your_event_mask': 635227602,
            'map_is_installed': 1,
            'visual': 1721640481,
            'backing_bit_planes': 206375047,
            'backing_store': 171,
            'win_class': 17392,
            'map_state': 146,
            'save_under': 0,
            'all_event_masks': 906761091,
            'colormap': 627072806,
            'win_gravity': 219,
            'bit_gravity': 207,
            'do_not_propagate_mask': 34958,
            'override_redirect': 1,
            }
        self.reply_bin_0 = '\x01\xab\x02\xac' '\x00\x00\x00\x03' \
            '\x66\x9e\x26\x21' '\x43\xf0\xcf\xdb' \
            '\x0c\x4d\x08\x87' '\x48\x7a\x81\x85' \
            '\x00\x01\x92\x01' '\x25\x60\x5f\x26' \
            '\x36\x0c\x13\x83' '\x25\xdc\xcd\xd2' \
            '\x88\x8e\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetWindowAttributes._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetWindowAttributes._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetWindowAttributes._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetWindowAttributes._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestDestroyWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1632489677,
            }
        self.req_bin_0 = '\x04\x00\x00\x02' '\x61\x4d\xd0\xcd'


    def testPackRequest0(self):
	bin = apply(request.DestroyWindow._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.DestroyWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestDestroySubWindows(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 826551555,
            }
        self.req_bin_0 = '\x05\x00\x00\x02' '\x31\x44\x2d\x03'


    def testPackRequest0(self):
	bin = apply(request.DestroySubWindows._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.DestroySubWindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeSaveSet(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1134467028,
            'mode': 1,
            }
        self.req_bin_0 = '\x06\x01\x00\x02' '\x43\x9e\x97\xd4'


    def testPackRequest0(self):
	bin = apply(request.ChangeSaveSet._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeSaveSet._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestReparentWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'parent': 646041806,
            'window': 1176456834,
            'x': -7243,
            'y': -14560,
            }
        self.req_bin_0 = '\x07\x00\x00\x04' '\x46\x1f\x4e\x82' \
            '\x26\x81\xd0\xce' '\xe3\xb5\xc7\x20'


    def testPackRequest0(self):
	bin = apply(request.ReparentWindow._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ReparentWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestMapWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 625741822,
            }
        self.req_bin_0 = '\x08\x00\x00\x02' '\x25\x4c\x0f\xfe'


    def testPackRequest0(self):
	bin = apply(request.MapWindow._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.MapWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestMapSubwindows(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1721765455,
            }
        self.req_bin_0 = '\x09\x00\x00\x02' '\x66\xa0\x0e\x4f'


    def testPackRequest0(self):
	bin = apply(request.MapSubwindows._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.MapSubwindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUnmapWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 31438060,
            }
        self.req_bin_0 = '\x0a\x00\x00\x02' '\x01\xdf\xb4\xec'


    def testPackRequest0(self):
	bin = apply(request.UnmapWindow._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UnmapWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUnmapSubwindows(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 677486736,
            }
        self.req_bin_0 = '\x0b\x00\x00\x02' '\x28\x61\xa0\x90'


    def testPackRequest0(self):
	bin = apply(request.UnmapSubwindows._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UnmapSubwindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestConfigureWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 885962653,
            'attrs': {'height': 62873, 'stack_mode': 0, 'border_width': -10216, 'width': 52140, 'x': -10545, 'y': -2207, 'sibling': 71494572},
            }
        self.req_bin_0 = '\x0c\x00\x00\x0a' '\x34\xce\xb7\x9d' \
            '\x00\x7f\x00\x00' '\xd6\xcf\x00\x00' \
            '\xf7\x61\x00\x00' '\xcb\xac\x00\x00' \
            '\xf5\x99\x00\x00' '\xd8\x18\x00\x00' \
            '\x04\x42\xeb\xac' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.ConfigureWindow._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ConfigureWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCirculateWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 77364842,
            'direction': 1,
            }
        self.req_bin_0 = '\x0d\x01\x00\x02' '\x04\x9c\x7e\x6a'


    def testPackRequest0(self):
	bin = apply(request.CirculateWindow._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CirculateWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetGeometry(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 977796786,
            }
        self.req_bin_0 = '\x0e\x00\x00\x02' '\x3a\x47\xfe\xb2'

        self.reply_args_0 = {
            'height': 45221,
            'sequence_number': 9202,
            'root': 759718037,
            'border_width': 33359,
            'x': -12419,
            'y': -3489,
            'depth': 148,
            'width': 38496,
            }
        self.reply_bin_0 = '\x01\x94\x23\xf2' '\x00\x00\x00\x00' \
            '\x2d\x48\x60\x95' '\xcf\x7d\xf2\x5f' \
            '\x96\x60\xb0\xa5' '\x82\x4f\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetGeometry._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetGeometry._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetGeometry._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetGeometry._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryTree(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 49429933,
            }
        self.req_bin_0 = '\x0f\x00\x00\x02' '\x02\xf2\x3d\xad'

        self.reply_args_0 = {
            'sequence_number': 13932,
            'children': [1284111955, 1535789363, 997347451, 1390691755, 1415925637, 1112347998, 1171156860],
            'root': 1242921847,
            'parent': 1785248681,
            }
        self.reply_bin_0 = '\x01\x00\x36\x6c' '\x00\x00\x00\x07' \
            '\x4a\x15\x7b\x77' '\x6a\x68\xbb\xa9' \
            '\x00\x07\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x4c\x89\xfe\x53' '\x5b\x8a\x49\x33' \
            '\x3b\x72\x50\x7b' '\x52\xe4\x45\xab' \
            '\x54\x65\x4f\x85' '\x42\x4d\x15\x5e' \
            '\x45\xce\x6f\x7c'


    def testPackRequest0(self):
	bin = apply(request.QueryTree._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryTree._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryTree._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryTree._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestInternAtom(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'only_if_exists': 1,
            'name': 'fuzzy_prop',
            }
        self.req_bin_0 = '\x10\x01\x00\x05' '\x00\x0a\x00\x00' \
            '\x66\x75\x7a\x7a' '\x79\x5f\x70\x72' \
            '\x6f\x70\x00\x00'

        self.reply_args_0 = {
            'atom': 794539351,
            'sequence_number': 16414,
            }
        self.reply_bin_0 = '\x01\x00\x40\x1e' '\x00\x00\x00\x00' \
            '\x2f\x5b\xb5\x57' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.InternAtom._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.InternAtom._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.InternAtom._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.InternAtom._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetAtomName(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'atom': 316187350,
            }
        self.req_bin_0 = '\x11\x00\x00\x02' '\x12\xd8\xa2\xd6'

        self.reply_args_0 = {
            'sequence_number': 40025,
            'name': 'WM_CLASS',
            }
        self.reply_bin_0 = '\x01\x00\x9c\x59' '\x00\x00\x00\x02' \
            '\x00\x08\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x57\x4d\x5f\x43' '\x4c\x41\x53\x53'


    def testPackRequest0(self):
	bin = apply(request.GetAtomName._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetAtomName._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetAtomName._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetAtomName._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeProperty(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 2,
            'data': (8, ''),
            'property': 82619519,
            'window': 1936652744,
            'type': 1591525581,
            }
        self.req_bin_0 = '\x12\x02\x00\x06' '\x73\x6e\xf9\xc8' \
            '\x04\xec\xac\x7f' '\x5e\xdc\xc0\xcd' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_1 = {
            'mode': 0,
            'data': (8, 'foo'),
            'property': 803154106,
            'window': 981881030,
            'type': 1935232599,
            }
        self.req_bin_1 = '\x12\x00\x00\x07' '\x3a\x86\x50\xc6' \
            '\x2f\xdf\x28\xba' '\x73\x59\x4e\x57' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x03' \
            '\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'mode': 1,
            'data': (8, 'zoom'),
            'property': 1831275700,
            'window': 1853431204,
            'type': 799075221,
            }
        self.req_bin_2 = '\x12\x01\x00\x07' '\x6e\x79\x1d\xa4' \
            '\x6d\x27\x0c\xb4' '\x2f\xa0\xeb\x95' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x04' \
            '\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'mode': 1,
            'data': (16, []),
            'property': 1432188130,
            'window': 486904700,
            'type': 816234557,
            }
        self.req_bin_3 = '\x12\x01\x00\x06' '\x1d\x05\x93\x7c' \
            '\x55\x5d\x74\xe2' '\x30\xa6\xc0\x3d' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_4 = {
            'mode': 0,
            'data': (16, [1, 2, 3]),
            'property': 371065440,
            'window': 74539077,
            'type': 881569585,
            }
        self.req_bin_4 = '\x12\x00\x00\x08' '\x04\x71\x60\x45' \
            '\x16\x1e\x02\x60' '\x34\x8b\xaf\x31' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x03' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x00'

        self.req_args_5 = {
            'mode': 0,
            'data': (16, [1, 2, 3, 4]),
            'property': 504204653,
            'window': 1773466214,
            'type': 891164184,
            }
        self.req_bin_5 = '\x12\x00\x00\x08' '\x69\xb4\xf2\x66' \
            '\x1e\x0d\x8d\x6d' '\x35\x1e\x16\x18' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x04' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x04'

        self.req_args_6 = {
            'mode': 0,
            'data': (32, []),
            'property': 27953905,
            'window': 1297035056,
            'type': 1459050202,
            }
        self.req_bin_6 = '\x12\x00\x00\x06' '\x4d\x4f\x2f\x30' \
            '\x01\xaa\x8a\xf1' '\x56\xf7\x56\xda' \
            '\x20\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_7 = {
            'mode': 0,
            'data': (32, [1, 2, 3]),
            'property': 1741278545,
            'window': 1158053012,
            'type': 733433491,
            }
        self.req_bin_7 = '\x12\x00\x00\x09' '\x45\x06\x7c\x94' \
            '\x67\xc9\xcd\x51' '\x2b\xb7\x4e\x93' \
            '\x20\x00\x00\x00' '\x00\x00\x00\x03' \
            '\x00\x00\x00\x01' '\x00\x00\x00\x02' \
            '\x00\x00\x00\x03'


    def testPackRequest0(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest1(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_1)
	try:
	    assert bin == self.req_bin_1
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_1, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_1
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest2(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_2)
	try:
	    assert bin == self.req_bin_2
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest2(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_2, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_2
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest3(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_3)
	try:
	    assert bin == self.req_bin_3
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest3(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_3, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_3
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest4(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_4)
	try:
	    assert bin == self.req_bin_4
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest4(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_4, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_4
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest5(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_5)
	try:
	    assert bin == self.req_bin_5
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest5(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_5, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_5
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest6(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_6)
	try:
	    assert bin == self.req_bin_6
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest6(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_6, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_6
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest7(self):
	bin = apply(request.ChangeProperty._request.to_binary, (), self.req_args_7)
	try:
	    assert bin == self.req_bin_7
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest7(self):
	args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_7, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_7
	except AssertionError:
	    raise AssertionError(args)


class TestDeleteProperty(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'property': 1994510403,
            'window': 466309545,
            }
        self.req_bin_0 = '\x13\x00\x00\x03' '\x1b\xcb\x51\xa9' \
            '\x76\xe1\xd0\x43'


    def testPackRequest0(self):
	bin = apply(request.DeleteProperty._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.DeleteProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetProperty(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'delete': 0,
            'long_offset': 1283540610,
            'type': 485645138,
            'property': 1402311712,
            'window': 791763871,
            'long_length': 534564962,
            }
        self.req_bin_0 = '\x14\x00\x00\x06' '\x2f\x31\x5b\x9f' \
            '\x53\x95\x94\x20' '\x1c\xf2\x5b\x52' \
            '\x4c\x81\x46\x82' '\x1f\xdc\xd0\x62'

        self.reply_args_0 = {
            'value': (8, ''),
            'sequence_number': 27146,
            'property_type': 884105478,
            'bytes_after': 85920624,
            }
        self.reply_bin_0 = '\x01\x08\x6a\x0a' '\x00\x00\x00\x00' \
            '\x34\xb2\x61\x06' '\x05\x1f\x0b\x70' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_1 = {
            'value': (8, 'foo'),
            'sequence_number': 28401,
            'property_type': 380401845,
            'bytes_after': 1645202351,
            }
        self.reply_bin_1 = '\x01\x08\x6e\xf1' '\x00\x00\x00\x01' \
            '\x16\xac\x78\xb5' '\x62\x0f\xcb\xaf' \
            '\x00\x00\x00\x03' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'value': (8, 'zoom'),
            'sequence_number': 50575,
            'property_type': 435515687,
            'bytes_after': 911516252,
            }
        self.reply_bin_2 = '\x01\x08\xc5\x8f' '\x00\x00\x00\x01' \
            '\x19\xf5\x71\x27' '\x36\x54\xa2\x5c' \
            '\x00\x00\x00\x04' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'value': (16, []),
            'sequence_number': 19997,
            'property_type': 1790987501,
            'bytes_after': 1155806822,
            }
        self.reply_bin_3 = '\x01\x10\x4e\x1d' '\x00\x00\x00\x00' \
            '\x6a\xc0\x4c\xed' '\x44\xe4\x36\x66' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_4 = {
            'value': (16, [1, 2, 3]),
            'sequence_number': 17501,
            'property_type': 577570483,
            'bytes_after': 1781252251,
            }
        self.reply_bin_4 = '\x01\x10\x44\x5d' '\x00\x00\x00\x02' \
            '\x22\x6d\x06\xb3' '\x6a\x2b\xc0\x9b' \
            '\x00\x00\x00\x03' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x00'

        self.reply_args_5 = {
            'value': (16, [1, 2, 3, 4]),
            'sequence_number': 63601,
            'property_type': 1342924557,
            'bytes_after': 1300307621,
            }
        self.reply_bin_5 = '\x01\x10\xf8\x71' '\x00\x00\x00\x02' \
            '\x50\x0b\x67\x0d' '\x4d\x81\x1e\xa5' \
            '\x00\x00\x00\x04' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x04'

        self.reply_args_6 = {
            'value': (32, []),
            'sequence_number': 50241,
            'property_type': 1454033561,
            'bytes_after': 1795857659,
            }
        self.reply_bin_6 = '\x01\x20\xc4\x41' '\x00\x00\x00\x00' \
            '\x56\xaa\xca\x99' '\x6b\x0a\x9c\xfb' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_7 = {
            'value': (32, [1, 2, 3]),
            'sequence_number': 45389,
            'property_type': 231398758,
            'bytes_after': 420608897,
            }
        self.reply_bin_7 = '\x01\x20\xb1\x4d' '\x00\x00\x00\x03' \
            '\x0d\xca\xdd\x66' '\x19\x11\xfb\x81' \
            '\x00\x00\x00\x03' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x01' '\x00\x00\x00\x02' \
            '\x00\x00\x00\x03'


    def testPackRequest0(self):
	bin = apply(request.GetProperty._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply1(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_1)
	try:
	    assert bin == self.reply_bin_1
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply1(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_1
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply2(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_2)
	try:
	    assert bin == self.reply_bin_2
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply2(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_2, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_2
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply3(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_3)
	try:
	    assert bin == self.reply_bin_3
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply3(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_3, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_3
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply4(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_4)
	try:
	    assert bin == self.reply_bin_4
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply4(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_4, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_4
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply5(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_5)
	try:
	    assert bin == self.reply_bin_5
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply5(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_5, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_5
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply6(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_6)
	try:
	    assert bin == self.reply_bin_6
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply6(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_6, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_6
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply7(self):
	bin = apply(request.GetProperty._reply.to_binary, (), self.reply_args_7)
	try:
	    assert bin == self.reply_bin_7
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply7(self):
	args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_7, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_7
	except AssertionError:
	    raise AssertionError(args)


class TestListProperties(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 341494173,
            }
        self.req_bin_0 = '\x15\x00\x00\x02' '\x14\x5a\xc9\x9d'

        self.reply_args_0 = {
            'atoms': [1617001909, 966627805, 408888265, 2125379596, 336611549, 1299489908, 1153481135, 1085240351, 1922638622, 685228525, 914772856, 716185178, 301566504, 1129819135, 1664787249, 2052336342, 664569412, 194232880, 1711457295, 754508835, 842780763, 542652673, 1217861008],
            'sequence_number': 7569,
            }
        self.reply_bin_0 = '\x01\x00\x1d\x91' '\x00\x00\x00\x17' \
            '\x00\x17\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x60\x61\x7d\xb5' '\x39\x9d\x91\xdd' \
            '\x18\x5f\x23\xc9' '\x7e\xae\xb8\x0c' \
            '\x14\x10\x48\xdd' '\x4d\x74\xa4\x74' \
            '\x44\xc0\xb9\xaf' '\x40\xaf\x74\x1f' \
            '\x72\x99\x23\x1e' '\x28\xd7\xc1\xed' \
            '\x36\x86\x53\x78' '\x2a\xb0\x1e\x5a' \
            '\x11\xf9\x8a\x28' '\x43\x57\xab\xff' \
            '\x63\x3a\xa3\x31' '\x7a\x54\x2a\xd6' \
            '\x27\x9c\x86\x44' '\x0b\x93\xc2\x30' \
            '\x66\x02\xc4\x0f' '\x2c\xf8\xe4\x23' \
            '\x32\x3b\xd0\x5b' '\x20\x58\x39\x01' \
            '\x48\x97\x15\x90'


    def testPackRequest0(self):
	bin = apply(request.ListProperties._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ListProperties._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.ListProperties._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.ListProperties._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetSelectionOwner(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'selection': 1027330706,
            'window': 704808783,
            'time': 902673423,
            }
        self.req_bin_0 = '\x16\x00\x00\x04' '\x2a\x02\x87\x4f' \
            '\x3d\x3b\xd2\x92' '\x35\xcd\xb4\x0f'


    def testPackRequest0(self):
	bin = apply(request.SetSelectionOwner._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetSelectionOwner._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetSelectionOwner(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'selection': 645944405,
            }
        self.req_bin_0 = '\x17\x00\x00\x02' '\x26\x80\x54\x55'

        self.reply_args_0 = {
            'sequence_number': 1155,
            'owner': 1352532776,
            }
        self.reply_bin_0 = '\x01\x00\x04\x83' '\x00\x00\x00\x00' \
            '\x50\x9e\x03\x28' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetSelectionOwner._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetSelectionOwner._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetSelectionOwner._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetSelectionOwner._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestConvertSelection(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'property': 2021418962,
            'time': 1724767916,
            'target': 2069704072,
            'selection': 1440635975,
            'requestor': 271146474,
            }
        self.req_bin_0 = '\x18\x00\x00\x06' '\x10\x29\x5d\xea' \
            '\x55\xde\x5c\x47' '\x7b\x5d\x2d\x88' \
            '\x78\x7c\x67\xd2' '\x66\xcd\xde\xac'


    def testPackRequest0(self):
	bin = apply(request.ConvertSelection._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ConvertSelection._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSendEvent(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'event': Xlib.protocol.event.Expose(height = 6296, sequence_number = 0, type = 12, x = 5357, y = 17190, window = 207976521, width = 31176, count = 17217),
            'propagate': 0,
            'destination': 193753361,
            'event_mask': 1487265129,
            }
        self.req_bin_0 = '\x19\x00\x00\x0b' '\x0b\x8c\x71\x11' \
            '\x58\xa5\xdd\x69' '\x0c\x00\x00\x00' \
            '\x0c\x65\x78\x49' '\x14\xed\x43\x26' \
            '\x79\xc8\x18\x98' '\x43\x41\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.SendEvent._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SendEvent._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGrabPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 1,
            'grab_window': 1960374026,
            'confine_to': 1443156680,
            'event_mask': 8447,
            'pointer_mode': 1,
            'time': 404826547,
            'keyboard_mode': 1,
            'cursor': 791268577,
            }
        self.req_bin_0 = '\x1a\x01\x00\x06' '\x74\xd8\xef\x0a' \
            '\x20\xff\x01\x01' '\x56\x04\xd2\xc8' \
            '\x2f\x29\xcc\xe1' '\x18\x21\x29\xb3'

        self.reply_args_0 = {
            'sequence_number': 53605,
            'status': 241,
            }
        self.reply_bin_0 = '\x01\xf1\xd1\x65' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GrabPointer._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GrabPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GrabPointer._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GrabPointer._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUngrabPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 1988722845,
            }
        self.req_bin_0 = '\x1b\x00\x00\x02' '\x76\x89\x80\x9d'


    def testPackRequest0(self):
	bin = apply(request.UngrabPointer._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UngrabPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGrabButton(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 1,
            'grab_window': 849162323,
            'confine_to': 1710457950,
            'event_mask': 1098,
            'pointer_mode': 1,
            'modifiers': 27305,
            'button': 222,
            'keyboard_mode': 1,
            'cursor': 1192326105,
            }
        self.req_bin_0 = '\x1c\x01\x00\x06' '\x32\x9d\x30\x53' \
            '\x04\x4a\x01\x01' '\x65\xf3\x84\x5e' \
            '\x47\x11\x73\xd9' '\xde\x00\x6a\xa9'


    def testPackRequest0(self):
	bin = apply(request.GrabButton._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GrabButton._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUngrabButton(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'grab_window': 88688623,
            'button': 228,
            'modifiers': 54310,
            }
        self.req_bin_0 = '\x1d\xe4\x00\x03' '\x05\x49\x47\xef' \
            '\xd4\x26\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.UngrabButton._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UngrabButton._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeActivePointerGrab(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 980556286,
            'event_mask': 16740,
            'cursor': 170697366,
            }
        self.req_bin_0 = '\x1e\x00\x00\x04' '\x0a\x2c\xa2\x96' \
            '\x3a\x72\x19\xfe' '\x41\x64\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.ChangeActivePointerGrab._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeActivePointerGrab._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGrabKeyboard(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 1,
            'grab_window': 1936508551,
            'time': 631287008,
            'pointer_mode': 0,
            'keyboard_mode': 0,
            }
        self.req_bin_0 = '\x1f\x01\x00\x04' '\x73\x6c\xc6\x87' \
            '\x25\xa0\xac\xe0' '\x00\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 17578,
            'status': 136,
            }
        self.reply_bin_0 = '\x01\x88\x44\xaa' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GrabKeyboard._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GrabKeyboard._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GrabKeyboard._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GrabKeyboard._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUngrabKeyboard(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 1440514801,
            }
        self.req_bin_0 = '\x20\x00\x00\x02' '\x55\xdc\x82\xf1'


    def testPackRequest0(self):
	bin = apply(request.UngrabKeyboard._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UngrabKeyboard._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGrabKey(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 0,
            'grab_window': 1287894516,
            'pointer_mode': 0,
            'keyboard_mode': 0,
            'modifiers': 5159,
            'key': 234,
            }
        self.req_bin_0 = '\x21\x00\x00\x04' '\x4c\xc3\xb5\xf4' \
            '\x14\x27\xea\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GrabKey._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GrabKey._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUngrabKey(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'grab_window': 1406098011,
            'key': 186,
            'modifiers': 943,
            }
        self.req_bin_0 = '\x22\xba\x00\x03' '\x53\xcf\x5a\x5b' \
            '\x03\xaf\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.UngrabKey._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UngrabKey._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestAllowEvents(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 1018375987,
            'mode': 0,
            }
        self.req_bin_0 = '\x23\x00\x00\x02' '\x3c\xb3\x2f\x33'


    def testPackRequest0(self):
	bin = apply(request.AllowEvents._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.AllowEvents._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGrabServer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x24\x00\x00\x01'


    def testPackRequest0(self):
	bin = apply(request.GrabServer._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GrabServer._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUngrabServer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x25\x00\x00\x01'


    def testPackRequest0(self):
	bin = apply(request.UngrabServer._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UngrabServer._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1326561993,
            }
        self.req_bin_0 = '\x26\x00\x00\x02' '\x4f\x11\xba\xc9'

        self.reply_args_0 = {
            'win_y': -32115,
            'same_screen': 0,
            'sequence_number': 37616,
            'root': 491255377,
            'root_x': -13798,
            'root_y': -27508,
            'mask': 7071,
            'child': 1553693675,
            'win_x': -19638,
            }
        self.reply_bin_0 = '\x01\x00\x92\xf0' '\x00\x00\x00\x00' \
            '\x1d\x47\xf6\x51' '\x5c\x9b\x7b\xeb' \
            '\xca\x1a\x94\x8c' '\xb3\x4a\x82\x8d' \
            '\x1b\x9f\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.QueryPointer._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryPointer._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryPointer._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetMotionEvents(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 808316951,
            'start': 1723735382,
            'stop': 1217054863,
            }
        self.req_bin_0 = '\x27\x00\x00\x04' '\x30\x2d\xf0\x17' \
            '\x66\xbe\x1d\x56' '\x48\x8a\xc8\x8f'

        self.reply_args_0 = {
            'sequence_number': 52617,
            'events': [{'time': 645811678, 'x': -18081, 'y': -24568}, {'time': 829159667, 'x': -17903, 'y': -1674}, {'time': 1116921863, 'x': -29115, 'y': -9275}, {'time': 444509732, 'x': -29034, 'y': -3025}, {'time': 279123109, 'x': -10579, 'y': -24468}],
            }
        self.reply_bin_0 = '\x01\x00\xcd\x89' '\x00\x00\x00\x0a' \
            '\x00\x00\x00\x05' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x26\x7e\x4d\xde' '\xb9\x5f\xa0\x08' \
            '\x31\x6b\xf8\xf3' '\xba\x11\xf9\x76' \
            '\x42\x92\xe0\x07' '\x8e\x45\xdb\xc5' \
            '\x1a\x7e\xae\x24' '\x8e\x96\xf4\x2f' \
            '\x10\xa3\x14\xa5' '\xd6\xad\xa0\x6c'


    def testPackRequest0(self):
	bin = apply(request.GetMotionEvents._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetMotionEvents._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetMotionEvents._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetMotionEvents._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestTranslateCoords(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_y': -14604,
            'src_x': -30988,
            'src_wid': 1191300478,
            'dst_wid': 1366635300,
            }
        self.req_bin_0 = '\x28\x00\x00\x04' '\x47\x01\xcd\x7e' \
            '\x51\x75\x33\x24' '\x86\xf4\xc6\xf4'

        self.reply_args_0 = {
            'child': 930603862,
            'same_screen': 0,
            'sequence_number': 22968,
            'x': -30980,
            'y': -12207,
            }
        self.reply_bin_0 = '\x01\x00\x59\xb8' '\x00\x00\x00\x00' \
            '\x37\x77\xe3\x56' '\x86\xfc\xd0\x51' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.TranslateCoords._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.TranslateCoords._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.TranslateCoords._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.TranslateCoords._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestWarpPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_height': 60128,
            'src_window': 290331047,
            'dst_window': 1731920741,
            'src_width': 11047,
            'src_y': -27951,
            'src_x': -18615,
            'dst_x': -23496,
            'dst_y': -7485,
            }
        self.req_bin_0 = '\x29\x00\x00\x06' '\x11\x4e\x19\xa7' \
            '\x67\x3b\x03\x65' '\xb7\x49\x92\xd1' \
            '\x2b\x27\xea\xe0' '\xa4\x38\xe2\xc3'


    def testPackRequest0(self):
	bin = apply(request.WarpPointer._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.WarpPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetInputFocus(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'revert_to': 2,
            'time': 34713408,
            'focus': 613012524,
            }
        self.req_bin_0 = '\x2a\x02\x00\x03' '\x24\x89\xd4\x2c' \
            '\x02\x11\xaf\x40'


    def testPackRequest0(self):
	bin = apply(request.SetInputFocus._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetInputFocus._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetInputFocus(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x2b\x00\x00\x01'

        self.reply_args_0 = {
            'revert_to': 188,
            'sequence_number': 55940,
            'focus': 868028771,
            }
        self.reply_bin_0 = '\x01\xbc\xda\x84' '\x00\x00\x00\x00' \
            '\x33\xbd\x11\x63' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetInputFocus._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetInputFocus._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetInputFocus._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetInputFocus._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryKeymap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x2c\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 23745,
            'map': [189, 133, 239, 131, 150, 128, 153, 220, 214, 234, 210, 156, 184, 153, 246, 187, 173, 177, 245, 162, 144, 142, 210, 190, 189, 129, 247, 170, 202, 231, 206, 186],
            }
        self.reply_bin_0 = '\x01\x00\x5c\xc1' '\x00\x00\x00\x02' \
            '\xbd\x85\xef\x83' '\x96\x80\x99\xdc' \
            '\xd6\xea\xd2\x9c' '\xb8\x99\xf6\xbb' \
            '\xad\xb1\xf5\xa2' '\x90\x8e\xd2\xbe' \
            '\xbd\x81\xf7\xaa' '\xca\xe7\xce\xba'


    def testPackRequest0(self):
	bin = apply(request.QueryKeymap._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryKeymap._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryKeymap._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryKeymap._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestOpenFont(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'fid': 2075939773,
            'name': 'foofont',
            }
        self.req_bin_0 = '\x2d\x00\x00\x05' '\x7b\xbc\x53\xbd' \
            '\x00\x07\x00\x00' '\x66\x6f\x6f\x66' \
            '\x6f\x6e\x74\x00'


    def testPackRequest0(self):
	bin = apply(request.OpenFont._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.OpenFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCloseFont(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'font': 88898711,
            }
        self.req_bin_0 = '\x2e\x00\x00\x02' '\x05\x4c\x7c\x97'


    def testPackRequest0(self):
	bin = apply(request.CloseFont._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CloseFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryFont(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'font': 716293692,
            }
        self.req_bin_0 = '\x2f\x00\x00\x02' '\x2a\xb1\xc6\x3c'

        self.reply_args_0 = {
            'sequence_number': 50820,
            'properties': [{'value': 713484825, 'name': 1692974835}],
            'min_byte1': 218,
            'max_byte1': 200,
            'char_infos': [{'descent': -22353, 'ascent': -9095, 'character_width': -6458, 'left_side_bearing': -1262, 'right_side_bearing': -19985, 'attributes': 60178}, {'descent': -21211, 'ascent': -544, 'character_width': -23225, 'left_side_bearing': -30015, 'right_side_bearing': -26583, 'attributes': 20388}, {'descent': -10287, 'ascent': -8442, 'character_width': -12897, 'left_side_bearing': -19304, 'right_side_bearing': -24896, 'attributes': 52972}],
            'max_char_or_byte2': 29619,
            'default_char': 49313,
            'min_char_or_byte2': 19883,
            'draw_direction': 253,
            'min_bounds': {'descent': -19681, 'ascent': -3713, 'character_width': -11983, 'left_side_bearing': -10184, 'right_side_bearing': -8954, 'attributes': 62773},
            'all_chars_exist': 1,
            'font_ascent': -30023,
            'font_descent': -18769,
            'max_bounds': {'descent': -3417, 'ascent': -21488, 'character_width': -11884, 'left_side_bearing': -27819, 'right_side_bearing': -17428, 'attributes': 17493},
            }
        self.reply_bin_0 = '\x01\x00\xc6\x84' '\x00\x00\x00\x12' \
            '\xd8\x38\xdd\x06' '\xd1\x31\xf1\x7f' \
            '\xb3\x1f\xf5\x35' '\x00\x00\x00\x00' \
            '\x93\x55\xbb\xec' '\xd1\x94\xac\x10' \
            '\xf2\xa7\x44\x55' '\x00\x00\x00\x00' \
            '\x4d\xab\x73\xb3' '\xc0\xa1\x00\x01' \
            '\xfd\xda\xc8\x01' '\x8a\xb9\xb6\xaf' \
            '\x00\x00\x00\x03' '\x64\xe8\xbe\xf3' \
            '\x2a\x86\xea\x19' '\xfb\x12\xb1\xef' \
            '\xe6\xc6\xdc\x79' '\xa8\xaf\xeb\x12' \
            '\x8a\xc1\x98\x29' '\xa5\x47\xfd\xe0' \
            '\xad\x25\x4f\xa4' '\xb4\x98\x9e\xc0' \
            '\xcd\x9f\xdf\x06' '\xd7\xd1\xce\xec'


    def testPackRequest0(self):
	bin = apply(request.QueryFont._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryFont._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryFont._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryTextExtents(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'font': 1817418879,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = '\x30\x01\x00\x04' '\x6c\x53\x9c\x7f' \
            '\x00\x66\x00\x6f' '\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'overall_width': -1268975420,
            'draw_direction': 197,
            'sequence_number': 53207,
            'font_ascent': -20024,
            'overall_ascent': -21313,
            'overall_descent': -12047,
            'overall_right': -478689925,
            'overall_left': -1183220348,
            'font_descent': -11736,
            }
        self.reply_bin_0 = '\x01\xc5\xcf\xd7' '\x00\x00\x00\x00' \
            '\xb1\xc8\xd2\x28' '\xac\xbf\xd0\xf1' \
            '\xb4\x5c\xf8\xc4' '\xb9\x79\x7d\x84' \
            '\xe3\x77\xc5\x7b' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.QueryTextExtents._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryTextExtents._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryTextExtents._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryTextExtents._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestListFonts(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'max_names': 43767,
            'pattern': 'bhazr',
            }
        self.req_bin_0 = '\x31\x00\x00\x04' '\xaa\xf7\x00\x05' \
            '\x62\x68\x61\x7a' '\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 43371,
            }
        self.reply_bin_0 = '\x01\x00\xa9\x6b' '\x00\x00\x00\x05' \
            '\x00\x03\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x03\x66\x69\x65' '\x05\x66\x75\x7a' \
            '\x7a\x79\x08\x66' '\x6f\x6f\x7a\x6f' \
            '\x6f\x6f\x6d\x00'


    def testPackRequest0(self):
	bin = apply(request.ListFonts._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ListFonts._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.ListFonts._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.ListFonts._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestListFontsWithInfo(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'max_names': 30605,
            'pattern': 'bhazr2',
            }
        self.req_bin_0 = '\x32\x00\x00\x04' '\x77\x8d\x00\x06' \
            '\x62\x68\x61\x7a' '\x72\x32\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 18397,
            'properties': [{'value': 890678602, 'name': 1360918406}],
            'min_byte1': 222,
            'max_byte1': 203,
            'max_char_or_byte2': 31725,
            'default_char': 24807,
            'min_char_or_byte2': 16168,
            'draw_direction': 237,
            'replies_hint': 1055777945,
            'min_bounds': {'descent': -32699, 'ascent': -24692, 'character_width': -29002, 'left_side_bearing': -13863, 'right_side_bearing': -12569, 'attributes': 44827},
            'all_chars_exist': 0,
            'name': 'fontfont',
            'font_ascent': -16158,
            'font_descent': -16573,
            'max_bounds': {'descent': -31395, 'ascent': -20537, 'character_width': -3642, 'left_side_bearing': -19158, 'right_side_bearing': -14776, 'attributes': 27483},
            }
        self.reply_bin_0 = '\x01\x08\x47\xdd' '\x00\x00\x00\x0b' \
            '\xc9\xd9\xce\xe7' '\x8e\xb6\x9f\x8c' \
            '\x80\x45\xaf\x1b' '\x00\x00\x00\x00' \
            '\xb5\x2a\xc6\x48' '\xf1\xc6\xaf\xc7' \
            '\x85\x5d\x6b\x5b' '\x00\x00\x00\x00' \
            '\x3f\x28\x7b\xed' '\x60\xe7\x00\x01' \
            '\xed\xde\xcb\x00' '\xc0\xe2\xbf\x43' \
            '\x3e\xed\xe4\x99' '\x51\x1d\xf7\x86' \
            '\x35\x16\xad\x4a' '\x66\x6f\x6e\x74' \
            '\x66\x6f\x6e\x74'


    def testPackRequest0(self):
	bin = apply(request.ListFontsWithInfo._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ListFontsWithInfo._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.ListFontsWithInfo._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.ListFontsWithInfo._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetFontPath(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'path': ['foo', 'bar', 'gazonk'],
            }
        self.req_bin_0 = '\x33\x00\x00\x06' '\x00\x03\x00\x00' \
            '\x03\x66\x6f\x6f' '\x03\x62\x61\x72' \
            '\x06\x67\x61\x7a' '\x6f\x6e\x6b\x00'

        self.req_args_1 = {
            'path': [],
            }
        self.req_bin_1 = '\x33\x00\x00\x02' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.SetFontPath._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetFontPath._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest1(self):
	bin = apply(request.SetFontPath._request.to_binary, (), self.req_args_1)
	try:
	    assert bin == self.req_bin_1
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
	args, remain = request.SetFontPath._request.parse_binary(self.req_bin_1, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_1
	except AssertionError:
	    raise AssertionError(args)


class TestGetFontPath(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x34\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 14600,
            'paths': ['path1', 'path2232'],
            }
        self.reply_bin_0 = '\x01\x00\x39\x08' '\x00\x00\x00\x04' \
            '\x00\x02\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x05\x70\x61\x74' '\x68\x31\x08\x70' \
            '\x61\x74\x68\x32' '\x32\x33\x32\x00'

        self.reply_args_1 = {
            'sequence_number': 45691,
            'paths': [],
            }
        self.reply_bin_1 = '\x01\x00\xb2\x7b' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetFontPath._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetFontPath._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetFontPath._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetFontPath._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply1(self):
	bin = apply(request.GetFontPath._reply.to_binary, (), self.reply_args_1)
	try:
	    assert bin == self.reply_bin_1
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply1(self):
	args, remain = request.GetFontPath._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_1
	except AssertionError:
	    raise AssertionError(args)


class TestCreatePixmap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 5554,
            'drawable': 317771446,
            'pid': 925741638,
            'depth': 183,
            'width': 21598,
            }
        self.req_bin_0 = '\x35\xb7\x00\x04' '\x37\x2d\xb2\x46' \
            '\x12\xf0\xce\xb6' '\x54\x5e\x15\xb2'


    def testPackRequest0(self):
	bin = apply(request.CreatePixmap._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CreatePixmap._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestFreePixmap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'pixmap': 1023774795,
            }
        self.req_bin_0 = '\x36\x00\x00\x02' '\x3d\x05\x90\x4b'


    def testPackRequest0(self):
	bin = apply(request.FreePixmap._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.FreePixmap._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCreateGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cid': 1381133851,
            'drawable': 91017816,
            'attrs': {'dashes': 219, 'fill_rule': 0, 'clip_mask': 861969422, 'plane_mask': 593066296, 'line_style': 2, 'tile': 1986771117, 'arc_mode': 0, 'clip_y_origin': -3660, 'dash_offset': 37616, 'line_width': 51683, 'background': 1292485193, 'clip_x_origin': -17653, 'join_style': 0, 'graphics_exposures': 0, 'font': 1609857894, 'tile_stipple_y_origin': -16927, 'stipple': 1272814461, 'fill_style': 3, 'cap_style': 1, 'subwindow_mode': 1, 'tile_stipple_x_origin': -212, 'foreground': 1790735461, 'function': 9},
            }
        self.req_bin_0 = '\x37\x00\x00\x1b' '\x52\x52\x6e\x1b' \
            '\x05\x6c\xd2\x58' '\x00\x7f\xff\xff' \
            '\x09\x00\x00\x00' '\x23\x59\x79\x38' \
            '\x6a\xbc\x74\x65' '\x4d\x09\xc2\x49' \
            '\xc9\xe3\x00\x00' '\x02\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x76\x6b\xb8\xad' '\x4b\xdd\x9b\x7d' \
            '\xff\x2c\x00\x00' '\xbd\xe1\x00\x00' \
            '\x5f\xf4\x7b\x66' '\x01\x00\x00\x00' \
            '\x00\x00\x00\x00' '\xbb\x0b\x00\x00' \
            '\xf1\xb4\x00\x00' '\x33\x60\x9c\x0e' \
            '\x92\xf0\x00\x00' '\xdb\x00\x00\x00' \
            '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.CreateGC._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CreateGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'dashes': 248, 'fill_rule': 1, 'clip_mask': 1387552951, 'plane_mask': 1431371572, 'line_style': 2, 'tile': 1552010050, 'arc_mode': 1, 'clip_y_origin': -22774, 'dash_offset': 40648, 'line_width': 41997, 'background': 1557535429, 'clip_x_origin': -8361, 'join_style': 0, 'graphics_exposures': 1, 'font': 1820226908, 'tile_stipple_y_origin': -5459, 'stipple': 967107010, 'fill_style': 2, 'cap_style': 2, 'subwindow_mode': 1, 'tile_stipple_x_origin': -12145, 'foreground': 677647350, 'function': 0},
            'gc': 417521765,
            }
        self.req_bin_0 = '\x38\x00\x00\x1a' '\x18\xe2\xe0\x65' \
            '\x00\x7f\xff\xff' '\x00\x00\x00\x00' \
            '\x55\x50\xff\x34' '\x28\x64\x13\xf6' \
            '\x5c\xd6\x1a\xc5' '\xa4\x0d\x00\x00' \
            '\x02\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x5c\x81\xcb\x42' \
            '\x39\xa4\xe1\xc2' '\xd0\x8f\x00\x00' \
            '\xea\xad\x00\x00' '\x6c\x7e\x75\x5c' \
            '\x01\x00\x00\x00' '\x01\x00\x00\x00' \
            '\xdf\x57\x00\x00' '\xa7\x0a\x00\x00' \
            '\x52\xb4\x60\xb7' '\x9e\xc8\x00\x00' \
            '\xf8\x00\x00\x00' '\x01\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.ChangeGC._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCopyGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mask': 90485554,
            'src_gc': 255344098,
            'dst_gc': 2070891280,
            }
        self.req_bin_0 = '\x39\x00\x00\x04' '\x0f\x38\x3d\xe2' \
            '\x7b\x6f\x4b\x10' '\x05\x64\xb3\x32'


    def testPackRequest0(self):
	bin = apply(request.CopyGC._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CopyGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetDashes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'dashes': [129, 203, 216, 234, 219, 227, 217, 177, 225],
            'dash_offset': 60834,
            'gc': 1793434845,
            }
        self.req_bin_0 = '\x3a\x00\x00\x06' '\x6a\xe5\xa4\xdd' \
            '\xed\xa2\x00\x09' '\x81\xcb\xd8\xea' \
            '\xdb\xe3\xd9\xb1' '\xe1\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.SetDashes._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetDashes._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetClipRectangles(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'rectangles': [{'height': 34898, 'x': -14844, 'width': 5118, 'y': -25063}, {'height': 13735, 'x': -23640, 'width': 17082, 'y': -16488}],
            'gc': 1981622127,
            'x_origin': -23730,
            'y_origin': -3988,
            'ordering': 2,
            }
        self.req_bin_0 = '\x3b\x02\x00\x07' '\x76\x1d\x27\x6f' \
            '\xa3\x4e\xf0\x6c' '\xc6\x04\x9e\x19' \
            '\x13\xfe\x88\x52' '\xa3\xa8\xbf\x98' \
            '\x42\xba\x35\xa7'

        self.req_args_1 = {
            'rectangles': [],
            'gc': 191480574,
            'x_origin': -298,
            'y_origin': -27836,
            'ordering': 0,
            }
        self.req_bin_1 = '\x3b\x00\x00\x03' '\x0b\x69\xc2\xfe' \
            '\xfe\xd6\x93\x44'


    def testPackRequest0(self):
	bin = apply(request.SetClipRectangles._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetClipRectangles._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest1(self):
	bin = apply(request.SetClipRectangles._request.to_binary, (), self.req_args_1)
	try:
	    assert bin == self.req_bin_1
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
	args, remain = request.SetClipRectangles._request.parse_binary(self.req_bin_1, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_1
	except AssertionError:
	    raise AssertionError(args)


class TestFreeGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 2138728270,
            }
        self.req_bin_0 = '\x3c\x00\x00\x02' '\x7f\x7a\x67\x4e'


    def testPackRequest0(self):
	bin = apply(request.FreeGC._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.FreeGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestClearArea(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'exposures': 0,
            'height': 26634,
            'width': 3904,
            'window': 1135114634,
            'x': -3311,
            'y': -16106,
            }
        self.req_bin_0 = '\x3d\x00\x00\x04' '\x43\xa8\x79\x8a' \
            '\xf3\x11\xc1\x16' '\x0f\x40\x68\x0a'


    def testPackRequest0(self):
	bin = apply(request.ClearArea._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ClearArea._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCopyArea(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_drawable': 505249724,
            'dst_drawable': 81122993,
            'src_y': -30707,
            'src_x': -9611,
            'gc': 393558693,
            'width': 12934,
            'height': 15260,
            'dst_x': -15969,
            'dst_y': -13283,
            }
        self.req_bin_0 = '\x3e\x00\x00\x07' '\x1e\x1d\x7f\xbc' \
            '\x04\xd5\xd6\xb1' '\x17\x75\x3a\xa5' \
            '\xda\x75\x88\x0d' '\xc1\x9f\xcc\x1d' \
            '\x32\x86\x3b\x9c'


    def testPackRequest0(self):
	bin = apply(request.CopyArea._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CopyArea._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCopyPlane(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_drawable': 420068101,
            'bit_plane': 161794758,
            'dst_drawable': 1367735048,
            'src_y': -27619,
            'src_x': -27049,
            'gc': 1700053256,
            'width': 43263,
            'height': 25272,
            'dst_x': -18193,
            'dst_y': -31452,
            }
        self.req_bin_0 = '\x3f\x00\x00\x08' '\x19\x09\xbb\x05' \
            '\x51\x85\xfb\x08' '\x65\x54\xc1\x08' \
            '\x96\x57\x94\x1d' '\xb8\xef\x85\x24' \
            '\xa8\xff\x62\xb8' '\x09\xa4\xca\xc6'


    def testPackRequest0(self):
	bin = apply(request.CopyPlane._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CopyPlane._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyPoint(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 1921455533,
            'points': [{'x': -2137, 'y': -32465}, {'x': -17011, 'y': -16542}, {'x': -15858, 'y': -13944}],
            'drawable': 653131111,
            'coord_mode': 1,
            }
        self.req_bin_0 = '\x40\x01\x00\x06' '\x26\xed\xfd\x67' \
            '\x72\x87\x15\xad' '\xf7\xa7\x81\x2f' \
            '\xbd\x8d\xbf\x62' '\xc2\x0e\xc9\x88'


    def testPackRequest0(self):
	bin = apply(request.PolyPoint._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyPoint._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyLine(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 1647920800,
            'points': [{'x': -27888, 'y': -13284}, {'x': -15812, 'y': -30440}, {'x': -2832, 'y': -16757}, {'x': -32077, 'y': -25008}, {'x': -27895, 'y': -21204}],
            'drawable': 539389233,
            'coord_mode': 1,
            }
        self.req_bin_0 = '\x41\x01\x00\x08' '\x20\x26\x6d\x31' \
            '\x62\x39\x46\xa0' '\x93\x10\xcc\x1c' \
            '\xc2\x3c\x89\x18' '\xf4\xf0\xbe\x8b' \
            '\x82\xb3\x9e\x50' '\x93\x09\xad\x2c'


    def testPackRequest0(self):
	bin = apply(request.PolyLine._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyLine._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolySegment(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'segments': [{'y1': -23343, 'y2': -2928, 'x1': -2667, 'x2': -27645}],
            'drawable': 663896944,
            'gc': 1675975833,
            }
        self.req_bin_0 = '\x42\x00\x00\x05' '\x27\x92\x43\x70' \
            '\x63\xe5\x5c\x99' '\xf5\x95\xa4\xd1' \
            '\x94\x03\xf4\x90'


    def testPackRequest0(self):
	bin = apply(request.PolySegment._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolySegment._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyRectangle(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 1813268911,
            'gc': 2137230781,
            'rectangles': [{'height': 33055, 'x': -22476, 'width': 39441, 'y': -1428}, {'height': 60975, 'x': -28929, 'width': 61738, 'y': -10493}, {'height': 55557, 'x': -9635, 'width': 61503, 'y': -6789}],
            }
        self.req_bin_0 = '\x43\x00\x00\x09' '\x6c\x14\x49\xaf' \
            '\x7f\x63\x8d\xbd' '\xa8\x34\xfa\x6c' \
            '\x9a\x11\x81\x1f' '\x8e\xff\xd7\x03' \
            '\xf1\x2a\xee\x2f' '\xda\x5d\xe5\x7b' \
            '\xf0\x3f\xd9\x05'


    def testPackRequest0(self):
	bin = apply(request.PolyRectangle._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyRectangle._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyArc(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'arcs': [{'height': 35864, 'angle1': -27767, 'x': -25716, 'angle2': -15887, 'width': 13224, 'y': -6339}, {'height': 9681, 'angle1': -25365, 'x': -11301, 'angle2': -755, 'width': 18712, 'y': -18285}, {'height': 23986, 'angle1': -2451, 'x': -19871, 'angle2': -982, 'width': 45297, 'y': -23613}],
            'drawable': 2136720622,
            'gc': 507464865,
            }
        self.req_bin_0 = '\x44\x00\x00\x0c' '\x7f\x5b\xc4\xee' \
            '\x1e\x3f\x4c\xa1' '\x9b\x8c\xe7\x3d' \
            '\x33\xa8\x8c\x18' '\x93\x89\xc1\xf1' \
            '\xd3\xdb\xb8\x93' '\x49\x18\x25\xd1' \
            '\x9c\xeb\xfd\x0d' '\xb2\x61\xa3\xc3' \
            '\xb0\xf1\x5d\xb2' '\xf6\x6d\xfc\x2a'


    def testPackRequest0(self):
	bin = apply(request.PolyArc._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyArc._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestFillPoly(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'shape': 2,
            'gc': 1286424315,
            'points': [{'x': -9202, 'y': -32639}, {'x': -31906, 'y': -4321}, {'x': -8888, 'y': -22009}],
            'drawable': 1079742746,
            'coord_mode': 1,
            }
        self.req_bin_0 = '\x45\x00\x00\x07' '\x40\x5b\x91\x1a' \
            '\x4c\xad\x46\xfb' '\x02\x01\x00\x00' \
            '\xdc\x0e\x80\x81' '\x83\x5e\xef\x1f' \
            '\xdd\x48\xaa\x07'


    def testPackRequest0(self):
	bin = apply(request.FillPoly._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.FillPoly._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyFillRectangle(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 327943084,
            'gc': 492302835,
            'rectangles': [{'height': 16613, 'x': -3755, 'width': 27808, 'y': -2254}, {'height': 17046, 'x': -27231, 'width': 42106, 'y': -4518}],
            }
        self.req_bin_0 = '\x46\x00\x00\x07' '\x13\x8c\x03\xac' \
            '\x1d\x57\xf1\xf3' '\xf1\x55\xf7\x32' \
            '\x6c\xa0\x40\xe5' '\x95\xa1\xee\x5a' \
            '\xa4\x7a\x42\x96'


    def testPackRequest0(self):
	bin = apply(request.PolyFillRectangle._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyFillRectangle._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyFillArc(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'arcs': [{'height': 57042, 'angle1': -22158, 'x': -29483, 'angle2': -12271, 'width': 62469, 'y': -7823}],
            'drawable': 1614203180,
            'gc': 1530067949,
            }
        self.req_bin_0 = '\x47\x00\x00\x06' '\x60\x36\xc9\x2c' \
            '\x5b\x32\xfb\xed' '\x8c\xd5\xe1\x71' \
            '\xf4\x05\xde\xd2' '\xa9\x72\xd0\x11'


    def testPackRequest0(self):
	bin = apply(request.PolyFillArc._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyFillArc._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPutImage(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 35862,
            'data': 'bit map data',
            'drawable': 523720567,
            'left_pad': 157,
            'format': 1,
            'dst_x': -19727,
            'gc': 1395936690,
            'depth': 158,
            'width': 25645,
            'dst_y': -8819,
            }
        self.req_bin_0 = '\x48\x01\x00\x09' '\x1f\x37\x57\x77' \
            '\x53\x34\x4d\xb2' '\x64\x2d\x8c\x16' \
            '\xb2\xf1\xdd\x8d' '\x9d\x9e\x00\x00' \
            '\x62\x69\x74\x20' '\x6d\x61\x70\x20' \
            '\x64\x61\x74\x61'


    def testPackRequest0(self):
	bin = apply(request.PutImage._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PutImage._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetImage(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 52936,
            'plane_mask': 26203517,
            'drawable': 1218479570,
            'x': -9746,
            'y': -31384,
            'format': 2,
            'width': 12151,
            }
        self.req_bin_0 = '\x49\x02\x00\x05' '\x48\xa0\x85\xd2' \
            '\xd9\xee\x85\x68' '\x2f\x77\xce\xc8' \
            '\x01\x8f\xd5\x7d'

        self.reply_args_0 = {
            'sequence_number': 50329,
            'data': 'this is real ly imag e b-map',
            'visual': 236013784,
            'depth': 244,
            }
        self.reply_bin_0 = '\x01\xf4\xc4\x99' '\x00\x00\x00\x07' \
            '\x0e\x11\x48\xd8' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x74\x68\x69\x73' '\x20\x69\x73\x20' \
            '\x72\x65\x61\x6c' '\x20\x6c\x79\x20' \
            '\x69\x6d\x61\x67' '\x20\x65\x20\x62' \
            '\x2d\x6d\x61\x70'


    def testPackRequest0(self):
	bin = apply(request.GetImage._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetImage._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetImage._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetImage._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyText8(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 1432094356,
            'x': -23281,
            'drawable': 1715483382,
            'items': [{'delta': 2, 'string': 'zoo'}, 16909060, {'delta': 0, 'string': 'ie'}],
            'y': -13421,
            }
        self.req_bin_0 = '\x4a\x00\x00\x08' '\x66\x40\x32\xf6' \
            '\x55\x5c\x06\x94' '\xa5\x0f\xcb\x93' \
            '\x03\x02\x7a\x6f' '\x6f\xff\x01\x02' \
            '\x03\x04\x02\x00' '\x69\x65\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.PolyText8._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyText8._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestPolyText16(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 1006078466,
            'x': -7852,
            'drawable': 1296382109,
            'items': [{'delta': 2, 'string': (4131, 18)}, 16909060],
            'y': -32557,
            }
        self.req_bin_0 = '\x4b\x00\x00\x07' '\x4d\x45\x38\x9d' \
            '\x3b\xf7\x8a\x02' '\xe1\x54\x80\xd3' \
            '\x02\x02\x10\x23' '\x00\x12\xff\x01' \
            '\x02\x03\x04\x00'


    def testPackRequest0(self):
	bin = apply(request.PolyText16._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.PolyText16._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestImageText8(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'string': 'showme',
            'gc': 1921198827,
            'drawable': 1995840673,
            'x': -6872,
            'y': -19083,
            }
        self.req_bin_0 = '\x4c\x06\x00\x06' '\x76\xf6\x1c\xa1' \
            '\x72\x83\x2a\xeb' '\xe5\x28\xb5\x75' \
            '\x73\x68\x6f\x77' '\x6d\x65\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.ImageText8._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ImageText8._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestImageText16(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'string': (115, 104, 111, 119, 109, 111, 114, 101),
            'gc': 1262368880,
            'drawable': 978048831,
            'x': -31198,
            'y': -25974,
            }
        self.req_bin_0 = '\x4d\x08\x00\x08' '\x3a\x4b\xd7\x3f' \
            '\x4b\x3e\x38\x70' '\x86\x22\x9a\x8a' \
            '\x00\x73\x00\x68' '\x00\x6f\x00\x77' \
            '\x00\x6d\x00\x6f' '\x00\x72\x00\x65'


    def testPackRequest0(self):
	bin = apply(request.ImageText16._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ImageText16._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCreateColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mid': 1450570079,
            'alloc': 0,
            'visual': 1606574442,
            'window': 1005808268,
            }
        self.req_bin_0 = '\x4e\x00\x00\x04' '\x56\x75\xf1\x5f' \
            '\x3b\xf3\x6a\x8c' '\x5f\xc2\x61\x6a'


    def testPackRequest0(self):
	bin = apply(request.CreateColormap._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CreateColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestFreeColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 766091652,
            }
        self.req_bin_0 = '\x4f\x00\x00\x02' '\x2d\xa9\xa1\x84'


    def testPackRequest0(self):
	bin = apply(request.FreeColormap._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.FreeColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCopyColormapAndFree(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_cmap': 324810306,
            'mid': 1306938061,
            }
        self.req_bin_0 = '\x50\x00\x00\x03' '\x4d\xe6\x4a\xcd' \
            '\x13\x5c\x36\x42'


    def testPackRequest0(self):
	bin = apply(request.CopyColormapAndFree._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CopyColormapAndFree._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestInstallColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 198601885,
            }
        self.req_bin_0 = '\x51\x00\x00\x02' '\x0b\xd6\x6c\x9d'


    def testPackRequest0(self):
	bin = apply(request.InstallColormap._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.InstallColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestUninstallColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1136427824,
            }
        self.req_bin_0 = '\x52\x00\x00\x02' '\x43\xbc\x83\x30'


    def testPackRequest0(self):
	bin = apply(request.UninstallColormap._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.UninstallColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestListInstalledColormaps(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1557085787,
            }
        self.req_bin_0 = '\x53\x00\x00\x02' '\x5c\xcf\x3e\x5b'

        self.reply_args_0 = {
            'cmaps': [1805181410, 1107704601],
            'sequence_number': 36831,
            }
        self.reply_bin_0 = '\x01\x00\x8f\xdf' '\x00\x00\x00\x02' \
            '\x00\x02\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x6b\x98\xe1\xe2' '\x42\x06\x3b\x19'


    def testPackRequest0(self):
	bin = apply(request.ListInstalledColormaps._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ListInstalledColormaps._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.ListInstalledColormaps._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.ListInstalledColormaps._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestAllocColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'red': 9657,
            'green': 10463,
            'cmap': 408147072,
            'blue': 30726,
            }
        self.req_bin_0 = '\x54\x00\x00\x04' '\x18\x53\xd4\x80' \
            '\x25\xb9\x28\xdf' '\x78\x06\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 52356,
            'red': 39559,
            'green': 40934,
            'pixel': 2067348738,
            'blue': 4648,
            }
        self.reply_bin_0 = '\x01\x00\xcc\x84' '\x00\x00\x00\x00' \
            '\x9a\x87\x9f\xe6' '\x12\x28\x00\x00' \
            '\x7b\x39\x3d\x02' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.AllocColor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.AllocColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.AllocColor._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.AllocColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestAllocNamedColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1848064244,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x55\x00\x00\x05' '\x6e\x27\x38\xf4' \
            '\x00\x07\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 21996,
            'pixel': 685646700,
            'screen_green': 50142,
            'screen_red': 7654,
            'exact_green': 47364,
            'exact_blue': 13721,
            'screen_blue': 37864,
            'exact_red': 53336,
            }
        self.reply_bin_0 = '\x01\x00\x55\xec' '\x00\x00\x00\x00' \
            '\x28\xde\x23\x6c' '\xd0\x58\xb9\x04' \
            '\x35\x99\x1d\xe6' '\xc3\xde\x93\xe8' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.AllocNamedColor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.AllocNamedColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.AllocNamedColor._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.AllocNamedColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestAllocColorCells(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'planes': 14211,
            'colors': 39126,
            'cmap': 728763056,
            'contiguous': 1,
            }
        self.req_bin_0 = '\x56\x01\x00\x03' '\x2b\x70\x0a\xb0' \
            '\x98\xd6\x37\x83'

        self.reply_args_0 = {
            'masks': [673189359, 613687858, 1253544771],
            'pixels': [1055448762, 576649021, 957271074, 972492501, 478690059, 805915700, 1892175399, 1127310308, 51194806, 1175782781, 1279277951, 1620188879, 1498522893, 383804958, 1328220753, 1788528957, 1094969478],
            'sequence_number': 57887,
            }
        self.reply_bin_0 = '\x01\x00\xe2\x1f' '\x00\x00\x00\x14' \
            '\x00\x11\x00\x03' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x3e\xe8\xde\xba' '\x22\x5e\xf7\x3d' \
            '\x39\x0e\xcc\x22' '\x39\xf7\x0e\xd5' \
            '\x1c\x88\x3b\x0b' '\x30\x09\x4c\x34' \
            '\x70\xc8\x4e\x27' '\x43\x31\x63\xe4' \
            '\x03\x0d\x2b\xb6' '\x46\x15\x05\x7d' \
            '\x4c\x40\x3b\x7f' '\x60\x92\x1e\xcf' \
            '\x59\x51\xa5\x0d' '\x16\xe0\x66\x1e' \
            '\x4f\x2b\x0a\x51' '\x6a\x9a\xc9\x3d' \
            '\x41\x43\xe8\x86' '\x28\x20\x0d\xef' \
            '\x24\x94\x22\x32' '\x4a\xb7\x93\x43'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 8198,
            }
        self.reply_bin_1 = '\x01\x00\x20\x06' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.AllocColorCells._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.AllocColorCells._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.AllocColorCells._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.AllocColorCells._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply1(self):
	bin = apply(request.AllocColorCells._reply.to_binary, (), self.reply_args_1)
	try:
	    assert bin == self.reply_bin_1
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply1(self):
	args, remain = request.AllocColorCells._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_1
	except AssertionError:
	    raise AssertionError(args)


class TestAllocColorPlanes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'red': 15067,
            'colors': 29805,
            'green': 9319,
            'cmap': 759681180,
            'contiguous': 0,
            'blue': 48360,
            }
        self.req_bin_0 = '\x57\x00\x00\x04' '\x2d\x47\xd0\x9c' \
            '\x74\x6d\x3a\xdb' '\x24\x67\xbc\xe8'

        self.reply_args_0 = {
            'green_mask': 1050073473,
            'sequence_number': 4658,
            'pixels': [1797267037, 949126831, 65155923, 889040943],
            'blue_mask': 1049586870,
            'red_mask': 373382478,
            }
        self.reply_bin_0 = '\x01\x00\x12\x32' '\x00\x00\x00\x04' \
            '\x00\x04\x00\x00' '\x16\x41\x5d\x4e' \
            '\x3e\x96\xd9\x81' '\x3e\x8f\x6c\xb6' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x6b\x20\x1e\x5d' '\x38\x92\x86\xaf' \
            '\x03\xe2\x33\x53' '\x34\xfd\xb0\x2f'


    def testPackRequest0(self):
	bin = apply(request.AllocColorPlanes._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.AllocColorPlanes._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.AllocColorPlanes._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.AllocColorPlanes._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestFreeColors(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 821125207,
            'pixels': [1360557811, 1047698027, 1254627248, 1864953432, 227656240, 748997388, 1244873112, 1786862932, 1070459421, 413938130, 908103552, 438979061, 1836746946, 756977662, 2062476198, 1535191520, 1160725678],
            'plane_mask': 1249725572,
            }
        self.req_bin_0 = '\x58\x00\x00\x14' '\x30\xf1\x60\x57' \
            '\x4a\x7d\x4c\x84' '\x51\x18\x76\xf3' \
            '\x3e\x72\x9a\x6b' '\x4a\xc8\x17\xb0' \
            '\x6f\x28\xee\x58' '\x0d\x91\xc2\x30' \
            '\x2c\xa4\xcb\x0c' '\x4a\x33\x41\x98' \
            '\x6a\x81\x5d\x54' '\x3f\xcd\xea\x1d' \
            '\x18\xac\x31\xd2' '\x36\x20\x8f\x80' \
            '\x1a\x2a\x49\xf5' '\x6d\x7a\x88\xc2' \
            '\x2d\x1e\x8f\xfe' '\x7a\xee\xe3\xa6' \
            '\x5b\x81\x29\xe0' '\x45\x2f\x44\xae'


    def testPackRequest0(self):
	bin = apply(request.FreeColors._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.FreeColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestStoreColors(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1539899115,
            'items': [{'red': 10509, 'pixel': 1785803906, 'green': 50424, 'flags': 203, 'blue': 19210}, {'red': 45218, 'pixel': 11405404, 'green': 28678, 'flags': 158, 'blue': 41097}, {'red': 61218, 'pixel': 420472179, 'green': 26907, 'flags': 158, 'blue': 60456}, {'red': 11565, 'pixel': 589230162, 'green': 48299, 'flags': 155, 'blue': 31325}],
            }
        self.req_bin_0 = '\x59\x00\x00\x0e' '\x5b\xc8\xfe\xeb' \
            '\x6a\x71\x34\x82' '\x29\x0d\xc4\xf8' \
            '\x4b\x0a\xcb\x00' '\x00\xae\x08\x5c' \
            '\xb0\xa2\x70\x06' '\xa0\x89\x9e\x00' \
            '\x19\x0f\xe5\x73' '\xef\x22\x69\x1b' \
            '\xec\x28\x9e\x00' '\x23\x1e\xf0\x52' \
            '\x2d\x2d\xbc\xab' '\x7a\x5d\x9b\x00'


    def testPackRequest0(self):
	bin = apply(request.StoreColors._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.StoreColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestStoreNamedColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'name': 'blue',
            'flags': 188,
            'cmap': 1873267112,
            'pixel': 1695496397,
            }
        self.req_bin_0 = '\x5a\xbc\x00\x05' '\x6f\xa7\xc9\xa8' \
            '\x65\x0f\x38\xcd' '\x00\x04\x00\x00' \
            '\x62\x6c\x75\x65'


    def testPackRequest0(self):
	bin = apply(request.StoreNamedColor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.StoreNamedColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryColors(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1831947624,
            'pixels': [138560686, 90940250, 1773637147, 68450239, 632118774, 1583812645, 1410435764, 401211928],
            }
        self.req_bin_0 = '\x5b\x00\x00\x0a' '\x6d\x31\x4d\x68' \
            '\x08\x42\x44\xae' '\x05\x6b\xa3\x5a' \
            '\x69\xb7\x8e\x1b' '\x04\x14\x77\xbf' \
            '\x25\xad\x5d\xf6' '\x5e\x67\x10\x25' \
            '\x54\x11\x8a\xb4' '\x17\xea\x02\x18'

        self.reply_args_0 = {
            'colors': [{'red': 30388, 'blue': 46627, 'green': 31051}, {'red': 28005, 'blue': 52416, 'green': 15684}, {'red': 19421, 'blue': 54971, 'green': 7252}, {'red': 54355, 'blue': 41386, 'green': 32974}, {'red': 2132, 'blue': 23156, 'green': 45302}],
            'sequence_number': 21962,
            }
        self.reply_bin_0 = '\x01\x00\x55\xca' '\x00\x00\x00\x0a' \
            '\x00\x05\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x76\xb4\x79\x4b' '\xb6\x23\x00\x00' \
            '\x6d\x65\x3d\x44' '\xcc\xc0\x00\x00' \
            '\x4b\xdd\x1c\x54' '\xd6\xbb\x00\x00' \
            '\xd4\x53\x80\xce' '\xa1\xaa\x00\x00' \
            '\x08\x54\xb0\xf6' '\x5a\x74\x00\x00'

        self.req_args_1 = {
            'cmap': 783333245,
            'pixels': [],
            }
        self.req_bin_1 = '\x5b\x00\x00\x02' '\x2e\xb0\xb7\x7d'


    def testPackRequest0(self):
	bin = apply(request.QueryColors._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackRequest1(self):
	bin = apply(request.QueryColors._request.to_binary, (), self.req_args_1)
	try:
	    assert bin == self.req_bin_1
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
	args, remain = request.QueryColors._request.parse_binary(self.req_bin_1, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_1
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryColors._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryColors._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestLookupColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1064138527,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x5c\x00\x00\x05' '\x3f\x6d\x77\x1f' \
            '\x00\x07\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 35560,
            'screen_green': 22861,
            'screen_red': 44460,
            'exact_green': 34018,
            'exact_blue': 21897,
            'screen_blue': 24504,
            'exact_red': 9744,
            }
        self.reply_bin_0 = '\x01\x00\x8a\xe8' '\x00\x00\x00\x00' \
            '\x26\x10\x84\xe2' '\x55\x89\xad\xac' \
            '\x59\x4d\x5f\xb8' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.LookupColor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.LookupColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.LookupColor._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.LookupColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCreateCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'x': 58979,
            'fore_red': 24347,
            'back_green': 21856,
            'mask': 775908779,
            'back_blue': 60412,
            'y': 27460,
            'cid': 1896951376,
            'fore_blue': 4834,
            'fore_green': 23033,
            'back_red': 24893,
            'source': 1081255796,
            }
        self.req_bin_0 = '\x5d\x00\x00\x08' '\x71\x11\x2e\x50' \
            '\x40\x72\xa7\x74' '\x2e\x3f\x6d\xab' \
            '\x5f\x1b\x59\xf9' '\x12\xe2\x61\x3d' \
            '\x55\x60\xeb\xfc' '\xe6\x63\x6b\x44'


    def testPackRequest0(self):
	bin = apply(request.CreateCursor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CreateCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestCreateGlyphCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'fore_red': 64621,
            'source_char': 24645,
            'mask': 568167754,
            'back_blue': 8168,
            'cid': 77572484,
            'mask_char': 49589,
            'fore_blue': 5853,
            'fore_green': 5595,
            'back_red': 24854,
            'source': 894416391,
            'back_green': 59443,
            }
        self.req_bin_0 = '\x5e\x00\x00\x08' '\x04\x9f\xa9\x84' \
            '\x35\x4f\xb6\x07' '\x21\xdd\x8d\x4a' \
            '\x60\x45\xc1\xb5' '\xfc\x6d\x15\xdb' \
            '\x16\xdd\x61\x16' '\xe8\x33\x1f\xe8'


    def testPackRequest0(self):
	bin = apply(request.CreateGlyphCursor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.CreateGlyphCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestFreeCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cursor': 2026541541,
            }
        self.req_bin_0 = '\x5f\x00\x00\x02' '\x78\xca\x91\xe5'


    def testPackRequest0(self):
	bin = apply(request.FreeCursor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.FreeCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestRecolorCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'fore_red': 49660,
            'fore_green': 53605,
            'back_blue': 6796,
            'back_green': 20445,
            'fore_blue': 9271,
            'back_red': 17292,
            'cursor': 2079143221,
            }
        self.req_bin_0 = '\x60\x00\x00\x05' '\x7b\xed\x35\x35' \
            '\xc1\xfc\xd1\x65' '\x24\x37\x43\x8c' \
            '\x4f\xdd\x1a\x8c'


    def testPackRequest0(self):
	bin = apply(request.RecolorCursor._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.RecolorCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryBestSize(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 48910,
            'drawable': 273543467,
            'item_class': 2,
            'width': 61806,
            }
        self.req_bin_0 = '\x61\x02\x00\x03' '\x10\x4d\xf1\x2b' \
            '\xf1\x6e\xbf\x0e'

        self.reply_args_0 = {
            'height': 52435,
            'sequence_number': 27523,
            'width': 33996,
            }
        self.reply_bin_0 = '\x01\x00\x6b\x83' '\x00\x00\x00\x00' \
            '\x84\xcc\xcc\xd3' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.QueryBestSize._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryBestSize._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryBestSize._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryBestSize._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestQueryExtension(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'name': 'XTRA',
            }
        self.req_bin_0 = '\x62\x00\x00\x03' '\x00\x04\x00\x00' \
            '\x58\x54\x52\x41'

        self.reply_args_0 = {
            'sequence_number': 61699,
            'major_opcode': 145,
            'first_error': 221,
            'present': 1,
            'first_event': 136,
            }
        self.reply_bin_0 = '\x01\x00\xf1\x03' '\x00\x00\x00\x00' \
            '\x01\x91\x88\xdd' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.QueryExtension._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.QueryExtension._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.QueryExtension._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.QueryExtension._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestListExtensions(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x63\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 22455,
            'names': ['XTRA', 'XTRA-II'],
            }
        self.reply_bin_0 = '\x01\x02\x57\xb7' '\x00\x00\x00\x04' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x04\x58\x54\x52' '\x41\x07\x58\x54' \
            '\x52\x41\x2d\x49' '\x49\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.ListExtensions._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ListExtensions._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.ListExtensions._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.ListExtensions._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeKeyboardMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'keysyms': [[871050509, 46548, 351428718], [1678689598, 2088016698, 1574254797], [605897756, 59276201, 1938792631], [1550782822, 1049972288, 1666021165], [977908414, 1154765501, 787957326], [403606238, 1743574428, 1073307771], [215115121, 347950970, 694975710], [1266266951, 1236946779, 953826099], [469906703, 1822999228, 1297605989], [673576745, 287974090, 1245537298], [1673366984, 872060933, 215673318], [476025559, 128754980, 658291674], [40202845, 1432855550, 122370483], [392867898, 1421578349, 1499688650], [1593982516, 1904897842, 1172966297], [2090372535, 1186827688, 561721927], [1158349513, 1574654642, 611004388], [1090713564, 1431598823, 1169933730], [429965382, 1754948580, 1534203752], [510380465, 857291909, 954644015]],
            'first_keycode': 177,
            }
        self.req_bin_0 = '\x64\x14\x00\x3e' '\xb1\x03\x00\x00' \
            '\x33\xeb\x2d\x0d' '\x00\x00\xb5\xd4' \
            '\x14\xf2\x60\x6e' '\x64\x0e\xc5\x3e' \
            '\x7c\x74\x9b\x3a' '\x5d\xd5\x38\xcd' \
            '\x24\x1d\x44\x1c' '\x03\x88\x7b\xa9' \
            '\x73\x8f\xa0\xb7' '\x5c\x6f\x11\x66' \
            '\x3e\x95\x4e\x40' '\x63\x4d\x77\x2d' \
            '\x3a\x49\xb2\xbe' '\x44\xd4\x52\xbd' \
            '\x2e\xf7\x46\x4e' '\x18\x0e\x8a\xde' \
            '\x67\xec\xd5\x9c' '\x3f\xf9\x60\x7b' \
            '\x0c\xd2\x65\x71' '\x14\xbd\x4f\x7a' \
            '\x29\x6c\x7c\xde' '\x4b\x79\xb3\x47' \
            '\x49\xba\x4f\x5b' '\x38\xda\x3b\x33' \
            '\x1c\x02\x35\x0f' '\x6c\xa8\xc2\xbc' \
            '\x4d\x57\xe5\x65' '\x28\x25\xf7\x29' \
            '\x11\x2a\x22\xca' '\x4a\x3d\x64\x12' \
            '\x63\xbd\x8d\xc8' '\x33\xfa\x98\x05' \
            '\x0c\xda\xe9\xe6' '\x1c\x5f\x92\xd7' \
            '\x07\xac\xa5\x24' '\x27\x3c\xbb\xda' \
            '\x02\x65\x72\x5d' '\x55\x67\xa3\xfe' \
            '\x07\x4b\x39\xb3' '\x17\x6a\xb0\x3a' \
            '\x54\xbb\x90\x6d' '\x59\x63\x6e\xca' \
            '\x5f\x02\x3e\x34' '\x71\x8a\x6f\x32' \
            '\x45\xea\x0b\x99' '\x7c\x98\x8d\xb7' \
            '\x46\xbd\x8d\xa8' '\x21\x7b\x32\x47' \
            '\x45\x0b\x02\xc9' '\x5d\xdb\x52\xb2' \
            '\x24\x6b\x2f\xe4' '\x41\x02\xf7\xdc' \
            '\x55\x54\x76\xe7' '\x45\xbb\xc5\xa2' \
            '\x19\xa0\xc0\x46' '\x68\x9a\x63\xe4' \
            '\x5b\x72\x17\x68' '\x1e\x6b\xc9\xb1' \
            '\x33\x19\x3c\x85' '\x38\xe6\xb6\x2f'


    def testPackRequest0(self):
	bin = apply(request.ChangeKeyboardMapping._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeKeyboardMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetKeyboardMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'count': 225,
            'first_keycode': 225,
            }
        self.req_bin_0 = '\x65\x00\x00\x02' '\xe1\xe1\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[982244672, 1365661998, 1341204086], [1529056479, 1786083677, 1563398685], [1569695004, 1080191687, 692503403], [386928496, 1976629508, 1449421104], [1579986411, 936919103, 1822205117], [634040790, 1956790648, 1132386658], [306476874, 765942818, 35736709], [1132170362, 1117019525, 1678345995], [1549758437, 972517776, 1480029581], [1809975818, 1171491588, 1270076985], [1095917295, 2109792933, 506423545], [646458957, 927851321, 537630814], [1004484279, 1935660577, 1681801082], [826692607, 144952184, 1908052863], [1736007245, 2051699875, 1538774874], [894319506, 1865649148, 2055778681], [428070598, 2071498428, 1575090907], [1435450437, 301776739, 832276301], [1827733048, 1129611385, 61731195], [454306896, 831151286, 2094485253]],
            'sequence_number': 64956,
            }
        self.reply_bin_0 = '\x01\x03\xfd\xbc' '\x00\x00\x00\x3c' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x3a\x8b\xdd\x40' '\x51\x66\x59\x2e' \
            '\x4f\xf1\x26\x76' '\x5b\x23\x8c\xdf' \
            '\x6a\x75\x79\x5d' '\x5d\x2f\x92\x1d' \
            '\x5d\x8f\xa5\x1c' '\x40\x62\x6a\xc7' \
            '\x29\x46\xc3\x6b' '\x17\x10\x0f\x70' \
            '\x75\xd0\xf9\x04' '\x56\x64\x69\x30' \
            '\x5e\x2c\xad\xeb' '\x37\xd8\x40\x3f' \
            '\x6c\x9c\xa4\xbd' '\x25\xca\xb1\xd6' \
            '\x74\xa2\x41\x78' '\x43\x7e\xd9\x62' \
            '\x12\x44\x77\x4a' '\x2d\xa7\x5c\x22' \
            '\x02\x21\x4c\x85' '\x43\x7b\x8c\x7a' \
            '\x42\x94\x5d\x85' '\x64\x09\x87\x0b' \
            '\x5c\x5f\x6f\xe5' '\x39\xf7\x71\x90' \
            '\x58\x37\x75\x8d' '\x6b\xe2\x0a\x0a' \
            '\x45\xd3\x8b\x04' '\x4b\xb3\xd6\x39' \
            '\x41\x52\x5e\xef' '\x7d\xc0\xe2\xa5' \
            '\x1e\x2f\x68\xf9' '\x26\x88\x2e\x4d' \
            '\x37\x4d\xe3\x39' '\x20\x0b\x98\x5e' \
            '\x3b\xdf\x36\xb7' '\x73\x5f\xd6\x21' \
            '\x64\x3e\x3f\x7a' '\x31\x46\x53\xff' \
            '\x08\xa3\xcb\x78' '\x71\xba\x93\x7f' \
            '\x67\x79\x5e\x4d' '\x7a\x4a\x74\xa3' \
            '\x5b\xb7\xd7\x5a' '\x35\x4e\x3b\x92' \
            '\x6f\x33\x8b\xfc' '\x7a\x88\xb1\x79' \
            '\x19\x83\xd6\xc6' '\x7b\x78\x8e\xbc' \
            '\x5d\xe1\xfa\xdb' '\x55\x8f\x3c\x45' \
            '\x11\xfc\xbf\x63' '\x31\x9b\x87\x4d' \
            '\x6c\xf0\xfe\x38' '\x43\x54\x80\x79' \
            '\x03\xad\xf1\x7b' '\x1b\x14\x2c\x50' \
            '\x31\x8a\x5c\xb6' '\x7c\xd7\x4f\x05'


    def testPackRequest0(self):
	bin = apply(request.GetKeyboardMapping._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetKeyboardMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetKeyboardMapping._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetKeyboardMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeKeyboardControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'key_click_percent': -34, 'bell_percent': -79, 'led_mode': 0, 'bell_pitch': -21776, 'auto_repeat_mode': 0, 'bell_duration': -31164, 'key': 187, 'led': 251},
            }
        self.req_bin_0 = '\x66\x00\x00\x0a' '\x00\x00\x00\xff' \
            '\xde\x00\x00\x00' '\xb1\x00\x00\x00' \
            '\xaa\xf0\x00\x00' '\x86\x44\x00\x00' \
            '\xfb\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xbb\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.ChangeKeyboardControl._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeKeyboardControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetKeyboardControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x67\x00\x00\x01'

        self.reply_args_0 = {
            'key_click_percent': 231,
            'sequence_number': 26495,
            'bell_percent': 220,
            'bell_pitch': 45067,
            'auto_repeats': [2109016337, 1109211173, 1978037988, 1722547404, 1586747901, 149637172, 1889158819, 758625671],
            'global_auto_repeat': 1,
            'led_mask': 1291522043,
            'bell_duration': 51914,
            }
        self.reply_bin_0 = '\x01\x01\x67\x7f' '\x00\x00\x00\x05' \
            '\x4c\xfb\x0f\xfb' '\xe7\xdc\xb0\x0b' \
            '\xca\xca\x00\x00' '\x7d\xb5\x09\x11' \
            '\x42\x1d\x38\x25' '\x75\xe6\x76\xe4' \
            '\x66\xab\xfc\xcc' '\x5e\x93\xd9\xfd' \
            '\x08\xeb\x48\x34' '\x70\x9a\x46\xa3' \
            '\x2d\x37\xb5\x87'


    def testPackRequest0(self):
	bin = apply(request.GetKeyboardControl._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetKeyboardControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetKeyboardControl._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetKeyboardControl._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestBell(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'percent': -6,
            }
        self.req_bin_0 = '\x68\xfa\x00\x01'


    def testPackRequest0(self):
	bin = apply(request.Bell._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.Bell._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangePointerControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'accel_denum': -17334,
            'accel_num': -30135,
            'do_accel': 1,
            'do_thresh': 1,
            'threshold': -353,
            }
        self.req_bin_0 = '\x69\x00\x00\x03' '\x8a\x49\xbc\x4a' \
            '\xfe\x9f\x01\x01'


    def testPackRequest0(self):
	bin = apply(request.ChangePointerControl._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangePointerControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetPointerControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x6a\x00\x00\x01'

        self.reply_args_0 = {
            'accel_denom': 42465,
            'sequence_number': 38488,
            'threshold': 41143,
            'accel_num': 51665,
            }
        self.reply_bin_0 = '\x01\x00\x96\x58' '\x00\x00\x00\x00' \
            '\xc9\xd1\xa5\xe1' '\xa0\xb7\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetPointerControl._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetPointerControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetPointerControl._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetPointerControl._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetScreenSaver(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'allow_exposures': 0,
            'timeout': -8157,
            'interval': -1202,
            'prefer_blank': 2,
            }
        self.req_bin_0 = '\x6b\x00\x00\x03' '\xe0\x23\xfb\x4e' \
            '\x02\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.SetScreenSaver._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetScreenSaver(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x6c\x00\x00\x01'

        self.reply_args_0 = {
            'allow_exposures': 1,
            'timeout': 10937,
            'sequence_number': 24710,
            'prefer_blanking': 1,
            'interval': 20258,
            }
        self.reply_bin_0 = '\x01\x00\x60\x86' '\x00\x00\x00\x00' \
            '\x2a\xb9\x4f\x22' '\x01\x01\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetScreenSaver._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetScreenSaver._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetScreenSaver._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestChangeHosts(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'host': [151, 227, 244, 242],
            'mode': 0,
            'host_family': 1,
            }
        self.req_bin_0 = '\x6d\x00\x00\x03' '\x01\x00\x00\x04' \
            '\x97\xe3\xf4\xf2'


    def testPackRequest0(self):
	bin = apply(request.ChangeHosts._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ChangeHosts._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestListHosts(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x6e\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 65441,
            'mode': 0,
            'hosts': [{'family': 0, 'name': [34, 23, 178, 12]}, {'family': 0, 'name': [130, 236, 254, 15]}],
            }
        self.reply_bin_0 = '\x01\x00\xff\xa1' '\x00\x00\x00\x04' \
            '\x00\x02\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x04' '\x22\x17\xb2\x0c' \
            '\x00\x00\x00\x04' '\x82\xec\xfe\x0f'


    def testPackRequest0(self):
	bin = apply(request.ListHosts._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ListHosts._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.ListHosts._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.ListHosts._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetAccessControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 0,
            }
        self.req_bin_0 = '\x6f\x00\x00\x01'


    def testPackRequest0(self):
	bin = apply(request.SetAccessControl._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetAccessControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetCloseDownMode(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 1,
            }
        self.req_bin_0 = '\x70\x01\x00\x01'


    def testPackRequest0(self):
	bin = apply(request.SetCloseDownMode._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetCloseDownMode._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestKillClient(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'resource': 242928655,
            }
        self.req_bin_0 = '\x71\x00\x00\x02' '\x0e\x7a\xcc\x0f'


    def testPackRequest0(self):
	bin = apply(request.KillClient._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.KillClient._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestRotateProperties(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'delta': -5085,
            'window': 1006448130,
            'properties': [895980169, 689578094, 352214452, 1512686315, 945965582, 1292261388, 97817273, 362335406, 424856644, 1127751013, 953906105, 1927097915],
            }
        self.req_bin_0 = '\x72\x00\x00\x0f' '\x3b\xfd\x2e\x02' \
            '\x00\x0c\xec\x23' '\x35\x67\x92\x89' \
            '\x29\x1a\x20\x6e' '\x14\xfe\x5d\xb4' \
            '\x5a\x29\xc2\xeb' '\x38\x62\x4a\x0e' \
            '\x4d\x06\x58\x0c' '\x05\xd4\x92\xb9' \
            '\x15\x98\xcc\xae' '\x19\x52\xcc\x44' \
            '\x43\x38\x1d\x65' '\x38\xdb\x73\xb9' \
            '\x72\xdd\x2e\x3b'


    def testPackRequest0(self):
	bin = apply(request.RotateProperties._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.RotateProperties._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestForceScreenSaver(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 1,
            }
        self.req_bin_0 = '\x73\x01\x00\x01'


    def testPackRequest0(self):
	bin = apply(request.ForceScreenSaver._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.ForceScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetPointerMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'map': [170, 192, 148, 216, 208],
            }
        self.req_bin_0 = '\x74\x05\x00\x03' '\xaa\xc0\x94\xd8' \
            '\xd0\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 6496,
            'status': 240,
            }
        self.reply_bin_0 = '\x01\xf0\x19\x60' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.SetPointerMapping._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetPointerMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.SetPointerMapping._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.SetPointerMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetPointerMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x75\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 20034,
            'map': [138, 185, 172, 220, 148],
            }
        self.reply_bin_0 = '\x01\x05\x4e\x42' '\x00\x00\x00\x02' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x8a\xb9\xac\xdc' '\x94\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.GetPointerMapping._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetPointerMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetPointerMapping._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetPointerMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestSetModifierMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'keycodes': [[221, 165], [156, 197], [97, 20], [71, 23], [166, 113], [75, 122], [86, 90], [110, 203]],
            }
        self.req_bin_0 = '\x76\x02\x00\x05' '\xdd\xa5\x9c\xc5' \
            '\x61\x14\x47\x17' '\xa6\x71\x4b\x7a' \
            '\x56\x5a\x6e\xcb'

        self.reply_args_0 = {
            'sequence_number': 37737,
            'status': 161,
            }
        self.reply_bin_0 = '\x01\xa1\x93\x69' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'


    def testPackRequest0(self):
	bin = apply(request.SetModifierMapping._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.SetModifierMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.SetModifierMapping._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.SetModifierMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestGetModifierMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x77\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 3636,
            'keycodes': [[49, 167], [203, 89], [42, 23], [191, 134], [189, 37], [50, 244], [92, 12], [71, 131]],
            }
        self.reply_bin_0 = '\x01\x02\x0e\x34' '\x00\x00\x00\x04' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x31\xa7\xcb\x59' '\x2a\x17\xbf\x86' \
            '\xbd\x25\x32\xf4' '\x5c\x0c\x47\x83'


    def testPackRequest0(self):
	bin = apply(request.GetModifierMapping._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.GetModifierMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)

    def testPackReply0(self):
	bin = apply(request.GetModifierMapping._reply.to_binary, (), self.reply_args_0)
	try:
	    assert bin == self.reply_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
	args, remain = request.GetModifierMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_0
	except AssertionError:
	    raise AssertionError(args)


class TestNoOperation(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = '\x7f\x00\x00\x01'


    def testPackRequest0(self):
	bin = apply(request.NoOperation._request.to_binary, (), self.req_args_0)
	try:
	    assert bin == self.req_bin_0
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
	args, remain = request.NoOperation._request.parse_binary(self.req_bin_0, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_0
	except AssertionError:
	    raise AssertionError(args)


if __name__ == "__main__":
    check_endian()
    unittest.main()
