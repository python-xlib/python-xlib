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
    if struct.unpack('BB', struct.pack('H', 0x0100))[0] != 0:
        sys.stderr.write('Little-endian tests, skipping on this system.\n')
        sys.exit(0)



class TestCreateWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 38021,
            'window_class': 1,
            'border_width': 40039,
            'visual': 776534316,
            'x': -28762,
            'y': -16360,
            'parent': 1814461159,
            'attrs': {'backing_pixel': 871598872, 'cursor': 1858407784, 'background_pixmap': 893794953, 'border_pixmap': 547359306, 'backing_planes': 346161430, 'win_gravity': 7, 'backing_store': 2, 'event_mask': 598655212, 'save_under': 0, 'background_pixel': 760825547, 'colormap': 1973567145, 'border_pixel': 1754416628, 'bit_gravity': 7, 'do_not_propagate_mask': 2022623564, 'override_redirect': 1},
            'wid': 317506508,
            'depth': 217,
            'width': 48737,
            }
        self.req_bin_0 = '\x01\xd9\x17\x00' '\xcc\xc3\xec\x12' \
            '\xe7\x7a\x26\x6c' '\xa6\x8f\x18\xc0' \
            '\x61\xbe\x85\x94' '\x67\x9c\x01\x00' \
            '\x2c\xf9\x48\x2e' '\xff\x7f\x00\x00' \
            '\x89\x3a\x46\x35' '\xcb\x46\x59\x2d' \
            '\x4a\x0a\xa0\x20' '\xf4\x45\x92\x68' \
            '\x07\x00\x00\x00' '\x07\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x16\x01\xa2\x14' \
            '\x18\x8b\xf3\x33' '\x01\x00\x00\x00' \
            '\x00\x00\x00\x00' '\xec\xc0\xae\x23' \
            '\x4c\xc9\x8e\x78' '\xa9\x3e\xa2\x75' \
            '\x68\x0d\xc5\x6e'


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
            'window': 124747182,
            'attrs': {'backing_pixel': 942145571, 'cursor': 1203497842, 'background_pixmap': 492335580, 'border_pixmap': 960723051, 'backing_planes': 996771216, 'win_gravity': 10, 'backing_store': 1, 'event_mask': 92077622, 'save_under': 0, 'background_pixel': 1740503060, 'colormap': 769651275, 'border_pixel': 659570677, 'bit_gravity': 6, 'do_not_propagate_mask': 332547250, 'override_redirect': 0},
            }
        self.req_bin_0 = '\x02\x00\x12\x00' '\xae\x7d\x6f\x07' \
            '\xff\x7f\x00\x00' '\xdc\x71\x58\x1d' \
            '\x14\xf8\xbd\x67' '\x6b\x78\x43\x39' \
            '\xf5\x3f\x50\x27' '\x06\x00\x00\x00' \
            '\x0a\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x90\x85\x69\x3b' '\x23\x00\x28\x38' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x36\xfe\x7c\x05' '\xb2\x44\xd2\x13' \
            '\x4b\xf2\xdf\x2d' '\x72\xeb\xbb\x47'


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
            'window': 93721452,
            }
        self.req_bin_0 = '\x03\x00\x02\x00' '\x6c\x13\x96\x05'

        self.reply_args_0 = {
            'sequence_number': 28970,
            'backing_pixel': 1423542622,
            'your_event_mask': 1658711012,
            'map_is_installed': 0,
            'visual': 687682747,
            'backing_bit_planes': 839791295,
            'backing_store': 159,
            'win_class': 17021,
            'map_state': 145,
            'save_under': 0,
            'all_event_masks': 213397994,
            'colormap': 192306923,
            'win_gravity': 138,
            'bit_gravity': 161,
            'do_not_propagate_mask': 46621,
            'override_redirect': 0,
            }
        self.reply_bin_0 = '\x01\x9f\x2a\x71' '\x03\x00\x00\x00' \
            '\xbb\x34\xfd\x28' '\x7d\x42\xa1\x8a' \
            '\xbf\x32\x0e\x32' '\x5e\x89\xd9\x54' \
            '\x00\x00\x91\x00' '\xeb\x5e\x76\x0b' \
            '\xea\x31\xb8\x0c' '\xe4\xeb\xdd\x62' \
            '\x1d\xb6\x00\x00'


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
            'window': 400369500,
            }
        self.req_bin_0 = '\x04\x00\x02\x00' '\x5c\x27\xdd\x17'


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
            'window': 601888041,
            }
        self.req_bin_0 = '\x05\x00\x02\x00' '\x29\x15\xe0\x23'


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
            'window': 1691418399,
            'mode': 1,
            }
        self.req_bin_0 = '\x06\x01\x02\x00' '\x1f\xff\xd0\x64'


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
            'parent': 1185189251,
            'window': 1686640449,
            'x': -32728,
            'y': -5645,
            }
        self.req_bin_0 = '\x07\x00\x04\x00' '\x41\x17\x88\x64' \
            '\x83\x8d\xa4\x46' '\x28\x80\xf3\xe9'


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
            'window': 1592975374,
            }
        self.req_bin_0 = '\x08\x00\x02\x00' '\x0e\xe0\xf2\x5e'


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
            'window': 2012662160,
            }
        self.req_bin_0 = '\x09\x00\x02\x00' '\x90\xc9\xf6\x77'


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
            'window': 115327986,
            }
        self.req_bin_0 = '\x0a\x00\x02\x00' '\xf2\xc3\xdf\x06'


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
            'window': 174185741,
            }
        self.req_bin_0 = '\x0b\x00\x02\x00' '\x0d\xdd\x61\x0a'


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
            'window': 1152812659,
            'attrs': {'height': 65253, 'stack_mode': 3, 'border_width': -15603, 'width': 52932, 'x': -22948, 'y': -13736, 'sibling': 2142295333},
            }
        self.req_bin_0 = '\x0c\x00\x0a\x00' '\x73\x86\xb6\x44' \
            '\x7f\x00\x00\x00' '\x5c\xa6\x00\x00' \
            '\x58\xca\x00\x00' '\xc4\xce\x00\x00' \
            '\xe5\xfe\x00\x00' '\x0d\xc3\x00\x00' \
            '\x25\xd5\xb0\x7f' '\x03\x00\x00\x00'


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
            'window': 211023483,
            'direction': 0,
            }
        self.req_bin_0 = '\x0d\x00\x02\x00' '\x7b\xf6\x93\x0c'


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
            'drawable': 956388361,
            }
        self.req_bin_0 = '\x0e\x00\x02\x00' '\x09\x54\x01\x39'

        self.reply_args_0 = {
            'height': 23124,
            'sequence_number': 47415,
            'root': 2020202233,
            'border_width': 28899,
            'x': -905,
            'y': -2717,
            'depth': 223,
            'width': 47535,
            }
        self.reply_bin_0 = '\x01\xdf\x37\xb9' '\x00\x00\x00\x00' \
            '\xf9\xd6\x69\x78' '\x77\xfc\x63\xf5' \
            '\xaf\xb9\x54\x5a' '\xe3\x70\x00\x00' \
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
            'window': 344112764,
            }
        self.req_bin_0 = '\x0f\x00\x02\x00' '\x7c\xbe\x82\x14'

        self.reply_args_0 = {
            'sequence_number': 8359,
            'children': [1323302134, 1268410130, 69119660, 1288661724, 1309064298, 1990810241, 767681953],
            'root': 1735710999,
            'parent': 1757620548,
            }
        self.reply_bin_0 = '\x01\x00\xa7\x20' '\x07\x00\x00\x00' \
            '\x17\xd9\x74\x67' '\x44\x29\xc3\x68' \
            '\x07\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xf6\xfc\xdf\x4e' '\x12\x67\x9a\x4b' \
            '\xac\xae\x1e\x04' '\xdc\x6a\xcf\x4c' \
            '\x6a\xbc\x06\x4e' '\x81\x5a\xa9\x76' \
            '\xa1\xe5\xc1\x2d'


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
            'atom': 657505434,
            'sequence_number': 59130,
            }
        self.reply_bin_0 = '\x01\x00\xfa\xe6' '\x00\x00\x00\x00' \
            '\x9a\xbc\x30\x27' '\x00\x00\x00\x00' \
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
            'atom': 1072847806,
            }
        self.req_bin_0 = '\x11\x00\x02\x00' '\xbe\x5b\xf2\x3f'

        self.reply_args_0 = {
            'sequence_number': 9383,
            'name': 'WM_CLASS',
            }
        self.reply_bin_0 = '\x01\x00\xa7\x24' '\x02\x00\x00\x00' \
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
            'property': 411539214,
            'window': 1812694476,
            'type': 1559030878,
            }
        self.req_bin_0 = '\x12\x00\x06\x00' '\xcc\x85\x0b\x6c' \
            '\x0e\x97\x87\x18' '\x5e\xec\xec\x5c' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_1 = {
            'mode': 2,
            'data': (8, 'foo'),
            'property': 1057505493,
            'window': 1720045526,
            'type': 1352395550,
            }
        self.req_bin_1 = '\x12\x02\x07\x00' '\xd6\xcf\x85\x66' \
            '\xd5\x40\x08\x3f' '\x1e\xeb\x9b\x50' \
            '\x08\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'mode': 1,
            'data': (8, 'zoom'),
            'property': 746321540,
            'window': 992957700,
            'type': 213122374,
            }
        self.req_bin_2 = '\x12\x01\x07\x00' '\x04\x55\x2f\x3b' \
            '\x84\xf6\x7b\x2c' '\x46\xfd\xb3\x0c' \
            '\x08\x00\x00\x00' '\x04\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'mode': 1,
            'data': (16, []),
            'property': 660411223,
            'window': 125152569,
            'type': 844480588,
            }
        self.req_bin_3 = '\x12\x01\x06\x00' '\x39\xad\x75\x07' \
            '\x57\x13\x5d\x27' '\x4c\xc0\x55\x32' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_4 = {
            'mode': 2,
            'data': (16, [1, 2, 3]),
            'property': 1342927746,
            'window': 1031193361,
            'type': 1653118599,
            }
        self.req_bin_4 = '\x12\x02\x08\x00' '\x11\xc3\x76\x3d' \
            '\x82\x73\x0b\x50' '\x87\x96\x88\x62' \
            '\x10\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x00\x00'

        self.req_args_5 = {
            'mode': 0,
            'data': (16, [1, 2, 3, 4]),
            'property': 623793834,
            'window': 467136593,
            'type': 169291963,
            }
        self.req_bin_5 = '\x12\x00\x08\x00' '\x51\xf0\xd7\x1b' \
            '\xaa\x56\x2e\x25' '\xbb\x30\x17\x0a' \
            '\x10\x00\x00\x00' '\x04\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x04\x00'

        self.req_args_6 = {
            'mode': 1,
            'data': (32, []),
            'property': 2047123147,
            'window': 480157794,
            'type': 2020298383,
            }
        self.req_bin_6 = '\x12\x01\x06\x00' '\x62\xa0\x9e\x1c' \
            '\xcb\x9e\x04\x7a' '\x8f\x4e\x6b\x78' \
            '\x20\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_7 = {
            'mode': 0,
            'data': (32, [1, 2, 3]),
            'property': 1492474934,
            'window': 190664484,
            'type': 877682789,
            }
        self.req_bin_7 = '\x12\x00\x09\x00' '\x24\x4f\x5d\x0b' \
            '\x36\x5c\xf5\x58' '\x65\x60\x50\x34' \
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
            'property': 1992152045,
            'window': 1299090930,
            }
        self.req_bin_0 = '\x13\x00\x03\x00' '\xf2\x8d\x6e\x4d' \
            '\xed\xd3\xbd\x76'


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
            'long_offset': 1136574657,
            'type': 823305861,
            'property': 255537708,
            'window': 496983087,
            'long_length': 1207082978,
            }
        self.req_bin_0 = '\x14\x00\x06\x00' '\x2f\x5c\x9f\x1d' \
            '\x2c\x32\x3b\x0f' '\x85\xa6\x12\x31' \
            '\xc1\xc0\xbe\x43' '\xe2\x9f\xf2\x47'

        self.reply_args_0 = {
            'value': (8, ''),
            'sequence_number': 35882,
            'property_type': 1627235076,
            'bytes_after': 1547228683,
            }
        self.reply_bin_0 = '\x01\x08\x2a\x8c' '\x00\x00\x00\x00' \
            '\x04\xa3\xfd\x60' '\x0b\xd6\x38\x5c' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_1 = {
            'value': (8, 'foo'),
            'sequence_number': 65337,
            'property_type': 198737068,
            'bytes_after': 247134558,
            }
        self.reply_bin_1 = '\x01\x08\x39\xff' '\x01\x00\x00\x00' \
            '\xac\x7c\xd8\x0b' '\x5e\xf9\xba\x0e' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'value': (8, 'zoom'),
            'sequence_number': 37727,
            'property_type': 1559208537,
            'bytes_after': 2063332400,
            }
        self.reply_bin_2 = '\x01\x08\x5f\x93' '\x01\x00\x00\x00' \
            '\x59\xa2\xef\x5c' '\x30\xf4\xfb\x7a' \
            '\x04\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'value': (16, []),
            'sequence_number': 55596,
            'property_type': 2120898612,
            'bytes_after': 210691616,
            }
        self.reply_bin_3 = '\x01\x10\x2c\xd9' '\x00\x00\x00\x00' \
            '\x34\x58\x6a\x7e' '\x20\xe6\x8e\x0c' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_4 = {
            'value': (16, [1, 2, 3]),
            'sequence_number': 16806,
            'property_type': 1071816064,
            'bytes_after': 860537153,
            }
        self.reply_bin_4 = '\x01\x10\xa6\x41' '\x02\x00\x00\x00' \
            '\x80\x9d\xe2\x3f' '\x41\xc1\x4a\x33' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x00\x00'

        self.reply_args_5 = {
            'value': (16, [1, 2, 3, 4]),
            'sequence_number': 51558,
            'property_type': 1449416458,
            'bytes_after': 604180991,
            }
        self.reply_bin_5 = '\x01\x10\x66\xc9' '\x02\x00\x00\x00' \
            '\x0a\x57\x64\x56' '\xff\x11\x03\x24' \
            '\x04\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x04\x00'

        self.reply_args_6 = {
            'value': (32, []),
            'sequence_number': 33160,
            'property_type': 1148922332,
            'bytes_after': 460686163,
            }
        self.reply_bin_6 = '\x01\x20\x88\x81' '\x00\x00\x00\x00' \
            '\xdc\x29\x7b\x44' '\x53\x83\x75\x1b' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_7 = {
            'value': (32, [1, 2, 3]),
            'sequence_number': 1740,
            'property_type': 51830840,
            'bytes_after': 785744714,
            }
        self.reply_bin_7 = '\x01\x20\xcc\x06' '\x03\x00\x00\x00' \
            '\x38\xe0\x16\x03' '\x4a\x83\xd5\x2e' \
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
            'window': 1342766761,
            }
        self.req_bin_0 = '\x15\x00\x02\x00' '\xa9\xfe\x08\x50'

        self.reply_args_0 = {
            'atoms': [1954756500, 2115810850, 1419673611, 1772734693, 1479655839, 1907857508, 1079938367, 45570346, 1092605212, 1802440326, 1213718650, 193992097, 183543050, 295390398, 750998302, 1519346985, 1321033083, 1896698494, 1324333835, 1374455526, 1742908891, 1525326791, 1219815843],
            'sequence_number': 13087,
            }
        self.reply_bin_0 = '\x01\x00\x1f\x33' '\x17\x00\x00\x00' \
            '\x17\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x94\x37\x83\x74' '\x22\xb6\x1c\x7e' \
            '\x0b\x80\x9e\x54' '\xe5\xc8\xa9\x69' \
            '\x9f\xc1\x31\x58' '\x64\x98\xb7\x71' \
            '\x3f\x8d\x5e\x40' '\x2a\x59\xb7\x02' \
            '\x1c\xd5\x1f\x41' '\x86\x0e\x6f\x6b' \
            '\x7a\xe0\x57\x48' '\xa1\x15\x90\x0b' \
            '\x0a\xa5\xf0\x0a' '\xbe\x4c\x9b\x11' \
            '\x1e\x53\xc3\x2c' '\x29\x65\x8f\x5a' \
            '\x7b\x5d\xbd\x4e' '\x7e\x52\x0d\x71' \
            '\x0b\xbb\xef\x4e' '\xe6\x86\xec\x51' \
            '\xdb\xad\xe2\x67' '\xc7\xa3\xea\x5a' \
            '\xa3\xe9\xb4\x48'


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
            'selection': 1186676355,
            'window': 950408616,
            'time': 220763431,
            }
        self.req_bin_0 = '\x16\x00\x04\x00' '\xa8\x15\xa6\x38' \
            '\x83\x3e\xbb\x46' '\x27\x95\x28\x0d'


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
            'selection': 1780514514,
            }
        self.req_bin_0 = '\x17\x00\x02\x00' '\xd2\x7e\x20\x6a'

        self.reply_args_0 = {
            'sequence_number': 56214,
            'owner': 1200687926,
            }
        self.reply_bin_0 = '\x01\x00\x96\xdb' '\x00\x00\x00\x00' \
            '\x36\x0b\x91\x47' '\x00\x00\x00\x00' \
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
            'property': 46867726,
            'time': 1193502039,
            'target': 1238352609,
            'selection': 1862818332,
            'requestor': 1747922610,
            }
        self.req_bin_0 = '\x18\x00\x06\x00' '\xb2\x2e\x2f\x68' \
            '\x1c\x5a\x08\x6f' '\xe1\xc2\xcf\x49' \
            '\x0e\x25\xcb\x02' '\x57\x65\x23\x47'


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
            'event': Xlib.protocol.event.Expose(height = 33513, sequence_number = 0, type = 12, x = 59331, y = 26835, window = 111956820, width = 2403, count = 11479),
            'propagate': 1,
            'destination': 1639254427,
            'event_mask': 1278993692,
            }
        self.req_bin_0 = '\x19\x01\x0b\x00' '\x9b\x09\xb5\x61' \
            '\x1c\xe5\x3b\x4c' '\x0c\x00\x00\x00' \
            '\x54\x53\xac\x06' '\xc3\xe7\xd3\x68' \
            '\x63\x09\xe9\x82' '\xd7\x2c\x00\x00' \
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
            'grab_window': 1742752289,
            'confine_to': 1542461659,
            'event_mask': 30582,
            'pointer_mode': 1,
            'time': 1696078427,
            'keyboard_mode': 1,
            'cursor': 2004095233,
            }
        self.req_bin_0 = '\x1a\x01\x06\x00' '\x21\x4a\xe0\x67' \
            '\x76\x77\x01\x01' '\xdb\x18\xf0\x5b' \
            '\x01\x11\x74\x77' '\x5b\x1a\x18\x65'

        self.reply_args_0 = {
            'sequence_number': 43258,
            'status': 221,
            }
        self.reply_bin_0 = '\x01\xdd\xfa\xa8' '\x00\x00\x00\x00' \
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
            'time': 1975457497,
            }
        self.req_bin_0 = '\x1b\x00\x02\x00' '\xd9\x16\xbf\x75'


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
            'grab_window': 153110452,
            'confine_to': 147004650,
            'event_mask': 17994,
            'pointer_mode': 1,
            'modifiers': 57365,
            'button': 235,
            'keyboard_mode': 0,
            'cursor': 1439559401,
            }
        self.req_bin_0 = '\x1c\x01\x06\x00' '\xb4\x47\x20\x09' \
            '\x4a\x46\x01\x00' '\xea\x1c\xc3\x08' \
            '\xe9\xee\xcd\x55' '\xeb\x00\x15\xe0'


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
            'grab_window': 1901496169,
            'button': 156,
            'modifiers': 2905,
            }
        self.req_bin_0 = '\x1d\x9c\x03\x00' '\x69\x87\x56\x71' \
            '\x59\x0b\x00\x00'


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
            'time': 1105019192,
            'event_mask': 16005,
            'cursor': 648954808,
            }
        self.req_bin_0 = '\x1e\x00\x04\x00' '\xb8\x43\xae\x26' \
            '\x38\x41\xdd\x41' '\x85\x3e\x00\x00'


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
            'grab_window': 1085601014,
            'time': 2005732374,
            'pointer_mode': 0,
            'keyboard_mode': 1,
            }
        self.req_bin_0 = '\x1f\x01\x04\x00' '\xf6\xf4\xb4\x40' \
            '\x16\x0c\x8d\x77' '\x00\x01\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 47502,
            'status': 194,
            }
        self.reply_bin_0 = '\x01\xc2\x8e\xb9' '\x00\x00\x00\x00' \
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
            'time': 112385041,
            }
        self.req_bin_0 = '\x20\x00\x02\x00' '\x11\xdc\xb2\x06'


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
            'grab_window': 358541782,
            'pointer_mode': 1,
            'keyboard_mode': 0,
            'modifiers': 35557,
            'key': 148,
            }
        self.req_bin_0 = '\x21\x00\x04\x00' '\xd6\xe9\x5e\x15' \
            '\xe5\x8a\x94\x01' '\x00\x00\x00\x00'


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
            'grab_window': 1620755995,
            'key': 225,
            'modifiers': 11285,
            }
        self.req_bin_0 = '\x22\xe1\x03\x00' '\x1b\xc6\x9a\x60' \
            '\x15\x2c\x00\x00'


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
            'time': 1308967540,
            'mode': 0,
            }
        self.req_bin_0 = '\x23\x00\x02\x00' '\x74\x42\x05\x4e'


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
            'window': 591615695,
            }
        self.req_bin_0 = '\x26\x00\x02\x00' '\xcf\x56\x43\x23'

        self.reply_args_0 = {
            'win_y': -19118,
            'same_screen': 0,
            'sequence_number': 24807,
            'root': 629416207,
            'root_x': -1840,
            'root_y': -15421,
            'mask': 61131,
            'child': 1771256696,
            'win_x': -23501,
            }
        self.reply_bin_0 = '\x01\x00\xe7\x60' '\x00\x00\x00\x00' \
            '\x0f\x21\x84\x25' '\x78\x3b\x93\x69' \
            '\xd0\xf8\xc3\xc3' '\x33\xa4\x52\xb5' \
            '\xcb\xee\x00\x00' '\x00\x00\x00\x00'


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
            'window': 1039518963,
            'start': 1932157705,
            'stop': 1900678847,
            }
        self.req_bin_0 = '\x27\x00\x04\x00' '\xf3\xcc\xf5\x3d' \
            '\x09\x63\x2a\x73' '\xbf\x0e\x4a\x71'

        self.reply_args_0 = {
            'sequence_number': 64458,
            'events': [{'time': 923291236, 'x': -18578, 'y': -6471}, {'time': 1773390907, 'x': -1393, 'y': -32310}, {'time': 586569986, 'x': -30687, 'y': -24296}, {'time': 1657780196, 'x': -31421, 'y': -22126}, {'time': 1570918743, 'x': -8734, 'y': -24476}],
            }
        self.reply_bin_0 = '\x01\x00\xca\xfb' '\x0a\x00\x00\x00' \
            '\x05\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x64\x4e\x08\x37' '\x6e\xb7\xb9\xe6' \
            '\x3b\xcc\xb3\x69' '\x8f\xfa\xca\x81' \
            '\x02\x59\xf6\x22' '\x21\x88\x18\xa1' \
            '\xe4\xb7\xcf\x62' '\x43\x85\x92\xa9' \
            '\x57\x51\xa2\x5d' '\xe2\xdd\x64\xa0'


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
            'src_y': -19757,
            'src_x': -8581,
            'src_wid': 1760544765,
            'dst_wid': 690720620,
            }
        self.req_bin_0 = '\x28\x00\x04\x00' '\xfd\xc7\xef\x68' \
            '\x6c\x8f\x2b\x29' '\x7b\xde\xd3\xb2'

        self.reply_args_0 = {
            'child': 574496393,
            'same_screen': 1,
            'sequence_number': 8714,
            'x': -18848,
            'y': -22764,
            }
        self.reply_bin_0 = '\x01\x01\x0a\x22' '\x00\x00\x00\x00' \
            '\x89\x1e\x3e\x22' '\x60\xb6\x14\xa7' \
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
            'src_height': 53009,
            'src_window': 1980908172,
            'dst_window': 876846941,
            'src_width': 41756,
            'src_y': -14846,
            'src_x': -27017,
            'dst_x': -15888,
            'dst_y': -1154,
            }
        self.req_bin_0 = '\x29\x00\x06\x00' '\x8c\x42\x12\x76' \
            '\x5d\x9f\x43\x34' '\x77\x96\x02\xc6' \
            '\x1c\xa3\x11\xcf' '\xf0\xc1\x7e\xfb'


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
            'time': 1914609690,
            'focus': 613817318,
            }
        self.req_bin_0 = '\x2a\x00\x03\x00' '\xe6\x1b\x96\x24' \
            '\x1a\xa0\x1e\x72'


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
            'revert_to': 222,
            'sequence_number': 52919,
            'focus': 1137574880,
            }
        self.reply_bin_0 = '\x01\xde\xb7\xce' '\x00\x00\x00\x00' \
            '\xe0\x03\xce\x43' '\x00\x00\x00\x00' \
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
            'sequence_number': 4263,
            'map': [211, 220, 146, 166, 185, 132, 224, 238, 253, 222, 194, 251, 141, 143, 237, 255, 178, 130, 249, 220, 233, 203, 197, 164, 194, 241, 161, 165, 218, 231, 216, 168],
            }
        self.reply_bin_0 = '\x01\x00\xa7\x10' '\x02\x00\x00\x00' \
            '\xd3\xdc\x92\xa6' '\xb9\x84\xe0\xee' \
            '\xfd\xde\xc2\xfb' '\x8d\x8f\xed\xff' \
            '\xb2\x82\xf9\xdc' '\xe9\xcb\xc5\xa4' \
            '\xc2\xf1\xa1\xa5' '\xda\xe7\xd8\xa8'


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
            'fid': 660582488,
            'name': 'foofont',
            }
        self.req_bin_0 = '\x2d\x00\x05\x00' '\x58\xb0\x5f\x27' \
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
            'font': 1680528662,
            }
        self.req_bin_0 = '\x2e\x00\x02\x00' '\x16\xd5\x2a\x64'


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
            'font': 1813755272,
            }
        self.req_bin_0 = '\x2f\x00\x02\x00' '\x88\xb5\x1b\x6c'

        self.reply_args_0 = {
            'sequence_number': 50377,
            'properties': [{'value': 995308643, 'name': 1054264899}],
            'min_byte1': 168,
            'max_byte1': 207,
            'char_infos': [{'descent': -23120, 'ascent': -17135, 'character_width': -10592, 'left_side_bearing': -4391, 'right_side_bearing': -6857, 'attributes': 375}, {'descent': -1532, 'ascent': -32270, 'character_width': -28345, 'left_side_bearing': -10079, 'right_side_bearing': -19763, 'attributes': 45400}, {'descent': -20622, 'ascent': -29713, 'character_width': -11593, 'left_side_bearing': -25007, 'right_side_bearing': -10219, 'attributes': 32589}],
            'max_char_or_byte2': 47759,
            'default_char': 20012,
            'min_char_or_byte2': 21472,
            'draw_direction': 158,
            'min_bounds': {'descent': -25122, 'ascent': -29259, 'character_width': -23352, 'left_side_bearing': -20145, 'right_side_bearing': -14415, 'attributes': 45627},
            'all_chars_exist': 1,
            'font_ascent': -3881,
            'font_descent': -29796,
            'max_bounds': {'descent': -32039, 'ascent': -27162, 'character_width': -20182, 'left_side_bearing': -5907, 'right_side_bearing': -22176, 'attributes': 42093},
            }
        self.reply_bin_0 = '\x01\x00\xc9\xc4' '\x12\x00\x00\x00' \
            '\x4f\xb1\xb1\xc7' '\xc8\xa4\xb5\x8d' \
            '\xde\x9d\x3b\xb2' '\x00\x00\x00\x00' \
            '\xed\xe8\x60\xa9' '\x2a\xb1\xe6\x95' \
            '\xd9\x82\x6d\xa4' '\x00\x00\x00\x00' \
            '\xe0\x53\x8f\xba' '\x2c\x4e\x01\x00' \
            '\x9e\xa8\xcf\x01' '\xd7\xf0\x9c\x8b' \
            '\x03\x00\x00\x00' '\x43\xce\xd6\x3e' \
            '\x63\x34\x53\x3b' '\xd9\xee\x37\xe5' \
            '\xa0\xd6\x11\xbd' '\xb0\xa5\x77\x01' \
            '\xa1\xd8\xcd\xb2' '\x47\x91\xf2\x81' \
            '\x04\xfa\x58\xb1' '\x51\x9e\x15\xd8' \
            '\xb7\xd2\xef\x8b' '\x72\xaf\x4d\x7f'


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
            'font': 1390443646,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = '\x30\x01\x04\x00' '\x7e\x7c\xe0\x52' \
            '\x00\x66\x00\x6f' '\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'overall_width': -125606587,
            'draw_direction': 180,
            'sequence_number': 49919,
            'font_ascent': -28825,
            'overall_ascent': -28631,
            'overall_descent': -25654,
            'overall_right': -1587455483,
            'overall_left': -1126866075,
            'font_descent': -10751,
            }
        self.reply_bin_0 = '\x01\xb4\xff\xc2' '\x00\x00\x00\x00' \
            '\x67\x8f\x01\xd6' '\x29\x90\xca\x9b' \
            '\x45\x65\x83\xf8' '\x65\x63\xd5\xbc' \
            '\x05\x5a\x61\xa1' '\x00\x00\x00\x00'


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
            'max_names': 18185,
            'pattern': 'bhazr',
            }
        self.req_bin_0 = '\x31\x00\x04\x00' '\x09\x47\x05\x00' \
            '\x62\x68\x61\x7a' '\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 49432,
            }
        self.reply_bin_0 = '\x01\x00\x18\xc1' '\x05\x00\x00\x00' \
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
            'max_names': 3114,
            'pattern': 'bhazr2',
            }
        self.req_bin_0 = '\x32\x00\x04\x00' '\x2a\x0c\x06\x00' \
            '\x62\x68\x61\x7a' '\x72\x32\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 25581,
            'properties': [{'value': 211748211, 'name': 1081860977}],
            'min_byte1': 148,
            'max_byte1': 143,
            'max_char_or_byte2': 61321,
            'default_char': 7553,
            'min_char_or_byte2': 41553,
            'draw_direction': 184,
            'replies_hint': 1103357017,
            'min_bounds': {'descent': -15722, 'ascent': -29342, 'character_width': -15831, 'left_side_bearing': -29788, 'right_side_bearing': -11288, 'attributes': 25764},
            'all_chars_exist': 1,
            'name': 'fontfont',
            'font_ascent': -21897,
            'font_descent': -1063,
            'max_bounds': {'descent': -21908, 'ascent': -5079, 'character_width': -32302, 'left_side_bearing': -22403, 'right_side_bearing': -32742, 'attributes': 64254},
            }
        self.reply_bin_0 = '\x01\x08\xed\x63' '\x0b\x00\x00\x00' \
            '\xa4\x8b\xe8\xd3' '\x29\xc2\x62\x8d' \
            '\x96\xc2\xa4\x64' '\x00\x00\x00\x00' \
            '\x7d\xa8\x1a\x80' '\xd2\x81\x29\xec' \
            '\x6c\xaa\xfe\xfa' '\x00\x00\x00\x00' \
            '\x51\xa2\x89\xef' '\x81\x1d\x01\x00' \
            '\xb8\x94\x8f\x01' '\x77\xaa\xd9\xfb' \
            '\x59\xe4\xc3\x41' '\x71\xe3\x7b\x40' \
            '\x73\x05\x9f\x0c' '\x66\x6f\x6e\x74' \
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
            'sequence_number': 16390,
            'paths': ['path1', 'path2232'],
            }
        self.reply_bin_0 = '\x01\x00\x06\x40' '\x04\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x05\x70\x61\x74' '\x68\x31\x08\x70' \
            '\x61\x74\x68\x32' '\x32\x33\x32\x00'

        self.reply_args_1 = {
            'sequence_number': 47473,
            'paths': [],
            }
        self.reply_bin_1 = '\x01\x00\x71\xb9' '\x00\x00\x00\x00' \
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
            'height': 10888,
            'drawable': 1026358127,
            'pid': 226024885,
            'depth': 201,
            'width': 43563,
            }
        self.req_bin_0 = '\x35\xc9\x04\x00' '\xb5\xdd\x78\x0d' \
            '\x6f\xfb\x2c\x3d' '\x2b\xaa\x88\x2a'


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
            'pixmap': 2093809224,
            }
        self.req_bin_0 = '\x36\x00\x02\x00' '\x48\xfe\xcc\x7c'


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
            'cid': 1512752950,
            'drawable': 563936881,
            'attrs': {'dashes': 188, 'fill_rule': 1, 'clip_mask': 83231865, 'plane_mask': 1813900561, 'line_style': 2, 'tile': 2117700777, 'arc_mode': 0, 'clip_y_origin': -26355, 'dash_offset': 64709, 'line_width': 51518, 'background': 24174242, 'clip_x_origin': -2065, 'join_style': 1, 'graphics_exposures': 1, 'font': 1255791817, 'tile_stipple_y_origin': -19096, 'stipple': 1739014875, 'fill_style': 0, 'cap_style': 0, 'subwindow_mode': 0, 'tile_stipple_x_origin': -6401, 'foreground': 254964641, 'function': 3},
            }
        self.req_bin_0 = '\x37\x00\x1b\x00' '\x36\xc7\x2a\x5a' \
            '\x71\xfe\x9c\x21' '\xff\xff\x7f\x00' \
            '\x03\x00\x00\x00' '\x11\xed\x1d\x6c' \
            '\xa1\x73\x32\x0f' '\xa2\xde\x70\x01' \
            '\x3e\xc9\x00\x00' '\x02\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x01\x00\x00\x00' \
            '\xa9\x8c\x39\x7e' '\xdb\x42\xa7\x67' \
            '\xff\xe6\x00\x00' '\x68\xb5\x00\x00' \
            '\xc9\xdc\xd9\x4a' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\xef\xf7\x00\x00' \
            '\x0d\x99\x00\x00' '\x79\x04\xf6\x04' \
            '\xc5\xfc\x00\x00' '\xbc\x00\x00\x00' \
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
            'attrs': {'dashes': 157, 'fill_rule': 1, 'clip_mask': 1135076694, 'plane_mask': 1547614209, 'line_style': 1, 'tile': 978363404, 'arc_mode': 1, 'clip_y_origin': -23955, 'dash_offset': 48845, 'line_width': 59186, 'background': 1302864533, 'clip_x_origin': -14011, 'join_style': 1, 'graphics_exposures': 1, 'font': 140584624, 'tile_stipple_y_origin': -2996, 'stipple': 251789661, 'fill_style': 1, 'cap_style': 3, 'subwindow_mode': 0, 'tile_stipple_x_origin': -520, 'foreground': 595163666, 'function': 3},
            'gc': 188653228,
            }
        self.req_bin_0 = '\x38\x00\x1a\x00' '\xac\x9e\x3e\x0b' \
            '\xff\xff\x7f\x00' '\x03\x00\x00\x00' \
            '\x01\xb8\x3e\x5c' '\x12\x7a\x79\x23' \
            '\x95\x22\xa8\x4d' '\x32\xe7\x00\x00' \
            '\x01\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x0c\xa4\x50\x3a' \
            '\x5d\x01\x02\x0f' '\xf8\xfd\x00\x00' \
            '\x4c\xf4\x00\x00' '\xb0\x26\x61\x08' \
            '\x00\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x45\xc9\x00\x00' '\x6d\xa2\x00\x00' \
            '\x56\xe5\xa7\x43' '\xcd\xbe\x00\x00' \
            '\x9d\x00\x00\x00' '\x01\x00\x00\x00'


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
            'mask': 735797814,
            'src_gc': 269185894,
            'dst_gc': 226333295,
            }
        self.req_bin_0 = '\x39\x00\x04\x00' '\x66\x73\x0b\x10' \
            '\x6f\x92\x7d\x0d' '\x36\x62\xdb\x2b'


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
            'dashes': [194, 215, 187, 203, 161, 132, 245, 196, 240],
            'dash_offset': 42612,
            'gc': 1583039454,
            }
        self.req_bin_0 = '\x3a\x00\x06\x00' '\xde\x43\x5b\x5e' \
            '\x74\xa6\x09\x00' '\xc2\xd7\xbb\xcb' \
            '\xa1\x84\xf5\xc4' '\xf0\x00\x00\x00'


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
            'rectangles': [{'height': 13060, 'x': -16188, 'width': 21082, 'y': -31118}, {'height': 53259, 'x': -22772, 'width': 9954, 'y': -24477}],
            'gc': 978363680,
            'x_origin': -20925,
            'y_origin': -8416,
            'ordering': 1,
            }
        self.req_bin_0 = '\x3b\x01\x07\x00' '\x20\xa5\x50\x3a' \
            '\x43\xae\x20\xdf' '\xc4\xc0\x72\x86' \
            '\x5a\x52\x04\x33' '\x0c\xa7\x63\xa0' \
            '\xe2\x26\x0b\xd0'

        self.req_args_1 = {
            'rectangles': [],
            'gc': 134284501,
            'x_origin': -14607,
            'y_origin': -26670,
            'ordering': 1,
            }
        self.req_bin_1 = '\x3b\x01\x03\x00' '\xd5\x04\x01\x08' \
            '\xf1\xc6\xd2\x97'


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
            'gc': 760419619,
            }
        self.req_bin_0 = '\x3c\x00\x02\x00' '\x23\x15\x53\x2d'


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
            'height': 17576,
            'width': 3775,
            'window': 297453120,
            'x': -259,
            'y': -15648,
            }
        self.req_bin_0 = '\x3d\x00\x04\x00' '\x40\xc6\xba\x11' \
            '\xfd\xfe\xe0\xc2' '\xbf\x0e\xa8\x44'


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
            'src_drawable': 1106753280,
            'dst_drawable': 1231592374,
            'src_y': -29065,
            'src_x': -14690,
            'gc': 1326857727,
            'width': 15120,
            'height': 875,
            'dst_x': -25102,
            'dst_y': -24985,
            }
        self.req_bin_0 = '\x3e\x00\x07\x00' '\x00\xb7\xf7\x41' \
            '\xb6\x9b\x68\x49' '\xff\x3d\x16\x4f' \
            '\x9e\xc6\x77\x8e' '\xf2\x9d\x67\x9e' \
            '\x10\x3b\x6b\x03'


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
            'src_drawable': 646594097,
            'bit_plane': 1948097912,
            'dst_drawable': 1090801080,
            'src_y': -16917,
            'src_x': -30997,
            'gc': 1883735050,
            'width': 64910,
            'height': 12424,
            'dst_x': -17405,
            'dst_y': -802,
            }
        self.req_bin_0 = '\x3f\x00\x08\x00' '\x31\x3e\x8a\x26' \
            '\xb8\x4d\x04\x41' '\x0a\x84\x47\x70' \
            '\xeb\x86\xeb\xbd' '\x03\xbc\xde\xfc' \
            '\x8e\xfd\x88\x30' '\x78\x9d\x1d\x74'


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
            'gc': 1865801827,
            'points': [{'x': -26835, 'y': -30751}, {'x': -24066, 'y': -5345}, {'x': -28859, 'y': -31234}],
            'drawable': 1094232167,
            'coord_mode': 1,
            }
        self.req_bin_0 = '\x40\x01\x06\x00' '\x67\xa8\x38\x41' \
            '\x63\xe0\x35\x6f' '\x2d\x97\xe1\x87' \
            '\xfe\xa1\x1f\xeb' '\x45\x8f\xfe\x85'


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
            'gc': 235090384,
            'points': [{'x': -4235, 'y': -24752}, {'x': -325, 'y': -17727}, {'x': -29990, 'y': -26621}, {'x': -14654, 'y': -16236}, {'x': -5290, 'y': -26868}],
            'drawable': 2076076346,
            'coord_mode': 0,
            }
        self.req_bin_0 = '\x41\x00\x08\x00' '\x3a\x69\xbe\x7b' \
            '\xd0\x31\x03\x0e' '\x75\xef\x50\x9f' \
            '\xbb\xfe\xc1\xba' '\xda\x8a\x03\x98' \
            '\xc2\xc6\x94\xc0' '\x56\xeb\x0c\x97'


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
            'segments': [{'y1': -24178, 'y2': -15998, 'x1': -24054, 'x2': -32444}],
            'drawable': 1265403450,
            'gc': 163461204,
            }
        self.req_bin_0 = '\x42\x00\x05\x00' '\x3a\x86\x6c\x4b' \
            '\x54\x38\xbe\x09' '\x0a\xa2\x8e\xa1' \
            '\x44\x81\x82\xc1'


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
            'drawable': 1586963121,
            'gc': 1337116310,
            'rectangles': [{'height': 47141, 'x': -30858, 'width': 22703, 'y': -22260}, {'height': 63948, 'x': -14019, 'width': 23263, 'y': -3488}, {'height': 44968, 'x': -20595, 'width': 38456, 'y': -16710}],
            }
        self.req_bin_0 = '\x43\x00\x09\x00' '\xb1\x22\x97\x5e' \
            '\x96\xc6\xb2\x4f' '\x76\x87\x0c\xa9' \
            '\xaf\x58\x25\xb8' '\x3d\xc9\x60\xf2' \
            '\xdf\x5a\xcc\xf9' '\x8d\xaf\xba\xbe' \
            '\x38\x96\xa8\xaf'


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
            'arcs': [{'height': 53734, 'angle1': -15167, 'x': -14115, 'angle2': -11099, 'width': 37805, 'y': -328}, {'height': 40872, 'angle1': -30564, 'x': -3747, 'angle2': -4697, 'width': 63216, 'y': -24973}, {'height': 24777, 'angle1': -32080, 'x': -7867, 'angle2': -7064, 'width': 36916, 'y': -25281}],
            'drawable': 772678682,
            'gc': 44290074,
            }
        self.req_bin_0 = '\x44\x00\x0c\x00' '\x1a\x24\x0e\x2e' \
            '\x1a\xd0\xa3\x02' '\xdd\xc8\xb8\xfe' \
            '\xad\x93\xe6\xd1' '\xc1\xc4\xa5\xd4' \
            '\x5d\xf1\x73\x9e' '\xf0\xf6\xa8\x9f' \
            '\x9c\x88\xa7\xed' '\x45\xe1\x3f\x9d' \
            '\x34\x90\xc9\x60' '\xb0\x82\x68\xe4'


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
            'gc': 1560298486,
            'points': [{'x': -24217, 'y': -6404}, {'x': -11796, 'y': -10041}, {'x': -15697, 'y': -17636}],
            'drawable': 1318542944,
            'coord_mode': 0,
            }
        self.req_bin_0 = '\x45\x00\x07\x00' '\x60\x5e\x97\x4e' \
            '\xf6\x43\x00\x5d' '\x02\x00\x00\x00' \
            '\x67\xa1\xfc\xe6' '\xec\xd1\xc7\xd8' \
            '\xaf\xc2\x1c\xbb'


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
            'drawable': 1757405486,
            'gc': 189394778,
            'rectangles': [{'height': 65400, 'x': -21866, 'width': 7039, 'y': -20043}, {'height': 23977, 'x': -27368, 'width': 5697, 'y': -24557}],
            }
        self.req_bin_0 = '\x46\x00\x07\x00' '\x2e\xe1\xbf\x68' \
            '\x5a\xef\x49\x0b' '\x96\xaa\xb5\xb1' \
            '\x7f\x1b\x78\xff' '\x18\x95\x13\xa0' \
            '\x41\x16\xa9\x5d'


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
            'arcs': [{'height': 6533, 'angle1': -21286, 'x': -31886, 'angle2': -4778, 'width': 11285, 'y': -21482}],
            'drawable': 1187948405,
            'gc': 1326939593,
            }
        self.req_bin_0 = '\x47\x00\x06\x00' '\x75\xa7\xce\x46' \
            '\xc9\x7d\x17\x4f' '\x72\x83\x16\xac' \
            '\x15\x2c\x85\x19' '\xda\xac\x56\xed'


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
            'height': 59040,
            'data': 'bit map data',
            'drawable': 1820327999,
            'left_pad': 212,
            'format': 0,
            'dst_x': -24929,
            'gc': 2113747248,
            'depth': 154,
            'width': 30377,
            'dst_y': -7047,
            }
        self.req_bin_0 = '\x48\x00\x09\x00' '\x3f\x00\x80\x6c' \
            '\x30\x39\xfd\x7d' '\xa9\x76\xa0\xe6' \
            '\x9f\x9e\x79\xe4' '\xd4\x9a\x00\x00' \
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
            'height': 17193,
            'plane_mask': 132230866,
            'drawable': 976624286,
            'x': -22878,
            'y': -7157,
            'format': 1,
            'width': 56515,
            }
        self.req_bin_0 = '\x49\x01\x05\x00' '\x9e\x1a\x36\x3a' \
            '\xa2\xa6\x0b\xe4' '\xc3\xdc\x29\x43' \
            '\xd2\xae\xe1\x07'

        self.reply_args_0 = {
            'sequence_number': 26455,
            'data': 'this is real ly imag e b-map',
            'visual': 1813537620,
            'depth': 210,
            }
        self.reply_bin_0 = '\x01\xd2\x57\x67' '\x07\x00\x00\x00' \
            '\x54\x63\x18\x6c' '\x00\x00\x00\x00' \
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
            'gc': 751101917,
            'x': -12878,
            'drawable': 2138919940,
            'items': [{'delta': 2, 'string': 'zoo'}, 16909060, {'delta': 0, 'string': 'ie'}],
            'y': -22850,
            }
        self.req_bin_0 = '\x4a\x00\x08\x00' '\x04\x54\x7d\x7f' \
            '\xdd\xe7\xc4\x2c' '\xb2\xcd\xbe\xa6' \
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
            'gc': 1536955328,
            'x': -7538,
            'drawable': 2036666267,
            'items': [{'delta': 2, 'string': (4131, 18)}, 16909060],
            'y': -19412,
            }
        self.req_bin_0 = '\x4b\x00\x07\x00' '\x9b\x0f\x65\x79' \
            '\xc0\x13\x9c\x5b' '\x8e\xe2\x2c\xb4' \
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
            'gc': 59182486,
            'drawable': 1440093738,
            'x': -18388,
            'y': -30915,
            }
        self.req_bin_0 = '\x4c\x06\x06\x00' '\x2a\x16\xd6\x55' \
            '\x96\x0d\x87\x03' '\x2c\xb8\x3d\x87' \
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
            'gc': 422213662,
            'drawable': 297997933,
            'x': -29988,
            'y': -7714,
            }
        self.req_bin_0 = '\x4d\x08\x08\x00' '\x6d\x16\xc3\x11' \
            '\x1e\x78\x2a\x19' '\xdc\x8a\xde\xe1' \
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
            'mid': 2035115729,
            'alloc': 1,
            'visual': 1350027281,
            'window': 1338197963,
            }
        self.req_bin_0 = '\x4e\x01\x04\x00' '\xd1\x66\x4d\x79' \
            '\xcb\x47\xc3\x4f' '\x11\xc8\x77\x50'


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
            'cmap': 1676125715,
            }
        self.req_bin_0 = '\x4f\x00\x02\x00' '\x13\xa6\xe7\x63'


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
            'src_cmap': 928435434,
            'mid': 1786543933,
            }
        self.req_bin_0 = '\x50\x00\x03\x00' '\x3d\x7f\x7c\x6a' \
            '\xea\xcc\x56\x37'


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
            'cmap': 391260723,
            }
        self.req_bin_0 = '\x51\x00\x02\x00' '\x33\x2a\x52\x17'


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
            'cmap': 1992797340,
            }
        self.req_bin_0 = '\x52\x00\x02\x00' '\x9c\xac\xc7\x76'


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
            'window': 1285835740,
            }
        self.req_bin_0 = '\x53\x00\x02\x00' '\xdc\x4b\xa4\x4c'

        self.reply_args_0 = {
            'cmaps': [966254780, 266052823],
            'sequence_number': 5548,
            }
        self.reply_bin_0 = '\x01\x00\xac\x15' '\x02\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xbc\xe0\x97\x39' '\xd7\xa4\xdb\x0f'


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
            'red': 21862,
            'green': 57302,
            'cmap': 656383350,
            'blue': 5008,
            }
        self.req_bin_0 = '\x54\x00\x04\x00' '\x76\x9d\x1f\x27' \
            '\x66\x55\xd6\xdf' '\x90\x13\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 8439,
            'red': 53502,
            'green': 10630,
            'pixel': 961310294,
            'blue': 47165,
            }
        self.reply_bin_0 = '\x01\x00\xf7\x20' '\x00\x00\x00\x00' \
            '\xfe\xd0\x86\x29' '\x3d\xb8\x00\x00' \
            '\x56\x6e\x4c\x39' '\x00\x00\x00\x00' \
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
            'cmap': 1895533759,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x55\x00\x05\x00' '\xbf\x8c\xfb\x70' \
            '\x07\x00\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 54650,
            'pixel': 368878330,
            'screen_green': 22466,
            'screen_red': 33111,
            'exact_green': 59422,
            'exact_blue': 17338,
            'screen_blue': 42112,
            'exact_red': 4523,
            }
        self.reply_bin_0 = '\x01\x00\x7a\xd5' '\x00\x00\x00\x00' \
            '\xfa\xa2\xfc\x15' '\xab\x11\x1e\xe8' \
            '\xba\x43\x57\x81' '\xc2\x57\x80\xa4' \
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
            'planes': 26584,
            'colors': 35776,
            'cmap': 889584285,
            'contiguous': 1,
            }
        self.req_bin_0 = '\x56\x01\x03\x00' '\x9d\xfa\x05\x35' \
            '\xc0\x8b\xd8\x67'

        self.reply_args_0 = {
            'masks': [1500271932, 899360639, 47484188],
            'pixels': [573754460, 1168946758, 1964382625, 1165039199, 1033611559, 84665295, 63625308, 1794941852, 252199630, 1904497807, 712237651, 315260717, 1697410484, 1190883937, 423096008, 1152002184, 744271207],
            'sequence_number': 58336,
            }
        self.reply_bin_0 = '\x01\x00\xe0\xe3' '\x14\x00\x00\x00' \
            '\x11\x00\x03\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x5c\xcc\x32\x22' '\x46\xb6\xac\x45' \
            '\xa1\x19\x16\x75' '\x5f\x16\x71\x45' \
            '\x27\xa9\x9b\x3d' '\xcf\xe3\x0b\x05' \
            '\x5c\xd8\xca\x03' '\x9c\xa3\xfc\x6a' \
            '\xce\x42\x08\x0f' '\x8f\x54\x84\x71' \
            '\x53\xe2\x73\x2a' '\x2d\x7f\xca\x12' \
            '\xb4\x6d\x2c\x65' '\x61\x72\xfb\x46' \
            '\xc8\xee\x37\x19' '\x88\x28\xaa\x44' \
            '\x67\xad\x5c\x2c' '\x3c\x55\x6c\x59' \
            '\x7f\x27\x9b\x35' '\x1c\x8d\xd4\x02'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 39566,
            }
        self.reply_bin_1 = '\x01\x00\x8e\x9a' '\x00\x00\x00\x00' \
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
            'red': 27954,
            'colors': 61744,
            'green': 51989,
            'cmap': 1925921683,
            'contiguous': 1,
            'blue': 42414,
            }
        self.req_bin_0 = '\x57\x01\x04\x00' '\x93\x3b\xcb\x72' \
            '\x30\xf1\x32\x6d' '\x15\xcb\xae\xa5'

        self.reply_args_0 = {
            'green_mask': 500386899,
            'sequence_number': 36320,
            'pixels': [870307617, 413856470, 486007305, 42178968],
            'blue_mask': 1533073068,
            'red_mask': 28282988,
            }
        self.reply_bin_0 = '\x01\x00\xe0\x8d' '\x04\x00\x00\x00' \
            '\x04\x00\x00\x00' '\x6c\x90\xaf\x01' \
            '\x53\x4c\xd3\x1d' '\xac\xd6\x60\x5b' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x21\xd7\xdf\x33' '\xd6\xf2\xaa\x18' \
            '\x09\xe2\xf7\x1c' '\x98\x99\x83\x02'


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
            'cmap': 1419481893,
            'pixels': [1093462060, 406978499, 1648224149, 1220843518, 2022370793, 1011215691, 284009195, 169428415, 996883880, 2092602709, 1603478372, 1918494822, 733511358, 1359010747, 1496846062, 179372425, 282089306],
            'plane_mask': 1902996433,
            }
        self.req_bin_0 = '\x58\x00\x14\x00' '\x25\x93\x9b\x54' \
            '\xd1\x6b\x6d\x71' '\x2c\xe8\x2c\x41' \
            '\xc3\xff\x41\x18' '\x95\xe7\x3d\x62' \
            '\xfe\x97\xc4\x48' '\xe9\xed\x8a\x78' \
            '\x4b\xed\x45\x3c' '\xeb\xa2\xed\x10' \
            '\xbf\x45\x19\x0a' '\xa8\x3d\x6b\x3b' \
            '\x55\x95\xba\x7c' '\x64\x23\x93\x5f' \
            '\x66\xe8\x59\x72' '\xbe\x7e\xb8\x2b' \
            '\xbb\xdb\x00\x51' '\xee\x0e\x38\x59' \
            '\x89\x01\xb1\x0a' '\x5a\x57\xd0\x10'


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
            'cmap': 95312901,
            'items': [{'red': 45128, 'pixel': 1091968760, 'green': 20858, 'flags': 149, 'blue': 33313}, {'red': 45187, 'pixel': 922101810, 'green': 27906, 'flags': 179, 'blue': 7632}, {'red': 36932, 'pixel': 1947001931, 'green': 60447, 'flags': 140, 'blue': 33086}, {'red': 14976, 'pixel': 198101566, 'green': 3534, 'flags': 250, 'blue': 28732}],
            }
        self.req_bin_0 = '\x59\x00\x0e\x00' '\x05\x5c\xae\x05' \
            '\xf8\x1e\x16\x41' '\x48\xb0\x7a\x51' \
            '\x21\x82\x95\x00' '\x32\x28\xf6\x36' \
            '\x83\xb0\x02\x6d' '\xd0\x1d\xb3\x00' \
            '\x4b\xe4\x0c\x74' '\x44\x90\x1f\xec' \
            '\x3e\x81\x8c\x00' '\x3e\xca\xce\x0b' \
            '\x80\x3a\xce\x0d' '\x3c\x70\xfa\x00'


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
            'flags': 208,
            'cmap': 672248001,
            'pixel': 1418075042,
            }
        self.req_bin_0 = '\x5a\xd0\x05\x00' '\xc1\xb0\x11\x28' \
            '\xa2\x1b\x86\x54' '\x04\x00\x00\x00' \
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
            'cmap': 118431257,
            'pixels': [1881580369, 1837360035, 1919132928, 1793208889, 1882117561, 1711937043, 391950363, 701498580],
            }
        self.req_bin_0 = '\x5b\x00\x0a\x00' '\x19\x1e\x0f\x07' \
            '\x51\xa3\x26\x70' '\xa3\xe3\x83\x6d' \
            '\x00\xa5\x63\x72' '\x39\x32\xe2\x6a' \
            '\xb9\xd5\x2e\x70' '\x13\x16\x0a\x66' \
            '\x1b\xb0\x5c\x17' '\xd4\x04\xd0\x29'

        self.reply_args_0 = {
            'colors': [{'red': 43453, 'blue': 63972, 'green': 15316}, {'red': 50644, 'blue': 64162, 'green': 45019}, {'red': 56401, 'blue': 15839, 'green': 13850}, {'red': 41449, 'blue': 2614, 'green': 4424}, {'red': 10914, 'blue': 64026, 'green': 64062}],
            'sequence_number': 62190,
            }
        self.reply_bin_0 = '\x01\x00\xee\xf2' '\x0a\x00\x00\x00' \
            '\x05\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xbd\xa9\xd4\x3b' '\xe4\xf9\x00\x00' \
            '\xd4\xc5\xdb\xaf' '\xa2\xfa\x00\x00' \
            '\x51\xdc\x1a\x36' '\xdf\x3d\x00\x00' \
            '\xe9\xa1\x48\x11' '\x36\x0a\x00\x00' \
            '\xa2\x2a\x3e\xfa' '\x1a\xfa\x00\x00'

        self.req_args_1 = {
            'cmap': 1845758272,
            'pixels': [],
            }
        self.req_bin_1 = '\x5b\x00\x02\x00' '\x40\x09\x04\x6e'


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
            'cmap': 430165363,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x5c\x00\x05\x00' '\x73\xcd\xa3\x19' \
            '\x07\x00\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 17448,
            'screen_green': 64996,
            'screen_red': 23871,
            'exact_green': 15113,
            'exact_blue': 21540,
            'screen_blue': 17039,
            'exact_red': 19827,
            }
        self.reply_bin_0 = '\x01\x00\x28\x44' '\x00\x00\x00\x00' \
            '\x73\x4d\x09\x3b' '\x24\x54\x3f\x5d' \
            '\xe4\xfd\x8f\x42' '\x00\x00\x00\x00' \
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
            'x': 28924,
            'fore_red': 43783,
            'back_green': 23550,
            'mask': 1541754765,
            'back_blue': 9285,
            'y': 54115,
            'cid': 1826455369,
            'fore_blue': 15825,
            'fore_green': 14135,
            'back_red': 20699,
            'source': 1468306744,
            }
        self.req_bin_0 = '\x5d\x00\x08\x00' '\x49\x7f\xdd\x6c' \
            '\x38\x95\x84\x57' '\x8d\x4f\xe5\x5b' \
            '\x07\xab\x37\x37' '\xd1\x3d\xdb\x50' \
            '\xfe\x5b\x45\x24' '\xfc\x70\x63\xd3'


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
            'fore_red': 26637,
            'source_char': 44638,
            'mask': 711790560,
            'back_blue': 2189,
            'cid': 2012386198,
            'mask_char': 33026,
            'fore_blue': 35042,
            'fore_green': 15709,
            'back_red': 32827,
            'source': 30003602,
            'back_green': 2545,
            }
        self.req_bin_0 = '\x5e\x00\x08\x00' '\x96\x93\xf2\x77' \
            '\x92\xd1\xc9\x01' '\xe0\x0f\x6d\x2a' \
            '\x5e\xae\x02\x81' '\x0d\x68\x5d\x3d' \
            '\xe2\x88\x3b\x80' '\xf1\x09\x8d\x08'


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
            'cursor': 319754858,
            }
        self.req_bin_0 = '\x5f\x00\x02\x00' '\x6a\x12\x0f\x13'


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
            'fore_red': 19643,
            'fore_green': 29297,
            'back_blue': 60147,
            'back_green': 31133,
            'fore_blue': 54081,
            'back_red': 4842,
            'cursor': 1717380504,
            }
        self.req_bin_0 = '\x60\x00\x05\x00' '\x98\x25\x5d\x66' \
            '\xbb\x4c\x71\x72' '\x41\xd3\xea\x12' \
            '\x9d\x79\xf3\xea'


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
            'height': 1363,
            'drawable': 565254362,
            'item_class': 2,
            'width': 52375,
            }
        self.req_bin_0 = '\x61\x02\x03\x00' '\xda\x18\xb1\x21' \
            '\x97\xcc\x53\x05'

        self.reply_args_0 = {
            'height': 41676,
            'sequence_number': 58096,
            'width': 21167,
            }
        self.reply_bin_0 = '\x01\x00\xf0\xe2' '\x00\x00\x00\x00' \
            '\xaf\x52\xcc\xa2' '\x00\x00\x00\x00' \
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
            'sequence_number': 28856,
            'major_opcode': 162,
            'first_error': 139,
            'present': 1,
            'first_event': 130,
            }
        self.reply_bin_0 = '\x01\x00\xb8\x70' '\x00\x00\x00\x00' \
            '\x01\xa2\x82\x8b' '\x00\x00\x00\x00' \
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
            'sequence_number': 16271,
            'names': ['XTRA', 'XTRA-II'],
            }
        self.reply_bin_0 = '\x01\x02\x8f\x3f' '\x04\x00\x00\x00' \
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
            'keysyms': [[1984342405, 2001170232, 1365946607], [386893915, 77937896, 454705874], [1625982251, 37606140, 1596307683], [857039297, 1923577183, 1562159750], [1181017509, 1801450564, 2065409318], [168502110, 830529422, 1257048702], [1926286151, 1664126523, 372581795], [1849577214, 1787744910, 1499290165], [34811221, 1041412791, 1402240865], [884476213, 43921707, 656930139], [1977403406, 1320357149, 1901590233], [534060450, 1417998919, 524474568], [328088196, 1452114944, 389393397], [1989820788, 1564756057, 1140944625], [1840076939, 352176238, 588265924], [1784801113, 434688690, 558746702], [338107459, 519833825, 1865666760], [416362536, 969344478, 764392487], [927195390, 144832852, 47088030], [594319628, 960079397, 819655840]],
            'first_keycode': 135,
            }
        self.req_bin_0 = '\x64\x14\x3e\x00' '\x87\x03\x00\x00' \
            '\x85\xa9\x46\x76' '\x38\x6f\x47\x77' \
            '\xef\xb0\x6a\x51' '\x5b\x88\x0f\x17' \
            '\xe8\x3c\xa5\x04' '\xd2\x42\x1a\x1b' \
            '\x2b\x85\xea\x60' '\xfc\xd2\x3d\x02' \
            '\xe3\xb8\x25\x5f' '\xc1\x61\x15\x33' \
            '\x5f\x75\xa7\x72' '\x86\xaa\x1c\x5d' \
            '\xa5\xe5\x64\x46' '\x44\xf4\x5f\x6b' \
            '\x26\xa5\x1b\x7b' '\x5e\x23\x0b\x0a' \
            '\x8e\xdf\x80\x31' '\x7e\x0a\xed\x4a' \
            '\x47\xcb\xd0\x72' '\x3b\x8e\x30\x63' \
            '\xa3\x25\x35\x16' '\xfe\x4e\x3e\x6e' \
            '\x8e\xd2\x8e\x6a' '\x35\x5a\x5d\x59' \
            '\x55\x2d\x13\x02' '\xb7\xb2\x12\x3e' \
            '\x61\x7f\x94\x53' '\x35\x09\xb8\x34' \
            '\x2b\x31\x9e\x02' '\x5b\xf5\x27\x27' \
            '\x0e\xc8\xdc\x75' '\x1d\x0d\xb3\x4e' \
            '\xd9\xf6\x57\x71' '\xa2\x1d\xd5\x1f' \
            '\x47\xf2\x84\x54' '\xc8\xd8\x42\x1f' \
            '\x84\x3a\x8e\x13' '\x00\x84\x8d\x56' \
            '\xf5\xab\x35\x17' '\x74\x41\x9a\x76' \
            '\x59\x48\x44\x5d' '\xf1\x6e\x01\x44' \
            '\x8b\x58\xad\x6d' '\x6e\xc8\xfd\x14' \
            '\xc4\x39\x10\x23' '\x59\xe7\x61\x6a' \
            '\xb2\xd2\xe8\x19' '\x4e\xcc\x4d\x21' \
            '\x43\x1c\x27\x14' '\xe1\x08\xfc\x1e' \
            '\xc8\xd0\x33\x6f' '\x28\x30\xd1\x18' \
            '\xde\x05\xc7\x39' '\x27\xb4\x8f\x2d' \
            '\xfe\xe0\x43\x37' '\x54\xf9\xa1\x08' \
            '\x9e\x81\xce\x02' '\x0c\x99\x6c\x23' \
            '\x25\xa6\x39\x39' '\xa0\xf4\xda\x30'


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
            'count': 229,
            'first_keycode': 177,
            }
        self.req_bin_0 = '\x65\x00\x02\x00' '\xb1\xe5\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[1315952678, 1435248405, 421592609], [492015292, 1813972105, 1639138001], [1347222359, 1776898187, 494036130], [1186535996, 596657418, 1581319433], [1177201158, 1568564436, 416083309], [1028804652, 382659714, 505395324], [480018091, 239214138, 1314322319], [1137095180, 1069808119, 545235538], [310619302, 162781725, 104392489], [465078118, 1221610659, 1328359903], [233205012, 1285581222, 1357063086], [1900271563, 1311383762, 1220986746], [451397605, 1600099996, 559661452], [2118046997, 923584305, 1860891377], [415163756, 1279685793, 1752780267], [728156017, 1263986708, 1976273604], [1595076080, 1474696059, 1722142716], [1147030734, 959104031, 874034575], [23200791, 615850829, 7810557], [258161661, 1164978363, 501216100]],
            'sequence_number': 6846,
            }
        self.reply_bin_0 = '\x01\x03\xbe\x1a' '\x3c\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x26\xd8\x6f\x4e' '\x15\x27\x8c\x55' \
            '\x21\xfe\x20\x19' '\xbc\x8e\x53\x1d' \
            '\x89\x04\x1f\x6c' '\xd1\x42\xb3\x61' \
            '\x57\xfb\x4c\x50' '\x8b\x50\xe9\x69' \
            '\xa2\x64\x72\x1d' '\x3c\x1a\xb9\x46' \
            '\x0a\x45\x90\x23' '\x09\x05\x41\x5e' \
            '\x06\xaa\x2a\x46' '\xd4\x64\x7e\x5d' \
            '\x6d\xed\xcc\x18' '\x2c\x50\x52\x3d' \
            '\x82\xec\xce\x16' '\x7c\xb8\x1f\x1e' \
            '\xab\x7e\x9c\x1c' '\x3a\x1e\x42\x0e' \
            '\x8f\xf7\x56\x4e' '\x0c\xb2\xc6\x43' \
            '\xf7\xf9\xc3\x3f' '\x52\xa2\x7f\x20' \
            '\xa6\xac\x83\x12' '\x1d\xda\xb3\x09' \
            '\x29\xe7\x38\x06' '\x66\x87\xb8\x1b' \
            '\xa3\x4c\xd0\x48' '\xdf\x29\x2d\x4f' \
            '\x14\x6d\xe6\x0d' '\xa6\x69\xa0\x4c' \
            '\xae\x23\xe3\x50' '\xcb\xd7\x43\x71' \
            '\xd2\x20\x2a\x4e' '\x7a\xc7\xc6\x48' \
            '\xe5\xc7\xe7\x1a' '\x9c\x96\x5f\x5f' \
            '\x8c\xc1\x5b\x21' '\x15\xd5\x3e\x7e' \
            '\x31\xc7\x0c\x37' '\xf1\xf2\xea\x6e' \
            '\x6c\xe5\xbe\x18' '\xa1\x74\x46\x4c' \
            '\xeb\x4d\x79\x68' '\x71\xc7\x66\x2b' \
            '\x14\xe8\x56\x4b' '\xc4\x8a\xcb\x75' \
            '\xf0\xed\x12\x5f' '\x7b\x13\xe6\x57' \
            '\xfc\xcf\xa5\x66' '\xce\x4c\x5e\x44' \
            '\x1f\xc4\x2a\x39' '\x8f\xb5\x18\x34' \
            '\x17\x04\x62\x01' '\x4d\x23\xb5\x24' \
            '\xfd\x2d\x77\x00' '\xfd\x3b\x63\x0f' \
            '\xbb\x28\x70\x45' '\x64\xf3\xdf\x1d'


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
            'attrs': {'key_click_percent': -120, 'bell_percent': -116, 'led_mode': 0, 'bell_pitch': -15627, 'auto_repeat_mode': 0, 'bell_duration': -30822, 'key': 163, 'led': 166},
            }
        self.req_bin_0 = '\x66\x00\x0a\x00' '\xff\x00\x00\x00' \
            '\x88\x00\x00\x00' '\x8c\x00\x00\x00' \
            '\xf5\xc2\x00\x00' '\x9a\x87\x00\x00' \
            '\xa6\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xa3\x00\x00\x00' '\x00\x00\x00\x00'


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
            'key_click_percent': 236,
            'sequence_number': 8689,
            'bell_percent': 237,
            'bell_pitch': 29543,
            'auto_repeats': [587926677, 1981061368, 549272228, 321606829, 1587872282, 191068140, 527426755, 1282378391],
            'global_auto_repeat': 0,
            'led_mask': 907900197,
            'bell_duration': 46211,
            }
        self.reply_bin_0 = '\x01\x00\xf1\x21' '\x05\x00\x00\x00' \
            '\x25\x75\x1d\x36' '\xec\xed\x67\x73' \
            '\x83\xb4\x00\x00' '\x95\x0c\x0b\x23' \
            '\xf8\x98\x14\x76' '\xa4\x3a\xbd\x20' \
            '\xad\x54\x2b\x13' '\x1a\x02\xa5\x5e' \
            '\xec\x77\x63\x0b' '\xc3\xe4\x6f\x1f' \
            '\x97\x8a\x6f\x4c'


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
            'percent': -77,
            }
        self.req_bin_0 = '\x68\xb3\x01\x00'


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
            'accel_denum': -17097,
            'accel_num': -6617,
            'do_accel': 1,
            'do_thresh': 1,
            'threshold': -3788,
            }
        self.req_bin_0 = '\x69\x00\x03\x00' '\x27\xe6\x37\xbd' \
            '\x34\xf1\x01\x01'


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
            'accel_denom': 42279,
            'sequence_number': 26174,
            'threshold': 3273,
            'accel_num': 17643,
            }
        self.reply_bin_0 = '\x01\x00\x3e\x66' '\x00\x00\x00\x00' \
            '\xeb\x44\x27\xa5' '\xc9\x0c\x00\x00' \
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
            'timeout': -9255,
            'interval': -30111,
            'prefer_blank': 0,
            }
        self.req_bin_0 = '\x6b\x00\x03\x00' '\xd9\xdb\x61\x8a' \
            '\x00\x01\x00\x00'


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
            'timeout': 18439,
            'sequence_number': 23805,
            'prefer_blanking': 0,
            'interval': 22229,
            }
        self.reply_bin_0 = '\x01\x00\xfd\x5c' '\x00\x00\x00\x00' \
            '\x07\x48\xd5\x56' '\x00\x01\x00\x00' \
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
            'host': [167, 251, 186, 173],
            'mode': 0,
            'host_family': 1,
            }
        self.req_bin_0 = '\x6d\x00\x03\x00' '\x01\x00\x04\x00' \
            '\xa7\xfb\xba\xad'


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
            'sequence_number': 45029,
            'mode': 1,
            'hosts': [{'family': 0, 'name': [34, 23, 178, 12]}, {'family': 0, 'name': [130, 236, 254, 15]}],
            }
        self.reply_bin_0 = '\x01\x01\xe5\xaf' '\x04\x00\x00\x00' \
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
            'mode': 0,
            }
        self.req_bin_0 = '\x6f\x00\x01\x00'


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
            'mode': 0,
            }
        self.req_bin_0 = '\x70\x00\x01\x00'


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
            'resource': 671617714,
            }
        self.req_bin_0 = '\x71\x00\x02\x00' '\xb2\x12\x08\x28'


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
            'delta': -3170,
            'window': 2019466322,
            'properties': [520652578, 1051302774, 1387625639, 642650474, 869868451, 1645819186, 2143678474, 1740854050, 1542175106, 559964702, 1771731181, 654800757],
            }
        self.req_bin_0 = '\x72\x00\x0f\x00' '\x52\x9c\x5e\x78' \
            '\x0c\x00\x9e\xf3' '\x22\x87\x08\x1f' \
            '\x76\x9b\xa9\x3e' '\xa7\x7c\xb5\x52' \
            '\x6a\x11\x4e\x26' '\xa3\x23\xd9\x33' \
            '\x32\x35\x19\x62' '\x0a\xf0\xc5\x7f' \
            '\x22\x53\xc3\x67' '\x82\xb9\xeb\x5b' \
            '\x1e\x62\x60\x21' '\xed\x78\x9a\x69' \
            '\x75\x77\x07\x27'


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
            'mode': 0,
            }
        self.req_bin_0 = '\x73\x00\x01\x00'


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
            'map': [241, 165, 176, 252, 204],
            }
        self.req_bin_0 = '\x74\x05\x03\x00' '\xf1\xa5\xb0\xfc' \
            '\xcc\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 58678,
            'status': 164,
            }
        self.reply_bin_0 = '\x01\xa4\x36\xe5' '\x00\x00\x00\x00' \
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
            'sequence_number': 40415,
            'map': [227, 251, 168, 183, 202],
            }
        self.reply_bin_0 = '\x01\x05\xdf\x9d' '\x02\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xe3\xfb\xa8\xb7' '\xca\x00\x00\x00'


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
            'keycodes': [[207, 20], [18, 148], [192, 124], [159, 83], [17, 59], [70, 87], [148, 234], [161, 170]],
            }
        self.req_bin_0 = '\x76\x02\x05\x00' '\xcf\x14\x12\x94' \
            '\xc0\x7c\x9f\x53' '\x11\x3b\x46\x57' \
            '\x94\xea\xa1\xaa'

        self.reply_args_0 = {
            'sequence_number': 5643,
            'status': 183,
            }
        self.reply_bin_0 = '\x01\xb7\x0b\x16' '\x00\x00\x00\x00' \
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
            'sequence_number': 1153,
            'keycodes': [[240, 126], [175, 198], [154, 36], [233, 251], [205, 207], [233, 120], [27, 239], [196, 191]],
            }
        self.reply_bin_0 = '\x01\x02\x81\x04' '\x04\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xf0\x7e\xaf\xc6' '\x9a\x24\xe9\xfb' \
            '\xcd\xcf\xe9\x78' '\x1b\xef\xc4\xbf'


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
