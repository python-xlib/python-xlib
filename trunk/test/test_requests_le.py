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



class TestCreateWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 51124,
            'window_class': 2,
            'border_width': 60527,
            'visual': 655551457,
            'x': -29331,
            'y': -31237,
            'parent': 396285146,
            'attrs': {'backing_pixel': 2024529177, 'cursor': 1480094021, 'background_pixmap': 433235588, 'border_pixmap': 231786777, 'backing_planes': 1157998695, 'win_gravity': 10, 'backing_store': 2, 'event_mask': 227484423, 'save_under': 0, 'background_pixel': 1308429407, 'colormap': 1525011822, 'border_pixel': 387731971, 'bit_gravity': 10, 'do_not_propagate_mask': 405717137, 'override_redirect': 1},
            'wid': 87262202,
            'depth': 146,
            'width': 36620,
            }
        self.req_bin_0 = '\x01\x92\x17\x00' '\xfa\x83\x33\x05' \
            '\xda\xd4\x9e\x17' '\x6d\x8d\xfb\x85' \
            '\x0c\x8f\xb4\xc7' '\x6f\xec\x02\x00' \
            '\xe1\xeb\x12\x27' '\xff\x7f\x00\x00' \
            '\x84\xa6\xd2\x19' '\x5f\x0c\xfd\x4d' \
            '\x19\xc9\xd0\x0d' '\x03\x52\x1c\x17' \
            '\x0a\x00\x00\x00' '\x0a\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x67\xa8\x05\x45' \
            '\x19\xdd\xab\x78' '\x01\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x07\x23\x8f\x0d' \
            '\x91\xc0\x2e\x18' '\x6e\xd5\xe5\x5a' \
            '\x45\x71\x38\x58'


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
            'window': 428303190,
            'attrs': {'backing_pixel': 2013832962, 'cursor': 446042242, 'background_pixmap': 1770035686, 'border_pixmap': 812895035, 'backing_planes': 1821077423, 'win_gravity': 4, 'backing_store': 1, 'event_mask': 597203900, 'save_under': 1, 'background_pixel': 622761630, 'colormap': 276109855, 'border_pixel': 1471256576, 'bit_gravity': 5, 'do_not_propagate_mask': 1301887008, 'override_redirect': 1},
            }
        self.req_bin_0 = '\x02\x00\x12\x00' '\x56\x63\x87\x19' \
            '\xff\x7f\x00\x00' '\xe6\x99\x80\x69' \
            '\x9e\x96\x1e\x25' '\x3b\xcb\x73\x30' \
            '\x00\x98\xb1\x57' '\x05\x00\x00\x00' \
            '\x04\x00\x00\x00' '\x01\x00\x00\x00' \
            '\xaf\x6f\x8b\x6c' '\x02\xa7\x08\x78' \
            '\x01\x00\x00\x00' '\x01\x00\x00\x00' \
            '\xbc\x9b\x98\x23' '\x20\x38\x99\x4d' \
            '\x1f\x1a\x75\x10' '\x82\x10\x96\x1a'


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
            'window': 1468217358,
            }
        self.req_bin_0 = '\x03\x00\x02\x00' '\x0e\x38\x83\x57'

        self.reply_args_0 = {
            'sequence_number': 30708,
            'backing_pixel': 1202902034,
            'your_event_mask': 655820393,
            'map_is_installed': 1,
            'visual': 2102184134,
            'backing_bit_planes': 576708831,
            'backing_store': 212,
            'win_class': 36191,
            'map_state': 246,
            'save_under': 0,
            'all_event_masks': 1933312178,
            'colormap': 2134283233,
            'win_gravity': 246,
            'bit_gravity': 231,
            'do_not_propagate_mask': 50149,
            'override_redirect': 0,
            }
        self.reply_bin_0 = '\x01\xd4\xf4\x77' '\x03\x00\x00\x00' \
            '\xc6\xc8\x4c\x7d' '\x5f\x8d\xe7\xf6' \
            '\xdf\xe0\x5f\x22' '\x12\xd4\xb2\x47' \
            '\x00\x01\xf6\x00' '\xe1\x93\x36\x7f' \
            '\xb2\x00\x3c\x73' '\x69\x06\x17\x27' \
            '\xe5\xc3\x00\x00'


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
            'window': 1053047735,
            }
        self.req_bin_0 = '\x04\x00\x02\x00' '\xb7\x3b\xc4\x3e'


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
            'window': 1972810342,
            }
        self.req_bin_0 = '\x05\x00\x02\x00' '\x66\xb2\x96\x75'


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
            'window': 964012970,
            'mode': 1,
            }
        self.req_bin_0 = '\x06\x01\x02\x00' '\xaa\xab\x75\x39'


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
            'parent': 516914876,
            'window': 1038537138,
            'x': -20176,
            'y': -11696,
            }
        self.req_bin_0 = '\x07\x00\x04\x00' '\xb2\xd1\xe6\x3d' \
            '\xbc\x7e\xcf\x1e' '\x30\xb1\x50\xd2'


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
            'window': 1471601038,
            }
        self.req_bin_0 = '\x08\x00\x02\x00' '\x8e\xd9\xb6\x57'


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
            'window': 918108457,
            }
        self.req_bin_0 = '\x09\x00\x02\x00' '\x29\x39\xb9\x36'


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
            'window': 1471465231,
            }
        self.req_bin_0 = '\x0a\x00\x02\x00' '\x0f\xc7\xb4\x57'


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
            'window': 46050971,
            }
        self.req_bin_0 = '\x0b\x00\x02\x00' '\x9b\xae\xbe\x02'


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
            'window': 600527345,
            'attrs': {'height': 37290, 'stack_mode': 0, 'border_width': -3125, 'width': 43449, 'x': -3108, 'y': -26495, 'sibling': 334943607},
            }
        self.req_bin_0 = '\x0c\x00\x0a\x00' '\xf1\x51\xcb\x23' \
            '\x7f\x00\x00\x00' '\xdc\xf3\x00\x00' \
            '\x81\x98\x00\x00' '\xb9\xa9\x00\x00' \
            '\xaa\x91\x00\x00' '\xcb\xf3\x00\x00' \
            '\x77\xd5\xf6\x13' '\x00\x00\x00\x00'


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
            'window': 927018730,
            'direction': 1,
            }
        self.req_bin_0 = '\x0d\x01\x02\x00' '\xea\x2e\x41\x37'


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
            'drawable': 637076745,
            }
        self.req_bin_0 = '\x0e\x00\x02\x00' '\x09\x05\xf9\x25'

        self.reply_args_0 = {
            'height': 27858,
            'sequence_number': 59599,
            'root': 105430693,
            'border_width': 11695,
            'x': -17478,
            'y': -25040,
            'depth': 160,
            'width': 64250,
            }
        self.reply_bin_0 = '\x01\xa0\xcf\xe8' '\x00\x00\x00\x00' \
            '\xa5\xbe\x48\x06' '\xba\xbb\x30\x9e' \
            '\xfa\xfa\xd2\x6c' '\xaf\x2d\x00\x00' \
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
            'window': 1264746583,
            }
        self.req_bin_0 = '\x0f\x00\x02\x00' '\x57\x80\x62\x4b'

        self.reply_args_0 = {
            'sequence_number': 50903,
            'children': [654537453, 1040229650, 1640530307, 165160403, 1214529268, 1743961639, 51396303],
            'root': 161188428,
            'parent': 1054157135,
            }
        self.reply_bin_0 = '\x01\x00\xd7\xc6' '\x07\x00\x00\x00' \
            '\x4c\x8a\x9b\x09' '\x4f\x29\xd5\x3e' \
            '\x07\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xed\x72\x03\x27' '\x12\xa5\x00\x3e' \
            '\x83\x81\xc8\x61' '\xd3\x25\xd8\x09' \
            '\xf4\x3e\x64\x48' '\x27\xbe\xf2\x67' \
            '\xcf\x3e\x10\x03'


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
            'only_if_exists': 0,
            'name': 'fuzzy_prop',
            }
        self.req_bin_0 = '\x10\x00\x05\x00' '\x0a\x00\x00\x00' \
            '\x66\x75\x7a\x7a' '\x79\x5f\x70\x72' \
            '\x6f\x70\x00\x00'

        self.reply_args_0 = {
            'atom': 878448168,
            'sequence_number': 7500,
            }
        self.reply_bin_0 = '\x01\x00\x4c\x1d' '\x00\x00\x00\x00' \
            '\x28\x0e\x5c\x34' '\x00\x00\x00\x00' \
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
            'atom': 1237888948,
            }
        self.req_bin_0 = '\x11\x00\x02\x00' '\xb4\xaf\xc8\x49'

        self.reply_args_0 = {
            'sequence_number': 12161,
            'name': 'WM_CLASS',
            }
        self.reply_bin_0 = '\x01\x00\x81\x2f' '\x02\x00\x00\x00' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x00' \
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
            'mode': 0,
            'data': (8, ''),
            'property': 121293556,
            'window': 908893600,
            'type': 293676524,
            }
        self.req_bin_0 = '\x12\x00\x06\x00' '\xa0\x9d\x2c\x36' \
            '\xf4\xca\x3a\x07' '\xec\x25\x81\x11' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_1 = {
            'mode': 2,
            'data': (8, 'foo'),
            'property': 9530378,
            'window': 1108403910,
            'type': 1531473809,
            }
        self.req_bin_1 = '\x12\x02\x07\x00' '\xc6\xe6\x10\x42' \
            '\x0a\x6c\x91\x00' '\x91\x6f\x48\x5b' \
            '\x08\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'mode': 2,
            'data': (8, 'zoom'),
            'property': 1439134784,
            'window': 2019158,
            'type': 2124763244,
            }
        self.req_bin_2 = '\x12\x02\x07\x00' '\x56\xcf\x1e\x00' \
            '\x40\x74\xc7\x55' '\x6c\x50\xa5\x7e' \
            '\x08\x00\x00\x00' '\x04\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'mode': 1,
            'data': (16, []),
            'property': 1992921248,
            'window': 1136657542,
            'type': 1911776403,
            }
        self.req_bin_3 = '\x12\x01\x06\x00' '\x86\x04\xc0\x43' \
            '\xa0\x90\xc9\x76' '\x93\x64\xf3\x71' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_4 = {
            'mode': 2,
            'data': (16, [1, 2, 3]),
            'property': 1597584543,
            'window': 1358126866,
            'type': 835160206,
            }
        self.req_bin_4 = '\x12\x02\x08\x00' '\x12\x5f\xf3\x50' \
            '\x9f\x34\x39\x5f' '\x8e\x88\xc7\x31' \
            '\x10\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x00\x00'

        self.req_args_5 = {
            'mode': 1,
            'data': (16, [1, 2, 3, 4]),
            'property': 435291509,
            'window': 1472905410,
            'type': 1230605914,
            }
        self.req_bin_5 = '\x12\x01\x08\x00' '\xc2\xc0\xca\x57' \
            '\x75\x05\xf2\x19' '\x5a\x8e\x59\x49' \
            '\x10\x00\x00\x00' '\x04\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x04\x00'

        self.req_args_6 = {
            'mode': 1,
            'data': (32, []),
            'property': 55094983,
            'window': 1324723691,
            'type': 692600279,
            }
        self.req_bin_6 = '\x12\x01\x06\x00' '\xeb\xad\xf5\x4e' \
            '\xc7\xae\x48\x03' '\xd7\x3d\x48\x29' \
            '\x20\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_7 = {
            'mode': 1,
            'data': (32, [1, 2, 3]),
            'property': 193494084,
            'window': 534513211,
            'type': 1917666975,
            }
        self.req_bin_7 = '\x12\x01\x09\x00' '\x3b\x06\xdc\x1f' \
            '\x44\x7c\x88\x0b' '\x9f\x46\x4d\x72' \
            '\x20\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x03\x00\x00\x00'


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
            'property': 725061552,
            'window': 946299812,
            }
        self.req_bin_0 = '\x13\x00\x03\x00' '\xa4\x63\x67\x38' \
            '\xb0\x8f\x37\x2b'


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
            'long_offset': 1776979845,
            'type': 1984541036,
            'property': 143828948,
            'window': 1110123856,
            'long_length': 1858952230,
            }
        self.req_bin_0 = '\x14\x00\x06\x00' '\x50\x25\x2b\x42' \
            '\xd4\xa7\x92\x08' '\x6c\xb1\x49\x76' \
            '\x85\x8f\xea\x69' '\x26\x5c\xcd\x6e'

        self.reply_args_0 = {
            'value': (8, ''),
            'sequence_number': 13616,
            'property_type': 1903154626,
            'bytes_after': 429333510,
            }
        self.reply_bin_0 = '\x01\x08\x30\x35' '\x00\x00\x00\x00' \
            '\xc2\xd5\x6f\x71' '\x06\x1c\x97\x19' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_1 = {
            'value': (8, 'foo'),
            'sequence_number': 6304,
            'property_type': 416583633,
            'bytes_after': 383556417,
            }
        self.reply_bin_1 = '\x01\x08\xa0\x18' '\x01\x00\x00\x00' \
            '\xd1\x8f\xd4\x18' '\x41\x9b\xdc\x16' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'value': (8, 'zoom'),
            'sequence_number': 23761,
            'property_type': 525482017,
            'bytes_after': 968458080,
            }
        self.reply_bin_2 = '\x01\x08\xd1\x5c' '\x01\x00\x00\x00' \
            '\x21\x38\x52\x1f' '\x60\x7f\xb9\x39' \
            '\x04\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'value': (16, []),
            'sequence_number': 39012,
            'property_type': 955456122,
            'bytes_after': 1673384749,
            }
        self.reply_bin_3 = '\x01\x10\x64\x98' '\x00\x00\x00\x00' \
            '\x7a\x1a\xf3\x38' '\x2d\xd3\xbd\x63' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_4 = {
            'value': (16, [1, 2, 3]),
            'sequence_number': 43089,
            'property_type': 579984768,
            'bytes_after': 663160557,
            }
        self.reply_bin_4 = '\x01\x10\x51\xa8' '\x02\x00\x00\x00' \
            '\x80\xdd\x91\x22' '\xed\x06\x87\x27' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x00\x00'

        self.reply_args_5 = {
            'value': (16, [1, 2, 3, 4]),
            'sequence_number': 981,
            'property_type': 2084450501,
            'bytes_after': 1582487365,
            }
        self.reply_bin_5 = '\x01\x10\xd5\x03' '\x02\x00\x00\x00' \
            '\xc5\x30\x3e\x7c' '\x45\xd7\x52\x5e' \
            '\x04\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x04\x00'

        self.reply_args_6 = {
            'value': (32, []),
            'sequence_number': 21070,
            'property_type': 1131917309,
            'bytes_after': 834655976,
            }
        self.reply_bin_6 = '\x01\x20\x4e\x52' '\x00\x00\x00\x00' \
            '\xfd\xaf\x77\x43' '\xe8\xd6\xbf\x31' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_7 = {
            'value': (32, [1, 2, 3]),
            'sequence_number': 28879,
            'property_type': 438551069,
            'bytes_after': 1454353077,
            }
        self.reply_bin_7 = '\x01\x20\xcf\x70' '\x03\x00\x00\x00' \
            '\x1d\xc2\x23\x1a' '\xb5\xaa\xaf\x56' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x03\x00\x00\x00'


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
            'window': 1389230424,
            }
        self.req_bin_0 = '\x15\x00\x02\x00' '\x58\xf9\xcd\x52'

        self.reply_args_0 = {
            'atoms': [536523536, 556191291, 1480806825, 1577232047, 1205972758, 270648009, 1574990777, 1385953923, 1255905273, 671061654, 869217092, 1769215442, 1212418217, 2114817618, 830211314, 6547534, 1397331668, 463966829, 389129174, 1342247752, 781417559, 1718055207, 130849301],
            'sequence_number': 26980,
            }
        self.reply_bin_0 = '\x01\x00\x64\x69' '\x17\x00\x00\x00' \
            '\x17\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x10\xb3\xfa\x1f' '\x3b\xce\x26\x21' \
            '\xa9\x51\x43\x58' '\xaf\xa6\x02\x5e' \
            '\x16\xaf\xe1\x47' '\xc9\xc2\x21\x10' \
            '\xb9\x73\xe0\x5d' '\x83\xfa\x9b\x52' \
            '\xf9\x97\xdb\x4a' '\x96\x96\xff\x27' \
            '\x44\x33\xcf\x33' '\xd2\x15\x74\x69' \
            '\xa9\x08\x44\x48' '\x52\x8e\x0d\x7e' \
            '\xf2\x04\x7c\x31' '\x4e\xe8\x63\x00' \
            '\xd4\x96\x49\x53' '\x6d\x92\xa7\x1b' \
            '\xd6\xa3\x31\x17' '\x48\x13\x01\x50' \
            '\x57\x7c\x93\x2e' '\x27\x71\x67\x66' \
            '\x15\x9a\xcc\x07'


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
            'selection': 583630041,
            'window': 2122770016,
            'time': 1747527786,
            }
        self.req_bin_0 = '\x16\x00\x04\x00' '\x60\xe6\x86\x7e' \
            '\xd9\x7c\xc9\x22' '\x6a\x28\x29\x68'


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
            'selection': 1569820391,
            }
        self.req_bin_0 = '\x17\x00\x02\x00' '\xe7\x8e\x91\x5d'

        self.reply_args_0 = {
            'sequence_number': 34389,
            'owner': 218603020,
            }
        self.reply_bin_0 = '\x01\x00\x55\x86' '\x00\x00\x00\x00' \
            '\x0c\x9e\x07\x0d' '\x00\x00\x00\x00' \
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
            'property': 1974057043,
            'time': 1469364033,
            'target': 1182414718,
            'selection': 397784400,
            'requestor': 1796890929,
            }
        self.req_bin_0 = '\x18\x00\x06\x00' '\x31\x61\x1a\x6b' \
            '\x50\xb5\xb5\x17' '\x7e\x37\x7a\x46' \
            '\x53\xb8\xa9\x75' '\x41\xb7\x94\x57'


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
            'event': Xlib.protocol.event.Expose(height = 1245, sequence_number = 0, type = 12, x = 11102, y = 38573, window = 1560692102, width = 18473, count = 10670),
            'propagate': 1,
            'destination': 1582767848,
            'event_mask': 494644249,
            }
        self.req_bin_0 = '\x19\x01\x0b\x00' '\xe8\x1e\x57\x5e' \
            '\x19\xac\x7b\x1d' '\x0c\x00\x00\x00' \
            '\x86\x45\x06\x5d' '\x5e\x2b\xad\x96' \
            '\x29\x48\xdd\x04' '\xae\x29\x00\x00' \
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
            'owner_events': 0,
            'grab_window': 976989570,
            'confine_to': 1752487064,
            'event_mask': 14389,
            'pointer_mode': 1,
            'time': 1130197441,
            'keyboard_mode': 1,
            'cursor': 1471123675,
            }
        self.req_bin_0 = '\x1a\x00\x06\x00' '\x82\xad\x3b\x3a' \
            '\x35\x38\x01\x01' '\x98\xd4\x74\x68' \
            '\xdb\x90\xaf\x57' '\xc1\x71\x5d\x43'

        self.reply_args_0 = {
            'sequence_number': 52537,
            'status': 225,
            }
        self.reply_bin_0 = '\x01\xe1\x39\xcd' '\x00\x00\x00\x00' \
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
            'time': 1336010176,
            }
        self.req_bin_0 = '\x1b\x00\x02\x00' '\xc0\xe5\xa1\x4f'


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
            'grab_window': 1052101051,
            'confine_to': 242344469,
            'event_mask': 21170,
            'pointer_mode': 1,
            'modifiers': 15942,
            'button': 218,
            'keyboard_mode': 0,
            'cursor': 1695355667,
            }
        self.req_bin_0 = '\x1c\x01\x06\x00' '\xbb\xc9\xb5\x3e' \
            '\xb2\x52\x01\x00' '\x15\xe2\x71\x0e' \
            '\x13\x13\x0d\x65' '\xda\x00\x46\x3e'


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
            'grab_window': 1664831678,
            'button': 145,
            'modifiers': 51572,
            }
        self.req_bin_0 = '\x1d\x91\x03\x00' '\xbe\x50\x3b\x63' \
            '\x74\xc9\x00\x00'


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
            'time': 191100319,
            'event_mask': 30855,
            'cursor': 1650226962,
            }
        self.req_bin_0 = '\x1e\x00\x04\x00' '\x12\x77\x5c\x62' \
            '\x9f\xf5\x63\x0b' '\x87\x78\x00\x00'


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
            'owner_events': 0,
            'grab_window': 565108870,
            'time': 475934574,
            'pointer_mode': 1,
            'keyboard_mode': 1,
            }
        self.req_bin_0 = '\x1f\x00\x04\x00' '\x86\xe0\xae\x21' \
            '\x6e\x2f\x5e\x1c' '\x01\x01\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 19651,
            'status': 164,
            }
        self.reply_bin_0 = '\x01\xa4\xc3\x4c' '\x00\x00\x00\x00' \
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
            'time': 1156958567,
            }
        self.req_bin_0 = '\x20\x00\x02\x00' '\x67\xc9\xf5\x44'


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
            'grab_window': 1072490405,
            'pointer_mode': 1,
            'keyboard_mode': 1,
            'modifiers': 43121,
            'key': 189,
            }
        self.req_bin_0 = '\x21\x00\x04\x00' '\xa5\xe7\xec\x3f' \
            '\x71\xa8\xbd\x01' '\x01\x00\x00\x00'


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
            'grab_window': 1500951121,
            'key': 140,
            'modifiers': 45139,
            }
        self.req_bin_0 = '\x22\x8c\x03\x00' '\x51\xb2\x76\x59' \
            '\x53\xb0\x00\x00'


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
            'time': 968389540,
            'mode': 4,
            }
        self.req_bin_0 = '\x23\x04\x02\x00' '\xa4\x73\xb8\x39'


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
        self.req_bin_0 = '\x24\x00\x01\x00'


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
        self.req_bin_0 = '\x25\x00\x01\x00'


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
            'window': 262597814,
            }
        self.req_bin_0 = '\x26\x00\x02\x00' '\xb6\xec\xa6\x0f'

        self.reply_args_0 = {
            'win_y': -3349,
            'same_screen': 0,
            'sequence_number': 23607,
            'root': 2017523480,
            'root_x': -7820,
            'root_y': -7526,
            'mask': 19191,
            'child': 1777351886,
            'win_x': -27037,
            }
        self.reply_bin_0 = '\x01\x00\x37\x5c' '\x00\x00\x00\x00' \
            '\x18\xf7\x40\x78' '\xce\x3c\xf0\x69' \
            '\x74\xe1\x9a\xe2' '\x63\x96\xeb\xf2' \
            '\xf7\x4a\x00\x00' '\x00\x00\x00\x00'


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
            'window': 1010501129,
            'start': 1661685958,
            'stop': 81291471,
            }
        self.req_bin_0 = '\x27\x00\x04\x00' '\x09\x06\x3b\x3c' \
            '\xc6\x50\x0b\x63' '\xcf\x68\xd8\x04'

        self.reply_args_0 = {
            'sequence_number': 45121,
            'events': [{'time': 1179256144, 'x': -27324, 'y': -28271}, {'time': 722407962, 'x': -12852, 'y': -22265}, {'time': 168294967, 'x': -11495, 'y': -30868}, {'time': 1304824361, 'x': -13714, 'y': -13359}, {'time': 745684637, 'x': -694, 'y': -4687}],
            }
        self.reply_bin_0 = '\x01\x00\x41\xb0' '\x0a\x00\x00\x00' \
            '\x05\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x50\x05\x4a\x46' '\x44\x95\x91\x91' \
            '\x1a\x12\x0f\x2b' '\xcc\xcd\x07\xa9' \
            '\x37\xfa\x07\x0a' '\x19\xd3\x6c\x87' \
            '\x29\x0a\xc6\x4d' '\x6e\xca\xd1\xcb' \
            '\x9d\x3e\x72\x2c' '\x4a\xfd\xb1\xed'


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
            'src_y': -23239,
            'src_x': -26618,
            'src_wid': 839434595,
            'dst_wid': 652120060,
            }
        self.req_bin_0 = '\x28\x00\x04\x00' '\x63\xc1\x08\x32' \
            '\xfc\x8f\xde\x26' '\x06\x98\x39\xa5'

        self.reply_args_0 = {
            'child': 1701829380,
            'same_screen': 1,
            'sequence_number': 30919,
            'x': -17337,
            'y': -13527,
            }
        self.reply_bin_0 = '\x01\x01\xc7\x78' '\x00\x00\x00\x00' \
            '\x04\xdb\x6f\x65' '\x47\xbc\x29\xcb' \
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
            'src_height': 52067,
            'src_window': 625454028,
            'dst_window': 337365843,
            'src_width': 12683,
            'src_y': -30345,
            'src_x': -29305,
            'dst_x': -26932,
            'dst_y': -14922,
            }
        self.req_bin_0 = '\x29\x00\x06\x00' '\xcc\xab\x47\x25' \
            '\x53\xcb\x1b\x14' '\x87\x8d\x77\x89' \
            '\x8b\x31\x63\xcb' '\xcc\x96\xb6\xc5'


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
            'revert_to': 0,
            'time': 206785411,
            'focus': 899929038,
            }
        self.req_bin_0 = '\x2a\x00\x03\x00' '\xce\xd3\xa3\x35' \
            '\x83\x4b\x53\x0c'


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
        self.req_bin_0 = '\x2b\x00\x01\x00'

        self.reply_args_0 = {
            'revert_to': 142,
            'sequence_number': 46535,
            'focus': 1656806831,
            }
        self.reply_bin_0 = '\x01\x8e\xc7\xb5' '\x00\x00\x00\x00' \
            '\xaf\xdd\xc0\x62' '\x00\x00\x00\x00' \
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
        self.req_bin_0 = '\x2c\x00\x01\x00'

        self.reply_args_0 = {
            'sequence_number': 44941,
            'map': [158, 227, 139, 158, 150, 199, 177, 170, 224, 151, 175, 202, 156, 139, 246, 165, 164, 145, 225, 199, 181, 154, 130, 171, 150, 162, 185, 154, 217, 130, 160, 176],
            }
        self.reply_bin_0 = '\x01\x00\x8d\xaf' '\x02\x00\x00\x00' \
            '\x9e\xe3\x8b\x9e' '\x96\xc7\xb1\xaa' \
            '\xe0\x97\xaf\xca' '\x9c\x8b\xf6\xa5' \
            '\xa4\x91\xe1\xc7' '\xb5\x9a\x82\xab' \
            '\x96\xa2\xb9\x9a' '\xd9\x82\xa0\xb0'


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
            'fid': 1618185695,
            'name': 'foofont',
            }
        self.req_bin_0 = '\x2d\x00\x05\x00' '\xdf\x8d\x73\x60' \
            '\x07\x00\x00\x00' '\x66\x6f\x6f\x66' \
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
            'font': 1737763153,
            }
        self.req_bin_0 = '\x2e\x00\x02\x00' '\x51\x29\x94\x67'


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
            'font': 2009329799,
            }
        self.req_bin_0 = '\x2f\x00\x02\x00' '\x87\xf0\xc3\x77'

        self.reply_args_0 = {
            'sequence_number': 64047,
            'properties': [{'value': 362685469, 'name': 1666904561}],
            'min_byte1': 164,
            'max_byte1': 207,
            'char_infos': [{'descent': -30261, 'ascent': -4694, 'character_width': -5223, 'left_side_bearing': -19959, 'right_side_bearing': -12547, 'attributes': 51634}, {'descent': -29573, 'ascent': -30961, 'character_width': -18492, 'left_side_bearing': -26603, 'right_side_bearing': -21416, 'attributes': 23202}, {'descent': -28315, 'ascent': -14655, 'character_width': -23355, 'left_side_bearing': -4152, 'right_side_bearing': -32308, 'attributes': 61921}],
            'max_char_or_byte2': 9466,
            'default_char': 44982,
            'min_char_or_byte2': 30824,
            'draw_direction': 179,
            'min_bounds': {'descent': -1422, 'ascent': -25809, 'character_width': -13091, 'left_side_bearing': -1024, 'right_side_bearing': -11291, 'attributes': 55408},
            'all_chars_exist': 0,
            'font_ascent': -13885,
            'font_descent': -25099,
            'max_bounds': {'descent': -23672, 'ascent': -27764, 'character_width': -5091, 'left_side_bearing': -22156, 'right_side_bearing': -10975, 'attributes': 59628},
            }
        self.reply_bin_0 = '\x01\x00\x2f\xfa' '\x12\x00\x00\x00' \
            '\x00\xfc\xe5\xd3' '\xdd\xcc\x2f\x9b' \
            '\x72\xfa\x70\xd8' '\x00\x00\x00\x00' \
            '\x74\xa9\x21\xd5' '\x1d\xec\x8c\x93' \
            '\x88\xa3\xec\xe8' '\x00\x00\x00\x00' \
            '\x68\x78\xfa\x24' '\xb6\xaf\x01\x00' \
            '\xb3\xa4\xcf\x00' '\xc3\xc9\xf5\x9d' \
            '\x03\x00\x00\x00' '\xf1\xf1\x5a\x63' \
            '\x1d\x24\x9e\x15' '\x09\xb2\xfd\xce' \
            '\x99\xeb\xaa\xed' '\xcb\x89\xb2\xc9' \
            '\x15\x98\x58\xac' '\xc4\xb7\x0f\x87' \
            '\x7b\x8c\xa2\x5a' '\xc8\xef\xcc\x81' \
            '\xc5\xa4\xc1\xc6' '\x65\x91\xe1\xf1'


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
            'font': 2009834150,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = '\x30\x01\x04\x00' '\xa6\xa2\xcb\x77' \
            '\x00\x66\x00\x6f' '\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'overall_width': -232775227,
            'draw_direction': 197,
            'sequence_number': 4221,
            'font_ascent': -10066,
            'overall_ascent': -32157,
            'overall_descent': -30716,
            'overall_right': -1206665106,
            'overall_left': -655678256,
            'font_descent': -20110,
            }
        self.reply_bin_0 = '\x01\xc5\x7d\x10' '\x00\x00\x00\x00' \
            '\xae\xd8\x72\xb1' '\x63\x82\x04\x88' \
            '\xc5\x21\x20\xf2' '\xd0\x24\xeb\xd8' \
            '\x6e\xc0\x13\xb8' '\x00\x00\x00\x00'


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
            'max_names': 12046,
            'pattern': 'bhazr',
            }
        self.req_bin_0 = '\x31\x00\x04\x00' '\x0e\x2f\x05\x00' \
            '\x62\x68\x61\x7a' '\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 7783,
            }
        self.reply_bin_0 = '\x01\x00\x67\x1e' '\x05\x00\x00\x00' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
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
            'max_names': 33718,
            'pattern': 'bhazr2',
            }
        self.req_bin_0 = '\x32\x00\x04\x00' '\xb6\x83\x06\x00' \
            '\x62\x68\x61\x7a' '\x72\x32\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 11974,
            'properties': [{'value': 2098678446, 'name': 908345694}],
            'min_byte1': 165,
            'max_byte1': 234,
            'max_char_or_byte2': 19009,
            'default_char': 3843,
            'min_char_or_byte2': 58498,
            'draw_direction': 130,
            'replies_hint': 2071349253,
            'min_bounds': {'descent': -12918, 'ascent': -4478, 'character_width': -753, 'left_side_bearing': -7475, 'right_side_bearing': -20789, 'attributes': 50847},
            'all_chars_exist': 0,
            'name': 'fontfont',
            'font_ascent': -14735,
            'font_descent': -15421,
            'max_bounds': {'descent': -21236, 'ascent': -28279, 'character_width': -21657, 'left_side_bearing': -3137, 'right_side_bearing': -23095, 'attributes': 43267},
            }
        self.reply_bin_0 = '\x01\x08\xc6\x2e' '\x0b\x00\x00\x00' \
            '\xcd\xe2\xcb\xae' '\x0f\xfd\x82\xee' \
            '\x8a\xcd\x9f\xc6' '\x00\x00\x00\x00' \
            '\xbf\xf3\xc9\xa5' '\x67\xab\x89\x91' \
            '\x0c\xad\x03\xa9' '\x00\x00\x00\x00' \
            '\x82\xe4\x41\x4a' '\x03\x0f\x01\x00' \
            '\x82\xa5\xea\x00' '\x71\xc6\xc3\xc3' \
            '\x05\x48\x76\x7b' '\x5e\x41\x24\x36' \
            '\xae\x4a\x17\x7d' '\x66\x6f\x6e\x74' \
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
        self.req_bin_0 = '\x33\x00\x06\x00' '\x03\x00\x00\x00' \
            '\x03\x66\x6f\x6f' '\x03\x62\x61\x72' \
            '\x06\x67\x61\x7a' '\x6f\x6e\x6b\x00'

        self.req_args_1 = {
            'path': [],
            }
        self.req_bin_1 = '\x33\x00\x02\x00' '\x00\x00\x00\x00'


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
        self.req_bin_0 = '\x34\x00\x01\x00'

        self.reply_args_0 = {
            'sequence_number': 3447,
            'paths': ['path1', 'path2232'],
            }
        self.reply_bin_0 = '\x01\x00\x77\x0d' '\x04\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x05\x70\x61\x74' '\x68\x31\x08\x70' \
            '\x61\x74\x68\x32' '\x32\x33\x32\x00'

        self.reply_args_1 = {
            'sequence_number': 31069,
            'paths': [],
            }
        self.reply_bin_1 = '\x01\x00\x5d\x79' '\x00\x00\x00\x00' \
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
            'height': 5766,
            'drawable': 1167482187,
            'pid': 70917632,
            'depth': 209,
            'width': 54374,
            }
        self.req_bin_0 = '\x35\xd1\x04\x00' '\x00\x1e\x3a\x04' \
            '\x4b\x5d\x96\x45' '\x66\xd4\x86\x16'


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
            'pixmap': 1525266413,
            }
        self.req_bin_0 = '\x36\x00\x02\x00' '\xed\xb7\xe9\x5a'


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
            'cid': 942123885,
            'drawable': 102951441,
            'attrs': {'dashes': 137, 'fill_rule': 0, 'clip_mask': 2107351630, 'plane_mask': 727789750, 'line_style': 0, 'tile': 30832839, 'arc_mode': 1, 'clip_y_origin': -21007, 'dash_offset': 54269, 'line_width': 35630, 'background': 1326892219, 'clip_x_origin': -32730, 'join_style': 0, 'graphics_exposures': 1, 'font': 532212415, 'tile_stipple_y_origin': -597, 'stipple': 723220473, 'fill_style': 3, 'cap_style': 1, 'subwindow_mode': 0, 'tile_stipple_x_origin': -15370, 'foreground': 780435917, 'function': 0},
            }
        self.req_bin_0 = '\x37\x00\x1b\x00' '\x6d\xab\x27\x38' \
            '\x11\xea\x22\x06' '\xff\xff\x7f\x00' \
            '\x00\x00\x00\x00' '\xb6\x30\x61\x2b' \
            '\xcd\x81\x84\x2e' '\xbb\xc4\x16\x4f' \
            '\x2e\x8b\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xc7\x78\xd6\x01' '\xf9\x77\x1b\x2b' \
            '\xf6\xc3\x00\x00' '\xab\xfd\x00\x00' \
            '\xbf\xea\xb8\x1f' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x26\x80\x00\x00' \
            '\xf1\xad\x00\x00' '\x4e\xa2\x9b\x7d' \
            '\xfd\xd3\x00\x00' '\x89\x00\x00\x00' \
            '\x01\x00\x00\x00'


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
            'attrs': {'dashes': 178, 'fill_rule': 1, 'clip_mask': 820711299, 'plane_mask': 545619193, 'line_style': 2, 'tile': 880175152, 'arc_mode': 0, 'clip_y_origin': -27458, 'dash_offset': 63686, 'line_width': 54406, 'background': 1409122638, 'clip_x_origin': -21504, 'join_style': 0, 'graphics_exposures': 0, 'font': 1909809300, 'tile_stipple_y_origin': -15328, 'stipple': 228451178, 'fill_style': 1, 'cap_style': 0, 'subwindow_mode': 0, 'tile_stipple_x_origin': -28280, 'foreground': 2057030041, 'function': 9},
            'gc': 1752776894,
            }
        self.req_bin_0 = '\x38\x00\x1a\x00' '\xbe\x40\x79\x68' \
            '\xff\xff\x7f\x00' '\x09\x00\x00\x00' \
            '\xf9\x7c\x85\x20' '\x99\xc9\x9b\x7a' \
            '\x4e\x81\xfd\x53' '\x86\xd4\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x30\x68\x76\x34' \
            '\x6a\xe3\x9d\x0d' '\x88\x91\x00\x00' \
            '\x20\xc4\x00\x00' '\x94\x60\xd5\x71' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\xac\x00\x00' '\xbe\x94\x00\x00' \
            '\x83\x0f\xeb\x30' '\xc6\xf8\x00\x00' \
            '\xb2\x00\x00\x00' '\x00\x00\x00\x00'


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
            'mask': 1859370956,
            'src_gc': 1039140461,
            'dst_gc': 890571964,
            }
        self.req_bin_0 = '\x39\x00\x04\x00' '\x6d\x06\xf0\x3d' \
            '\xbc\x0c\x15\x35' '\xcc\xbf\xd3\x6e'


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
            'dashes': [130, 226, 250, 200, 241, 203, 187, 196, 243],
            'dash_offset': 59917,
            'gc': 228428376,
            }
        self.req_bin_0 = '\x3a\x00\x06\x00' '\x58\x8a\x9d\x0d' \
            '\x0d\xea\x09\x00' '\x82\xe2\xfa\xc8' \
            '\xf1\xcb\xbb\xc4' '\xf3\x00\x00\x00'


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
            'rectangles': [{'height': 49269, 'x': -23940, 'width': 27217, 'y': -21180}, {'height': 25721, 'x': -24644, 'width': 35197, 'y': -14850}],
            'gc': 886009,
            'x_origin': -18334,
            'y_origin': -5096,
            'ordering': 1,
            }
        self.req_bin_0 = '\x3b\x01\x07\x00' '\xf9\x84\x0d\x00' \
            '\x62\xb8\x18\xec' '\x7c\xa2\x44\xad' \
            '\x51\x6a\x75\xc0' '\xbc\x9f\xfe\xc5' \
            '\x7d\x89\x79\x64'

        self.req_args_1 = {
            'rectangles': [],
            'gc': 66224262,
            'x_origin': -7219,
            'y_origin': -6453,
            'ordering': 2,
            }
        self.req_bin_1 = '\x3b\x02\x03\x00' '\x86\x80\xf2\x03' \
            '\xcd\xe3\xcb\xe6'


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
            'gc': 337358059,
            }
        self.req_bin_0 = '\x3c\x00\x02\x00' '\xeb\xac\x1b\x14'


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
            'height': 43136,
            'width': 22500,
            'window': 665196869,
            'x': -17967,
            'y': -1695,
            }
        self.req_bin_0 = '\x3d\x00\x04\x00' '\x45\x19\xa6\x27' \
            '\xd1\xb9\x61\xf9' '\xe4\x57\x80\xa8'


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
            'src_drawable': 105361612,
            'dst_drawable': 1923450424,
            'src_y': -2270,
            'src_x': -27972,
            'gc': 1584121403,
            'width': 22765,
            'height': 50821,
            'dst_x': -31849,
            'dst_y': -28966,
            }
        self.req_bin_0 = '\x3e\x00\x07\x00' '\xcc\xb0\x47\x06' \
            '\x38\x86\xa5\x72' '\x3b\xc6\x6b\x5e' \
            '\xbc\x92\x22\xf7' '\x97\x83\xda\x8e' \
            '\xed\x58\x85\xc6'


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
            'src_drawable': 1020374669,
            'bit_plane': 1623509536,
            'dst_drawable': 61228905,
            'src_y': -23435,
            'src_x': -25546,
            'gc': 1159239082,
            'width': 32661,
            'height': 64577,
            'dst_x': -9980,
            'dst_y': -2344,
            }
        self.req_bin_0 = '\x3f\x00\x08\x00' '\x8d\xae\xd1\x3c' \
            '\x69\x47\xa6\x03' '\xaa\x95\x18\x45' \
            '\x36\x9c\x75\xa4' '\x04\xd9\xd8\xf6' \
            '\x95\x7f\x41\xfc' '\x20\xca\xc4\x60'


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
            'gc': 2113017639,
            'points': [{'x': -4715, 'y': -1522}, {'x': -23697, 'y': -29709}, {'x': -6180, 'y': -23780}],
            'drawable': 1140067368,
            'coord_mode': 1,
            }
        self.req_bin_0 = '\x40\x01\x06\x00' '\x28\x0c\xf4\x43' \
            '\x27\x17\xf2\x7d' '\x95\xed\x0e\xfa' \
            '\x6f\xa3\xf3\x8b' '\xdc\xe7\x1c\xa3'


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
            'gc': 1814543514,
            'points': [{'x': -25584, 'y': -28073}, {'x': -16618, 'y': -23040}, {'x': -16767, 'y': -18595}, {'x': -6392, 'y': -11205}, {'x': -29083, 'y': -23846}],
            'drawable': 1679768533,
            'coord_mode': 0,
            }
        self.req_bin_0 = '\x41\x00\x08\x00' '\xd5\x3b\x1f\x64' \
            '\x9a\xbc\x27\x6c' '\x10\x9c\x57\x92' \
            '\x16\xbf\x00\xa6' '\x81\xbe\x5d\xb7' \
            '\x08\xe7\x3b\xd4' '\x65\x8e\xda\xa2'


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
            'segments': [{'y1': -23980, 'y2': -17603, 'x1': -13202, 'x2': -21848}],
            'drawable': 443588989,
            'gc': 1574871651,
            }
        self.req_bin_0 = '\x42\x00\x05\x00' '\x7d\xa1\x70\x1a' \
            '\x63\xa2\xde\x5d' '\x6e\xcc\x54\xa2' \
            '\xa8\xaa\x3d\xbb'


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
            'drawable': 1972205573,
            'gc': 161292394,
            'rectangles': [{'height': 24274, 'x': -13483, 'width': 22048, 'y': -7854}, {'height': 12180, 'x': -8087, 'width': 22657, 'y': -4415}, {'height': 25888, 'x': -5499, 'width': 26390, 'y': -27407}],
            }
        self.req_bin_0 = '\x43\x00\x09\x00' '\x05\x78\x8d\x75' \
            '\x6a\x20\x9d\x09' '\x55\xcb\x52\xe1' \
            '\x20\x56\xd2\x5e' '\x69\xe0\xc1\xee' \
            '\x81\x58\x94\x2f' '\x85\xea\xf1\x94' \
            '\x16\x67\x20\x65'


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
            'arcs': [{'height': 45962, 'angle1': -28920, 'x': -6896, 'angle2': -14659, 'width': 15865, 'y': -22529}, {'height': 27198, 'angle1': -7303, 'x': -3296, 'angle2': -17048, 'width': 58653, 'y': -24192}, {'height': 2736, 'angle1': -7064, 'x': -25407, 'angle2': -1242, 'width': 20740, 'y': -5043}],
            'drawable': 1438546991,
            'gc': 2050849964,
            }
        self.req_bin_0 = '\x44\x00\x0c\x00' '\x2f\x7c\xbe\x55' \
            '\xac\x7c\x3d\x7a' '\x10\xe5\xff\xa7' \
            '\xf9\x3d\x8a\xb3' '\x08\x8f\xbd\xc6' \
            '\x20\xf3\x80\xa1' '\x1d\xe5\x3e\x6a' \
            '\x79\xe3\x68\xbd' '\xc1\x9c\x4d\xec' \
            '\x04\x51\xb0\x0a' '\x68\xe4\x26\xfb'


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
            'gc': 199429228,
            'points': [{'x': -17668, 'y': -20040}, {'x': -25597, 'y': -481}, {'x': -7991, 'y': -8393}],
            'drawable': 51274902,
            'coord_mode': 0,
            }
        self.req_bin_0 = '\x45\x00\x07\x00' '\x96\x64\x0e\x03' \
            '\x6c\x0c\xe3\x0b' '\x02\x00\x00\x00' \
            '\xfc\xba\xb8\xb1' '\x03\x9c\x1f\xfe' \
            '\xc9\xe0\x37\xdf'


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
            'drawable': 584470648,
            'gc': 1421385174,
            'rectangles': [{'height': 20944, 'x': -14801, 'width': 49509, 'y': -4315}, {'height': 10143, 'x': -31526, 'width': 11966, 'y': -17830}],
            }
        self.req_bin_0 = '\x46\x00\x07\x00' '\x78\x50\xd6\x22' \
            '\xd6\x9d\xb8\x54' '\x2f\xc6\x25\xef' \
            '\x65\xc1\xd0\x51' '\xda\x84\x5a\xba' \
            '\xbe\x2e\x9f\x27'


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
            'arcs': [{'height': 37375, 'angle1': -22604, 'x': -14979, 'angle2': -24629, 'width': 19809, 'y': -19722}],
            'drawable': 1677906193,
            'gc': 985773241,
            }
        self.req_bin_0 = '\x47\x00\x06\x00' '\x11\xd1\x02\x64' \
            '\xb9\xb4\xc1\x3a' '\x7d\xc5\xf6\xb2' \
            '\x61\x4d\xff\x91' '\xb4\xa7\xcb\x9f'


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
            'height': 47476,
            'data': 'bit map data',
            'drawable': 617825660,
            'left_pad': 156,
            'format': 2,
            'dst_x': -26300,
            'gc': 765641900,
            'depth': 165,
            'width': 11101,
            'dst_y': -10462,
            }
        self.req_bin_0 = '\x48\x02\x09\x00' '\x7c\x45\xd3\x24' \
            '\xac\xc4\xa2\x2d' '\x5d\x2b\x74\xb9' \
            '\x44\x99\x22\xd7' '\x9c\xa5\x00\x00' \
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
            'height': 20976,
            'plane_mask': 1637449074,
            'drawable': 1797917309,
            'x': -12084,
            'y': -28811,
            'format': 1,
            'width': 40169,
            }
        self.req_bin_0 = '\x49\x01\x05\x00' '\x7d\x0a\x2a\x6b' \
            '\xcc\xd0\x75\x8f' '\xe9\x9c\xf0\x51' \
            '\x72\x7d\x99\x61'

        self.reply_args_0 = {
            'sequence_number': 42631,
            'data': 'this is real ly imag e b-map',
            'visual': 1645537050,
            'depth': 181,
            }
        self.reply_bin_0 = '\x01\xb5\x87\xa6' '\x07\x00\x00\x00' \
            '\x1a\xe7\x14\x62' '\x00\x00\x00\x00' \
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
            'gc': 1110169872,
            'x': -18724,
            'drawable': 1601859349,
            'items': [{'delta': 2, 'string': 'zoo'}, 16909060, {'delta': 0, 'string': 'ie'}],
            'y': -21056,
            }
        self.req_bin_0 = '\x4a\x00\x08\x00' '\x15\x6f\x7a\x5f' \
            '\x10\xd9\x2b\x42' '\xdc\xb6\xc0\xad' \
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
            'gc': 281766196,
            'x': -28820,
            'drawable': 1261275055,
            'items': [{'delta': 2, 'string': (4131, 18)}, 16909060],
            'y': -26890,
            }
        self.req_bin_0 = '\x4b\x00\x07\x00' '\xaf\x87\x2d\x4b' \
            '\x34\x69\xcb\x10' '\x6c\x8f\xf6\x96' \
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
            'gc': 54596862,
            'drawable': 368759934,
            'x': -4888,
            'y': -2970,
            }
        self.req_bin_0 = '\x4c\x06\x06\x00' '\x7e\xd4\xfa\x15' \
            '\xfe\x14\x41\x03' '\xe8\xec\x66\xf4' \
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
            'gc': 1547598265,
            'drawable': 891789770,
            'x': -11499,
            'y': -27806,
            }
        self.req_bin_0 = '\x4d\x08\x08\x00' '\xca\xa1\x27\x35' \
            '\xb9\x79\x3e\x5c' '\x15\xd3\x62\x93' \
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
            'mid': 179984095,
            'alloc': 0,
            'visual': 1860808354,
            'window': 576861162,
            }
        self.req_bin_0 = '\x4e\x00\x04\x00' '\xdf\x56\xba\x0a' \
            '\xea\x33\x62\x22' '\xa2\xae\xe9\x6e'


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
            'cmap': 210702022,
            }
        self.req_bin_0 = '\x4f\x00\x02\x00' '\xc6\x0e\x8f\x0c'


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
            'src_cmap': 106766776,
            'mid': 1503617936,
            }
        self.req_bin_0 = '\x50\x00\x03\x00' '\x90\x63\x9f\x59' \
            '\xb8\x21\x5d\x06'


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
            'cmap': 1231141722,
            }
        self.req_bin_0 = '\x51\x00\x02\x00' '\x5a\xbb\x61\x49'


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
            'cmap': 1990418085,
            }
        self.req_bin_0 = '\x52\x00\x02\x00' '\xa5\x5e\xa3\x76'


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
            'window': 1690595117,
            }
        self.req_bin_0 = '\x53\x00\x02\x00' '\x2d\x6f\xc4\x64'

        self.reply_args_0 = {
            'cmaps': [2139546518, 321148655],
            'sequence_number': 30051,
            }
        self.reply_bin_0 = '\x01\x00\x63\x75' '\x02\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x96\xe3\x86\x7f' '\xef\x56\x24\x13'


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
            'red': 35958,
            'green': 65252,
            'cmap': 270055965,
            'blue': 38468,
            }
        self.req_bin_0 = '\x54\x00\x04\x00' '\x1d\xba\x18\x10' \
            '\x76\x8c\xe4\xfe' '\x44\x96\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 58557,
            'red': 30530,
            'green': 2897,
            'pixel': 1644600692,
            'blue': 22274,
            }
        self.reply_bin_0 = '\x01\x00\xbd\xe4' '\x00\x00\x00\x00' \
            '\x42\x77\x51\x0b' '\x02\x57\x00\x00' \
            '\x74\x9d\x06\x62' '\x00\x00\x00\x00' \
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
            'cmap': 1096405321,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x55\x00\x05\x00' '\x49\xd1\x59\x41' \
            '\x07\x00\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 33239,
            'pixel': 29636462,
            'screen_green': 6136,
            'screen_red': 8199,
            'exact_green': 2921,
            'exact_blue': 7386,
            'screen_blue': 61688,
            'exact_red': 47162,
            }
        self.reply_bin_0 = '\x01\x00\xd7\x81' '\x00\x00\x00\x00' \
            '\x6e\x37\xc4\x01' '\x3a\xb8\x69\x0b' \
            '\xda\x1c\x07\x20' '\xf8\x17\xf8\xf0' \
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
            'planes': 10190,
            'colors': 57246,
            'cmap': 1943160776,
            'contiguous': 1,
            }
        self.req_bin_0 = '\x56\x01\x03\x00' '\xc8\x47\xd2\x73' \
            '\x9e\xdf\xce\x27'

        self.reply_args_0 = {
            'masks': [605383893, 629763508, 1549198905],
            'pixels': [775343836, 1977815959, 1899113485, 1237852859, 60402291, 1501499806, 272926930, 1037677730, 480726817, 1705793339, 1475965043, 1042466556, 1178365570, 228717671, 1238906379, 1590872550, 311967592],
            'sequence_number': 54860,
            }
        self.reply_bin_0 = '\x01\x00\x4c\xd6' '\x14\x00\x00\x00' \
            '\x11\x00\x03\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xdc\xce\x36\x2e' '\x97\x13\xe3\x75' \
            '\x0d\x2c\x32\x71' '\xbb\x22\xc8\x49' \
            '\x73\xaa\x99\x03' '\x9e\x11\x7f\x59' \
            '\xd2\x88\x44\x10' '\xa2\xb4\xd9\x3d' \
            '\x21\x4f\xa7\x1c' '\x3b\x57\xac\x65' \
            '\x73\x70\xf9\x57' '\xfc\xc6\x22\x3e' \
            '\x82\x6e\x3c\x46' '\x67\xf4\xa1\x0d' \
            '\x0b\x36\xd8\x49' '\xe6\xc9\xd2\x5e' \
            '\x68\x3f\x98\x12' '\xd5\x6c\x15\x24' \
            '\xb4\x6d\x89\x25' '\x39\xe6\x56\x5c'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 23096,
            }
        self.reply_bin_1 = '\x01\x00\x38\x5a' '\x00\x00\x00\x00' \
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
            'red': 17631,
            'colors': 25352,
            'green': 22528,
            'cmap': 2135012935,
            'contiguous': 1,
            'blue': 45575,
            }
        self.req_bin_0 = '\x57\x01\x04\x00' '\x47\xb6\x41\x7f' \
            '\x08\x63\xdf\x44' '\x00\x58\x07\xb2'

        self.reply_args_0 = {
            'green_mask': 1691817041,
            'sequence_number': 25627,
            'pixels': [60341392, 1384451529, 44659146, 1235187973],
            'blue_mask': 1422726993,
            'red_mask': 508966598,
            }
        self.reply_bin_0 = '\x01\x00\x1b\x64' '\x04\x00\x00\x00' \
            '\x04\x00\x00\x00' '\xc6\x36\x56\x1e' \
            '\x51\x14\xd7\x64' '\x51\x17\xcd\x54' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x90\xbc\x98\x03' '\xc9\x0d\x85\x52' \
            '\xca\x71\xa9\x02' '\x05\x79\x9f\x49'


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
            'cmap': 863176684,
            'pixels': [205462329, 21812143, 338290035, 1176994944, 876041665, 698700577, 331836163, 959610315, 1120922205, 1750723000, 1247640710, 50965176, 1677820270, 1606878681, 261433175, 1630878244, 467555676],
            'plane_mask': 446374417,
            }
        self.req_bin_0 = '\x58\x00\x14\x00' '\xec\x07\x73\x33' \
            '\x11\x22\x9b\x1a' '\x39\x1b\x3f\x0c' \
            '\xaf\xd3\x4c\x01' '\x73\xe5\x29\x14' \
            '\x80\x84\x27\x46' '\xc1\x55\x37\x34' \
            '\x21\x53\xa5\x29' '\x03\x6b\xc7\x13' \
            '\xcb\x7d\x32\x39' '\x5d\xea\xcf\x42' \
            '\xb8\xe9\x59\x68' '\x86\x7c\x5d\x4a' \
            '\xb8\xaa\x09\x03' '\x6e\x81\x01\x64' \
            '\xd9\x05\xc7\x5f' '\x57\x27\x95\x0f' \
            '\x24\x3a\x35\x61' '\x5c\x55\xde\x1b'


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
            'cmap': 654229560,
            'items': [{'red': 13023, 'pixel': 1654610818, 'green': 3380, 'flags': 188, 'blue': 60303}, {'red': 28737, 'pixel': 1642037105, 'green': 10644, 'flags': 168, 'blue': 27555}, {'red': 24034, 'pixel': 1598004397, 'green': 5883, 'flags': 238, 'blue': 25585}, {'red': 32764, 'pixel': 1292176524, 'green': 29839, 'flags': 152, 'blue': 5007}],
            }
        self.req_bin_0 = '\x59\x00\x0e\x00' '\x38\xc0\xfe\x26' \
            '\x82\x5b\x9f\x62' '\xdf\x32\x34\x0d' \
            '\x8f\xeb\xbc\x00' '\x71\x7f\xdf\x61' \
            '\x41\x70\x94\x29' '\xa3\x6b\xa8\x00' \
            '\xad\x9c\x3f\x5f' '\xe2\x5d\xfb\x16' \
            '\xf1\x63\xee\x00' '\x8c\x0c\x05\x4d' \
            '\xfc\x7f\x8f\x74' '\x8f\x13\x98\x00'


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
            'flags': 217,
            'cmap': 357517672,
            'pixel': 884022979,
            }
        self.req_bin_0 = '\x5a\xd9\x05\x00' '\x68\x49\x4f\x15' \
            '\xc3\x1e\xb1\x34' '\x04\x00\x00\x00' \
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
            'cmap': 396716168,
            'pixels': [1092503529, 1060117576, 521059953, 1580106214, 1939278543, 4032639, 1524456491, 328855608],
            }
        self.req_bin_0 = '\x5b\x00\x0a\x00' '\x88\x68\xa5\x17' \
            '\xe9\x47\x1e\x41' '\x48\x1c\x30\x3f' \
            '\x71\xbe\x0e\x1f' '\xe6\x81\x2e\x5e' \
            '\xcf\x0a\x97\x73' '\x7f\x88\x3d\x00' \
            '\x2b\x5c\xdd\x5a' '\x38\xf0\x99\x13'

        self.reply_args_0 = {
            'colors': [{'red': 4250, 'blue': 59417, 'green': 30399}, {'red': 6983, 'blue': 28307, 'green': 8133}, {'red': 59004, 'blue': 37734, 'green': 15765}, {'red': 38870, 'blue': 21119, 'green': 22185}, {'red': 55967, 'blue': 35571, 'green': 10901}],
            'sequence_number': 30501,
            }
        self.reply_bin_0 = '\x01\x00\x25\x77' '\x0a\x00\x00\x00' \
            '\x05\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x9a\x10\xbf\x76' '\x19\xe8\x00\x00' \
            '\x47\x1b\xc5\x1f' '\x93\x6e\x00\x00' \
            '\x7c\xe6\x95\x3d' '\x66\x93\x00\x00' \
            '\xd6\x97\xa9\x56' '\x7f\x52\x00\x00' \
            '\x9f\xda\x95\x2a' '\xf3\x8a\x00\x00'

        self.req_args_1 = {
            'cmap': 1447182765,
            'pixels': [],
            }
        self.req_bin_1 = '\x5b\x00\x02\x00' '\xad\x41\x42\x56'


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
            'cmap': 1635752518,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x5c\x00\x05\x00' '\x46\x9a\x7f\x61' \
            '\x07\x00\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 14192,
            'screen_green': 12609,
            'screen_red': 44158,
            'exact_green': 54085,
            'exact_blue': 41198,
            'screen_blue': 38767,
            'exact_red': 54646,
            }
        self.reply_bin_0 = '\x01\x00\x70\x37' '\x00\x00\x00\x00' \
            '\x76\xd5\x45\xd3' '\xee\xa0\x7e\xac' \
            '\x41\x31\x6f\x97' '\x00\x00\x00\x00' \
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
            'x': 20273,
            'fore_red': 51926,
            'back_green': 13493,
            'mask': 684940609,
            'back_blue': 25150,
            'y': 56176,
            'cid': 276470411,
            'fore_blue': 33524,
            'fore_green': 52699,
            'back_red': 18804,
            'source': 1415607272,
            }
        self.req_bin_0 = '\x5d\x00\x08\x00' '\x8b\x9a\x7a\x10' \
            '\xe8\x73\x60\x54' '\x41\x5d\xd3\x28' \
            '\xd6\xca\xdb\xcd' '\xf4\x82\x74\x49' \
            '\xb5\x34\x3e\x62' '\x31\x4f\x70\xdb'


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
            'fore_red': 54576,
            'source_char': 63131,
            'mask': 909596778,
            'back_blue': 18366,
            'cid': 788244358,
            'mask_char': 16171,
            'fore_blue': 6841,
            'fore_green': 42797,
            'back_red': 61066,
            'source': 33598694,
            'back_green': 14852,
            }
        self.req_bin_0 = '\x5e\x00\x08\x00' '\x86\xa7\xfb\x2e' \
            '\xe6\xac\x00\x02' '\x6a\x58\x37\x36' \
            '\x9b\xf6\x2b\x3f' '\x30\xd5\x2d\xa7' \
            '\xb9\x1a\x8a\xee' '\x04\x3a\xbe\x47'


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
            'cursor': 1114151564,
            }
        self.req_bin_0 = '\x5f\x00\x02\x00' '\x8c\x9a\x68\x42'


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
            'fore_red': 57725,
            'fore_green': 65477,
            'back_blue': 21805,
            'back_green': 5675,
            'fore_blue': 45216,
            'back_red': 40229,
            'cursor': 1488786041,
            }
        self.req_bin_0 = '\x60\x00\x05\x00' '\x79\x12\xbd\x58' \
            '\x7d\xe1\xc5\xff' '\xa0\xb0\x25\x9d' \
            '\x2b\x16\x2d\x55'


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
            'height': 1133,
            'drawable': 1183331241,
            'item_class': 0,
            'width': 64148,
            }
        self.req_bin_0 = '\x61\x00\x03\x00' '\xa9\x33\x88\x46' \
            '\x94\xfa\x6d\x04'

        self.reply_args_0 = {
            'height': 11084,
            'sequence_number': 4106,
            'width': 49945,
            }
        self.reply_bin_0 = '\x01\x00\x0a\x10' '\x00\x00\x00\x00' \
            '\x19\xc3\x4c\x2b' '\x00\x00\x00\x00' \
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
        self.req_bin_0 = '\x62\x00\x03\x00' '\x04\x00\x00\x00' \
            '\x58\x54\x52\x41'

        self.reply_args_0 = {
            'sequence_number': 37561,
            'major_opcode': 183,
            'first_error': 225,
            'present': 1,
            'first_event': 167,
            }
        self.reply_bin_0 = '\x01\x00\xb9\x92' '\x00\x00\x00\x00' \
            '\x01\xb7\xa7\xe1' '\x00\x00\x00\x00' \
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
        self.req_bin_0 = '\x63\x00\x01\x00'

        self.reply_args_0 = {
            'sequence_number': 9109,
            'names': ['XTRA', 'XTRA-II'],
            }
        self.reply_bin_0 = '\x01\x02\x95\x23' '\x04\x00\x00\x00' \
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
            'keysyms': [[1259559628, 2045077316, 2082414925], [1886269034, 752123879, 1768750083], [1471711624, 510617929, 1212393449], [1257382364, 317207541, 746234185], [1308289701, 157817881, 1014220836], [691426599, 1840512545, 1200793127], [246711512, 1161748202, 868218585], [112278118, 1383654285, 443899598], [996155790, 384948073, 1743503362], [745531818, 921111621, 1252700361], [903635808, 1950708131, 556480546], [1861597017, 1744483521, 947502767], [826869818, 2017559748, 1753347994], [1710993019, 1299023394, 1050282398], [772941331, 1414686820, 215942690], [185968993, 471272881, 1632461491], [719371534, 674344255, 1454582773], [294492925, 231410390, 310671464], [1399021756, 598846092, 2013964746], [894657931, 353954485, 1078266175]],
            'first_keycode': 188,
            }
        self.req_bin_0 = '\x64\x14\x3e\x00' '\xbc\x03\x00\x00' \
            '\xcc\x5a\x13\x4b' '\x44\x67\xe5\x79' \
            '\x4d\x21\x1f\x7c' '\x6a\x2e\x6e\x70' \
            '\xe7\x7f\xd4\x2c' '\x03\xfc\x6c\x69' \
            '\x88\x89\xb8\x57' '\x49\x69\x6f\x1e' \
            '\xe9\xa7\x43\x48' '\xdc\x21\xf2\x4a' \
            '\xf5\x33\xe8\x12' '\x49\xa1\x7a\x2c' \
            '\xa5\xea\xfa\x4d' '\x19\x1c\x68\x09' \
            '\x24\xc8\x73\x3c' '\x27\x55\x36\x29' \
            '\x21\xfe\xb3\x6d' '\x27\xa6\x92\x47' \
            '\xd8\x84\xb4\x0e' '\xea\xde\x3e\x45' \
            '\xd9\xf6\xbf\x33' '\x66\x3a\xb1\x06' \
            '\x8d\xe3\x78\x52' '\xce\x5e\x75\x1a' \
            '\x8e\x21\x60\x3b' '\x69\xd7\xf1\x16' \
            '\x02\xc0\xeb\x67' '\xaa\xe9\x6f\x2c' \
            '\x45\x0c\xe7\x36' '\xc9\xb0\xaa\x4a' \
            '\x60\x63\xdc\x35' '\xa3\x71\x45\x74' \
            '\x22\x38\x2b\x21' '\x59\xb7\xf5\x6e' \
            '\xc1\xb4\xfa\x67' '\xaf\xbe\x79\x38' \
            '\x3a\x08\x49\x31' '\xc4\x84\x41\x78' \
            '\x9a\xf7\x81\x68' '\x7b\xae\xfb\x65' \
            '\x22\x86\x6d\x4d' '\x9e\x09\x9a\x3e' \
            '\x13\x26\x12\x2e' '\x64\x68\x52\x54' \
            '\x22\x06\xdf\x0c' '\x61\xa9\x15\x0b' \
            '\xb1\x0d\x17\x1c' '\xb3\x62\x4d\x61' \
            '\x0e\xbd\xe0\x2a' '\x3f\xad\x31\x28' \
            '\xf5\x2b\xb3\x56' '\xfd\x9a\x8d\x11' \
            '\xd6\x0a\xcb\x0d' '\x68\x78\x84\x12' \
            '\xbc\x60\x63\x53' '\x8c\xaa\xb1\x23' \
            '\xca\xa9\x0a\x78' '\x8b\x65\x53\x35' \
            '\xb5\xea\x18\x15' '\x3f\x09\x45\x40'


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
            'count': 161,
            'first_keycode': 139,
            }
        self.req_bin_0 = '\x65\x00\x02\x00' '\x8b\xa1\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[340026412, 1630571412, 1769760540], [2146758935, 1349758610, 1851984613], [232122344, 38033462, 804867143], [1985825334, 1801057060, 272736572], [302016244, 1067544194, 933939692], [561887589, 1873593731, 789656546], [1398218948, 1681731798, 832355113], [934871413, 2074410785, 1067731836], [1166301875, 1579874535, 522625098], [1829247103, 1892229726, 1507878084], [1908217370, 1767204927, 473777454], [893952907, 1860637547, 1182281115], [1481383191, 477325701, 310094541], [1154376029, 399253231, 995349115], [911335712, 544249971, 838785515], [491087365, 1786657572, 1810905978], [1952068086, 1500179024, 1347928336], [1352699442, 831978183, 23264201], [674430661, 974636540, 1734056001], [809886015, 326421325, 440315569]],
            'sequence_number': 12968,
            }
        self.reply_bin_0 = '\x01\x03\xa8\x32' '\x3c\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x2c\x64\x44\x14' '\x94\x8b\x30\x61' \
            '\x1c\x67\x7c\x69' '\x17\xf1\xf4\x7f' \
            '\x92\xae\x73\x50' '\xe5\x0a\x63\x6e' \
            '\xe8\xe7\xd5\x0d' '\x36\x58\x44\x02' \
            '\x47\x4c\xf9\x2f' '\x36\x4a\x5d\x76' \
            '\x24\xf3\x59\x6b' '\x3c\xa1\x41\x10' \
            '\xf4\x66\x00\x12' '\x82\x6e\xa1\x3f' \
            '\xec\xc9\xaa\x37' '\x65\xb9\x7d\x21' \
            '\x83\xc5\xac\x6f' '\xe2\x33\x11\x2f' \
            '\xc4\x20\x57\x53' '\xd6\x30\x3d\x64' \
            '\x29\xbb\x9c\x31' '\x75\x01\xb9\x37' \
            '\x21\xff\xa4\x7b' '\x7c\x4b\xa4\x3f' \
            '\xb3\x5a\x84\x45' '\xe7\xf8\x2a\x5e' \
            '\x4a\xa0\x26\x1f' '\x7f\x18\x08\x6d' \
            '\x5e\x22\xc9\x70' '\xc4\x64\xe0\x59' \
            '\x1a\x16\xbd\x71' '\x3f\x68\x55\x69' \
            '\x2e\x45\x3d\x1c' '\x8b\xa3\x48\x35' \
            '\x6b\x13\xe7\x6e' '\x9b\x2d\x78\x46' \
            '\x17\x1d\x4c\x58' '\x85\x69\x73\x1c' \
            '\xcd\xaa\x7b\x12' '\x5d\x61\xce\x44' \
            '\xef\x1e\xcc\x17' '\x7b\xd2\x53\x3b' \
            '\x20\xe1\x51\x36' '\x73\x98\x70\x20' \
            '\xeb\xd9\xfe\x31' '\x05\x66\x45\x1d' \
            '\x24\x3b\x7e\x6a' '\x7a\x3b\xf0\x6b' \
            '\xf6\x31\x5a\x74' '\x50\xea\x6a\x59' \
            '\x10\xc1\x57\x50' '\x32\x8e\xa0\x50' \
            '\xc7\xfa\x96\x31' '\xc9\xfb\x62\x01' \
            '\xc5\xfe\x32\x28' '\xfc\xc5\x17\x3a' \
            '\x41\x98\x5b\x67' '\x3f\xe1\x45\x30' \
            '\x4d\xcb\x74\x13' '\xb1\xae\x3e\x1a'


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
            'attrs': {'key_click_percent': -63, 'bell_percent': -68, 'led_mode': 1, 'bell_pitch': -15086, 'auto_repeat_mode': 0, 'bell_duration': -28062, 'key': 133, 'led': 131},
            }
        self.req_bin_0 = '\x66\x00\x0a\x00' '\xff\x00\x00\x00' \
            '\xc1\x00\x00\x00' '\xbc\x00\x00\x00' \
            '\x12\xc5\x00\x00' '\x62\x92\x00\x00' \
            '\x83\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x85\x00\x00\x00' '\x00\x00\x00\x00'


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
        self.req_bin_0 = '\x67\x00\x01\x00'

        self.reply_args_0 = {
            'key_click_percent': 182,
            'sequence_number': 12165,
            'bell_percent': 241,
            'bell_pitch': 64707,
            'auto_repeats': [619618602, 2076087657, 531932829, 1160344334, 566327280, 1384248226, 1157363212, 589174356],
            'global_auto_repeat': 1,
            'led_mask': 1600144822,
            'bell_duration': 35319,
            }
        self.reply_bin_0 = '\x01\x01\x85\x2f' '\x05\x00\x00\x00' \
            '\xb6\x45\x60\x5f' '\xb6\xf1\xc3\xfc' \
            '\xf7\x89\x00\x00' '\x2a\xa1\xee\x24' \
            '\x69\x95\xbe\x7b' '\x9d\xa6\xb4\x1f' \
            '\x0e\x73\x29\x45' '\xf0\x77\xc1\x21' \
            '\xa2\xf3\x81\x52' '\x0c\xf6\xfb\x44' \
            '\x54\x16\x1e\x23'


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
            'percent': -30,
            }
        self.req_bin_0 = '\x68\xe2\x01\x00'


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
            'accel_denum': -12186,
            'accel_num': -15024,
            'do_accel': 0,
            'do_thresh': 1,
            'threshold': -26305,
            }
        self.req_bin_0 = '\x69\x00\x03\x00' '\x50\xc5\x66\xd0' \
            '\x3f\x99\x00\x01'


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
        self.req_bin_0 = '\x6a\x00\x01\x00'

        self.reply_args_0 = {
            'accel_denom': 23075,
            'sequence_number': 27063,
            'threshold': 57114,
            'accel_num': 33257,
            }
        self.reply_bin_0 = '\x01\x00\xb7\x69' '\x00\x00\x00\x00' \
            '\xe9\x81\x23\x5a' '\x1a\xdf\x00\x00' \
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
            'allow_exposures': 1,
            'timeout': -7644,
            'interval': -17410,
            'prefer_blank': 1,
            }
        self.req_bin_0 = '\x6b\x00\x03\x00' '\x24\xe2\xfe\xbb' \
            '\x01\x01\x00\x00'


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
        self.req_bin_0 = '\x6c\x00\x01\x00'

        self.reply_args_0 = {
            'allow_exposures': 1,
            'timeout': 5428,
            'sequence_number': 34852,
            'prefer_blanking': 0,
            'interval': 16009,
            }
        self.reply_bin_0 = '\x01\x00\x24\x88' '\x00\x00\x00\x00' \
            '\x34\x15\x89\x3e' '\x00\x01\x00\x00' \
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
            'host': [165, 163, 173, 145],
            'mode': 0,
            'host_family': 0,
            }
        self.req_bin_0 = '\x6d\x00\x03\x00' '\x00\x00\x04\x00' \
            '\xa5\xa3\xad\x91'


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
        self.req_bin_0 = '\x6e\x00\x01\x00'

        self.reply_args_0 = {
            'sequence_number': 49541,
            'mode': 1,
            'hosts': [{'family': 0, 'name': [34, 23, 178, 12]}, {'family': 0, 'name': [130, 236, 254, 15]}],
            }
        self.reply_bin_0 = '\x01\x01\x85\xc1' '\x04\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x04\x00' '\x22\x17\xb2\x0c' \
            '\x00\x00\x04\x00' '\x82\xec\xfe\x0f'


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
            'mode': 1,
            }
        self.req_bin_0 = '\x6f\x01\x01\x00'


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
            'mode': 2,
            }
        self.req_bin_0 = '\x70\x02\x01\x00'


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
            'resource': 1991754710,
            }
        self.req_bin_0 = '\x71\x00\x02\x00' '\xd6\xc3\xb7\x76'


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
            'delta': -31772,
            'window': 1131700021,
            'properties': [791050288, 1563425156, 224264387, 365085741, 337754145, 721831946, 1031915232, 433424990, 1269947187, 1002483222, 629908045, 486189648],
            }
        self.req_bin_0 = '\x72\x00\x0f\x00' '\x35\x5f\x74\x43' \
            '\x0c\x00\xe4\x83' '\x30\x78\x26\x2f' \
            '\x84\xf9\x2f\x5d' '\xc3\x00\x5e\x0d' \
            '\x2d\xc4\xc2\x15' '\x21\xb8\x21\x14' \
            '\x0a\x48\x06\x2b' '\xe0\xc6\x81\x3d' \
            '\x5e\x8a\xd5\x19' '\x33\xdb\xb1\x4b' \
            '\x16\xae\xc0\x3b' '\x4d\xa2\x8b\x25' \
            '\x50\xaa\xfa\x1c'


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
        self.req_bin_0 = '\x73\x01\x01\x00'


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
            'map': [198, 195, 239, 220, 240],
            }
        self.req_bin_0 = '\x74\x05\x03\x00' '\xc6\xc3\xef\xdc' \
            '\xf0\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 29620,
            'status': 239,
            }
        self.reply_bin_0 = '\x01\xef\xb4\x73' '\x00\x00\x00\x00' \
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
        self.req_bin_0 = '\x75\x00\x01\x00'

        self.reply_args_0 = {
            'sequence_number': 16491,
            'map': [131, 228, 230, 138, 131],
            }
        self.reply_bin_0 = '\x01\x05\x6b\x40' '\x02\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x83\xe4\xe6\x8a' '\x83\x00\x00\x00'


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
            'keycodes': [[173, 125], [102, 101], [211, 25], [186, 207], [22, 57], [100, 62], [66, 24], [19, 128]],
            }
        self.req_bin_0 = '\x76\x02\x05\x00' '\xad\x7d\x66\x65' \
            '\xd3\x19\xba\xcf' '\x16\x39\x64\x3e' \
            '\x42\x18\x13\x80'

        self.reply_args_0 = {
            'sequence_number': 52060,
            'status': 240,
            }
        self.reply_bin_0 = '\x01\xf0\x5c\xcb' '\x00\x00\x00\x00' \
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
        self.req_bin_0 = '\x77\x00\x01\x00'

        self.reply_args_0 = {
            'sequence_number': 16181,
            'keycodes': [[160, 0], [147, 203], [251, 151], [232, 140], [49, 117], [249, 213], [34, 8], [72, 2]],
            }
        self.reply_bin_0 = '\x01\x02\x35\x3f' '\x04\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xa0\x00\x93\xcb' '\xfb\x97\xe8\x8c' \
            '\x31\x75\xf9\xd5' '\x22\x08\x48\x02'


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
        self.req_bin_0 = '\x7f\x00\x01\x00'


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
