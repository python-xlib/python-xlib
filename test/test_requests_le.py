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
            'wid': 632893089,
            'parent': 563083824,
            'visual': 811875917,
            'height': 62043,
            'width': 55071,
            'depth': 198,
            'attrs': {'cursor': 788158760, 'override_redirect': 1, 'bit_gravity': 6, 'event_mask': 894192179, 'border_pixel': 1365270572, 'background_pixel': 712927020, 'save_under': 0, 'colormap': 980005049, 'do_not_propagate_mask': 667770563, 'backing_store': 1, 'win_gravity': 6, 'backing_planes': 885526468, 'border_pixmap': 513882421, 'backing_pixel': 1693821982, 'background_pixmap': 1314139736},
            'y': -29423,
            'x': -5822,
            'border_width': 29625,
            'window_class': 2,
            }
        self.req_bin_0 = '\x01\xc6\x17\x00' '\xa1\x2e\xb9\x25' \
            '\x30\xfa\x8f\x21' '\x42\xe9\x11\x8d' \
            '\x1f\xd7\x5b\xf2' '\xb9\x73\x02\x00' \
            '\x4d\x3e\x64\x30' '\xff\x7f\x00\x00' \
            '\x58\x2e\x54\x4e' '\x2c\x67\x7e\x2a' \
            '\x35\x39\xa1\x1e' '\x2c\x60\x60\x51' \
            '\x06\x00\x00\x00' '\x06\x00\x00\x00' \
            '\x01\x00\x00\x00' '\xc4\x0f\xc8\x34' \
            '\x1e\xac\xf5\x64' '\x01\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x33\x4a\x4c\x35' \
            '\xc3\x5e\xcd\x27' '\xb9\xb0\x69\x3a' \
            '\x28\x59\xfa\x2e'


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
            'window': 560274578,
            'attrs': {'cursor': 1238338372, 'override_redirect': 0, 'bit_gravity': 6, 'event_mask': 1980992429, 'border_pixel': 310964771, 'background_pixel': 1268171782, 'save_under': 1, 'colormap': 171538239, 'do_not_propagate_mask': 135558419, 'backing_store': 2, 'win_gravity': 10, 'backing_planes': 252687930, 'border_pixmap': 287169917, 'backing_pixel': 1114685309, 'background_pixmap': 2004887498},
            }
        self.req_bin_0 = '\x02\x00\x12\x00' '\x92\x1c\x65\x21' \
            '\xff\x7f\x00\x00' '\xca\x27\x80\x77' \
            '\x06\xc4\x96\x4b' '\x7d\xdd\x1d\x11' \
            '\x23\xf2\x88\x12' '\x06\x00\x00\x00' \
            '\x0a\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x3a\xb6\x0f\x0f' '\x7d\xbf\x70\x42' \
            '\x00\x00\x00\x00' '\x01\x00\x00\x00' \
            '\xad\x8b\x13\x76' '\x13\x75\x14\x08' \
            '\x3f\x77\x39\x0a' '\x44\x8b\xcf\x49'


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
            'window': 1672572666,
            }
        self.req_bin_0 = '\x03\x00\x02\x00' '\xfa\x6e\xb1\x63'

        self.reply_args_0 = {
            'do_not_propagate_mask': 33915,
            'your_event_mask': 172607058,
            'override_redirect': 0,
            'bit_gravity': 128,
            'all_event_masks': 1036583348,
            'save_under': 1,
            'visual': 1419731381,
            'map_state': 169,
            'win_class': 16168,
            'backing_bit_planes': 849532878,
            'backing_store': 215,
            'win_gravity': 140,
            'map_is_installed': 1,
            'backing_pixel': 933754009,
            'sequence_number': 38504,
            'colormap': 56062036,
            }
        self.reply_bin_0 = '\x01\xd7\x68\x96' '\x03\x00\x00\x00' \
            '\xb5\x61\x9f\x54' '\x28\x3f\x80\x8c' \
            '\xce\xd7\xa2\x32' '\x99\xf4\xa7\x37' \
            '\x01\x01\xa9\x00' '\x54\x70\x57\x03' \
            '\xb4\x01\xc9\x3d' '\x52\xc6\x49\x0a' \
            '\x7b\x84\x00\x00'


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
            'window': 533632985,
            }
        self.req_bin_0 = '\x04\x00\x02\x00' '\xd9\x97\xce\x1f'


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
            'window': 490680451,
            }
        self.req_bin_0 = '\x05\x00\x02\x00' '\x83\x30\x3f\x1d'


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
            'window': 1974200014,
            'mode': 0,
            }
        self.req_bin_0 = '\x06\x00\x02\x00' '\xce\xe6\xab\x75'


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
            'y': -12763,
            'x': -18160,
            'window': 2127670410,
            'parent': 1913134105,
            }
        self.req_bin_0 = '\x07\x00\x04\x00' '\x8a\xac\xd1\x7e' \
            '\x19\x1c\x08\x72' '\x10\xb9\x25\xce'


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
            'window': 962670079,
            }
        self.req_bin_0 = '\x08\x00\x02\x00' '\xff\x2d\x61\x39'


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
            'window': 447820952,
            }
        self.req_bin_0 = '\x09\x00\x02\x00' '\x98\x34\xb1\x1a'


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
            'window': 1130502889,
            }
        self.req_bin_0 = '\x0a\x00\x02\x00' '\xe9\x1a\x62\x43'


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
            'window': 2009442907,
            }
        self.req_bin_0 = '\x0b\x00\x02\x00' '\x5b\xaa\xc5\x77'


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
            'window': 2092974410,
            'attrs': {'sibling': 1102940930, 'width': 52077, 'y': -11332, 'x': -11514, 'border_width': -6900, 'stack_mode': 4, 'height': 62050},
            }
        self.req_bin_0 = '\x0c\x00\x0a\x00' '\x4a\x41\xc0\x7c' \
            '\x7f\x00\x00\x00' '\x06\xd3\x00\x00' \
            '\xbc\xd3\x00\x00' '\x6d\xcb\x00\x00' \
            '\x62\xf2\x00\x00' '\x0c\xe5\x00\x00' \
            '\x02\x8b\xbd\x41' '\x04\x00\x00\x00'


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
            'direction': 0,
            'window': 1132872732,
            }
        self.req_bin_0 = '\x0d\x00\x02\x00' '\x1c\x44\x86\x43'


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
            'drawable': 2036121058,
            }
        self.req_bin_0 = '\x0e\x00\x02\x00' '\xe2\xbd\x5c\x79'

        self.reply_args_0 = {
            'width': 65264,
            'depth': 253,
            'y': -12126,
            'x': -29040,
            'border_width': 19896,
            'root': 493091314,
            'sequence_number': 36173,
            'height': 9014,
            }
        self.reply_bin_0 = '\x01\xfd\x4d\x8d' '\x00\x00\x00\x00' \
            '\xf2\xf9\x63\x1d' '\x90\x8e\xa2\xd0' \
            '\xf0\xfe\x36\x23' '\xb8\x4d\x00\x00' \
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
            'window': 884880831,
            }
        self.req_bin_0 = '\x0f\x00\x02\x00' '\xbf\x35\xbe\x34'

        self.reply_args_0 = {
            'parent': 701348115,
            'root': 400550453,
            'children': [1089242139, 925689046, 1668140638, 775016596, 1024466546, 1245533043, 1733661379],
            'sequence_number': 10033,
            }
        self.reply_bin_0 = '\x01\x00\x31\x27' '\x07\x00\x00\x00' \
            '\x35\xea\xdf\x17' '\x13\xb9\xcd\x29' \
            '\x07\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x1b\x84\xec\x40' '\xd6\xe4\x2c\x37' \
            '\x5e\xce\x6d\x63' '\x94\xd0\x31\x2e' \
            '\x72\x1e\x10\x3d' '\x73\x53\x3d\x4a' \
            '\xc3\x92\x55\x67'


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
            'name': 'fuzzy_prop',
            'only_if_exists': 0,
            }
        self.req_bin_0 = '\x10\x00\x05\x00' '\x0a\x00\x00\x00' \
            '\x66\x75\x7a\x7a' '\x79\x5f\x70\x72' \
            '\x6f\x70\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 14401,
            'atom': 1112752381,
            }
        self.reply_bin_0 = '\x01\x00\x41\x38' '\x00\x00\x00\x00' \
            '\xfd\x40\x53\x42' '\x00\x00\x00\x00' \
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
            'atom': 1234624354,
            }
        self.req_bin_0 = '\x11\x00\x02\x00' '\x62\xdf\x96\x49'

        self.reply_args_0 = {
            'name': 'WM_CLASS',
            'sequence_number': 2504,
            }
        self.reply_bin_0 = '\x01\x00\xc8\x09' '\x02\x00\x00\x00' \
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
            'type': 1211092921,
            'window': 1252285733,
            'property': 237459721,
            'data': (8, ''),
            'mode': 2,
            }
        self.req_bin_0 = '\x12\x02\x06\x00' '\x25\x5d\xa4\x4a' \
            '\x09\x59\x27\x0e' '\xb9\xcf\x2f\x48' \
            '\x08\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_1 = {
            'type': 347282449,
            'window': 25619481,
            'property': 633953573,
            'data': (8, 'foo'),
            'mode': 1,
            }
        self.req_bin_1 = '\x12\x01\x07\x00' '\x19\xec\x86\x01' \
            '\x25\x5d\xc9\x25' '\x11\x1c\xb3\x14' \
            '\x08\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'type': 1524334051,
            'window': 481797824,
            'property': 658642629,
            'data': (8, 'zoom'),
            'mode': 1,
            }
        self.req_bin_2 = '\x12\x01\x07\x00' '\xc0\xa6\xb7\x1c' \
            '\xc5\x16\x42\x27' '\xe3\x7d\xdb\x5a' \
            '\x08\x00\x00\x00' '\x04\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'type': 1895805524,
            'window': 211607059,
            'property': 27240430,
            'data': (16, []),
            'mode': 2,
            }
        self.req_bin_3 = '\x12\x02\x06\x00' '\x13\xde\x9c\x0c' \
            '\xee\xa7\x9f\x01' '\x54\xb2\xff\x70' \
            '\x10\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_4 = {
            'type': 549788841,
            'window': 1498238012,
            'property': 1869628209,
            'data': (16, [1, 2, 3]),
            'mode': 0,
            }
        self.req_bin_4 = '\x12\x00\x08\x00' '\x3c\x4c\x4d\x59' \
            '\x31\x43\x70\x6f' '\xa9\x1c\xc5\x20' \
            '\x10\x00\x00\x00' '\x03\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x00\x00'

        self.req_args_5 = {
            'type': 1083661140,
            'window': 2019310438,
            'property': 394292367,
            'data': (16, [1, 2, 3, 4]),
            'mode': 2,
            }
        self.req_bin_5 = '\x12\x02\x08\x00' '\x66\x3b\x5c\x78' \
            '\x8f\x6c\x80\x17' '\x54\x5b\x97\x40' \
            '\x10\x00\x00\x00' '\x04\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x04\x00'

        self.req_args_6 = {
            'type': 761479544,
            'window': 1274166929,
            'property': 1743863777,
            'data': (32, []),
            'mode': 2,
            }
        self.req_bin_6 = '\x12\x02\x06\x00' '\x91\x3e\xf2\x4b' \
            '\xe1\x3f\xf1\x67' '\x78\x41\x63\x2d' \
            '\x20\x00\x00\x00' '\x00\x00\x00\x00'

        self.req_args_7 = {
            'type': 956119085,
            'window': 1018715281,
            'property': 686054590,
            'data': (32, [1, 2, 3]),
            'mode': 1,
            }
        self.req_bin_7 = '\x12\x01\x09\x00' '\x91\x5c\xb8\x3c' \
            '\xbe\x5c\xe4\x28' '\x2d\x38\xfd\x38' \
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
            'window': 1858113940,
            'property': 754854074,
            }
        self.req_bin_0 = '\x13\x00\x03\x00' '\x94\x91\xc0\x6e' \
            '\xba\x28\xfe\x2c'


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
            'window': 1675634394,
            'long_offset': 11483536,
            'property': 1943700626,
            'type': 223769899,
            'long_length': 1748032051,
            'delete': 0,
            }
        self.req_bin_0 = '\x14\x00\x06\x00' '\xda\x26\xe0\x63' \
            '\x92\x84\xda\x73' '\x2b\x75\x56\x0d' \
            '\x90\x39\xaf\x00' '\x33\xda\x30\x68'

        self.reply_args_0 = {
            'bytes_after': 1264377294,
            'property_type': 1306970370,
            'sequence_number': 34281,
            'value': (8, ''),
            }
        self.reply_bin_0 = '\x01\x08\xe9\x85' '\x00\x00\x00\x00' \
            '\x02\xc9\xe6\x4d' '\xce\xdd\x5c\x4b' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_1 = {
            'bytes_after': 902042689,
            'property_type': 1846820627,
            'sequence_number': 50371,
            'value': (8, 'foo'),
            }
        self.reply_bin_1 = '\x01\x08\xc3\xc4' '\x01\x00\x00\x00' \
            '\x13\x3f\x14\x6e' '\x41\x14\xc4\x35' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'bytes_after': 1782597051,
            'property_type': 1613677639,
            'sequence_number': 58679,
            'value': (8, 'zoom'),
            }
        self.reply_bin_2 = '\x01\x08\x37\xe5' '\x01\x00\x00\x00' \
            '\x47\xc4\x2e\x60' '\xbb\x45\x40\x6a' \
            '\x04\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'bytes_after': 1107167742,
            'property_type': 1964967674,
            'sequence_number': 49647,
            'value': (16, []),
            }
        self.reply_bin_3 = '\x01\x10\xef\xc1' '\x00\x00\x00\x00' \
            '\xfa\x06\x1f\x75' '\xfe\x09\xfe\x41' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_4 = {
            'bytes_after': 1602466976,
            'property_type': 638663972,
            'sequence_number': 58268,
            'value': (16, [1, 2, 3]),
            }
        self.reply_bin_4 = '\x01\x10\x9c\xe3' '\x02\x00\x00\x00' \
            '\x24\x3d\x11\x26' '\xa0\xb4\x83\x5f' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x00\x00'

        self.reply_args_5 = {
            'bytes_after': 651542717,
            'property_type': 947428838,
            'sequence_number': 26901,
            'value': (16, [1, 2, 3, 4]),
            }
        self.reply_bin_5 = '\x01\x10\x15\x69' '\x02\x00\x00\x00' \
            '\xe6\x9d\x78\x38' '\xbd\xc0\xd5\x26' \
            '\x04\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x02\x00' '\x03\x00\x04\x00'

        self.reply_args_6 = {
            'bytes_after': 602498418,
            'property_type': 43558782,
            'sequence_number': 11175,
            'value': (32, []),
            }
        self.reply_bin_6 = '\x01\x20\xa7\x2b' '\x00\x00\x00\x00' \
            '\x7e\xa7\x98\x02' '\x72\x65\xe9\x23' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00'

        self.reply_args_7 = {
            'bytes_after': 1661909208,
            'property_type': 607057672,
            'sequence_number': 4347,
            'value': (32, [1, 2, 3]),
            }
        self.reply_bin_7 = '\x01\x20\xfb\x10' '\x03\x00\x00\x00' \
            '\x08\xf7\x2e\x24' '\xd8\xb8\x0e\x63' \
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
            'window': 1002132678,
            }
        self.req_bin_0 = '\x15\x00\x02\x00' '\xc6\x54\xbb\x3b'

        self.reply_args_0 = {
            'sequence_number': 58554,
            'atoms': [497337753, 1561366096, 1429910722, 371682445, 1693790956, 124266489, 819023111, 1575252239, 1958056613, 76461795, 2044963121, 1187630009, 890357857, 639310702, 1708479530, 336050724, 1163834063, 1164094286, 1626309474, 136351014, 1163110454, 1416739018, 1380223836],
            }
        self.reply_bin_0 = '\x01\x00\xba\xe4' '\x17\x00\x00\x00' \
            '\x17\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x99\xc5\xa4\x1d' '\x50\x8e\x10\x5d' \
            '\xc2\xb4\x3a\x55' '\x8d\x6c\x27\x16' \
            '\xec\x32\xf5\x64' '\xf9\x27\x68\x07' \
            '\x07\x4d\xd1\x30' '\x0f\x71\xe4\x5d' \
            '\xa5\x92\xb5\x74' '\xe3\xb6\x8e\x04' \
            '\x31\xa9\xe3\x79' '\xb9\xcb\xc9\x46' \
            '\x61\xc8\x11\x35' '\x6e\x1b\x1b\x26' \
            '\x2a\x54\xd5\x65' '\x24\xba\x07\x14' \
            '\xcf\xb2\x5e\x45' '\x4e\xab\x62\x45' \
            '\x62\x83\xef\x60' '\x26\x8d\x20\x08' \
            '\x36\xa8\x53\x45' '\xca\xb8\x71\x54' \
            '\x5c\x8b\x44\x52'


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
            'window': 1573750861,
            'selection': 984224380,
            'time': 2112448956,
            }
        self.req_bin_0 = '\x16\x00\x04\x00' '\x4d\x88\xcd\x5d' \
            '\x7c\x12\xaa\x3a' '\xbc\x69\xe9\x7d'


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
            'selection': 1209066471,
            }
        self.req_bin_0 = '\x17\x00\x02\x00' '\xe7\xe3\x10\x48'

        self.reply_args_0 = {
            'owner': 1608499874,
            'sequence_number': 40856,
            }
        self.reply_bin_0 = '\x01\x00\x98\x9f' '\x00\x00\x00\x00' \
            '\xa2\xc2\xdf\x5f' '\x00\x00\x00\x00' \
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
            'property': 116271887,
            'requestor': 163844177,
            'selection': 246355390,
            'target': 1621875689,
            'time': 385931637,
            }
        self.req_bin_0 = '\x18\x00\x06\x00' '\x51\x10\xc4\x09' \
            '\xbe\x15\xaf\x0e' '\xe9\xdb\xab\x60' \
            '\x0f\x2b\xee\x06' '\x75\xd9\x00\x17'


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
            'event_mask': 985979728,
            'destination': 1646910168,
            'propagate': 1,
            'event': Xlib.protocol.event.Expose(count = 7721, width = 18606, window = 1339231972, y = 45287, x = 46510, type = 12, sequence_number = 0, height = 44735),
            }
        self.req_bin_0 = '\x19\x01\x0b\x00' '\xd8\xda\x29\x62' \
            '\x50\xdb\xc4\x3a' '\x0c\x00\x00\x00' \
            '\xe4\x0e\xd3\x4f' '\xae\xb5\xe7\xb0' \
            '\xae\x48\xbf\xae' '\x29\x1e\x00\x00' \
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
            'cursor': 1773330151,
            'keyboard_mode': 0,
            'pointer_mode': 1,
            'event_mask': 27410,
            'confine_to': 1526915530,
            'time': 1195309735,
            'grab_window': 1295558486,
            'owner_events': 1,
            }
        self.req_bin_0 = '\x1a\x01\x06\x00' '\x56\xa7\x38\x4d' \
            '\x12\x6b\x01\x00' '\xca\xe1\x02\x5b' \
            '\xe7\xde\xb2\x69' '\xa7\xfa\x3e\x47'

        self.reply_args_0 = {
            'status': 166,
            'sequence_number': 9454,
            }
        self.reply_bin_0 = '\x01\xa6\xee\x24' '\x00\x00\x00\x00' \
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
            'time': 1647345145,
            }
        self.req_bin_0 = '\x1b\x00\x02\x00' '\xf9\x7d\x30\x62'


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
            'cursor': 1510380761,
            'keyboard_mode': 0,
            'modifiers': 62613,
            'pointer_mode': 1,
            'event_mask': 23716,
            'confine_to': 2062912931,
            'button': 169,
            'grab_window': 2055413885,
            'owner_events': 0,
            }
        self.req_bin_0 = '\x1c\x00\x06\x00' '\x7d\x20\x83\x7a' \
            '\xa4\x5c\x01\x00' '\xa3\x8d\xf5\x7a' \
            '\xd9\x94\x06\x5a' '\xa9\x00\x95\xf4'


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
            'button': 220,
            'modifiers': 32389,
            'grab_window': 1891977189,
            }
        self.req_bin_0 = '\x1d\xdc\x03\x00' '\xe5\x47\xc5\x70' \
            '\x85\x7e\x00\x00'


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
            'cursor': 777967884,
            'event_mask': 12743,
            'time': 197998305,
            }
        self.req_bin_0 = '\x1e\x00\x04\x00' '\x0c\xd9\x5e\x2e' \
            '\xe1\x36\xcd\x0b' '\xc7\x31\x00\x00'


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
            'keyboard_mode': 1,
            'time': 1696403859,
            'pointer_mode': 0,
            'grab_window': 316814295,
            'owner_events': 0,
            }
        self.req_bin_0 = '\x1f\x00\x04\x00' '\xd7\x33\xe2\x12' \
            '\x93\x11\x1d\x65' '\x00\x01\x00\x00'

        self.reply_args_0 = {
            'status': 239,
            'sequence_number': 46747,
            }
        self.reply_bin_0 = '\x01\xef\x9b\xb6' '\x00\x00\x00\x00' \
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
            'time': 4211611,
            }
        self.req_bin_0 = '\x20\x00\x02\x00' '\x9b\x43\x40\x00'


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
            'keyboard_mode': 0,
            'modifiers': 62007,
            'key': 175,
            'pointer_mode': 0,
            'grab_window': 882662093,
            'owner_events': 1,
            }
        self.req_bin_0 = '\x21\x01\x04\x00' '\xcd\x5a\x9c\x34' \
            '\x37\xf2\xaf\x00' '\x00\x00\x00\x00'


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
            'modifiers': 18590,
            'grab_window': 1389213966,
            'key': 141,
            }
        self.req_bin_0 = '\x22\x8d\x03\x00' '\x0e\xb9\xcd\x52' \
            '\x9e\x48\x00\x00'


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
            'mode': 7,
            'time': 1088990319,
            }
        self.req_bin_0 = '\x23\x07\x02\x00' '\x6f\xac\xe8\x40'


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
            'window': 358895460,
            }
        self.req_bin_0 = '\x26\x00\x02\x00' '\x64\x4f\x64\x15'

        self.reply_args_0 = {
            'same_screen': 1,
            'child': 2139990686,
            'win_x': -30717,
            'root_y': -18418,
            'root_x': -2403,
            'root': 1853596468,
            'mask': 14486,
            'sequence_number': 29530,
            'win_y': -19690,
            }
        self.reply_bin_0 = '\x01\x01\x5a\x73' '\x00\x00\x00\x00' \
            '\x34\xa3\x7b\x6e' '\x9e\xaa\x8d\x7f' \
            '\x9d\xf6\x0e\xb8' '\x03\x88\x16\xb3' \
            '\x96\x38\x00\x00' '\x00\x00\x00\x00'


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
            'start': 2110367101,
            'window': 528148429,
            'stop': 1808786083,
            }
        self.req_bin_0 = '\x27\x00\x04\x00' '\xcd\xe7\x7a\x1f' \
            '\x7d\xa5\xc9\x7d' '\xa3\xe2\xcf\x6b'

        self.reply_args_0 = {
            'events': [{'y': -23108, 'x': -3461, 'time': 984326273}, {'y': -4096, 'x': -4908, 'time': 488459157}, {'y': -29782, 'x': -8325, 'time': 1162935901}, {'y': -26418, 'x': -10559, 'time': 275816904}, {'y': -3941, 'x': -2216, 'time': 656439277}],
            'sequence_number': 42652,
            }
        self.reply_bin_0 = '\x01\x00\x9c\xa6' '\x0a\x00\x00\x00' \
            '\x05\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x81\xa0\xab\x3a' '\x7b\xf2\xbc\xa5' \
            '\x95\x4b\x1d\x1d' '\xd4\xec\x00\xf0' \
            '\x5d\xfe\x50\x45' '\x7b\xdf\xaa\x8b' \
            '\xc8\xa1\x70\x10' '\xc1\xd6\xce\x98' \
            '\xed\x77\x20\x27' '\x58\xf7\x9b\xf0'


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
            'dst_wid': 246042608,
            'src_wid': 1251919501,
            'src_x': -18176,
            'src_y': -309,
            }
        self.req_bin_0 = '\x28\x00\x04\x00' '\x8d\xc6\x9e\x4a' \
            '\xf0\x4f\xaa\x0e' '\x00\xb9\xcb\xfe'

        self.reply_args_0 = {
            'y': -24269,
            'x': -29750,
            'sequence_number': 39515,
            'same_screen': 0,
            'child': 1548917071,
            }
        self.reply_bin_0 = '\x01\x00\x5b\x9a' '\x00\x00\x00\x00' \
            '\x4f\x99\x52\x5c' '\xca\x8b\x33\xa1' \
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
            'src_x': -1322,
            'dst_x': -15518,
            'src_width': 45129,
            'src_height': 8451,
            'src_y': -13238,
            'dst_y': -26121,
            'dst_window': 2139748563,
            'src_window': 1945176770,
            }
        self.req_bin_0 = '\x29\x00\x06\x00' '\xc2\x0a\xf1\x73' \
            '\xd3\xf8\x89\x7f' '\xd6\xfa\x4a\xcc' \
            '\x49\xb0\x03\x21' '\x62\xc3\xf7\x99'


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
            'focus': 1068495705,
            'time': 342883486,
            }
        self.req_bin_0 = '\x2a\x00\x03\x00' '\x59\xf3\xaf\x3f' \
            '\x9e\xfc\x6f\x14'


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
            'revert_to': 129,
            'focus': 1884243837,
            'sequence_number': 9052,
            }
        self.reply_bin_0 = '\x01\x81\x5c\x23' '\x00\x00\x00\x00' \
            '\x7d\x47\x4f\x70' '\x00\x00\x00\x00' \
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
            'map': [175, 212, 207, 139, 156, 192, 230, 219, 136, 198, 152, 156, 229, 233, 221, 209, 131, 229, 209, 249, 130, 189, 183, 135, 238, 149, 131, 204, 162, 229, 149, 246],
            'sequence_number': 19383,
            }
        self.reply_bin_0 = '\x01\x00\xb7\x4b' '\x02\x00\x00\x00' \
            '\xaf\xd4\xcf\x8b' '\x9c\xc0\xe6\xdb' \
            '\x88\xc6\x98\x9c' '\xe5\xe9\xdd\xd1' \
            '\x83\xe5\xd1\xf9' '\x82\xbd\xb7\x87' \
            '\xee\x95\x83\xcc' '\xa2\xe5\x95\xf6'


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
            'name': 'foofont',
            'fid': 1809550053,
            }
        self.req_bin_0 = '\x2d\x00\x05\x00' '\xe5\x8a\xdb\x6b' \
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
            'font': 405865016,
            }
        self.req_bin_0 = '\x2e\x00\x02\x00' '\x38\x02\x31\x18'


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
            'font': 173413537,
            }
        self.req_bin_0 = '\x2f\x00\x02\x00' '\xa1\x14\x56\x0a'

        self.reply_args_0 = {
            'max_bounds': {'left_side_bearing': -27346, 'descent': -13574, 'right_side_bearing': -29649, 'attributes': 58157, 'character_width': -6055, 'ascent': -4810},
            'all_chars_exist': 0,
            'font_ascent': -15846,
            'font_descent': -913,
            'draw_direction': 165,
            'min_char_or_byte2': 53512,
            'default_char': 28435,
            'max_char_or_byte2': 48394,
            'min_bounds': {'left_side_bearing': -8151, 'descent': -28819, 'right_side_bearing': -31752, 'attributes': 52666, 'character_width': -19612, 'ascent': -9876},
            'char_infos': [{'left_side_bearing': -20738, 'descent': -15296, 'right_side_bearing': -2753, 'attributes': 64507, 'character_width': -12227, 'ascent': -13881}, {'left_side_bearing': -10754, 'descent': -1625, 'right_side_bearing': -9647, 'attributes': 29864, 'character_width': -26871, 'ascent': -11229}, {'left_side_bearing': -30834, 'descent': -16816, 'right_side_bearing': -27729, 'attributes': 56962, 'character_width': -4251, 'ascent': -12215}],
            'max_byte1': 219,
            'min_byte1': 195,
            'properties': [{'name': 515636466, 'value': 1798456662}],
            'sequence_number': 52469,
            }
        self.reply_bin_0 = '\x01\x00\xf5\xcc' '\x12\x00\x00\x00' \
            '\x29\xe0\xf8\x83' '\x64\xb3\x6c\xd9' \
            '\x6d\x8f\xba\xcd' '\x00\x00\x00\x00' \
            '\x2e\x95\x2f\x8c' '\x59\xe8\x36\xed' \
            '\xfa\xca\x2d\xe3' '\x00\x00\x00\x00' \
            '\x08\xd1\x0a\xbd' '\x13\x6f\x01\x00' \
            '\xa5\xc3\xdb\x00' '\x1a\xc2\x6f\xfc' \
            '\x03\x00\x00\x00' '\xf2\xfc\xbb\x1e' \
            '\x56\x45\x32\x6b' '\xfe\xae\x3f\xf5' \
            '\x3d\xd0\xc7\xc9' '\x40\xc4\xfb\xfb' \
            '\xfe\xd5\x51\xda' '\x09\x97\x23\xd4' \
            '\xa7\xf9\xa8\x74' '\x8e\x87\xaf\x93' \
            '\x65\xef\x49\xd0' '\x50\xbe\x82\xde'


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
            'font': 1637171782,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = '\x30\x01\x04\x00' '\x46\x42\x95\x61' \
            '\x00\x66\x00\x6f' '\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'font_descent': -10581,
            'overall_left': -1212859291,
            'draw_direction': 195,
            'overall_right': -813911398,
            'overall_descent': -19862,
            'overall_ascent': -32654,
            'font_ascent': -22971,
            'sequence_number': 6206,
            'overall_width': -127705892,
            }
        self.reply_bin_0 = '\x01\xc3\x3e\x18' '\x00\x00\x00\x00' \
            '\x45\xa6\xab\xd6' '\x72\x80\x6a\xb2' \
            '\xdc\x5c\x63\xf8' '\x65\x3c\xb5\xb7' \
            '\x9a\xb2\x7c\xcf' '\x00\x00\x00\x00'


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
            'pattern': 'bhazr',
            'max_names': 57427,
            }
        self.req_bin_0 = '\x31\x00\x04\x00' '\x53\xe0\x05\x00' \
            '\x62\x68\x61\x7a' '\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 39409,
            }
        self.reply_bin_0 = '\x01\x00\xf1\x99' '\x05\x00\x00\x00' \
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
            'pattern': 'bhazr2',
            'max_names': 52288,
            }
        self.req_bin_0 = '\x32\x00\x04\x00' '\x40\xcc\x06\x00' \
            '\x62\x68\x61\x7a' '\x72\x32\x00\x00'

        self.reply_args_0 = {
            'max_bounds': {'left_side_bearing': -9255, 'descent': -26305, 'right_side_bearing': -6756, 'attributes': 49084, 'character_width': -4462, 'ascent': -3529},
            'all_chars_exist': 1,
            'font_ascent': -26930,
            'name': 'fontfont',
            'replies_hint': 1755082535,
            'font_descent': -25033,
            'draw_direction': 229,
            'min_char_or_byte2': 65093,
            'default_char': 39019,
            'max_char_or_byte2': 45170,
            'min_bounds': {'left_side_bearing': -8350, 'descent': -16956, 'right_side_bearing': -19578, 'attributes': 27352, 'character_width': -20897, 'ascent': -9972},
            'max_byte1': 221,
            'min_byte1': 158,
            'properties': [{'name': 213588122, 'value': 1789263183}],
            'sequence_number': 43812,
            }
        self.reply_bin_0 = '\x01\x08\x24\xab' '\x0b\x00\x00\x00' \
            '\x62\xdf\x86\xb3' '\x5f\xae\x0c\xd9' \
            '\xc4\xbd\xd8\x6a' '\x00\x00\x00\x00' \
            '\xd9\xdb\x9c\xe5' '\x92\xee\x37\xf2' \
            '\x3f\x99\xbc\xbf' '\x00\x00\x00\x00' \
            '\x45\xfe\x72\xb0' '\x6b\x98\x01\x00' \
            '\xe5\x9e\xdd\x01' '\xce\x96\x37\x9e' \
            '\x27\x6f\x9c\x68' '\x9a\x18\xbb\x0c' \
            '\x4f\xfd\xa5\x6a' '\x66\x6f\x6e\x74' \
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
            'paths': ['path1', 'path2232'],
            'sequence_number': 17086,
            }
        self.reply_bin_0 = '\x01\x00\xbe\x42' '\x04\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x05\x70\x61\x74' '\x68\x31\x08\x70' \
            '\x61\x74\x68\x32' '\x32\x33\x32\x00'

        self.reply_args_1 = {
            'paths': [],
            'sequence_number': 8511,
            }
        self.reply_bin_1 = '\x01\x00\x3f\x21' '\x00\x00\x00\x00' \
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
            'width': 32332,
            'depth': 179,
            'pid': 847631690,
            'drawable': 1358709134,
            'height': 16464,
            }
        self.req_bin_0 = '\x35\xb3\x04\x00' '\x4a\xd5\x85\x32' \
            '\x8e\x41\xfc\x50' '\x4c\x7e\x50\x40'


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
            'pixmap': 1323266674,
            }
        self.req_bin_0 = '\x36\x00\x02\x00' '\x72\x72\xdf\x4e'


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
            'drawable': 830249906,
            'attrs': {'function': 14, 'foreground': 814230008, 'background': 2072616911, 'clip_x_origin': -6987, 'subwindow_mode': 0, 'cap_style': 1, 'fill_style': 3, 'tile_stipple_y_origin': -25870, 'font': 264499208, 'graphics_exposures': 0, 'join_style': 2, 'line_width': 36600, 'stipple': 870974399, 'dash_offset': 49599, 'clip_y_origin': -5712, 'tile_stipple_x_origin': -32365, 'arc_mode': 0, 'tile': 1597988019, 'line_style': 2, 'plane_mask': 1650697305, 'clip_mask': 402937862, 'fill_rule': 0, 'dashes': 136},
            'cid': 779296774,
            }
        self.req_bin_0 = '\x37\x00\x1b\x00' '\x06\x20\x73\x2e' \
            '\xb2\x9b\x7c\x31' '\xff\xff\x7f\x00' \
            '\x0e\x00\x00\x00' '\x59\xa4\x63\x62' \
            '\xf8\x29\x88\x30' '\xcf\x9f\x89\x7b' \
            '\xf8\x8e\x00\x00' '\x02\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x02\x00\x00\x00' \
            '\x03\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xb3\x5c\x3f\x5f' '\xbf\x03\xea\x33' \
            '\x93\x81\x00\x00' '\xf2\x9a\x00\x00' \
            '\x08\xf0\xc3\x0f' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\xb5\xe4\x00\x00' \
            '\xb0\xe9\x00\x00' '\x06\x58\x04\x18' \
            '\xbf\xc1\x00\x00' '\x88\x00\x00\x00' \
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
            'gc': 1996372624,
            'attrs': {'function': 15, 'foreground': 1817174045, 'background': 840850119, 'clip_x_origin': -28415, 'subwindow_mode': 1, 'cap_style': 0, 'fill_style': 0, 'tile_stipple_y_origin': -24832, 'font': 240535139, 'graphics_exposures': 1, 'join_style': 2, 'line_width': 64290, 'stipple': 1739313208, 'dash_offset': 53189, 'clip_y_origin': -2802, 'tile_stipple_x_origin': -4548, 'arc_mode': 1, 'tile': 1091199324, 'line_style': 2, 'plane_mask': 1403123174, 'clip_mask': 1604118463, 'fill_rule': 1, 'dashes': 186},
            }
        self.req_bin_0 = '\x38\x00\x1a\x00' '\x90\x3a\xfe\x76' \
            '\xff\xff\x7f\x00' '\x0f\x00\x00\x00' \
            '\xe6\xf5\xa1\x53' '\x1d\xe0\x4f\x6c' \
            '\xc7\x5a\x1e\x32' '\x22\xfb\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x01\x00\x00\x00' '\x5c\x61\x0a\x41' \
            '\x38\xd0\xab\x67' '\x3c\xee\x00\x00' \
            '\x00\x9f\x00\x00' '\x63\x46\x56\x0e' \
            '\x01\x00\x00\x00' '\x01\x00\x00\x00' \
            '\x01\x91\x00\x00' '\x0e\xf5\x00\x00' \
            '\xbf\xe7\x9c\x5f' '\xc5\xcf\x00\x00' \
            '\xba\x00\x00\x00' '\x01\x00\x00\x00'


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
            'src_gc': 1605257018,
            'dst_gc': 2046321491,
            'mask': 996538407,
            }
        self.req_bin_0 = '\x39\x00\x04\x00' '\x3a\x47\xae\x5f' \
            '\x53\x63\xf8\x79' '\x27\xf8\x65\x3b'


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
            'dash_offset': 34958,
            'gc': 2119954025,
            'dashes': [146, 217, 181, 229, 212, 175, 201, 251, 248],
            }
        self.req_bin_0 = '\x3a\x00\x06\x00' '\x69\xee\x5b\x7e' \
            '\x8e\x88\x09\x00' '\x92\xd9\xb5\xe5' \
            '\xd4\xaf\xc9\xfb' '\xf8\x00\x00\x00'


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
            'ordering': 3,
            'gc': 2028835270,
            'y_origin': -15522,
            'rectangles': [{'y': -27524, 'x': -27245, 'height': 31014, 'width': 52432}, {'y': -8991, 'x': -11302, 'height': 9053, 'width': 11072}],
            'x_origin': -26003,
            }
        self.req_bin_0 = '\x3b\x03\x07\x00' '\xc6\x91\xed\x78' \
            '\x6d\x9a\x5e\xc3' '\x93\x95\x7c\x94' \
            '\xd0\xcc\x26\x79' '\xda\xd3\xe1\xdc' \
            '\x40\x2b\x5d\x23'

        self.req_args_1 = {
            'ordering': 1,
            'gc': 155607949,
            'y_origin': -32694,
            'rectangles': [],
            'x_origin': -23382,
            }
        self.req_bin_1 = '\x3b\x01\x03\x00' '\x8d\x63\x46\x09' \
            '\xaa\xa4\x4a\x80'


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
            'gc': 533809208,
            }
        self.req_bin_0 = '\x3c\x00\x02\x00' '\x38\x48\xd1\x1f'


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
            'width': 25049,
            'window': 451215820,
            'y': -6435,
            'x': -30623,
            'exposures': 0,
            'height': 27400,
            }
        self.req_bin_0 = '\x3d\x00\x04\x00' '\xcc\x01\xe5\x1a' \
            '\x61\x88\xdd\xe6' '\xd9\x61\x08\x6b'


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
            'dst_y': -10208,
            'dst_x': -3325,
            'gc': 544091206,
            'src_x': -14979,
            'src_y': -25188,
            'dst_drawable': 1518430886,
            'height': 46849,
            'width': 46860,
            'src_drawable': 197047820,
            }
        self.req_bin_0 = '\x3e\x00\x07\x00' '\x0c\xb6\xbe\x0b' \
            '\xa6\x6a\x81\x5a' '\x46\x2c\x6e\x20' \
            '\x7d\xc5\x9c\x9d' '\x03\xf3\x20\xd8' \
            '\x0c\xb7\x01\xb7'


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
            'dst_y': -24783,
            'dst_x': -17393,
            'bit_plane': 121248642,
            'gc': 2016534076,
            'src_x': -15677,
            'src_y': -24535,
            'dst_drawable': 626526507,
            'height': 9260,
            'width': 12445,
            'src_drawable': 1825271175,
            }
        self.req_bin_0 = '\x3f\x00\x08\x00' '\x87\x6d\xcb\x6c' \
            '\x2b\x09\x58\x25' '\x3c\xde\x31\x78' \
            '\xc3\xc2\x29\xa0' '\x0f\xbc\x31\x9f' \
            '\x9d\x30\x2c\x24' '\x82\x1b\x3a\x07'


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
            'coord_mode': 0,
            'drawable': 1127406891,
            'points': [{'y': -18047, 'x': -19763}, {'y': -5351, 'x': -20174}, {'y': -10573, 'x': -29362}],
            'gc': 1752128743,
            }
        self.req_bin_0 = '\x40\x00\x06\x00' '\x2b\xdd\x32\x43' \
            '\xe7\x5c\x6f\x68' '\xcd\xb2\x81\xb9' \
            '\x32\xb1\x19\xeb' '\x4e\x8d\xb3\xd6'


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
            'coord_mode': 1,
            'drawable': 1354888255,
            'points': [{'y': -22360, 'x': -25237}, {'y': -21145, 'x': -28948}, {'y': -16928, 'x': -3515}, {'y': -25838, 'x': -12335}, {'y': -31134, 'x': -12944}],
            'gc': 1308624032,
            }
        self.req_bin_0 = '\x41\x01\x08\x00' '\x3f\xf4\xc1\x50' \
            '\xa0\x04\x00\x4e' '\x6b\x9d\xa8\xa8' \
            '\xec\x8e\x67\xad' '\x45\xf2\xe0\xbd' \
            '\xd1\xcf\x12\x9b' '\x70\xcd\x62\x86'


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
            'segments': [{'y1': -3160, 'x2': -5139, 'x1': -2249, 'y2': -26872}],
            'gc': 2022424938,
            'drawable': 158182613,
            }
        self.req_bin_0 = '\x42\x00\x05\x00' '\xd5\xac\x6d\x09' \
            '\x6a\xc1\x8b\x78' '\x37\xf7\xa8\xf3' \
            '\xed\xeb\x08\x97'


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
            'gc': 1036376211,
            'drawable': 2136753875,
            'rectangles': [{'y': -29358, 'x': -6957, 'height': 19230, 'width': 32377}, {'y': -23694, 'x': -2777, 'height': 48827, 'width': 42548}, {'y': -22773, 'x': -12641, 'height': 9809, 'width': 30955}],
            }
        self.req_bin_0 = '\x43\x00\x09\x00' '\xd3\x46\x5c\x7f' \
            '\x93\xd8\xc5\x3d' '\xd3\xe4\x52\x8d' \
            '\x79\x7e\x1e\x4b' '\x27\xf5\x72\xa3' \
            '\x34\xa6\xbb\xbe' '\x9f\xce\x0b\xa7' \
            '\xeb\x78\x51\x26'


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
            'drawable': 2066514582,
            'gc': 956699423,
            'arcs': [{'width': 36714, 'angle1': -22260, 'angle2': -28493, 'y': -394, 'x': -6756, 'height': 63498}, {'width': 31212, 'angle1': -5166, 'angle2': -19039, 'y': -11179, 'x': -20569, 'height': 27113}, {'width': 62033, 'angle1': -18595, 'angle2': -26291, 'y': -8396, 'x': -7987, 'height': 11428}],
            }
        self.req_bin_0 = '\x44\x00\x0c\x00' '\x96\x82\x2c\x7b' \
            '\x1f\x13\x06\x39' '\x9c\xe5\x76\xfe' \
            '\x6a\x8f\x0a\xf8' '\x0c\xa9\xb3\x90' \
            '\xa7\xaf\x55\xd4' '\xec\x79\xe9\x69' \
            '\xd2\xeb\xa1\xb5' '\xcd\xe0\x34\xdf' \
            '\x51\xf2\xa4\x2c' '\x5d\xb7\x4d\x99'


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
            'coord_mode': 1,
            'drawable': 526750870,
            'points': [{'y': -765, 'x': -11821}, {'y': -10853, 'x': -1907}, {'y': -29710, 'x': -468}],
            'gc': 112110920,
            'shape': 0,
            }
        self.req_bin_0 = '\x45\x00\x07\x00' '\x96\x94\x65\x1f' \
            '\x48\xad\xae\x06' '\x00\x01\x00\x00' \
            '\xd3\xd1\x03\xfd' '\x8d\xf8\x9b\xd5' \
            '\x2c\xfe\xf2\x8b'


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
            'gc': 468793444,
            'drawable': 878946804,
            'rectangles': [{'y': -29169, 'x': -18095, 'height': 15301, 'width': 12078}, {'y': -7148, 'x': -18997, 'height': 7501, 'width': 17120}],
            }
        self.req_bin_0 = '\x46\x00\x07\x00' '\xf4\xa9\x63\x34' \
            '\x64\x38\xf1\x1b' '\x51\xb9\x0f\x8e' \
            '\x2e\x2f\xc5\x3b' '\xcb\xb5\x14\xe4' \
            '\xe0\x42\x4d\x1d'


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
            'drawable': 1286339124,
            'gc': 1256983120,
            'arcs': [{'width': 62526, 'angle1': -17496, 'angle2': -20949, 'y': -21843, 'x': -31746, 'height': 59073}],
            }
        self.req_bin_0 = '\x47\x00\x06\x00' '\x34\xfa\xab\x4c' \
            '\x50\x0a\xec\x4a' '\xfe\x83\xad\xaa' \
            '\x3e\xf4\xc1\xe6' '\xa8\xbb\x2b\xae'


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
            'dst_y': -18744,
            'width': 39512,
            'left_pad': 222,
            'gc': 1858057277,
            'dst_x': -9189,
            'format': 2,
            'drawable': 935710750,
            'data': 'bit map data',
            'depth': 218,
            'height': 16464,
            }
        self.req_bin_0 = '\x48\x02\x09\x00' '\x1e\xd0\xc5\x37' \
            '\x3d\xb4\xbf\x6e' '\x58\x9a\x50\x40' \
            '\x1b\xdc\xc8\xb6' '\xde\xda\x00\x00' \
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
            'width': 47689,
            'format': 1,
            'y': -2692,
            'x': -32705,
            'drawable': 377616775,
            'plane_mask': 849117586,
            'height': 24480,
            }
        self.req_bin_0 = '\x49\x01\x05\x00' '\x87\xf9\x81\x16' \
            '\x3f\x80\x7c\xf5' '\x49\xba\xa0\x5f' \
            '\x92\x81\x9c\x32'

        self.reply_args_0 = {
            'depth': 249,
            'data': 'this is real ly imag e b-map',
            'visual': 141686402,
            'sequence_number': 47197,
            }
        self.reply_bin_0 = '\x01\xf9\x5d\xb8' '\x07\x00\x00\x00' \
            '\x82\xf6\x71\x08' '\x00\x00\x00\x00' \
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
            'y': -7036,
            'items': [{'string': 'zoo', 'delta': 2}, 16909060, {'string': 'ie', 'delta': 0}],
            'drawable': 1736403224,
            'gc': 1348241590,
            'x': -27139,
            }
        self.req_bin_0 = '\x4a\x00\x08\x00' '\x18\x69\x7f\x67' \
            '\xb6\x88\x5c\x50' '\xfd\x95\x84\xe4' \
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
            'y': -10535,
            'items': [{'string': (4131, 18), 'delta': 2}, 16909060],
            'drawable': 1669371472,
            'gc': 327278878,
            'x': -31319,
            }
        self.req_bin_0 = '\x4b\x00\x07\x00' '\x50\x96\x80\x63' \
            '\x1e\xe1\x81\x13' '\xa9\x85\xd9\xd6' \
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
            'y': -3727,
            'x': -15149,
            'drawable': 2131605072,
            'gc': 581816261,
            'string': 'showme',
            }
        self.req_bin_0 = '\x4c\x06\x06\x00' '\x50\xb6\x0d\x7f' \
            '\xc5\xcf\xad\x22' '\xd3\xc4\x71\xf1' \
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
            'y': -1074,
            'x': -2847,
            'drawable': 1442818198,
            'gc': 145495998,
            'string': (115, 104, 111, 119, 109, 111, 114, 101),
            }
        self.req_bin_0 = '\x4d\x08\x08\x00' '\x96\xa8\xff\x55' \
            '\xbe\x17\xac\x08' '\xe1\xf4\xce\xfb' \
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
            'alloc': 0,
            'window': 1386427589,
            'visual': 1165319270,
            'mid': 1982619692,
            }
        self.req_bin_0 = '\x4e\x00\x04\x00' '\x2c\x60\x2c\x76' \
            '\xc5\x34\xa3\x52' '\x66\x5c\x75\x45'


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
            'cmap': 1948229362,
            }
        self.req_bin_0 = '\x4f\x00\x02\x00' '\xf2\x9e\x1f\x74'


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
            'src_cmap': 836376231,
            'mid': 1781544437,
            }
        self.req_bin_0 = '\x50\x00\x03\x00' '\xf5\x35\x30\x6a' \
            '\xa7\x16\xda\x31'


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
            'cmap': 1065317214,
            }
        self.req_bin_0 = '\x51\x00\x02\x00' '\x5e\x73\x7f\x3f'


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
            'cmap': 1636916558,
            }
        self.req_bin_0 = '\x52\x00\x02\x00' '\x4e\x5d\x91\x61'


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
            'window': 198767900,
            }
        self.req_bin_0 = '\x53\x00\x02\x00' '\x1c\xf5\xd8\x0b'

        self.reply_args_0 = {
            'cmaps': [6854304, 441133660],
            'sequence_number': 56438,
            }
        self.reply_bin_0 = '\x01\x00\x76\xdc' '\x02\x00\x00\x00' \
            '\x02\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xa0\x96\x68\x00' '\x5c\x2a\x4b\x1a'


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
            'blue': 57892,
            'cmap': 1775908575,
            'green': 61383,
            'red': 8870,
            }
        self.req_bin_0 = '\x54\x00\x04\x00' '\xdf\x36\xda\x69' \
            '\xa6\x22\xc7\xef' '\x24\xe2\x00\x00'

        self.reply_args_0 = {
            'blue': 22111,
            'green': 27536,
            'red': 54369,
            'sequence_number': 52666,
            'pixel': 1186287049,
            }
        self.reply_bin_0 = '\x01\x00\xba\xcd' '\x00\x00\x00\x00' \
            '\x61\xd4\x90\x6b' '\x5f\x56\x00\x00' \
            '\xc9\x4d\xb5\x46' '\x00\x00\x00\x00' \
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
            'cmap': 695059054,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x55\x00\x05\x00' '\x6e\xc2\x6d\x29' \
            '\x07\x00\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'exact_red': 45174,
            'screen_blue': 21718,
            'exact_green': 45002,
            'exact_blue': 55971,
            'screen_green': 47979,
            'screen_red': 60497,
            'sequence_number': 38835,
            'pixel': 580415589,
            }
        self.reply_bin_0 = '\x01\x00\xb3\x97' '\x00\x00\x00\x00' \
            '\x65\x70\x98\x22' '\x76\xb0\xca\xaf' \
            '\xa3\xda\x51\xec' '\x6b\xbb\xd6\x54' \
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
            'contiguous': 1,
            'cmap': 2071194037,
            'colors': 16292,
            'planes': 14978,
            }
        self.req_bin_0 = '\x56\x01\x03\x00' '\xb5\xe9\x73\x7b' \
            '\xa4\x3f\x82\x3a'

        self.reply_args_0 = {
            'pixels': [1664874569, 198876857, 135035151, 1499807858, 600240169, 1403510863, 757170725, 929995606, 155550883, 642439566, 971734621, 1359474267, 609593319, 669993327, 1837906914, 1355959290, 835285748],
            'masks': [50898278, 362272940, 1106373487],
            'sequence_number': 57786,
            }
        self.reply_bin_0 = '\x01\x00\xba\xe1' '\x14\x00\x00\x00' \
            '\x11\x00\x03\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x49\xf8\x3b\x63' '\xb9\x9e\xda\x0b' \
            '\x0f\x79\x0c\x08' '\x72\x40\x65\x59' \
            '\x29\xf0\xc6\x23' '\x4f\xe0\xa7\x53' \
            '\x25\x82\x21\x2d' '\x56\x9b\x6e\x37' \
            '\xa3\x84\x45\x09' '\x8e\xd9\x4a\x26' \
            '\x5d\x7e\xeb\x39' '\x5b\xee\x07\x51' \
            '\xe7\xa7\x55\x24' '\x6f\x49\xef\x27' \
            '\xe2\x3b\x8c\x6d' '\xfa\x4b\xd2\x50' \
            '\xf4\x72\xc9\x31' '\x66\xa5\x08\x03' \
            '\xac\xd8\x97\x15' '\x6f\xeb\xf1\x41'

        self.reply_args_1 = {
            'pixels': [],
            'masks': [],
            'sequence_number': 49324,
            }
        self.reply_bin_1 = '\x01\x00\xac\xc0' '\x00\x00\x00\x00' \
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
            'blue': 34241,
            'colors': 11903,
            'cmap': 2107895767,
            'green': 33790,
            'contiguous': 1,
            'red': 37700,
            }
        self.req_bin_0 = '\x57\x01\x04\x00' '\xd7\xef\xa3\x7d' \
            '\x7f\x2e\x44\x93' '\xfe\x83\xc1\x85'

        self.reply_args_0 = {
            'red_mask': 931105404,
            'blue_mask': 874671906,
            'pixels': [1675913921, 1252164172, 37816631, 1472651082],
            'sequence_number': 17565,
            'green_mask': 1072565720,
            }
        self.reply_bin_0 = '\x01\x00\x9d\x44' '\x04\x00\x00\x00' \
            '\x04\x00\x00\x00' '\x7c\x8a\x7f\x37' \
            '\xd8\x0d\xee\x3f' '\x22\x6f\x22\x34' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xc1\x6a\xe4\x63' '\x4c\x82\xa2\x4a' \
            '\x37\x09\x41\x02' '\x4a\xdf\xc6\x57'


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
            'cmap': 32694046,
            'plane_mask': 1074378407,
            'pixels': [2014216051, 1664038241, 1220941033, 1378294408, 197757808, 793595544, 1289781247, 713684847, 1724469541, 1432124373, 1426727603, 1787792301, 406458839, 1918513211, 441394489, 988895943, 146997744],
            }
        self.req_bin_0 = '\x58\x00\x14\x00' '\x1e\xdf\xf2\x01' \
            '\xa7\xb6\x09\x40' '\x73\x7f\x0e\x78' \
            '\x61\x35\x2f\x63' '\xe9\x14\xc6\x48' \
            '\x88\x1a\x27\x52' '\x70\x8b\xc9\x0b' \
            '\x98\x4e\x4d\x2f' '\xff\x7f\xe0\x4c' \
            '\x6f\xf7\x89\x2a' '\x25\x51\xc9\x66' \
            '\xd5\x7b\x5c\x55' '\xb3\x22\x0a\x55' \
            '\xad\x8b\x8f\x6a' '\xd7\x11\x3a\x18' \
            '\x3b\x30\x5a\x72' '\x39\x25\x4f\x1a' \
            '\xc7\x5a\xf1\x3a' '\xf0\x01\xc3\x08'


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
            'items': [{'blue': 3577, 'flags': 221, 'green': 15650, 'pixel': 330879354, 'red': 30294}, {'blue': 18226, 'flags': 219, 'green': 45614, 'pixel': 302874221, 'red': 54265}, {'blue': 32215, 'flags': 160, 'green': 48737, 'pixel': 1699694808, 'red': 60115}, {'blue': 28524, 'flags': 209, 'green': 37615, 'pixel': 710550693, 'red': 50488}],
            'cmap': 1791140577,
            }
        self.req_bin_0 = '\x59\x00\x0e\x00' '\xe1\xa2\xc2\x6a' \
            '\x7a\xd1\xb8\x13' '\x56\x76\x22\x3d' \
            '\xf9\x0d\xdd\x00' '\x6d\x7e\x0d\x12' \
            '\xf9\xd3\x2e\xb2' '\x32\x47\xdb\x00' \
            '\xd8\x48\x4f\x65' '\xd3\xea\x61\xbe' \
            '\xd7\x7d\xa0\x00' '\xa5\x24\x5a\x2a' \
            '\x38\xc5\xef\x92' '\x6c\x6f\xd1\x00'


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
            'cmap': 869324276,
            'flags': 169,
            'name': 'blue',
            'pixel': 413175613,
            }
        self.req_bin_0 = '\x5a\xa9\x05\x00' '\xf4\xd5\xd0\x33' \
            '\x3d\x8f\xa0\x18' '\x04\x00\x00\x00' \
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
            'cmap': 1750052450,
            'pixels': [1673396539, 1897675292, 1453845591, 816818886, 897340342, 1782049962, 796231465, 722380604],
            }
        self.req_bin_0 = '\x5b\x00\x0a\x00' '\x62\xae\x4f\x68' \
            '\x3b\x01\xbe\x63' '\x1c\x3a\x1c\x71' \
            '\x57\xec\xa7\x56' '\xc6\xaa\xaf\x30' \
            '\xb6\x53\x7c\x35' '\xaa\xec\x37\x6a' \
            '\x29\x87\x75\x2f' '\x3c\xa7\x0e\x2b'

        self.reply_args_0 = {
            'colors': [{'blue': 63820, 'green': 60107, 'red': 62261}, {'blue': 54480, 'green': 48839, 'red': 10033}, {'blue': 31765, 'green': 31737, 'red': 43117}, {'blue': 50953, 'green': 52009, 'red': 14234}, {'blue': 55150, 'green': 30330, 'red': 55956}],
            'sequence_number': 10895,
            }
        self.reply_bin_0 = '\x01\x00\x8f\x2a' '\x0a\x00\x00\x00' \
            '\x05\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x35\xf3\xcb\xea' '\x4c\xf9\x00\x00' \
            '\x31\x27\xc7\xbe' '\xd0\xd4\x00\x00' \
            '\x6d\xa8\xf9\x7b' '\x15\x7c\x00\x00' \
            '\x9a\x37\x29\xcb' '\x09\xc7\x00\x00' \
            '\x94\xda\x7a\x76' '\x6e\xd7\x00\x00'

        self.req_args_1 = {
            'cmap': 340337174,
            'pixels': [],
            }
        self.req_bin_1 = '\x5b\x00\x02\x00' '\x16\x22\x49\x14'


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
            'cmap': 2120409969,
            'name': 'octarin',
            }
        self.req_bin_0 = '\x5c\x00\x05\x00' '\x71\xe3\x62\x7e' \
            '\x07\x00\x00\x00' '\x6f\x63\x74\x61' \
            '\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'exact_red': 63730,
            'screen_blue': 9467,
            'exact_green': 24400,
            'exact_blue': 27493,
            'screen_green': 15878,
            'screen_red': 26587,
            'sequence_number': 2933,
            }
        self.reply_bin_0 = '\x01\x00\x75\x0b' '\x00\x00\x00\x00' \
            '\xf2\xf8\x50\x5f' '\x65\x6b\xdb\x67' \
            '\x06\x3e\xfb\x24' '\x00\x00\x00\x00' \
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
            'fore_blue': 45533,
            'cid': 1389570470,
            'fore_green': 32059,
            'mask': 1475520754,
            'back_blue': 7481,
            'fore_red': 42911,
            'source': 2060548957,
            'back_green': 9237,
            'y': 31911,
            'x': 731,
            'back_red': 30886,
            }
        self.req_bin_0 = '\x5d\x00\x08\x00' '\xa6\x29\xd3\x52' \
            '\x5d\x7b\xd1\x7a' '\xf2\xa8\xf2\x57' \
            '\x9f\xa7\x3b\x7d' '\xdd\xb1\xa6\x78' \
            '\x15\x24\x39\x1d' '\xdb\x02\xa7\x7c'


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
            'fore_blue': 25271,
            'mask_char': 19164,
            'cid': 1841424177,
            'mask': 277453392,
            'fore_green': 51196,
            'fore_red': 9195,
            'source': 21529898,
            'back_green': 55277,
            'back_blue': 7419,
            'source_char': 50271,
            'back_red': 13590,
            }
        self.req_bin_0 = '\x5e\x00\x08\x00' '\x31\xe7\xc1\x6d' \
            '\x2a\x85\x48\x01' '\x50\x9a\x89\x10' \
            '\x5f\xc4\xdc\x4a' '\xeb\x23\xfc\xc7' \
            '\xb7\x62\x16\x35' '\xed\xd7\xfb\x1c'


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
            'cursor': 830435200,
            }
        self.req_bin_0 = '\x5f\x00\x02\x00' '\x80\x6f\x7f\x31'


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
            'cursor': 602252227,
            'back_red': 6018,
            'fore_blue': 64036,
            'back_green': 49024,
            'back_blue': 15439,
            'fore_green': 39148,
            'fore_red': 48154,
            }
        self.req_bin_0 = '\x60\x00\x05\x00' '\xc3\xa3\xe5\x23' \
            '\x1a\xbc\xec\x98' '\x24\xfa\x82\x17' \
            '\x80\xbf\x4f\x3c'


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
            'width': 52832,
            'item_class': 1,
            'drawable': 1606665099,
            'height': 4701,
            }
        self.req_bin_0 = '\x61\x01\x03\x00' '\x8b\xc3\xc3\x5f' \
            '\x60\xce\x5d\x12'

        self.reply_args_0 = {
            'width': 33709,
            'sequence_number': 43788,
            'height': 12826,
            }
        self.reply_bin_0 = '\x01\x00\x0c\xab' '\x00\x00\x00\x00' \
            '\xad\x83\x1a\x32' '\x00\x00\x00\x00' \
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
            'first_event': 163,
            'first_error': 166,
            'major_opcode': 215,
            'present': 1,
            'sequence_number': 3124,
            }
        self.reply_bin_0 = '\x01\x00\x34\x0c' '\x00\x00\x00\x00' \
            '\x01\xd7\xa3\xa6' '\x00\x00\x00\x00' \
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
            'names': ['XTRA', 'XTRA-II'],
            'sequence_number': 21122,
            }
        self.reply_bin_0 = '\x01\x02\x82\x52' '\x04\x00\x00\x00' \
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
            'first_keycode': 131,
            'keysyms': [[1479273593, 495399194, 1752874714], [183124138, 826800766, 542058728], [519501686, 1358630902, 1051542205], [1363902850, 52079613, 1721268402], [2124568309, 323328202, 1426344655], [1775218167, 1821828429, 1704892958], [1784543283, 783698836, 1882907069], [1165130550, 1276086917, 957090966], [1623553701, 77158667, 420399405], [790514637, 1104383431, 1645303152], [879499287, 349457843, 1313813953], [367336866, 1207824094, 514125338], [767413913, 135340640, 756292967], [475442692, 2076098223, 1252936842], [964050497, 2006979633, 948353974], [1923834215, 1061136894, 1319606154], [1186538913, 1770176901, 715354628], [1470481551, 403222608, 252019996], [260033548, 1553379907, 1096456683], [2027881549, 1992616114, 382810564]],
            }
        self.req_bin_0 = '\x64\x14\x3e\x00' '\x83\x03\x00\x00' \
            '\x79\xec\x2b\x58' '\x1a\x31\x87\x1d' \
            '\xda\xbe\x7a\x68' '\xaa\x40\xea\x0a' \
            '\x7e\xfa\x47\x31' '\xe8\x28\x4f\x20' \
            '\x76\xf7\xf6\x1e' '\xf6\x0f\xfb\x50' \
            '\xbd\x42\xad\x3e' '\x82\x81\x4b\x51' \
            '\xfd\xab\x1a\x03' '\xb2\x78\x98\x66' \
            '\xf5\x56\xa2\x7e' '\xca\x98\x45\x13' \
            '\xcf\x4a\x04\x55' '\xf7\xad\xcf\x69' \
            '\x4d\xe5\x96\x6c' '\x1e\x9a\x9e\x65' \
            '\x33\xf8\x5d\x6a' '\x94\x4b\xb6\x2e' \
            '\xbd\xe1\x3a\x70' '\x36\x7b\x72\x45' \
            '\x85\x8a\x0f\x4c' '\x96\x0c\x0c\x39' \
            '\xa5\x76\xc5\x60' '\x0b\x59\x99\x04' \
            '\x2d\xc9\x0e\x19' '\xcd\x4b\x1e\x2f' \
            '\xc7\x8d\xd3\x41' '\x70\x55\x11\x62' \
            '\x17\x18\x6c\x34' '\xb3\x4d\xd4\x14' \
            '\xc1\x35\x4f\x4e' '\xa2\x1d\xe5\x15' \
            '\xde\xee\xfd\x47' '\x1a\xee\xa4\x1e' \
            '\x99\xce\xbd\x2d' '\x60\x22\x11\x08' \
            '\x67\x1d\x14\x2d' '\x04\xae\x56\x1c' \
            '\xaf\xbe\xbe\x7b' '\x8a\x4c\xae\x4a' \
            '\x41\x3e\x76\x39' '\x31\x14\xa0\x77' \
            '\xb6\xbb\x86\x38' '\x67\x61\xab\x72' \
            '\xfe\xa9\x3f\x3f' '\x8a\x97\xa7\x4e' \
            '\xa1\x25\xb9\x46' '\x85\xc1\x82\x69' \
            '\x04\x72\xa3\x2a' '\x8f\xc4\xa5\x57' \
            '\x50\xb0\x08\x18' '\x1c\x85\x05\x0f' \
            '\x0c\xcc\x7f\x0f' '\x43\xb2\x96\x5c' \
            '\xeb\x99\x5a\x41' '\x4d\x04\xdf\x78' \
            '\xb2\xe8\xc4\x76' '\xc4\x39\xd1\x16'


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
            'first_keycode': 174,
            'count': 233,
            }
        self.req_bin_0 = '\x65\x00\x02\x00' '\xae\xe9\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[536700486, 90972970, 1834434734], [604690854, 1612992766, 1785113276], [1258017014, 814047417, 79874791], [1752913778, 2069894554, 1342993084], [691283205, 2002270597, 1552550365], [1427239047, 80222814, 380890249], [932130695, 1233544402, 1343201446], [850296480, 830996690, 1219102856], [1427529259, 1334110395, 1423305447], [925543758, 1154246092, 389857513], [782217983, 1673349321, 296773941], [904384636, 788791004, 1427343811], [578056967, 1628142600, 882651915], [1727003528, 1202959768, 59536638], [932784259, 453243643, 1846802632], [1527858524, 2055184942, 1534128611], [134086768, 909769847, 323736641], [2080620639, 1573387975, 566724688], [1393924270, 1408645244, 1610610798], [391612329, 341605408, 484634403]],
            'sequence_number': 27901,
            }
        self.reply_bin_0 = '\x01\x03\xfd\x6c' '\x3c\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x46\x66\xfd\x1f' '\x2a\x23\x6c\x05' \
            '\xae\x40\x57\x6d' '\xa6\xd9\x0a\x24' \
            '\xfe\x50\x24\x60' '\xbc\xaa\x66\x6a' \
            '\xf6\xd0\xfb\x4a' '\xb9\x60\x85\x30' \
            '\xe7\xca\xc2\x04' '\x72\x57\x7b\x68' \
            '\x9a\x15\x60\x7b' '\xbc\x72\x0c\x50' \
            '\x05\x25\x34\x29' '\x85\x39\x58\x77' \
            '\xdd\x09\x8a\x5c' '\x87\xf0\x11\x55' \
            '\x5e\x1a\xc8\x04' '\x89\xec\xb3\x16' \
            '\x87\x2f\x8f\x37' '\xd2\x64\x86\x49' \
            '\xa6\xa0\x0f\x50' '\xa0\x7e\xae\x32' \
            '\xd2\x00\x88\x31' '\x88\x08\xaa\x48' \
            '\x2b\x5e\x16\x55' '\xbb\xe8\x84\x4f' \
            '\xe7\xea\xd5\x54' '\x4e\xad\x2a\x37' \
            '\xcc\x65\xcc\x44' '\xe9\xc0\x3c\x17' \
            '\xff\xb2\x9f\x2e' '\xc9\x48\xbd\x63' \
            '\x35\x69\xb0\x11' '\x7c\xd0\xe7\x35' \
            '\xdc\xfe\x03\x2f' '\xc3\x89\x13\x55' \
            '\x07\x73\x74\x22' '\x08\x7c\x0b\x61' \
            '\x0b\x33\x9c\x34' '\x88\xfb\xef\x66' \
            '\x98\xb5\xb3\x47' '\xfe\x74\x8c\x03' \
            '\x83\x28\x99\x37' '\xfb\xf2\x03\x1b' \
            '\xc8\xf8\x13\x6e' '\x5c\x45\x11\x5b' \
            '\x2e\xa2\x7f\x7a' '\xe3\xf1\x70\x5b' \
            '\x70\x00\xfe\x07' '\x77\xfc\x39\x36' \
            '\x41\xd4\x4b\x13' '\x5f\xc0\x03\x7c' \
            '\xc7\xfe\xc7\x5d' '\x50\x88\xc7\x21' \
            '\xae\x98\x15\x53' '\x7c\x38\xf6\x53' \
            '\x6e\xf8\xff\x5f' '\xa9\x87\x57\x17' \
            '\x20\x7c\x5c\x14' '\x23\xef\xe2\x1c'


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
            'attrs': {'led': 241, 'key': 193, 'bell_duration': -19485, 'auto_repeat_mode': 0, 'bell_pitch': -13220, 'key_click_percent': -3, 'bell_percent': -74, 'led_mode': 1},
            }
        self.req_bin_0 = '\x66\x00\x0a\x00' '\xff\x00\x00\x00' \
            '\xfd\x00\x00\x00' '\xb6\x00\x00\x00' \
            '\x5c\xcc\x00\x00' '\xe3\xb3\x00\x00' \
            '\xf1\x00\x00\x00' '\x01\x00\x00\x00' \
            '\xc1\x00\x00\x00' '\x00\x00\x00\x00'


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
            'led_mask': 1389423883,
            'global_auto_repeat': 1,
            'auto_repeats': [129, 211, 180, 202, 218, 145, 129, 136, 137, 165, 210, 160, 229, 223, 226, 130, 197, 233, 187, 166, 211, 241, 173, 183, 184, 216, 216, 218, 182, 224, 175, 210],
            'bell_pitch': 27576,
            'bell_duration': 26314,
            'bell_percent': 130,
            'sequence_number': 62321,
            'key_click_percent': 140,
            }
        self.reply_bin_0 = '\x01\x01\x71\xf3' '\x05\x00\x00\x00' \
            '\x0b\xed\xd0\x52' '\x8c\x82\xb8\x6b' \
            '\xca\x66\x00\x00' '\x81\xd3\xb4\xca' \
            '\xda\x91\x81\x88' '\x89\xa5\xd2\xa0' \
            '\xe5\xdf\xe2\x82' '\xc5\xe9\xbb\xa6' \
            '\xd3\xf1\xad\xb7' '\xb8\xd8\xd8\xda' \
            '\xb6\xe0\xaf\xd2'


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
            'percent': -14,
            }
        self.req_bin_0 = '\x68\xf2\x01\x00'


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
            'accel_num': -5554,
            'threshold': -10566,
            'do_accel': 1,
            'accel_denum': -24572,
            'do_thresh': 1,
            }
        self.req_bin_0 = '\x69\x00\x03\x00' '\x4e\xea\x04\xa0' \
            '\xba\xd6\x01\x01'


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
            'accel_num': 11888,
            'threshold': 36822,
            'sequence_number': 62480,
            'accel_denom': 46073,
            }
        self.reply_bin_0 = '\x01\x00\x10\xf4' '\x00\x00\x00\x00' \
            '\x70\x2e\xf9\xb3' '\xd6\x8f\x00\x00' \
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
            'prefer_blank': 1,
            'interval': -19218,
            'timeout': -2423,
            'allow_exposures': 2,
            }
        self.req_bin_0 = '\x6b\x00\x03\x00' '\x89\xf6\xee\xb4' \
            '\x01\x02\x00\x00'


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
            'interval': 51464,
            'prefer_blanking': 1,
            'timeout': 5207,
            'sequence_number': 45153,
            'allow_exposures': 1,
            }
        self.reply_bin_0 = '\x01\x00\x61\xb0' '\x00\x00\x00\x00' \
            '\x57\x14\x08\xc9' '\x01\x01\x00\x00' \
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
            'host': [150, 200, 205, 182],
            'mode': 0,
            'host_family': 0,
            }
        self.req_bin_0 = '\x6d\x00\x03\x00' '\x00\x00\x04\x00' \
            '\x96\xc8\xcd\xb6'


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
            'hosts': [{'name': [34, 23, 178, 12], 'family': 0}, {'name': [130, 236, 254, 15], 'family': 0}],
            'mode': 1,
            'sequence_number': 33455,
            }
        self.reply_bin_0 = '\x01\x01\xaf\x82' '\x04\x00\x00\x00' \
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
            'mode': 1,
            }
        self.req_bin_0 = '\x70\x01\x01\x00'


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
            'resource': 1900634441,
            }
        self.req_bin_0 = '\x71\x00\x02\x00' '\x49\x61\x49\x71'


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
            'window': 1149115389,
            'properties': [194806244, 1444715269, 486779871, 1850032482, 1083061497, 786546027, 807635511, 1716883082, 80335197, 1654299, 1459844212, 850673646],
            'delta': -27029,
            }
        self.req_bin_0 = '\x72\x00\x0f\x00' '\xfd\x1b\x7e\x44' \
            '\x0c\x00\x6b\x96' '\xe4\x81\x9c\x0b' \
            '\x05\x9b\x1c\x56' '\xdf\xab\x03\x1d' \
            '\x62\x41\x45\x6e' '\xf9\x34\x8e\x40' \
            '\x6b\xbd\xe1\x2e' '\x37\x8a\x23\x30' \
            '\x8a\x8e\x55\x66' '\x5d\xd1\xc9\x04' \
            '\x1b\x3e\x19\x00' '\x74\x74\x03\x57' \
            '\xee\x3f\xb4\x32'


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
            'map': [130, 178, 229, 218, 178],
            }
        self.req_bin_0 = '\x74\x05\x03\x00' '\x82\xb2\xe5\xda' \
            '\xb2\x00\x00\x00'

        self.reply_args_0 = {
            'status': 145,
            'sequence_number': 57045,
            }
        self.reply_bin_0 = '\x01\x91\xd5\xde' '\x00\x00\x00\x00' \
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
            'map': [248, 185, 227, 157, 133],
            'sequence_number': 20072,
            }
        self.reply_bin_0 = '\x01\x05\x68\x4e' '\x02\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\xf8\xb9\xe3\x9d' '\x85\x00\x00\x00'


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
            'keycodes': [[6, 191], [94, 123], [46, 94], [104, 116], [132, 158], [35, 75], [128, 63], [135, 221]],
            }
        self.req_bin_0 = '\x76\x02\x05\x00' '\x06\xbf\x5e\x7b' \
            '\x2e\x5e\x68\x74' '\x84\x9e\x23\x4b' \
            '\x80\x3f\x87\xdd'

        self.reply_args_0 = {
            'status': 149,
            'sequence_number': 26757,
            }
        self.reply_bin_0 = '\x01\x95\x85\x68' '\x00\x00\x00\x00' \
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
            'keycodes': [[85, 162], [139, 194], [12, 107], [120, 193], [26, 40], [125, 221], [27, 0], [220, 78]],
            'sequence_number': 17677,
            }
        self.reply_bin_0 = '\x01\x02\x0d\x45' '\x04\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x00\x00\x00\x00' '\x00\x00\x00\x00' \
            '\x55\xa2\x8b\xc2' '\x0c\x6b\x78\xc1' \
            '\x1a\x28\x7d\xdd' '\x1b\x00\xdc\x4e'


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
