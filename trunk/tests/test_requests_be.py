# Generated from gen/genprottest.py

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import string
import unittest
from Xlib.protocol import request, rq
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
            'height': 51338,
            'window_class': 1,
            'border_width': 57105,
            'visual': 752631105,
            'x': -2545,
            'y': -14158,
            'parent': 1434984674,
            'attrs': {'backing_pixel': 306331523, 'cursor': 1515266104, 'background_pixmap': 1333812131, 'border_pixmap': 1586014551, 'backing_planes': 2030508603, 'win_gravity': 2, 'backing_store': 1, 'event_mask': 576213620, 'save_under': 1, 'background_pixel': 1563170937, 'colormap': 996932493, 'border_pixel': 936741754, 'bit_gravity': 2, 'do_not_propagate_mask': 746538325, 'override_redirect': 1},
            'wid': 1011816541,
            'depth': 168,
            'width': 50328,
            }
        self.req_bin_0 = '\x01\xa8\x00\x17' '\x3c\x4f\x18\x5d' \
            '\x55\x88\x20\xe2' '\xf6\x0f\xc8\xb2' \
            '\xc4\x98\xc8\x8a' '\xdf\x11\x00\x01' \
            '\x2c\xdc\x3d\x41' '\x00\x00\x7f\xff' \
            '\x4f\x80\x5b\xa3' '\x5d\x2c\x18\x79' \
            '\x5e\x88\xa9\x57' '\x37\xd5\x8b\x7a' \
            '\x02\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x79\x07\x1a\x3b' \
            '\x12\x42\x3f\x83' '\x01\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x22\x58\x52\x74' \
            '\x2c\x7f\x45\x55' '\x3b\x6b\xfb\x8d' \
            '\x5a\x51\x20\x38'


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
            'window': 900699353,
            'attrs': {'backing_pixel': 1025011957, 'cursor': 376028564, 'background_pixmap': 1825900315, 'border_pixmap': 1764328047, 'backing_planes': 1530715389, 'win_gravity': 9, 'backing_store': 0, 'event_mask': 1385455374, 'save_under': 1, 'background_pixel': 441245965, 'colormap': 409081122, 'border_pixel': 1870963440, 'bit_gravity': 6, 'do_not_propagate_mask': 1963538952, 'override_redirect': 1},
            }
        self.req_bin_0 = '\x02\x00\x00\x12' '\x35\xaf\x94\xd9' \
            '\x00\x00\x7f\xff' '\x6c\xd5\x07\x1b' \
            '\x1a\x4c\xe1\x0d' '\x69\x29\x82\x6f' \
            '\x6f\x84\xa2\xf0' '\x06\x00\x00\x00' \
            '\x09\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x5b\x3c\xdc\xfd' '\x3d\x18\x70\xf5' \
            '\x01\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x52\x94\x5f\x0e' '\x75\x09\x3a\x08' \
            '\x18\x62\x15\x22' '\x16\x69\xbd\x94'


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
            'window': 802445789,
            }
        self.req_bin_0 = '\x03\x00\x00\x02' '\x2f\xd4\x59\xdd'

        self.reply_args_0 = {
            'sequence_number': 24431,
            'backing_pixel': 443696070,
            'your_event_mask': 1330874192,
            'map_is_installed': 0,
            'visual': 1141631654,
            'backing_bit_planes': 21271777,
            'backing_store': 212,
            'win_class': 4961,
            'map_state': 161,
            'save_under': 0,
            'all_event_masks': 1205017274,
            'colormap': 1039354343,
            'win_gravity': 215,
            'bit_gravity': 179,
            'do_not_propagate_mask': 44926,
            'override_redirect': 1,
            }
        self.reply_bin_0 = '\x01\xd4\x5f\x6f' '\x00\x00\x00\x03' \
            '\x44\x0b\xea\xa6' '\x13\x61\xb3\xd7' \
            '\x01\x44\x94\xe1' '\x1a\x72\x43\xc6' \
            '\x00\x00\xa1\x01' '\x3d\xf3\x49\xe7' \
            '\x47\xd3\x1a\xba' '\x4f\x53\x87\x50' \
            '\xaf\x7e\x00\x00'


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
            'window': 1032398604,
            }
        self.req_bin_0 = '\x04\x00\x00\x02' '\x3d\x89\x27\x0c'


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
            'window': 1885148304,
            }
        self.req_bin_0 = '\x05\x00\x00\x02' '\x70\x5d\x14\x90'


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
            'window': 1755736476,
            'mode': 0,
            }
        self.req_bin_0 = '\x06\x00\x00\x02' '\x68\xa6\x69\x9c'


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
            'parent': 492772504,
            'window': 331868391,
            'x': -1279,
            'y': -24108,
            }
        self.req_bin_0 = '\x07\x00\x00\x04' '\x13\xc7\xe8\xe7' \
            '\x1d\x5f\x1c\x98' '\xfb\x01\xa1\xd4'


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
            'window': 1867478418,
            }
        self.req_bin_0 = '\x08\x00\x00\x02' '\x6f\x4f\x75\x92'


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
            'window': 2146520940,
            }
        self.req_bin_0 = '\x09\x00\x00\x02' '\x7f\xf1\x4f\x6c'


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
            'window': 1541697409,
            }
        self.req_bin_0 = '\x0a\x00\x00\x02' '\x5b\xe4\x6f\x81'


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
            'window': 1117951845,
            }
        self.req_bin_0 = '\x0b\x00\x00\x02' '\x42\xa2\x97\x65'


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
            'window': 1266259436,
            'attrs': {'height': 46201, 'stack_mode': 3, 'border_width': -22847, 'width': 49410, 'x': -4914, 'y': -29358, 'sibling': 1025509288},
            }
        self.req_bin_0 = '\x0c\x00\x00\x0a' '\x4b\x79\x95\xec' \
            '\x00\x7f\x00\x00' '\xec\xce\x00\x00' \
            '\x8d\x52\x00\x00' '\xc1\x02\x00\x00' \
            '\xb4\x79\x00\x00' '\xa6\xc1\x00\x00' \
            '\x3d\x20\x07\xa8' '\x03\x00\x00\x00'


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
            'window': 2133193809,
            'direction': 0,
            }
        self.req_bin_0 = '\x0d\x00\x00\x02' '\x7f\x25\xf4\x51'


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
            'drawable': 696248119,
            }
        self.req_bin_0 = '\x0e\x00\x00\x02' '\x29\x7f\xe7\x37'

        self.reply_args_0 = {
            'height': 56899,
            'sequence_number': 2462,
            'root': 952445564,
            'border_width': 22864,
            'x': -32041,
            'y': -2637,
            'depth': 164,
            'width': 46912,
            }
        self.reply_bin_0 = '\x01\xa4\x09\x9e' '\x00\x00\x00\x00' \
            '\x38\xc5\x2a\x7c' '\x82\xd7\xf5\xb3' \
            '\xb7\x40\xde\x43' '\x59\x50\x00\x00' \
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
            'window': 926736833,
            }
        self.req_bin_0 = '\x0f\x00\x00\x02' '\x37\x3c\xe1\xc1'

        self.reply_args_0 = {
            'sequence_number': 28744,
            'children': [905163556, 1981308517, 1963355964, 2114530966, 460310351, 1897180607, 679524415],
            'root': 777151598,
            'parent': 505482186,
            }
        self.reply_bin_0 = '\x01\x00\x70\x48' '\x00\x00\x00\x07' \
            '\x2e\x52\x64\x6e' '\x1e\x21\x0b\xca' \
            '\x00\x07\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x35\xf3\xb3\x24' '\x76\x18\x5e\x65' \
            '\x75\x06\x6f\x3c' '\x7e\x09\x2e\x96' \
            '\x1b\x6f\xc7\x4f' '\x71\x14\xad\xbf' \
            '\x28\x80\xb8\x3f'


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
            'atom': 2065326993,
            'sequence_number': 22018,
            }
        self.reply_bin_0 = '\x01\x00\x56\x02' '\x00\x00\x00\x00' \
            '\x7b\x1a\x63\x91' '\x00\x00\x00\x00' \
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
            'atom': 452215613,
            }
        self.req_bin_0 = '\x11\x00\x00\x02' '\x1a\xf4\x43\x3d'

        self.reply_args_0 = {
            'sequence_number': 55994,
            'name': 'WM_CLASS',
            }
        self.reply_bin_0 = '\x01\x00\xda\xba' '\x00\x00\x00\x02' \
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
            'mode': 1,
            'data': (8, ''),
            'property': 1037137716,
            'window': 1579797457,
            'type': 1100848920,
            }
        self.req_bin_0 = '\x12\x01\x00\x06' '\x5e\x29\xcb\xd1' \
            '\x3d\xd1\x77\x34' '\x41\x9d\x9f\x18' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_1 = {
            'mode': 0,
            'data': (8, 'foo'),
            'property': 1826307390,
            'window': 1095034524,
            'type': 1843579373,
            }
        self.req_bin_1 = '\x12\x00\x00\x07' '\x41\x44\xe6\x9c' \
            '\x6c\xdb\x3d\x3e' '\x6d\xe2\xc9\xed' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x03' \
            '\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'mode': 2,
            'data': (8, 'zoom'),
            'property': 182591666,
            'window': 1793889783,
            'type': 283681296,
            }
        self.req_bin_2 = '\x12\x02\x00\x07' '\x6a\xec\x95\xf7' \
            '\x0a\xe2\x20\xb2' '\x10\xe8\xa2\x10' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x04' \
            '\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'mode': 2,
            'data': (16, []),
            'property': 1444352960,
            'window': 1084189409,
            'type': 454569933,
            }
        self.req_bin_3 = '\x12\x02\x00\x06' '\x40\x9f\x6a\xe1' \
            '\x56\x17\x13\xc0' '\x1b\x18\x2f\xcd' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_4 = {
            'mode': 0,
            'data': (16, [1, 2, 3]),
            'property': 2145146806,
            'window': 1444199760,
            'type': 397338770,
            }
        self.req_bin_4 = '\x12\x00\x00\x08' '\x56\x14\xbd\x50' \
            '\x7f\xdc\x57\xb6' '\x17\xae\xe8\x92' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x03' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x00'

        self.req_args_5 = {
            'mode': 2,
            'data': (16, [1, 2, 3, 4]),
            'property': 1581561698,
            'window': 682054712,
            'type': 955890910,
            }
        self.req_bin_5 = '\x12\x02\x00\x08' '\x28\xa7\x54\x38' \
            '\x5e\x44\xb7\x62' '\x38\xf9\xbc\xde' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x04' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x04'

        self.req_args_6 = {
            'mode': 0,
            'data': (32, []),
            'property': 2123317134,
            'window': 881316175,
            'type': 1430614889,
            }
        self.req_bin_6 = '\x12\x00\x00\x06' '\x34\x87\xd1\x4f' \
            '\x7e\x8f\x3f\x8e' '\x55\x45\x73\x69' \
            '\x20\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_7 = {
            'mode': 1,
            'data': (32, [1, 2, 3]),
            'property': 973487784,
            'window': 1673574881,
            'type': 1949457396,
            }
        self.req_bin_7 = '\x12\x01\x00\x09' '\x63\xc0\xb9\xe1' \
            '\x3a\x06\x3e\xa8' '\x74\x32\x5b\xf4' \
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
            'property': 248805346,
            'window': 163983810,
            }
        self.req_bin_0 = '\x13\x00\x00\x03' '\x09\xc6\x31\xc2' \
            '\x0e\xd4\x77\xe2'


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
            'delete': 1,
            'long_offset': 1019840159,
            'type': 537212214,
            'property': 1073732159,
            'window': 613204515,
            'long_length': 822862740,
            }
        self.req_bin_0 = '\x14\x01\x00\x06' '\x24\x8c\xc2\x23' \
            '\x3f\xff\xda\x3f' '\x20\x05\x35\x36' \
            '\x3c\xc9\x86\x9f' '\x31\x0b\xe3\x94'

        self.reply_args_0 = {
            'value': (8, ''),
            'sequence_number': 1789,
            'property_type': 152803832,
            'bytes_after': 548296802,
            }
        self.reply_bin_0 = '\x01\x08\x06\xfd' '\x00\x00\x00\x00' \
            '\x09\x1b\x99\xf8' '\x20\xae\x58\x62' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_1 = {
            'value': (8, 'foo'),
            'sequence_number': 59751,
            'property_type': 1209491492,
            'bytes_after': 212145538,
            }
        self.reply_bin_1 = '\x01\x08\xe9\x67' '\x00\x00\x00\x01' \
            '\x48\x17\x60\x24' '\x0c\xa5\x15\x82' \
            '\x00\x00\x00\x03' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'value': (8, 'zoom'),
            'sequence_number': 15933,
            'property_type': 942383785,
            'bytes_after': 1723485239,
            }
        self.reply_bin_2 = '\x01\x08\x3e\x3d' '\x00\x00\x00\x01' \
            '\x38\x2b\xa2\xa9' '\x66\xba\x4c\x37' \
            '\x00\x00\x00\x04' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'value': (16, []),
            'sequence_number': 57250,
            'property_type': 808142608,
            'bytes_after': 586346923,
            }
        self.reply_bin_3 = '\x01\x10\xdf\xa2' '\x00\x00\x00\x00' \
            '\x30\x2b\x47\x10' '\x22\xf2\xf1\xab' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_4 = {
            'value': (16, [1, 2, 3]),
            'sequence_number': 23088,
            'property_type': 772905710,
            'bytes_after': 1245363938,
            }
        self.reply_bin_4 = '\x01\x10\x5a\x30' '\x00\x00\x00\x02' \
            '\x2e\x11\x9a\xee' '\x4a\x3a\xbe\xe2' \
            '\x00\x00\x00\x03' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x00'

        self.reply_args_5 = {
            'value': (16, [1, 2, 3, 4]),
            'sequence_number': 17427,
            'property_type': 1247474802,
            'bytes_after': 1700932739,
            }
        self.reply_bin_5 = '\x01\x10\x44\x13' '\x00\x00\x00\x02' \
            '\x4a\x5a\xf4\x72' '\x65\x62\x2c\x83' \
            '\x00\x00\x00\x04' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x01\x00\x02' '\x00\x03\x00\x04'

        self.reply_args_6 = {
            'value': (32, []),
            'sequence_number': 37330,
            'property_type': 1806138978,
            'bytes_after': 1076250502,
            }
        self.reply_bin_6 = '\x01\x20\x91\xd2' '\x00\x00\x00\x00' \
            '\x6b\xa7\x7e\x62' '\x40\x26\x47\x86' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_7 = {
            'value': (32, [1, 2, 3]),
            'sequence_number': 53218,
            'property_type': 992987434,
            'bytes_after': 2074141973,
            }
        self.reply_bin_7 = '\x01\x20\xcf\xe2' '\x00\x00\x00\x03' \
            '\x3b\x2f\xc9\x2a' '\x7b\xa0\xe5\x15' \
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
            'window': 1964015558,
            }
        self.req_bin_0 = '\x15\x00\x00\x02' '\x75\x10\x7f\xc6'

        self.reply_args_0 = {
            'atoms': [1448505190, 476170857, 1313060969, 86239836, 1127972202, 1511570929, 47083026, 1642958244, 222290678, 616254102, 681054438, 1175305449, 934061085, 1091424709, 142977025, 1606118685, 443665559, 601648607, 1247949855, 48593928, 483888993, 440980669, 1007774206],
            'sequence_number': 1423,
            }
        self.reply_bin_0 = '\x01\x00\x05\x8f' '\x00\x00\x00\x17' \
            '\x00\x17\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x56\x56\x6f\x66' '\x1c\x61\xca\x69' \
            '\x4e\x43\xb8\x69' '\x05\x23\xea\x5c' \
            '\x43\x3b\x7d\x6a' '\x5a\x18\xbd\xf1' \
            '\x02\xce\x6e\x12' '\x61\xed\x8d\xa4' \
            '\x0d\x3f\xe2\xf6' '\x24\xbb\x4a\x96' \
            '\x28\x98\x10\xe6' '\x46\x0d\xbc\xe9' \
            '\x37\xac\xa4\x1d' '\x41\x0d\xd1\xc5' \
            '\x08\x85\xa8\x01' '\x5f\xbb\x6d\x1d' \
            '\x1a\x71\xcc\x97' '\x23\xdc\x6d\xdf' \
            '\x4a\x62\x34\x1f' '\x02\xe5\x7c\x08' \
            '\x1c\xd7\x8f\x61' '\x1a\x48\xd4\xbd' \
            '\x3c\x11\x69\xfe'


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
            'selection': 40873095,
            'window': 801285939,
            'time': 1156133883,
            }
        self.req_bin_0 = '\x16\x00\x00\x04' '\x2f\xc2\xa7\x33' \
            '\x02\x6f\xac\x87' '\x44\xe9\x33\xfb'


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
            'selection': 1432924899,
            }
        self.req_bin_0 = '\x17\x00\x00\x02' '\x55\x68\xb2\xe3'

        self.reply_args_0 = {
            'sequence_number': 5826,
            'owner': 1171450638,
            }
        self.reply_bin_0 = '\x01\x00\x16\xc2' '\x00\x00\x00\x00' \
            '\x45\xd2\xeb\x0e' '\x00\x00\x00\x00' \
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
            'property': 1836047090,
            'time': 2128742728,
            'target': 1971925603,
            'selection': 278928673,
            'requestor': 1784331242,
            }
        self.req_bin_0 = '\x18\x00\x00\x06' '\x6a\x5a\xbb\xea' \
            '\x10\xa0\x1d\x21' '\x75\x89\x32\x63' \
            '\x6d\x6f\xda\xf2' '\x7e\xe2\x09\x48'


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
            'event': Xlib.protocol.event.Expose(height = 15231, sequence_number = 0, type = 12, x = 64311, y = 34568, window = 71584977, width = 52927, count = 39405),
            'propagate': 0,
            'destination': 1327311518,
            'event_mask': 96477203,
            }
        self.req_bin_0 = '\x19\x00\x00\x0b' '\x4f\x1d\x2a\x9e' \
            '\x05\xc0\x20\x13' '\x0c\x00\x00\x00' \
            '\x04\x44\x4c\xd1' '\xfb\x37\x87\x08' \
            '\xce\xbf\x3b\x7f' '\x99\xed\x00\x00' \
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
            'grab_window': 607755184,
            'confine_to': 1395242985,
            'event_mask': 33902,
            'pointer_mode': 1,
            'time': 2111367756,
            'keyboard_mode': 0,
            'cursor': 1984189421,
            }
        self.req_bin_0 = '\x1a\x00\x00\x06' '\x24\x39\x9b\xb0' \
            '\x84\x6e\x01\x00' '\x53\x29\xb7\xe9' \
            '\x76\x44\x53\xed' '\x7d\xd8\xea\x4c'

        self.reply_args_0 = {
            'sequence_number': 63225,
            'status': 217,
            }
        self.reply_bin_0 = '\x01\xd9\xf6\xf9' '\x00\x00\x00\x00' \
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
            'time': 165427532,
            }
        self.req_bin_0 = '\x1b\x00\x00\x02' '\x09\xdc\x39\x4c'


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
            'owner_events': 0,
            'grab_window': 1656778032,
            'confine_to': 1852999245,
            'event_mask': 7760,
            'pointer_mode': 1,
            'modifiers': 56764,
            'button': 212,
            'keyboard_mode': 1,
            'cursor': 499754188,
            }
        self.req_bin_0 = '\x1c\x00\x00\x06' '\x62\xc0\x6d\x30' \
            '\x1e\x50\x01\x01' '\x6e\x72\x86\x4d' \
            '\x1d\xc9\xa4\xcc' '\xd4\x00\xdd\xbc'


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
            'grab_window': 1047705334,
            'button': 251,
            'modifiers': 35716,
            }
        self.req_bin_0 = '\x1d\xfb\x00\x03' '\x3e\x72\xb6\xf6' \
            '\x8b\x84\x00\x00'


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
            'time': 2114321987,
            'event_mask': 39111,
            'cursor': 1289913603,
            }
        self.req_bin_0 = '\x1e\x00\x00\x04' '\x4c\xe2\x85\x03' \
            '\x7e\x05\xfe\x43' '\x98\xc7\x00\x00'


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
            'grab_window': 371263215,
            'time': 729368827,
            'pointer_mode': 0,
            'keyboard_mode': 1,
            }
        self.req_bin_0 = '\x1f\x00\x00\x04' '\x16\x21\x06\xef' \
            '\x2b\x79\x48\xfb' '\x00\x01\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 20466,
            'status': 198,
            }
        self.reply_bin_0 = '\x01\xc6\x4f\xf2' '\x00\x00\x00\x00' \
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
            'time': 1130279738,
            }
        self.req_bin_0 = '\x20\x00\x00\x02' '\x43\x5e\xb3\x3a'


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
            'grab_window': 1229207347,
            'pointer_mode': 1,
            'keyboard_mode': 1,
            'modifiers': 40890,
            'key': 148,
            }
        self.req_bin_0 = '\x21\x00\x00\x04' '\x49\x44\x37\x33' \
            '\x9f\xba\x94\x01' '\x01\x00\x00\x00'


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
            'grab_window': 1205656398,
            'key': 151,
            'modifiers': 40447,
            }
        self.req_bin_0 = '\x22\x97\x00\x03' '\x47\xdc\xdb\x4e' \
            '\x9d\xff\x00\x00'


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
            'time': 1640130566,
            'mode': 5,
            }
        self.req_bin_0 = '\x23\x05\x00\x02' '\x61\xc2\x68\x06'


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
            'window': 1222670706,
            }
        self.req_bin_0 = '\x26\x00\x00\x02' '\x48\xe0\x79\x72'

        self.reply_args_0 = {
            'win_y': -26803,
            'same_screen': 0,
            'sequence_number': 40848,
            'root': 1255370704,
            'root_x': -28425,
            'root_y': -11688,
            'mask': 41671,
            'child': 1712001679,
            'win_x': -12376,
            }
        self.reply_bin_0 = '\x01\x00\x9f\x90' '\x00\x00\x00\x00' \
            '\x4a\xd3\x6f\xd0' '\x66\x0b\x12\x8f' \
            '\x90\xf7\xd2\x58' '\xcf\xa8\x97\x4d' \
            '\xa2\xc7\x00\x00' '\x00\x00\x00\x00'


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
            'window': 540661757,
            'start': 2109370140,
            'stop': 1637006627,
            }
        self.req_bin_0 = '\x27\x00\x00\x04' '\x20\x39\xd7\xfd' \
            '\x7d\xba\x6f\x1c' '\x61\x92\xbd\x23'

        self.reply_args_0 = {
            'sequence_number': 8755,
            'events': [{'time': 286903636, 'x': -27529, 'y': -12290}, {'time': 1306580447, 'x': -6191, 'y': -31441}, {'time': 1989739523, 'x': -23403, 'y': -11091}, {'time': 1563081363, 'x': -28619, 'y': -2487}, {'time': 1322577500, 'x': -21541, 'y': -15337}],
            }
        self.reply_bin_0 = '\x01\x00\x22\x33' '\x00\x00\x00\x0a' \
            '\x00\x00\x00\x05' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x11\x19\xcd\x54' '\x94\x77\xcf\xfe' \
            '\x4d\xe0\xd5\xdf' '\xe7\xd1\x85\x2f' \
            '\x76\x99\x04\x03' '\xa4\x95\xd4\xad' \
            '\x5d\x2a\xba\x93' '\x90\x35\xf6\x49' \
            '\x4e\xd4\xee\x5c' '\xab\xdb\xc4\x17'


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
            'src_y': -30143,
            'src_x': -18331,
            'src_wid': 376276259,
            'dst_wid': 253341128,
            }
        self.req_bin_0 = '\x28\x00\x00\x04' '\x16\x6d\x85\x23' \
            '\x0f\x19\xad\xc8' '\xb8\x65\x8a\x41'

        self.reply_args_0 = {
            'child': 431023944,
            'same_screen': 1,
            'sequence_number': 8040,
            'x': -25540,
            'y': -7648,
            }
        self.reply_bin_0 = '\x01\x01\x1f\x68' '\x00\x00\x00\x00' \
            '\x19\xb0\xe7\x48' '\x9c\x3c\xe2\x20' \
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
            'src_height': 53950,
            'src_window': 249819173,
            'dst_window': 1408887199,
            'src_width': 37413,
            'src_y': -28935,
            'src_x': -2597,
            'dst_x': -22353,
            'dst_y': -2907,
            }
        self.req_bin_0 = '\x29\x00\x00\x06' '\x0e\xe3\xf0\x25' \
            '\x53\xf9\xe9\x9f' '\xf5\xdb\x8e\xf9' \
            '\x92\x25\xd2\xbe' '\xa8\xaf\xf4\xa5'


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
            'time': 1024986488,
            'focus': 140695377,
            }
        self.req_bin_0 = '\x2a\x00\x00\x03' '\x08\x62\xd7\x51' \
            '\x3d\x18\x0d\x78'


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
            'revert_to': 221,
            'sequence_number': 14149,
            'focus': 1304519908,
            }
        self.reply_bin_0 = '\x01\xdd\x37\x45' '\x00\x00\x00\x00' \
            '\x4d\xc1\x64\xe4' '\x00\x00\x00\x00' \
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
            'sequence_number': 11636,
            'map': [197, 252, 218, 253, 151, 253, 222, 169, 233, 128, 224, 204, 154, 181, 152, 255, 226, 140, 189, 128, 197, 244, 251, 221, 151, 138, 130, 182, 254, 162, 144, 197],
            }
        self.reply_bin_0 = '\x01\x00\x2d\x74' '\x00\x00\x00\x02' \
            '\xc5\xfc\xda\xfd' '\x97\xfd\xde\xa9' \
            '\xe9\x80\xe0\xcc' '\x9a\xb5\x98\xff' \
            '\xe2\x8c\xbd\x80' '\xc5\xf4\xfb\xdd' \
            '\x97\x8a\x82\xb6' '\xfe\xa2\x90\xc5'


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
            'fid': 229736695,
            'name': 'foofont',
            }
        self.req_bin_0 = '\x2d\x00\x00\x05' '\x0d\xb1\x80\xf7' \
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
            'font': 566055567,
            }
        self.req_bin_0 = '\x2e\x00\x00\x02' '\x21\xbd\x52\x8f'


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
            'font': 1912111384,
            }
        self.req_bin_0 = '\x2f\x00\x00\x02' '\x71\xf8\x81\x18'

        self.reply_args_0 = {
            'sequence_number': 12196,
            'properties': [{'value': 1129396189, 'name': 1124333300}],
            'min_byte1': 211,
            'max_byte1': 209,
            'char_infos': [{'descent': -30573, 'ascent': -15524, 'character_width': -16338, 'left_side_bearing': -13196, 'right_side_bearing': -20508, 'attributes': 12473}, {'descent': -550, 'ascent': -7909, 'character_width': -30130, 'left_side_bearing': -19839, 'right_side_bearing': -13225, 'attributes': 37544}, {'descent': -28260, 'ascent': -27136, 'character_width': -22577, 'left_side_bearing': -29461, 'right_side_bearing': -20564, 'attributes': 60557}],
            'max_char_or_byte2': 60865,
            'default_char': 45294,
            'min_char_or_byte2': 21091,
            'draw_direction': 167,
            'min_bounds': {'descent': -9281, 'ascent': -2945, 'character_width': -21203, 'left_side_bearing': -7808, 'right_side_bearing': -16678, 'attributes': 60085},
            'all_chars_exist': 1,
            'font_ascent': -19929,
            'font_descent': -20541,
            'max_bounds': {'descent': -9632, 'ascent': -3680, 'character_width': -1632, 'left_side_bearing': -5741, 'right_side_bearing': -3544, 'attributes': 13262},
            }
        self.reply_bin_0 = '\x01\x00\x2f\xa4' '\x00\x00\x00\x12' \
            '\xe1\x80\xbe\xda' '\xad\x2d\xf4\x7f' \
            '\xdb\xbf\xea\xb5' '\x00\x00\x00\x00' \
            '\xe9\x93\xf2\x28' '\xf9\xa0\xf1\xa0' \
            '\xda\x60\x33\xce' '\x00\x00\x00\x00' \
            '\x52\x63\xed\xc1' '\xb0\xee\x00\x01' \
            '\xa7\xd3\xd1\x01' '\xb2\x27\xaf\xc3' \
            '\x00\x00\x00\x03' '\x43\x03\xf6\xf4' \
            '\x43\x51\x37\xdd' '\xcc\x74\xaf\xe4' \
            '\xc0\x2e\xc3\x5c' '\x88\x93\x30\xb9' \
            '\xb2\x81\xcc\x57' '\x8a\x4e\xe1\x1b' \
            '\xfd\xda\x92\xa8' '\x8c\xeb\xaf\xac' \
            '\xa7\xcf\x96\x00' '\x91\x9c\xec\x8d'


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
            'font': 792714047,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = '\x30\x01\x00\x04' '\x2f\x3f\xdb\x3f' \
            '\x00\x66\x00\x6f' '\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'overall_width': -1876385586,
            'draw_direction': 205,
            'sequence_number': 15421,
            'font_ascent': -2134,
            'overall_ascent': -8363,
            'overall_descent': -24649,
            'overall_right': -2054818235,
            'overall_left': -1218715126,
            'font_descent': -15670,
            }
        self.reply_bin_0 = '\x01\xcd\x3c\x3d' '\x00\x00\x00\x00' \
            '\xf7\xaa\xc2\xca' '\xdf\x55\x9f\xb7' \
            '\x90\x28\xa0\xce' '\xb7\x5b\xe2\x0a' \
            '\x85\x85\xf6\x45' '\x00\x00\x00\x00'


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
            'max_names': 41387,
            'pattern': 'bhazr',
            }
        self.req_bin_0 = '\x31\x00\x00\x04' '\xa1\xab\x00\x05' \
            '\x62\x68\x61\x7a' '\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 57054,
            }
        self.reply_bin_0 = '\x01\x00\xde\xde' '\x00\x00\x00\x05' \
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
            'max_names': 41728,
            'pattern': 'bhazr2',
            }
        self.req_bin_0 = '\x32\x00\x00\x04' '\xa3\x00\x00\x06' \
            '\x62\x68\x61\x7a' '\x72\x32\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 24555,
            'properties': [{'value': 1106326331, 'name': 473813079}],
            'min_byte1': 201,
            'max_byte1': 155,
            'max_char_or_byte2': 13873,
            'default_char': 62004,
            'min_char_or_byte2': 6272,
            'draw_direction': 171,
            'replies_hint': 621118830,
            'min_bounds': {'descent': -21827, 'ascent': -23224, 'character_width': -7769, 'left_side_bearing': -27599, 'right_side_bearing': -1822, 'attributes': 23072},
            'all_chars_exist': 0,
            'name': 'fontfont',
            'font_ascent': -10158,
            'font_descent': -29095,
            'max_bounds': {'descent': -28370, 'ascent': -27525, 'character_width': -23263, 'left_side_bearing': -6635, 'right_side_bearing': -18842, 'attributes': 36200},
            }
        self.reply_bin_0 = '\x01\x08\x5f\xeb' '\x00\x00\x00\x0b' \
            '\x94\x31\xf8\xe2' '\xe1\xa7\xa5\x48' \
            '\xaa\xbd\x5a\x20' '\x00\x00\x00\x00' \
            '\xe6\x15\xb6\x66' '\xa5\x21\x94\x7b' \
            '\x91\x2e\x8d\x68' '\x00\x00\x00\x00' \
            '\x18\x80\x36\x31' '\xf2\x34\x00\x01' \
            '\xab\xc9\x9b\x00' '\xd8\x52\x8e\x59' \
            '\x25\x05\x85\x6e' '\x1c\x3d\xd0\x57' \
            '\x41\xf1\x33\x3b' '\x66\x6f\x6e\x74' \
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
            'sequence_number': 9811,
            'paths': ['path1', 'path2232'],
            }
        self.reply_bin_0 = '\x01\x00\x26\x53' '\x00\x00\x00\x04' \
            '\x00\x02\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x05\x70\x61\x74' '\x68\x31\x08\x70' \
            '\x61\x74\x68\x32' '\x32\x33\x32\x00'

        self.reply_args_1 = {
            'sequence_number': 7231,
            'paths': [],
            }
        self.reply_bin_1 = '\x01\x00\x1c\x3f' '\x00\x00\x00\x00' \
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
            'height': 36624,
            'drawable': 270242365,
            'pid': 451180827,
            'depth': 152,
            'width': 3842,
            }
        self.req_bin_0 = '\x35\x98\x00\x04' '\x1a\xe4\x79\x1b' \
            '\x10\x1b\x92\x3d' '\x0f\x02\x8f\x10'


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
            'pixmap': 1221352707,
            }
        self.req_bin_0 = '\x36\x00\x00\x02' '\x48\xcc\x5d\x03'


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
            'cid': 431350032,
            'drawable': 1505849341,
            'attrs': {'dashes': 164, 'fill_rule': 0, 'clip_mask': 392680688, 'plane_mask': 413592852, 'line_style': 0, 'tile': 312785600, 'arc_mode': 0, 'clip_y_origin': -5469, 'dash_offset': 43610, 'line_width': 60228, 'background': 426077726, 'clip_x_origin': -15695, 'join_style': 0, 'graphics_exposures': 1, 'font': 308094811, 'tile_stipple_y_origin': -26131, 'stipple': 23285536, 'fill_style': 1, 'cap_style': 1, 'subwindow_mode': 0, 'tile_stipple_x_origin': -10377, 'foreground': 1713366794, 'function': 8},
            }
        self.req_bin_0 = '\x37\x00\x00\x1b' '\x19\xb5\xe1\x10' \
            '\x59\xc1\x6f\xfd' '\x00\x7f\xff\xff' \
            '\x08\x00\x00\x00' '\x18\xa6\xed\x14' \
            '\x66\x1f\xe7\x0a' '\x19\x65\x6e\x1e' \
            '\xeb\x44\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x12\xa4\xba\xc0' '\x01\x63\x4f\x20' \
            '\xd7\x77\x00\x00' '\x99\xed\x00\x00' \
            '\x12\x5d\x27\x5b' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\xc2\xb1\x00\x00' \
            '\xea\xa3\x00\x00' '\x17\x67\xd4\xf0' \
            '\xaa\x5a\x00\x00' '\xa4\x00\x00\x00' \
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
            'attrs': {'dashes': 140, 'fill_rule': 0, 'clip_mask': 1007716012, 'plane_mask': 1246436938, 'line_style': 1, 'tile': 443199796, 'arc_mode': 0, 'clip_y_origin': -6968, 'dash_offset': 49559, 'line_width': 53912, 'background': 803307323, 'clip_x_origin': -15640, 'join_style': 1, 'graphics_exposures': 1, 'font': 1111317074, 'tile_stipple_y_origin': -18330, 'stipple': 1157787422, 'fill_style': 0, 'cap_style': 1, 'subwindow_mode': 0, 'tile_stipple_x_origin': -15186, 'foreground': 1832956748, 'function': 0},
            'gc': 260729442,
            }
        self.req_bin_0 = '\x38\x00\x00\x1a' '\x0f\x8a\x6a\x62' \
            '\x00\x7f\xff\xff' '\x00\x00\x00\x00' \
            '\x4a\x4b\x1e\x4a' '\x6d\x40\xb3\x4c' \
            '\x2f\xe1\x7f\x3b' '\xd2\x98\x00\x00' \
            '\x01\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x1a\x6a\xb1\x34' \
            '\x45\x02\x6f\x1e' '\xc4\xae\x00\x00' \
            '\xb8\x66\x00\x00' '\x42\x3d\x5a\x52' \
            '\x00\x00\x00\x00' '\x01\x00\x00\x00' \
            '\xc2\xe8\x00\x00' '\xe4\xc8\x00\x00' \
            '\x3c\x10\x86\xac' '\xc1\x97\x00\x00' \
            '\x8c\x00\x00\x00' '\x00\x00\x00\x00'


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
            'mask': 1744373936,
            'src_gc': 955633145,
            'dst_gc': 1205246689,
            }
        self.req_bin_0 = '\x39\x00\x00\x04' '\x38\xf5\xcd\xf9' \
            '\x47\xd6\x9a\xe1' '\x67\xf9\x08\xb0'


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
            'dashes': [253, 215, 146, 243, 200, 151, 179, 203, 169],
            'dash_offset': 31429,
            'gc': 2089880163,
            }
        self.req_bin_0 = '\x3a\x00\x00\x06' '\x7c\x91\x0a\x63' \
            '\x7a\xc5\x00\x09' '\xfd\xd7\x92\xf3' \
            '\xc8\x97\xb3\xcb' '\xa9\x00\x00\x00'


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
            'rectangles': [{'height': 7420, 'x': -5698, 'width': 30606, 'y': -21373}, {'height': 37913, 'x': -21428, 'width': 36243, 'y': -22214}],
            'gc': 2053582814,
            'x_origin': -11698,
            'y_origin': -19544,
            'ordering': 0,
            }
        self.req_bin_0 = '\x3b\x00\x00\x07' '\x7a\x67\x2f\xde' \
            '\xd2\x4e\xb3\xa8' '\xe9\xbe\xac\x83' \
            '\x77\x8e\x1c\xfc' '\xac\x4c\xa9\x3a' \
            '\x8d\x93\x94\x19'

        self.req_args_1 = {
            'rectangles': [],
            'gc': 1509051871,
            'x_origin': -24949,
            'y_origin': -11342,
            'ordering': 0,
            }
        self.req_bin_1 = '\x3b\x00\x00\x03' '\x59\xf2\x4d\xdf' \
            '\x9e\x8b\xd3\xb2'


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
            'gc': 487007211,
            }
        self.req_bin_0 = '\x3c\x00\x00\x02' '\x1d\x07\x23\xeb'


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
            'height': 2760,
            'width': 1333,
            'window': 2113122571,
            'x': -6834,
            'y': -2057,
            }
        self.req_bin_0 = '\x3d\x00\x00\x04' '\x7d\xf3\xb1\x0b' \
            '\xe5\x4e\xf7\xf7' '\x05\x35\x0a\xc8'


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
            'src_drawable': 208517129,
            'dst_drawable': 1067145138,
            'src_y': -20556,
            'src_x': -15795,
            'gc': 2138387869,
            'width': 33113,
            'height': 63378,
            'dst_x': -11036,
            'dst_y': -3319,
            }
        self.req_bin_0 = '\x3e\x00\x00\x07' '\x0c\x6d\xb8\x09' \
            '\x3f\x9b\x57\xb2' '\x7f\x75\x35\x9d' \
            '\xc2\x4d\xaf\xb4' '\xd4\xe4\xf3\x09' \
            '\x81\x59\xf7\x92'


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
            'src_drawable': 766965326,
            'bit_plane': 435107973,
            'dst_drawable': 1743049858,
            'src_y': -17850,
            'src_x': -31095,
            'gc': 860038311,
            'width': 55221,
            'height': 12772,
            'dst_x': -13088,
            'dst_y': -18638,
            }
        self.req_bin_0 = '\x3f\x00\x00\x08' '\x2d\xb6\xf6\x4e' \
            '\x67\xe4\xd4\x82' '\x33\x43\x24\xa7' \
            '\x86\x89\xba\x46' '\xcc\xe0\xb7\x32' \
            '\xd7\xb5\x31\xe4' '\x19\xef\x38\x85'


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
            'gc': 2041506750,
            'points': [{'x': -11305, 'y': -16812}, {'x': -30688, 'y': -2971}, {'x': -2848, 'y': -679}],
            'drawable': 533405691,
            'coord_mode': 1,
            }
        self.req_bin_0 = '\x40\x01\x00\x06' '\x1f\xcb\x1f\xfb' \
            '\x79\xae\xeb\xbe' '\xd3\xd7\xbe\x54' \
            '\x88\x20\xf4\x65' '\xf4\xe0\xfd\x59'


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
            'gc': 392859086,
            'points': [{'x': -23896, 'y': -22901}, {'x': -8082, 'y': -17426}, {'x': -17617, 'y': -5320}, {'x': -17476, 'y': -6655}, {'x': -8910, 'y': -20417}],
            'drawable': 247659556,
            'coord_mode': 0,
            }
        self.req_bin_0 = '\x41\x00\x00\x08' '\x0e\xc2\xfc\x24' \
            '\x17\x6a\x8d\xce' '\xa2\xa8\xa6\x8b' \
            '\xe0\x6e\xbb\xee' '\xbb\x2f\xeb\x38' \
            '\xbb\xbc\xe6\x01' '\xdd\x32\xb0\x3f'


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
            'segments': [{'y1': -15864, 'y2': -21295, 'x1': -23568, 'x2': -28662}],
            'drawable': 709545806,
            'gc': 734581836,
            }
        self.req_bin_0 = '\x42\x00\x00\x05' '\x2a\x4a\xcf\x4e' \
            '\x2b\xc8\xd4\x4c' '\xa3\xf0\xc2\x08' \
            '\x90\x0a\xac\xd1'


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
            'drawable': 504267751,
            'gc': 770574683,
            'rectangles': [{'height': 27448, 'x': -14654, 'width': 54969, 'y': -1957}, {'height': 43849, 'x': -19075, 'width': 5703, 'y': -20002}, {'height': 2592, 'x': -17337, 'width': 44348, 'y': -17534}],
            }
        self.req_bin_0 = '\x43\x00\x00\x09' '\x1e\x0e\x83\xe7' \
            '\x2d\xee\x09\x5b' '\xc6\xc2\xf8\x5b' \
            '\xd6\xb9\x6b\x38' '\xb5\x7d\xb1\xde' \
            '\x16\x47\xab\x49' '\xbc\x47\xbb\x82' \
            '\xad\x3c\x0a\x20'


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
            'arcs': [{'height': 51321, 'angle1': -30816, 'x': -27485, 'angle2': -6827, 'width': 58130, 'y': -14699}, {'height': 16700, 'angle1': -27817, 'x': -26144, 'angle2': -4349, 'width': 6359, 'y': -12152}, {'height': 349, 'angle1': -30183, 'x': -26387, 'angle2': -3041, 'width': 41445, 'y': -7634}],
            'drawable': 606957189,
            'gc': 1539912993,
            }
        self.req_bin_0 = '\x44\x00\x00\x0c' '\x24\x2d\x6e\x85' \
            '\x5b\xc9\x35\x21' '\x94\xa3\xc6\x95' \
            '\xe3\x12\xc8\x79' '\x87\xa0\xe5\x55' \
            '\x99\xe0\xd0\x88' '\x18\xd7\x41\x3c' \
            '\x93\x57\xef\x03' '\x98\xed\xe2\x2e' \
            '\xa1\xe5\x01\x5d' '\x8a\x19\xf4\x1f'


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
            'shape': 0,
            'gc': 648415515,
            'points': [{'x': -1891, 'y': -12535}, {'x': -25824, 'y': -30616}, {'x': -25839, 'y': -18341}],
            'drawable': 40637777,
            'coord_mode': 0,
            }
        self.req_bin_0 = '\x45\x00\x00\x07' '\x02\x6c\x15\x51' \
            '\x26\xa6\x09\x1b' '\x00\x00\x00\x00' \
            '\xf8\x9d\xcf\x09' '\x9b\x20\x88\x68' \
            '\x9b\x11\xb8\x5b'


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
            'drawable': 70167590,
            'gc': 1715295825,
            'rectangles': [{'height': 61907, 'x': -22214, 'width': 29984, 'y': -3052}, {'height': 42805, 'x': -30092, 'width': 18804, 'y': -27911}],
            }
        self.req_bin_0 = '\x46\x00\x00\x07' '\x04\x2e\xac\x26' \
            '\x66\x3d\x56\x51' '\xa9\x3a\xf4\x14' \
            '\x75\x20\xf1\xd3' '\x8a\x74\x92\xf9' \
            '\x49\x74\xa7\x35'


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
            'arcs': [{'height': 29232, 'angle1': -3750, 'x': -2857, 'angle2': -3307, 'width': 38491, 'y': -27289}],
            'drawable': 482415860,
            'gc': 476082016,
            }
        self.req_bin_0 = '\x47\x00\x00\x06' '\x1c\xc1\x14\xf4' \
            '\x1c\x60\x6f\x60' '\xf4\xd7\x95\x67' \
            '\x96\x5b\x72\x30' '\xf1\x5a\xf3\x15'


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
            'height': 11196,
            'data': 'bit map data',
            'drawable': 1340290879,
            'left_pad': 170,
            'format': 2,
            'dst_x': -11353,
            'gc': 237898211,
            'depth': 160,
            'width': 42139,
            'dst_y': -26494,
            }
        self.req_bin_0 = '\x48\x02\x00\x09' '\x4f\xe3\x37\x3f' \
            '\x0e\x2e\x09\xe3' '\xa4\x9b\x2b\xbc' \
            '\xd3\xa7\x98\x82' '\xaa\xa0\x00\x00' \
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
            'height': 56958,
            'plane_mask': 2003492823,
            'drawable': 1619440599,
            'x': -15778,
            'y': -20045,
            'format': 2,
            'width': 63114,
            }
        self.req_bin_0 = '\x49\x02\x00\x05' '\x60\x86\xb3\xd7' \
            '\xc2\x5e\xb1\xb3' '\xf6\x8a\xde\x7e' \
            '\x77\x6a\xdf\xd7'

        self.reply_args_0 = {
            'sequence_number': 63877,
            'data': 'this is real ly imag e b-map',
            'visual': 536760605,
            'depth': 190,
            }
        self.reply_bin_0 = '\x01\xbe\xf9\x85' '\x00\x00\x00\x07' \
            '\x1f\xfe\x51\x1d' '\x00\x00\x00\x00' \
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
            'gc': 1799460488,
            'x': -17910,
            'drawable': 1708049506,
            'items': [{'delta': 2, 'string': 'zoo'}, 16909060, {'delta': 0, 'string': 'ie'}],
            'y': -18689,
            }
        self.req_bin_0 = '\x4a\x00\x00\x08' '\x65\xce\xc4\x62' \
            '\x6b\x41\x96\x88' '\xba\x0a\xb6\xff' \
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
            'gc': 1459026804,
            'x': -15550,
            'drawable': 1562879126,
            'items': [{'delta': 2, 'string': (4131, 18)}, 16909060],
            'y': -25379,
            }
        self.req_bin_0 = '\x4b\x00\x00\x07' '\x5d\x27\xa4\x96' \
            '\x56\xf6\xfb\x74' '\xc3\x42\x9c\xdd' \
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
            'gc': 547609349,
            'drawable': 1919096614,
            'x': -6133,
            'y': -12197,
            }
        self.req_bin_0 = '\x4c\x06\x00\x06' '\x72\x63\x17\x26' \
            '\x20\xa3\xdb\x05' '\xe8\x0b\xd0\x5b' \
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
            'gc': 999969487,
            'drawable': 409635149,
            'x': -21868,
            'y': -25321,
            }
        self.req_bin_0 = '\x4d\x08\x00\x08' '\x18\x6a\x89\x4d' \
            '\x3b\x9a\x52\xcf' '\xaa\x94\x9d\x17' \
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
            'mid': 1729503514,
            'alloc': 1,
            'visual': 234871847,
            'window': 716379305,
            }
        self.req_bin_0 = '\x4e\x01\x00\x04' '\x67\x16\x21\x1a' \
            '\x2a\xb3\x14\xa9' '\x0d\xff\xdc\x27'


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
            'cmap': 788546246,
            }
        self.req_bin_0 = '\x4f\x00\x00\x02' '\x2f\x00\x42\xc6'


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
            'src_cmap': 304830797,
            'mid': 1567568454,
            }
        self.req_bin_0 = '\x50\x00\x00\x03' '\x5d\x6f\x32\x46' \
            '\x12\x2b\x59\x4d'


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
            'cmap': 1636570888,
            }
        self.req_bin_0 = '\x51\x00\x00\x02' '\x61\x8c\x17\x08'


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
            'cmap': 12036730,
            }
        self.req_bin_0 = '\x52\x00\x00\x02' '\x00\xb7\xaa\x7a'


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
            'window': 1917219171,
            }
        self.req_bin_0 = '\x53\x00\x00\x02' '\x72\x46\x71\x63'

        self.reply_args_0 = {
            'cmaps': [1466686184, 742915485],
            'sequence_number': 7840,
            }
        self.reply_bin_0 = '\x01\x00\x1e\xa0' '\x00\x00\x00\x02' \
            '\x00\x02\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x57\x6b\xda\xe8' '\x2c\x47\xfd\x9d'


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
            'red': 18180,
            'green': 24249,
            'cmap': 53391968,
            'blue': 21979,
            }
        self.req_bin_0 = '\x54\x00\x00\x04' '\x03\x2e\xb2\x60' \
            '\x47\x04\x5e\xb9' '\x55\xdb\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 23968,
            'red': 59366,
            'green': 34037,
            'pixel': 1186630361,
            'blue': 39251,
            }
        self.reply_bin_0 = '\x01\x00\x5d\xa0' '\x00\x00\x00\x00' \
            '\xe7\xe6\x84\xf5' '\x99\x53\x00\x00' \
            '\x46\xba\x8a\xd9' '\x00\x00\x00\x00' \
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
            'cmap': 1658370346,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x55\x00\x00\x05' '\x62\xd8\xb9\x2a' \
            '\x00\x07\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 56879,
            'pixel': 386813293,
            'screen_green': 16502,
            'screen_red': 31884,
            'exact_green': 2513,
            'exact_blue': 20311,
            'screen_blue': 52144,
            'exact_red': 41402,
            }
        self.reply_bin_0 = '\x01\x00\xde\x2f' '\x00\x00\x00\x00' \
            '\x17\x0e\x4d\x6d' '\xa1\xba\x09\xd1' \
            '\x4f\x57\x7c\x8c' '\x40\x76\xcb\xb0' \
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
            'planes': 4288,
            'colors': 42087,
            'cmap': 1805186643,
            'contiguous': 1,
            }
        self.req_bin_0 = '\x56\x01\x00\x03' '\x6b\x98\xf6\x53' \
            '\xa4\x67\x10\xc0'

        self.reply_args_0 = {
            'masks': [995762341, 1165266384, 1038525242],
            'pixels': [1750540997, 2100042471, 1804383453, 606846337, 1596248709, 358596220, 1403039104, 1922778852, 698585220, 587929117, 308312801, 2026149752, 860491421, 1661962733, 556418112, 1557826064, 275411866],
            'sequence_number': 14700,
            }
        self.reply_bin_0 = '\x01\x00\x39\x6c' '\x00\x00\x00\x14' \
            '\x00\x11\x00\x03' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x68\x57\x22\xc5' '\x7d\x2c\x1a\xe7' \
            '\x6b\x8c\xb4\xdd' '\x24\x2b\xbd\x81' \
            '\x5f\x24\xd2\x85' '\x15\x5f\xbe\x7c' \
            '\x53\xa0\xad\x80' '\x72\x9b\x46\xe4' \
            '\x29\xa3\x90\x84' '\x23\x0b\x16\x1d' \
            '\x12\x60\x7a\xe1' '\x78\xc4\x97\x78' \
            '\x33\x4a\x0e\x9d' '\x63\x0f\x89\xed' \
            '\x21\x2a\x44\x40' '\x5c\xda\x8a\x10' \
            '\x10\x6a\x73\x9a' '\x3b\x5a\x20\xa5' \
            '\x45\x74\x8d\xd0' '\x3d\xe6\xa3\x3a'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 38539,
            }
        self.reply_bin_1 = '\x01\x00\x96\x8b' '\x00\x00\x00\x00' \
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
            'red': 13636,
            'colors': 1878,
            'green': 27505,
            'cmap': 1517762159,
            'contiguous': 1,
            'blue': 371,
            }
        self.req_bin_0 = '\x57\x01\x00\x04' '\x5a\x77\x36\x6f' \
            '\x07\x56\x35\x44' '\x6b\x71\x01\x73'

        self.reply_args_0 = {
            'green_mask': 1535062952,
            'sequence_number': 12327,
            'pixels': [1575345154, 670191425, 1417403688, 1954535300],
            'blue_mask': 1283218011,
            'red_mask': 981769758,
            }
        self.reply_bin_0 = '\x01\x00\x30\x27' '\x00\x00\x00\x04' \
            '\x00\x04\x00\x00' '\x3a\x84\x9e\x1e' \
            '\x5b\x7f\x33\xa8' '\x4c\x7c\x5a\x5b' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x5d\xe5\xdc\x02' '\x27\xf2\x4f\x41' \
            '\x54\x7b\xdd\x28' '\x74\x7f\xd7\x84'


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
            'cmap': 1361401045,
            'pixels': [459895467, 255031583, 234735044, 1996164499, 1204563412, 1507264268, 903054342, 1832829517, 932533094, 20664694, 386661577, 1559167857, 32537953, 368699232, 780563645, 910624209, 980312108],
            'plane_mask': 938362004,
            }
        self.req_bin_0 = '\x58\x00\x00\x14' '\x51\x25\x54\xd5' \
            '\x37\xee\x44\x94' '\x1b\x69\x72\xab' \
            '\x0f\x33\x79\x1f' '\x0d\xfd\xc5\xc4' \
            '\x76\xfb\x0d\x93' '\x47\xcc\x2d\xd4' \
            '\x59\xd7\x07\x0c' '\x35\xd3\x84\x06' \
            '\x6d\x3e\xc2\x4d' '\x37\x95\x53\x66' \
            '\x01\x3b\x51\x76' '\x17\x0b\xfc\xc9' \
            '\x5c\xef\x03\x71' '\x01\xf0\x7d\x61' \
            '\x15\xf9\xe7\x60' '\x2e\x86\x74\xbd' \
            '\x36\x47\x05\xd1' '\x3a\x6e\x60\x2c'


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
            'cmap': 2024580983,
            'items': [{'red': 64927, 'pixel': 2001260878, 'green': 18106, 'flags': 181, 'blue': 36986}, {'red': 56638, 'pixel': 972179075, 'green': 46814, 'flags': 252, 'blue': 59107}, {'red': 59536, 'pixel': 1430255901, 'green': 17958, 'flags': 130, 'blue': 20978}, {'red': 28038, 'pixel': 1847071918, 'green': 42387, 'flags': 230, 'blue': 31866}],
            }
        self.req_bin_0 = '\x59\x00\x00\x0e' '\x78\xac\xa7\x77' \
            '\x77\x48\xd1\x4e' '\xfd\x9f\x46\xba' \
            '\x90\x7a\xb5\x00' '\x39\xf2\x46\x83' \
            '\xdd\x3e\xb6\xde' '\xe6\xe3\xfc\x00' \
            '\x55\x3f\xf9\x1d' '\xe8\x90\x46\x26' \
            '\x51\xf2\x82\x00' '\x6e\x18\x14\xae' \
            '\x6d\x86\xa5\x93' '\x7c\x7a\xe6\x00'


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
            'flags': 150,
            'cmap': 406354043,
            'pixel': 1493370133,
            }
        self.req_bin_0 = '\x5a\x96\x00\x05' '\x18\x38\x78\x7b' \
            '\x59\x03\x05\x15' '\x00\x04\x00\x00' \
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
            'cmap': 1379497842,
            'pixels': [1515137134, 106421195, 831443625, 1751128164, 1363099624, 542530423, 212873337, 944839923],
            }
        self.req_bin_0 = '\x5b\x00\x00\x0a' '\x52\x39\x77\x72' \
            '\x5a\x4f\x28\x6e' '\x06\x57\xdb\xcb' \
            '\x31\x8e\xd2\xa9' '\x68\x60\x18\x64' \
            '\x51\x3f\x3f\xe8' '\x20\x56\x5b\x77' \
            '\x0c\xb0\x30\x79' '\x38\x51\x1c\xf3'

        self.reply_args_0 = {
            'colors': [{'red': 54674, 'blue': 38519, 'green': 13643}, {'red': 51294, 'blue': 50831, 'green': 60614}, {'red': 29637, 'blue': 15980, 'green': 64789}, {'red': 44718, 'blue': 20802, 'green': 1652}, {'red': 58906, 'blue': 20706, 'green': 25237}],
            'sequence_number': 6473,
            }
        self.reply_bin_0 = '\x01\x00\x19\x49' '\x00\x00\x00\x0a' \
            '\x00\x05\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xd5\x92\x35\x4b' '\x96\x77\x00\x00' \
            '\xc8\x5e\xec\xc6' '\xc6\x8f\x00\x00' \
            '\x73\xc5\xfd\x15' '\x3e\x6c\x00\x00' \
            '\xae\xae\x06\x74' '\x51\x42\x00\x00' \
            '\xe6\x1a\x62\x95' '\x50\xe2\x00\x00'

        self.req_args_1 = {
            'cmap': 802128808,
            'pixels': [],
            }
        self.req_bin_1 = '\x5b\x00\x00\x02' '\x2f\xcf\x83\xa8'


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
            'cmap': 878745244,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x5c\x00\x00\x05' '\x34\x60\x96\x9c' \
            '\x00\x07\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 35336,
            'screen_green': 21598,
            'screen_red': 3096,
            'exact_green': 23541,
            'exact_blue': 30270,
            'screen_blue': 8428,
            'exact_red': 22200,
            }
        self.reply_bin_0 = '\x01\x00\x8a\x08' '\x00\x00\x00\x00' \
            '\x56\xb8\x5b\xf5' '\x76\x3e\x0c\x18' \
            '\x54\x5e\x20\xec' '\x00\x00\x00\x00' \
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
            'x': 15326,
            'fore_red': 31462,
            'back_green': 18359,
            'mask': 87694263,
            'back_blue': 18234,
            'y': 6926,
            'cid': 1580097391,
            'fore_blue': 22121,
            'fore_green': 61494,
            'back_red': 41941,
            'source': 172929735,
            }
        self.req_bin_0 = '\x5d\x00\x00\x08' '\x5e\x2e\x5f\x6f' \
            '\x0a\x4e\xb2\xc7' '\x05\x3a\x1b\xb7' \
            '\x7a\xe6\xf0\x36' '\x56\x69\xa3\xd5' \
            '\x47\xb7\x47\x3a' '\x3b\xde\x1b\x0e'


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
            'fore_red': 18582,
            'source_char': 16884,
            'mask': 808195000,
            'back_blue': 27021,
            'cid': 1184164101,
            'mask_char': 18217,
            'fore_blue': 9646,
            'fore_green': 55721,
            'back_red': 51228,
            'source': 1672460383,
            'back_green': 63449,
            }
        self.req_bin_0 = '\x5e\x00\x00\x08' '\x46\x94\xe9\x05' \
            '\x63\xaf\xb8\x5f' '\x30\x2c\x13\xb8' \
            '\x41\xf4\x47\x29' '\x48\x96\xd9\xa9' \
            '\x25\xae\xc8\x1c' '\xf7\xd9\x69\x8d'


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
            'cursor': 465289524,
            }
        self.req_bin_0 = '\x5f\x00\x00\x02' '\x1b\xbb\xc1\x34'


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
            'fore_red': 60989,
            'fore_green': 47234,
            'back_blue': 54690,
            'back_green': 63372,
            'fore_blue': 48257,
            'back_red': 9508,
            'cursor': 1717013045,
            }
        self.req_bin_0 = '\x60\x00\x00\x05' '\x66\x57\x8a\x35' \
            '\xee\x3d\xb8\x82' '\xbc\x81\x25\x24' \
            '\xf7\x8c\xd5\xa2'


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
            'height': 8495,
            'drawable': 2083060371,
            'item_class': 0,
            'width': 41272,
            }
        self.req_bin_0 = '\x61\x00\x00\x03' '\x7c\x28\xfa\x93' \
            '\xa1\x38\x21\x2f'

        self.reply_args_0 = {
            'height': 42322,
            'sequence_number': 63634,
            'width': 27087,
            }
        self.reply_bin_0 = '\x01\x00\xf8\x92' '\x00\x00\x00\x00' \
            '\x69\xcf\xa5\x52' '\x00\x00\x00\x00' \
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
            'sequence_number': 43803,
            'major_opcode': 230,
            'first_error': 192,
            'present': 0,
            'first_event': 219,
            }
        self.reply_bin_0 = '\x01\x00\xab\x1b' '\x00\x00\x00\x00' \
            '\x00\xe6\xdb\xc0' '\x00\x00\x00\x00' \
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
            'sequence_number': 29641,
            'names': ['XTRA', 'XTRA-II'],
            }
        self.reply_bin_0 = '\x01\x02\x73\xc9' '\x00\x00\x00\x04' \
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
            'keysyms': [[2117607436, 467309079, 951637417], [1748035130, 1785116728, 1406223554], [350360637, 554964940, 705336131], [708581333, 2054461448, 1969694568], [101711792, 1806426232, 2061067207], [511186478, 1268298777, 196212264], [1623788614, 1518106932, 1860284177], [791292459, 397649261, 2081069842], [1568812263, 916111961, 1966479230], [1410793049, 556805351, 1661200235], [1836056302, 1128453182, 275719419], [1898574429, 1241387471, 1313026433], [2098887485, 1034343335, 1147336301], [1715862832, 350006704, 1386515327], [694016697, 1652507597, 945839138], [1216184374, 104202693, 571574409], [1186199776, 26324546, 1174511598], [1973770769, 612359985, 60529583], [600750044, 116581100, 1105303584], [501860062, 703320686, 1504723950]],
            'first_keycode': 134,
            }
        self.req_bin_0 = '\x64\x14\x00\x3e' '\x86\x03\x00\x00' \
            '\x7e\x38\x20\x0c' '\x1b\xda\x92\x17' \
            '\x38\xb8\xd5\xa9' '\x68\x30\xe6\x3a' \
            '\x6a\x66\xb8\x38' '\x53\xd1\x44\xc2' \
            '\x14\xe2\x14\x3d' '\x21\x14\x17\xcc' \
            '\x2a\x0a\x93\x43' '\x2a\x3c\x17\xd5' \
            '\x7a\x74\x98\x08' '\x75\x67\x27\x68' \
            '\x06\x0f\xff\xb0' '\x6b\xab\xe0\x78' \
            '\x7a\xd9\x63\xc7' '\x1e\x78\x16\x2e' \
            '\x4b\x98\xb4\x19' '\x0b\xb1\xf6\x28' \
            '\x60\xc9\x0c\x46' '\x5a\x7c\x79\x34' \
            '\x6e\xe1\xaf\x11' '\x2f\x2a\x2a\x2b' \
            '\x17\xb3\xa5\x6d' '\x7c\x0a\x9b\x12' \
            '\x5d\x82\x2c\xe7' '\x36\x9a\xc2\x59' \
            '\x75\x36\x17\x7e' '\x54\x16\xfe\x59' \
            '\x21\x30\x2c\xe7' '\x63\x03\xe7\x6b' \
            '\x6d\x6f\xfe\xee' '\x43\x42\xd4\x3e' \
            '\x10\x6f\x24\xfb' '\x71\x29\xf2\x5d' \
            '\x49\xfe\x11\xcf' '\x4e\x43\x31\x81' \
            '\x7d\x1a\x7b\x3d' '\x3d\xa6\xd3\xa7' \
            '\x44\x62\xf6\x6d' '\x66\x45\xfd\x30' \
            '\x14\xdc\xad\xb0' '\x52\xa4\x8b\x7f' \
            '\x29\x5d\xda\xb9' '\x62\x7f\x43\xcd' \
            '\x38\x60\x5c\x22' '\x48\x7d\x80\x36' \
            '\x06\x36\x01\xc5' '\x22\x11\x88\x89' \
            '\x46\xb3\xf8\xe0' '\x01\x91\xae\x42' \
            '\x46\x01\x9f\xee' '\x75\xa5\x5a\x11' \
            '\x24\x7f\xdf\x31' '\x03\x9b\x9b\xaf' \
            '\x23\xce\xb7\xdc' '\x06\xf2\xe2\xec' \
            '\x41\xe1\x98\x20' '\x1d\xe9\xc6\xde' \
            '\x29\xeb\xd2\x6e' '\x59\xb0\x43\xee'


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
            'count': 159,
            'first_keycode': 134,
            }
        self.req_bin_0 = '\x65\x00\x00\x02' '\x86\x9f\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[336695481, 1640249322, 1879439584], [816964361, 65612992, 96414], [891482556, 855216951, 1811105021], [624552922, 1937275200, 1716240166], [2054887906, 81126773, 1704361088], [506129834, 869240513, 1122686985], [1274240417, 1118939674, 925049942], [1303650133, 1259926830, 1027368708], [601936636, 634105139, 941380843], [1379435406, 417140511, 134171695], [897188161, 619569763, 692303801], [904313345, 209104714, 395066241], [299249796, 591900309, 107487797], [208832448, 1010810792, 983223750], [760385841, 638593506, 532152763], [1712157766, 1086193171, 1300287885], [1801032567, 1939194062, 442847080], [910996954, 38695297, 264831518], [1402759796, 634947225, 1229475387], [1507407258, 249900412, 795782523]],
            'sequence_number': 5773,
            }
        self.reply_bin_0 = '\x01\x03\x16\x8d' '\x00\x00\x00\x3c' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x14\x11\x90\xb9' '\x61\xc4\x37\xea' \
            '\x70\x05\xf8\xe0' '\x30\xb1\xe3\x09' \
            '\x03\xe9\x2c\xc0' '\x00\x01\x78\x9e' \
            '\x35\x22\xf1\xbc' '\x32\xf9\x93\x37' \
            '\x6b\xf3\x44\xfd' '\x25\x39\xeb\xda' \
            '\x73\x78\x79\x40' '\x66\x4b\xbf\x26' \
            '\x7a\x7b\x19\xe2' '\x04\xd5\xe5\x75' \
            '\x65\x96\x7c\x80' '\x1e\x2a\xed\xaa' \
            '\x33\xcf\x8e\xc1' '\x42\xea\xd8\x09' \
            '\x4b\xf3\x5d\xa1' '\x42\xb1\xaa\x1a' \
            '\x37\x23\x24\x56' '\x4d\xb4\x1f\x55' \
            '\x4b\x18\xf5\x2e' '\x3d\x3c\x67\x04' \
            '\x23\xe0\xd2\xfc' '\x25\xcb\xad\x33' \
            '\x38\x1c\x54\xeb' '\x52\x38\x83\x8e' \
            '\x18\xdd\x0f\x1f' '\x07\xff\x4c\x2f' \
            '\x35\x7a\x01\x41' '\x24\xed\xe2\x63' \
            '\x29\x43\xb7\xb9' '\x35\xe6\xba\x01' \
            '\x0c\x76\xaf\x4a' '\x17\x8c\x3b\x81' \
            '\x11\xd6\x30\x84' '\x23\x47\xae\x95' \
            '\x06\x68\x22\x35' '\x0c\x72\x87\xc0' \
            '\x3c\x3f\xbf\xa8' '\x3a\x9a\xcd\xc6' \
            '\x2d\x52\x91\x31' '\x26\x10\x29\xe2' \
            '\x1f\xb8\x01\xbb' '\x66\x0d\x74\x46' \
            '\x40\xbd\xfe\x13' '\x4d\x80\xd1\x8d' \
            '\x6b\x59\x93\x77' '\x73\x95\xc0\xce' \
            '\x1a\x65\x4f\x68' '\x36\x4c\xb5\xda' \
            '\x02\x4e\x71\x81' '\x0f\xc9\x02\x1e' \
            '\x53\x9c\x6a\x74' '\x25\xd8\x86\x99' \
            '\x49\x48\x4e\x3b' '\x59\xd9\x35\x9a' \
            '\x0e\xe5\x2d\x7c' '\x2f\x6e\xad\x7b'


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
            'attrs': {'key_click_percent': -124, 'bell_percent': -87, 'led_mode': 0, 'bell_pitch': -31397, 'auto_repeat_mode': 0, 'bell_duration': -15288, 'key': 156, 'led': 219},
            }
        self.req_bin_0 = '\x66\x00\x00\x0a' '\x00\x00\x00\xff' \
            '\x84\x00\x00\x00' '\xa9\x00\x00\x00' \
            '\x85\x5b\x00\x00' '\xc4\x48\x00\x00' \
            '\xdb\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x9c\x00\x00\x00' '\x00\x00\x00\x00'


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
            'sequence_number': 30048,
            'bell_percent': 144,
            'bell_pitch': 28554,
            'auto_repeats': [1334039811, 1689844747, 1376787395, 2059944496, 816245265, 1693189176, 1553814313, 1753043446],
            'global_auto_repeat': 1,
            'led_mask': 1604810476,
            'bell_duration': 55361,
            }
        self.reply_bin_0 = '\x01\x01\x75\x60' '\x00\x00\x00\x05' \
            '\x5f\xa7\x76\xec' '\xe7\x90\x6f\x8a' \
            '\xd8\x41\x00\x00' '\x4f\x83\xd5\x03' \
            '\x64\xb8\xfc\x0b' '\x52\x10\x1b\xc3' \
            '\x7a\xc8\x42\x30' '\x30\xa6\xea\x11' \
            '\x64\xec\x04\x38' '\x5c\x9d\x53\x29' \
            '\x68\x7d\x51\xf6'


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
            'percent': -88,
            }
        self.req_bin_0 = '\x68\xa8\x00\x01'


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
            'accel_denum': -32444,
            'accel_num': -32290,
            'do_accel': 1,
            'do_thresh': 1,
            'threshold': -23068,
            }
        self.req_bin_0 = '\x69\x00\x00\x03' '\x81\xde\x81\x44' \
            '\xa5\xe4\x01\x01'


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
            'accel_denom': 42503,
            'sequence_number': 24976,
            'threshold': 12235,
            'accel_num': 43938,
            }
        self.reply_bin_0 = '\x01\x00\x61\x90' '\x00\x00\x00\x00' \
            '\xab\xa2\xa6\x07' '\x2f\xcb\x00\x00' \
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
            'allow_exposures': 2,
            'timeout': -12745,
            'interval': -5593,
            'prefer_blank': 0,
            }
        self.req_bin_0 = '\x6b\x00\x00\x03' '\xce\x37\xea\x27' \
            '\x00\x02\x00\x00'


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
            'timeout': 55379,
            'sequence_number': 23766,
            'prefer_blanking': 1,
            'interval': 24886,
            }
        self.reply_bin_0 = '\x01\x00\x5c\xd6' '\x00\x00\x00\x00' \
            '\xd8\x53\x61\x36' '\x01\x01\x00\x00' \
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
            'host': [189, 193, 184, 196],
            'mode': 0,
            'host_family': 1,
            }
        self.req_bin_0 = '\x6d\x00\x00\x03' '\x01\x00\x00\x04' \
            '\xbd\xc1\xb8\xc4'


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
            'sequence_number': 59221,
            'mode': 1,
            'hosts': [{'family': 0, 'name': [34, 23, 178, 12]}, {'family': 0, 'name': [130, 236, 254, 15]}],
            }
        self.reply_bin_0 = '\x01\x01\xe7\x55' '\x00\x00\x00\x04' \
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
            'mode': 1,
            }
        self.req_bin_0 = '\x6f\x01\x00\x01'


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
            'resource': 1583445666,
            }
        self.req_bin_0 = '\x71\x00\x00\x02' '\x5e\x61\x76\xa2'


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
            'delta': -19246,
            'window': 1567668371,
            'properties': [1902605475, 902820585, 180229690, 267232936, 1023102392, 276320478, 1056686048, 980285318, 365082112, 724749476, 296965180, 1673629180],
            }
        self.req_bin_0 = '\x72\x00\x00\x0f' '\x5d\x70\xb8\x93' \
            '\x00\x0c\xb4\xd2' '\x71\x67\x74\xa3' \
            '\x35\xcf\xf2\xe9' '\x0a\xbe\x16\x3a' \
            '\x0f\xed\xa6\xa8' '\x3c\xfb\x4d\xb8' \
            '\x10\x78\x50\xde' '\x3e\xfb\xbf\xe0' \
            '\x3a\x6d\xf7\x86' '\x15\xc2\xb6\x00' \
            '\x2b\x32\xcc\xa4' '\x11\xb3\x54\x3c' \
            '\x63\xc1\x8d\xfc'


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
            'map': [188, 147, 189, 193, 209],
            }
        self.req_bin_0 = '\x74\x05\x00\x03' '\xbc\x93\xbd\xc1' \
            '\xd1\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 27171,
            'status': 201,
            }
        self.reply_bin_0 = '\x01\xc9\x6a\x23' '\x00\x00\x00\x00' \
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
            'sequence_number': 32748,
            'map': [170, 131, 249, 200, 144],
            }
        self.reply_bin_0 = '\x01\x05\x7f\xec' '\x00\x00\x00\x02' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xaa\x83\xf9\xc8' '\x90\x00\x00\x00'


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
            'keycodes': [[3, 205], [11, 238], [159, 184], [165, 113], [242, 173], [72, 103], [240, 186], [175, 141]],
            }
        self.req_bin_0 = '\x76\x02\x00\x05' '\x03\xcd\x0b\xee' \
            '\x9f\xb8\xa5\x71' '\xf2\xad\x48\x67' \
            '\xf0\xba\xaf\x8d'

        self.reply_args_0 = {
            'sequence_number': 47892,
            'status': 133,
            }
        self.reply_bin_0 = '\x01\x85\xbb\x14' '\x00\x00\x00\x00' \
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
            'sequence_number': 15026,
            'keycodes': [[208, 198], [157, 114], [239, 239], [191, 93], [127, 111], [233, 58], [53, 176], [238, 188]],
            }
        self.reply_bin_0 = '\x01\x02\x3a\xb2' '\x00\x00\x00\x04' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xd0\xc6\x9d\x72' '\xef\xef\xbf\x5d' \
            '\x7f\x6f\xe9\x3a' '\x35\xb0\xee\xbc'


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
