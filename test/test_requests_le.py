#!/usr/bin/env python2

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(__file__, '../..')))

import unittest
from Xlib.protocol import request, event
from . import LittleEndianTest as EndianTest
from . import DummyDisplay

dummy_display = DummyDisplay()


class TestCreateWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'cursor': 1395639147, 'override_redirect': 0, 'bit_gravity': 7, 'event_mask': 1085274634, 'border_pixel': 479392317, 'background_pixel': 53774084, 'save_under': 0, 'colormap': 427053108, 'do_not_propagate_mask': 57049357, 'backing_store': 2, 'win_gravity': 6, 'backing_planes': 186759559, 'border_pixmap': 590668475, 'backing_pixel': 906108093, 'background_pixmap': 1373182223},
            'border_width': 22467,
            'depth': 197,
            'height': 45830,
            'parent': 1265465337,
            'visual': 2055602223,
            'wid': 473443720,
            'width': 52859,
            'window_class': 0,
            'x': -6451,
            'y': -32557,
            }
        self.req_bin_0 = b'\x01\xc5\x17\x00' b'\x88\x2d\x38\x1c' \
            b'\xf9\x77\x6d\x4b' b'\xcd\xe6\xd3\x80' \
            b'\x7b\xce\x06\xb3' b'\xc3\x57\x00\x00' \
            b'\x2f\x00\x86\x7a' b'\xff\x7f\x00\x00' \
            b'\x0f\x19\xd9\x51' b'\x04\x87\x34\x03' \
            b'\xbb\xe2\x34\x23' b'\x3d\xf2\x92\x1c' \
            b'\x07\x00\x00\x00' b'\x06\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x87\xb9\x21\x0b' \
            b'\xbd\x1c\x02\x36' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x0a\xfa\xaf\x40' \
            b'\x0d\x81\x66\x03' b'\x34\x50\x74\x19' \
            b'\x6b\xc3\x2f\x53'


    def testPackRequest0(self):
        bin = request.CreateWindow._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CreateWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestChangeWindowAttributes(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'cursor': 1239881989, 'override_redirect': 0, 'bit_gravity': 5, 'event_mask': 1781144133, 'border_pixel': 1819990287, 'background_pixel': 199229639, 'save_under': 1, 'colormap': 1850510540, 'do_not_propagate_mask': 1328286054, 'backing_store': 2, 'win_gravity': 7, 'backing_planes': 1151571451, 'border_pixmap': 207756035, 'backing_pixel': 2089751951, 'background_pixmap': 722874758},
            'window': 1513075857,
            }
        self.req_bin_0 = b'\x02\x00\x12\x00' b'\x91\xb4\x2f\x5a' \
            b'\xff\x7f\x00\x00' b'\x86\x31\x16\x2b' \
            b'\xc7\x00\xe0\x0b' b'\x03\x1b\x62\x0c' \
            b'\x0f\xd9\x7a\x6c' b'\x05\x00\x00\x00' \
            b'\x07\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\xfb\x95\xa3\x44' b'\x8f\x15\x8f\x7c' \
            b'\x00\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x45\x1a\x2a\x6a' b'\x66\x09\x2c\x4f' \
            b'\xcc\x8c\x4c\x6e' b'\x05\x19\xe7\x49'


    def testPackRequest0(self):
        bin = request.ChangeWindowAttributes._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeWindowAttributes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetWindowAttributes(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 98469647,
            }
        self.req_bin_0 = b'\x03\x00\x02\x00' b'\x0f\x87\xde\x05'

        self.reply_args_0 = {
            'all_event_masks': 1308124489,
            'backing_bit_planes': 1365145824,
            'backing_pixel': 783512764,
            'backing_store': 157,
            'bit_gravity': 140,
            'colormap': 1391668458,
            'do_not_propagate_mask': 47853,
            'map_is_installed': 0,
            'map_state': 162,
            'override_redirect': 1,
            'save_under': 0,
            'sequence_number': 19147,
            'visual': 171412272,
            'win_class': 15452,
            'win_gravity': 163,
            'your_event_mask': 367571768,
            }
        self.reply_bin_0 = b'\x01\x9d\xcb\x4a' b'\x03\x00\x00\x00' \
            b'\x30\x8b\x37\x0a' b'\x5c\x3c\x8c\xa3' \
            b'\xe0\x78\x5e\x51' b'\xbc\x74\xb3\x2e' \
            b'\x00\x00\xa2\x01' b'\xea\x2c\xf3\x52' \
            b'\x49\x65\xf8\x4d' b'\x38\xb3\xe8\x15' \
            b'\xed\xba\x00\x00'


    def testPackRequest0(self):
        bin = request.GetWindowAttributes._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetWindowAttributes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetWindowAttributes._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetWindowAttributes._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestDestroyWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 350959010,
            }
        self.req_bin_0 = b'\x04\x00\x02\x00' b'\xa2\x35\xeb\x14'


    def testPackRequest0(self):
        bin = request.DestroyWindow._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.DestroyWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestDestroySubWindows(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 814915023,
            }
        self.req_bin_0 = b'\x05\x00\x02\x00' b'\xcf\x9d\x92\x30'


    def testPackRequest0(self):
        bin = request.DestroySubWindows._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.DestroySubWindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestChangeSaveSet(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'mode': 1,
            'window': 1374412611,
            }
        self.req_bin_0 = b'\x06\x01\x02\x00' b'\x43\xdf\xeb\x51'


    def testPackRequest0(self):
        bin = request.ChangeSaveSet._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeSaveSet._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestReparentWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'parent': 1470218577,
            'window': 1196069502,
            'x': -5365,
            'y': -7538,
            }
        self.req_bin_0 = b'\x07\x00\x04\x00' b'\x7e\x92\x4a\x47' \
            b'\x51\xc1\xa1\x57' b'\x0b\xeb\x8e\xe2'


    def testPackRequest0(self):
        bin = request.ReparentWindow._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ReparentWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestMapWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 491927514,
            }
        self.req_bin_0 = b'\x08\x00\x02\x00' b'\xda\x37\x52\x1d'


    def testPackRequest0(self):
        bin = request.MapWindow._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.MapWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestMapSubwindows(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 68998181,
            }
        self.req_bin_0 = b'\x09\x00\x02\x00' b'\x25\xd4\x1c\x04'


    def testPackRequest0(self):
        bin = request.MapSubwindows._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.MapSubwindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestUnmapWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 677475124,
            }
        self.req_bin_0 = b'\x0a\x00\x02\x00' b'\x34\x73\x61\x28'


    def testPackRequest0(self):
        bin = request.UnmapWindow._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UnmapWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestUnmapSubwindows(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 575017142,
            }
        self.req_bin_0 = b'\x0b\x00\x02\x00' b'\xb6\x10\x46\x22'


    def testPackRequest0(self):
        bin = request.UnmapSubwindows._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UnmapSubwindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestConfigureWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'width': 61485, 'stack_mode': 4, 'height': 43079, 'sibling': 849652645, 'y': -1871, 'x': -25855, 'border_width': -11291},
            'window': 985412314,
            }
        self.req_bin_0 = b'\x0c\x00\x0a\x00' b'\xda\x32\xbc\x3a' \
            b'\x7f\x00\x00\x00' b'\x01\x9b\x00\x00' \
            b'\xb1\xf8\x00\x00' b'\x2d\xf0\x00\x00' \
            b'\x47\xa8\x00\x00' b'\xe5\xd3\x00\x00' \
            b'\xa5\xab\xa4\x32' b'\x04\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ConfigureWindow._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ConfigureWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCirculateWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'direction': 0,
            'window': 529677912,
            }
        self.req_bin_0 = b'\x0d\x00\x02\x00' b'\x58\x3e\x92\x1f'


    def testPackRequest0(self):
        bin = request.CirculateWindow._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CirculateWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetGeometry(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 1205557634,
            }
        self.req_bin_0 = b'\x0e\x00\x02\x00' b'\x82\x59\xdb\x47'

        self.reply_args_0 = {
            'border_width': 6190,
            'depth': 161,
            'height': 33517,
            'root': 1928066656,
            'sequence_number': 38417,
            'width': 65375,
            'x': -19783,
            'y': -25638,
            }
        self.reply_bin_0 = b'\x01\xa1\x11\x96' b'\x00\x00\x00\x00' \
            b'\x60\xf6\xeb\x72' b'\xb9\xb2\xda\x9b' \
            b'\x5f\xff\xed\x82' b'\x2e\x18\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetGeometry._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetGeometry._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetGeometry._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetGeometry._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestQueryTree(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 101244093,
            }
        self.req_bin_0 = b'\x0f\x00\x02\x00' b'\xbd\xdc\x08\x06'

        self.reply_args_0 = {
            'children': [235528064, 1347454529, 1700991108, 906619494, 136486082, 819561703, 2139154628],
            'parent': 1848519458,
            'root': 2085376831,
            'sequence_number': 34796,
            }
        self.reply_bin_0 = b'\x01\x00\xec\x87' b'\x07\x00\x00\x00' \
            b'\x3f\x53\x4c\x7c' b'\x22\x2b\x2e\x6e' \
            b'\x07\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x80\xdf\x09\x0e' b'\x41\x86\x50\x50' \
            b'\x84\x10\x63\x65' b'\x66\xea\x09\x36' \
            b'\xc2\x9c\x22\x08' b'\xe7\x84\xd9\x30' \
            b'\xc4\xe8\x80\x7f'


    def testPackRequest0(self):
        bin = request.QueryTree._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryTree._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.QueryTree._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryTree._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestInternAtom(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'name': 'fuzzy_prop',
            'only_if_exists': 0,
            }
        self.req_bin_0 = b'\x10\x00\x05\x00' b'\x0a\x00\x00\x00' \
            b'\x66\x75\x7a\x7a' b'\x79\x5f\x70\x72' \
            b'\x6f\x70\x00\x00'

        self.reply_args_0 = {
            'atom': 1463982728,
            'sequence_number': 47304,
            }
        self.reply_bin_0 = b'\x01\x00\xc8\xb8' b'\x00\x00\x00\x00' \
            b'\x88\x9a\x42\x57' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.InternAtom._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.InternAtom._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.InternAtom._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.InternAtom._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestGetAtomName(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'atom': 1153165348,
            }
        self.req_bin_0 = b'\x11\x00\x02\x00' b'\x24\xe8\xbb\x44'

        self.reply_args_0 = {
            'name': 'WM_CLASS',
            'sequence_number': 17674,
            }
        self.reply_bin_0 = b'\x01\x00\x0a\x45' b'\x02\x00\x00\x00' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x57\x4d\x5f\x43' b'\x4c\x41\x53\x53'


    def testPackRequest0(self):
        bin = request.GetAtomName._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetAtomName._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetAtomName._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetAtomName._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestChangeProperty(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'data': (8, ''),
            'mode': 1,
            'property': 933688309,
            'type': 974400040,
            'window': 239614693,
            }
        self.req_bin_0 = b'\x12\x01\x06\x00' b'\xe5\x3a\x48\x0e' \
            b'\xf5\xf3\xa6\x37' b'\x28\x2a\x14\x3a' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_1 = {
            'data': (8, 'foo'),
            'mode': 2,
            'property': 565671953,
            'type': 1075033221,
            'window': 1880888002,
            }
        self.req_bin_1 = b'\x12\x02\x07\x00' b'\xc2\x12\x1c\x70' \
            b'\x11\x78\xb7\x21' b'\x85\xb4\x13\x40' \
            b'\x08\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'data': (8, 'zoom'),
            'mode': 0,
            'property': 1869432878,
            'type': 640951286,
            'window': 1959859086,
            }
        self.req_bin_2 = b'\x12\x00\x07\x00' b'\x8e\x13\xd1\x74' \
            b'\x2e\x48\x6d\x6f' b'\xf6\x23\x34\x26' \
            b'\x08\x00\x00\x00' b'\x04\x00\x00\x00' \
            b'\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'data': (16, []),
            'mode': 1,
            'property': 328275349,
            'type': 1637495037,
            'window': 1307779197,
            }
        self.req_bin_3 = b'\x12\x01\x06\x00' b'\x7d\x20\xf3\x4d' \
            b'\x95\x15\x91\x13' b'\xfd\x30\x9a\x61' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_4 = {
            'data': (16, [1, 2, 3]),
            'mode': 1,
            'property': 1138956616,
            'type': 1293636,
            'window': 1672102137,
            }
        self.req_bin_4 = b'\x12\x01\x08\x00' b'\xf9\x40\xaa\x63' \
            b'\x48\x19\xe3\x43' b'\x44\xbd\x13\x00' \
            b'\x10\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x00\x00'

        self.req_args_5 = {
            'data': (16, [1, 2, 3, 4]),
            'mode': 0,
            'property': 1995228731,
            'type': 1887048810,
            'window': 41890245,
            }
        self.req_bin_5 = b'\x12\x00\x08\x00' b'\xc5\x31\x7f\x02' \
            b'\x3b\xc6\xec\x76' b'\x6a\x14\x7a\x70' \
            b'\x10\x00\x00\x00' b'\x04\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x04\x00'

        self.req_args_6 = {
            'data': (32, []),
            'mode': 2,
            'property': 124455087,
            'type': 1885519250,
            'window': 660426938,
            }
        self.req_bin_6 = b'\x12\x02\x06\x00' b'\xba\x50\x5d\x27' \
            b'\xaf\x08\x6b\x07' b'\x92\xbd\x62\x70' \
            b'\x20\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_7 = {
            'data': (32, [1, 2, 3]),
            'mode': 2,
            'property': 1043690258,
            'type': 148693751,
            'window': 183999310,
            }
        self.req_bin_7 = b'\x12\x02\x09\x00' b'\x4e\x9b\xf7\x0a' \
            b'\x12\x73\x35\x3e' b'\xf7\xe2\xdc\x08' \
            b'\x20\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x01\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x03\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackRequest1(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_1)
        self.assertBinaryEqual(bin, self.req_bin_1)

    def testUnpackRequest1(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_1)

    def testPackRequest2(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_2)
        self.assertBinaryEqual(bin, self.req_bin_2)

    def testUnpackRequest2(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_2, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_2)

    def testPackRequest3(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_3)
        self.assertBinaryEqual(bin, self.req_bin_3)

    def testUnpackRequest3(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_3, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_3)

    def testPackRequest4(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_4)
        self.assertBinaryEqual(bin, self.req_bin_4)

    def testUnpackRequest4(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_4, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_4)

    def testPackRequest5(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_5)
        self.assertBinaryEqual(bin, self.req_bin_5)

    def testUnpackRequest5(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_5, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_5)

    def testPackRequest6(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_6)
        self.assertBinaryEqual(bin, self.req_bin_6)

    def testUnpackRequest6(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_6, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_6)

    def testPackRequest7(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_7)
        self.assertBinaryEqual(bin, self.req_bin_7)

    def testUnpackRequest7(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_7, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_7)


class TestDeleteProperty(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'property': 1644632259,
            'window': 1633396400,
            }
        self.req_bin_0 = b'\x13\x00\x03\x00' b'\xb0\xa6\x5b\x61' \
            b'\xc3\x18\x07\x62'


    def testPackRequest0(self):
        bin = request.DeleteProperty._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.DeleteProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetProperty(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'delete': 0,
            'long_length': 908719612,
            'long_offset': 1873544049,
            'property': 1180723730,
            'type': 569252941,
            'window': 1020695522,
            }
        self.req_bin_0 = b'\x14\x00\x06\x00' b'\xe2\x93\xd6\x3c' \
            b'\x12\x6a\x60\x46' b'\x4d\x1c\xee\x21' \
            b'\x71\x03\xac\x6f' b'\xfc\xf5\x29\x36'

        self.reply_args_0 = {
            'bytes_after': 1567532733,
            'property_type': 1158159724,
            'sequence_number': 14082,
            'value': (8, ''),
            }
        self.reply_bin_0 = b'\x01\x08\x02\x37' b'\x00\x00\x00\x00' \
            b'\x6c\x1d\x08\x45' b'\xbd\xa6\x6e\x5d' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_1 = {
            'bytes_after': 2137067287,
            'property_type': 669450745,
            'sequence_number': 13387,
            'value': (8, 'foo'),
            }
        self.reply_bin_1 = b'\x01\x08\x4b\x34' b'\x01\x00\x00\x00' \
            b'\xf9\x01\xe7\x27' b'\x17\x0f\x61\x7f' \
            b'\x03\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'bytes_after': 1111517270,
            'property_type': 940849590,
            'sequence_number': 42680,
            'value': (8, 'zoom'),
            }
        self.reply_bin_2 = b'\x01\x08\xb8\xa6' b'\x01\x00\x00\x00' \
            b'\xb6\x39\x14\x38' b'\x56\x68\x40\x42' \
            b'\x04\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'bytes_after': 726076595,
            'property_type': 482584667,
            'sequence_number': 8155,
            'value': (16, []),
            }
        self.reply_bin_3 = b'\x01\x10\xdb\x1f' b'\x00\x00\x00\x00' \
            b'\x5b\xa8\xc3\x1c' b'\xb3\x0c\x47\x2b' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_4 = {
            'bytes_after': 472964335,
            'property_type': 494218080,
            'sequence_number': 38660,
            'value': (16, [1, 2, 3]),
            }
        self.reply_bin_4 = b'\x01\x10\x04\x97' b'\x02\x00\x00\x00' \
            b'\x60\x2b\x75\x1d' b'\xef\xdc\x30\x1c' \
            b'\x03\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x00\x00'

        self.reply_args_5 = {
            'bytes_after': 491699268,
            'property_type': 1355307456,
            'sequence_number': 4890,
            'value': (16, [1, 2, 3, 4]),
            }
        self.reply_bin_5 = b'\x01\x10\x1a\x13' b'\x02\x00\x00\x00' \
            b'\xc0\x59\xc8\x50' b'\x44\xbc\x4e\x1d' \
            b'\x04\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x04\x00'

        self.reply_args_6 = {
            'bytes_after': 152225892,
            'property_type': 1846062163,
            'sequence_number': 59361,
            'value': (32, []),
            }
        self.reply_bin_6 = b'\x01\x20\xe1\xe7' b'\x00\x00\x00\x00' \
            b'\x53\xac\x08\x6e' b'\x64\xc8\x12\x09' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_7 = {
            'bytes_after': 460121536,
            'property_type': 1436640532,
            'sequence_number': 15792,
            'value': (32, [1, 2, 3]),
            }
        self.reply_bin_7 = b'\x01\x20\xb0\x3d' b'\x03\x00\x00\x00' \
            b'\x14\x65\xa1\x55' b'\xc0\xe5\x6c\x1b' \
            b'\x03\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x01\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x03\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetProperty._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)

    def testPackReply1(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_1)
        self.assertBinaryEqual(bin, self.reply_bin_1)

    def testUnpackReply1(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_1)

    def testPackReply2(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_2)
        self.assertBinaryEqual(bin, self.reply_bin_2)

    def testUnpackReply2(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_2, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_2)

    def testPackReply3(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_3)
        self.assertBinaryEqual(bin, self.reply_bin_3)

    def testUnpackReply3(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_3, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_3)

    def testPackReply4(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_4)
        self.assertBinaryEqual(bin, self.reply_bin_4)

    def testUnpackReply4(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_4, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_4)

    def testPackReply5(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_5)
        self.assertBinaryEqual(bin, self.reply_bin_5)

    def testUnpackReply5(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_5, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_5)

    def testPackReply6(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_6)
        self.assertBinaryEqual(bin, self.reply_bin_6)

    def testUnpackReply6(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_6, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_6)

    def testPackReply7(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_7)
        self.assertBinaryEqual(bin, self.reply_bin_7)

    def testUnpackReply7(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_7, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_7)


class TestListProperties(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 284194396,
            }
        self.req_bin_0 = b'\x15\x00\x02\x00' b'\x5c\x76\xf0\x10'

        self.reply_args_0 = {
            'atoms': [2009005759, 1226333816, 1015087858, 1684971497, 1734099213, 408955234, 208216521, 925712651, 909665942, 1002962766, 1565696219, 1446060760, 2113479735, 211409854, 864661769, 728690095, 1850436746, 534034650, 408523590, 963426393, 906021810, 598218424, 536504426],
            'sequence_number': 60526,
            }
        self.reply_bin_0 = b'\x01\x00\x6e\xec' b'\x17\x00\x00\x00' \
            b'\x17\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xbf\xfe\xbe\x77' b'\x78\x5e\x18\x49' \
            b'\xf2\x02\x81\x3c' b'\xe9\x9f\x6e\x64' \
            b'\x0d\x41\x5c\x67' b'\x62\x29\x60\x18' \
            b'\xc9\x21\x69\x0c' b'\x0b\x41\x2d\x37' \
            b'\x96\x66\x38\x36' b'\x4e\xff\xc7\x3b' \
            b'\xdb\xa0\x52\x5d' b'\xd8\x22\x31\x56' \
            b'\x37\x24\xf9\x7d' b'\xbe\xdb\x99\x0c' \
            b'\x09\xb1\x89\x33' b'\xaf\xed\x6e\x2b' \
            b'\x8a\x6c\x4b\x6e' b'\xda\xb8\xd4\x1f' \
            b'\x46\x93\x59\x18' b'\x59\xb8\x6c\x39' \
            b'\xb2\xcb\x00\x36' b'\xb8\x16\xa8\x23' \
            b'\x6a\x68\xfa\x1f'


    def testPackRequest0(self):
        bin = request.ListProperties._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ListProperties._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.ListProperties._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.ListProperties._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestSetSelectionOwner(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'selection': 1849742203,
            'time': 1181844078,
            'window': 951652523,
            }
        self.req_bin_0 = b'\x16\x00\x04\x00' b'\xab\x10\xb9\x38' \
            b'\x7b\xd3\x40\x6e' b'\x6e\x82\x71\x46'


    def testPackRequest0(self):
        bin = request.SetSelectionOwner._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetSelectionOwner._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetSelectionOwner(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'selection': 108699831,
            }
        self.req_bin_0 = b'\x17\x00\x02\x00' b'\xb7\xa0\x7a\x06'

        self.reply_args_0 = {
            'owner': 1795366313,
            'sequence_number': 65489,
            }
        self.reply_bin_0 = b'\x01\x00\xd1\xff' b'\x00\x00\x00\x00' \
            b'\xa9\x1d\x03\x6b' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetSelectionOwner._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetSelectionOwner._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetSelectionOwner._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetSelectionOwner._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestConvertSelection(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'property': 357205026,
            'requestor': 2080905648,
            'selection': 1989362772,
            'target': 1822570126,
            'time': 1042940084,
            }
        self.req_bin_0 = b'\x18\x00\x06\x00' b'\xb0\x19\x08\x7c' \
            b'\x54\x44\x93\x76' b'\x8e\x36\xa2\x6c' \
            b'\x22\x84\x4a\x15' b'\xb4\x00\x2a\x3e'


    def testPackRequest0(self):
        bin = request.ConvertSelection._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ConvertSelection._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestSendEvent(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'destination': 977158744,
            'event': event.Expose(count=17568, height=64576, sequence_number=0, type=12, width=24995, window=459070357, x=26435, y=4083),
            'event_mask': 908439472,
            'propagate': 1,
            }
        self.req_bin_0 = b'\x19\x01\x0b\x00' b'\x58\x42\x3e\x3a' \
            b'\xb0\xaf\x25\x36' b'\x0c\x00\x00\x00' \
            b'\x95\xdb\x5c\x1b' b'\x43\x67\xf3\x0f' \
            b'\xa3\x61\x40\xfc' b'\xa0\x44\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SendEvent._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SendEvent._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGrabPointer(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'confine_to': 637221294,
            'cursor': 2080289570,
            'event_mask': 36536,
            'grab_window': 2137654247,
            'keyboard_mode': 0,
            'owner_events': 1,
            'pointer_mode': 1,
            'time': 1243807782,
            }
        self.req_bin_0 = b'\x1a\x01\x06\x00' b'\xe7\x03\x6a\x7f' \
            b'\xb8\x8e\x01\x00' b'\xae\x39\xfb\x25' \
            b'\x22\xb3\xfe\x7b' b'\x26\x00\x23\x4a'

        self.reply_args_0 = {
            'sequence_number': 49083,
            'status': 197,
            }
        self.reply_bin_0 = b'\x01\xc5\xbb\xbf' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GrabPointer._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GrabPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GrabPointer._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GrabPointer._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestUngrabPointer(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'time': 122823278,
            }
        self.req_bin_0 = b'\x1b\x00\x02\x00' b'\x6e\x22\x52\x07'


    def testPackRequest0(self):
        bin = request.UngrabPointer._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UngrabPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGrabButton(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'button': 204,
            'confine_to': 172098347,
            'cursor': 399109422,
            'event_mask': 55921,
            'grab_window': 1079895555,
            'keyboard_mode': 1,
            'modifiers': 44333,
            'owner_events': 1,
            'pointer_mode': 0,
            }
        self.req_bin_0 = b'\x1c\x01\x06\x00' b'\x03\xe6\x5d\x40' \
            b'\x71\xda\x00\x01' b'\x2b\x03\x42\x0a' \
            b'\x2e\xed\xc9\x17' b'\xcc\x00\x2d\xad'


    def testPackRequest0(self):
        bin = request.GrabButton._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GrabButton._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestUngrabButton(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'button': 158,
            'grab_window': 257512222,
            'modifiers': 58373,
            }
        self.req_bin_0 = b'\x1d\x9e\x03\x00' b'\x1e\x53\x59\x0f' \
            b'\x05\xe4\x00\x00'


    def testPackRequest0(self):
        bin = request.UngrabButton._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UngrabButton._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestChangeActivePointerGrab(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cursor': 528792833,
            'event_mask': 40689,
            'time': 1276746733,
            }
        self.req_bin_0 = b'\x1e\x00\x04\x00' b'\x01\xbd\x84\x1f' \
            b'\xed\x9b\x19\x4c' b'\xf1\x9e\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangeActivePointerGrab._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeActivePointerGrab._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGrabKeyboard(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'grab_window': 1253453980,
            'keyboard_mode': 0,
            'owner_events': 0,
            'pointer_mode': 1,
            'time': 1122698607,
            }
        self.req_bin_0 = b'\x1f\x00\x04\x00' b'\x9c\x30\xb6\x4a' \
            b'\x6f\x05\xeb\x42' b'\x01\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 15837,
            'status': 219,
            }
        self.reply_bin_0 = b'\x01\xdb\xdd\x3d' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GrabKeyboard._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GrabKeyboard._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GrabKeyboard._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GrabKeyboard._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestUngrabKeyboard(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'time': 849983231,
            }
        self.req_bin_0 = b'\x20\x00\x02\x00' b'\xff\xb6\xa9\x32'


    def testPackRequest0(self):
        bin = request.UngrabKeyboard._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UngrabKeyboard._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGrabKey(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'grab_window': 644284698,
            'key': 224,
            'keyboard_mode': 0,
            'modifiers': 20896,
            'owner_events': 1,
            'pointer_mode': 0,
            }
        self.req_bin_0 = b'\x21\x01\x04\x00' b'\x1a\x01\x67\x26' \
            b'\xa0\x51\xe0\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GrabKey._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GrabKey._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestUngrabKey(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'grab_window': 2139101088,
            'key': 255,
            'modifiers': 5038,
            }
        self.req_bin_0 = b'\x22\xff\x03\x00' b'\xa0\x17\x80\x7f' \
            b'\xae\x13\x00\x00'


    def testPackRequest0(self):
        bin = request.UngrabKey._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UngrabKey._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestAllowEvents(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'mode': 1,
            'time': 569561709,
            }
        self.req_bin_0 = b'\x23\x01\x02\x00' b'\x6d\xd2\xf2\x21'


    def testPackRequest0(self):
        bin = request.AllowEvents._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.AllowEvents._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGrabServer(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x24\x00\x01\x00'


    def testPackRequest0(self):
        bin = request.GrabServer._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GrabServer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestUngrabServer(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x25\x00\x01\x00'


    def testPackRequest0(self):
        bin = request.UngrabServer._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UngrabServer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestQueryPointer(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 2004163626,
            }
        self.req_bin_0 = b'\x26\x00\x02\x00' b'\x2a\x1c\x75\x77'

        self.reply_args_0 = {
            'child': 338813940,
            'mask': 42947,
            'root': 793594698,
            'root_x': -5661,
            'root_y': -9894,
            'same_screen': 1,
            'sequence_number': 57654,
            'win_x': -12881,
            'win_y': -671,
            }
        self.reply_bin_0 = b'\x01\x01\x36\xe1' b'\x00\x00\x00\x00' \
            b'\x4a\x4b\x4d\x2f' b'\xf4\xe3\x31\x14' \
            b'\xe3\xe9\x5a\xd9' b'\xaf\xcd\x61\xfd' \
            b'\xc3\xa7\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryPointer._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.QueryPointer._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryPointer._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestGetMotionEvents(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'start': 1754729754,
            'stop': 642956890,
            'window': 16865017,
            }
        self.req_bin_0 = b'\x27\x00\x04\x00' b'\xf9\x56\x01\x01' \
            b'\x1a\x0d\x97\x68' b'\x5a\xbe\x52\x26'

        self.reply_args_0 = {
            'events': [{'y': -28402, 'x': -2241, 'time': 1424638477}, {'y': -14782, 'x': -29288, 'time': 247939153}, {'y': -9437, 'x': -13104, 'time': 584911019}, {'y': -24186, 'x': -12148, 'time': 437274091}, {'y': -5259, 'x': -3333, 'time': 1049147683}],
            'sequence_number': 6281,
            }
        self.reply_bin_0 = b'\x01\x00\x89\x18' b'\x0a\x00\x00\x00' \
            b'\x05\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x0d\x42\xea\x54' b'\x3f\xf7\x0e\x91' \
            b'\x51\x40\xc7\x0e' b'\x98\x8d\x42\xc6' \
            b'\xab\x08\xdd\x22' b'\xd0\xcc\x23\xdb' \
            b'\xeb\x45\x10\x1a' b'\x8c\xd0\x86\xa1' \
            b'\x23\xb9\x88\x3e' b'\xfb\xf2\x75\xeb'


    def testPackRequest0(self):
        bin = request.GetMotionEvents._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetMotionEvents._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetMotionEvents._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetMotionEvents._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestTranslateCoords(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'dst_wid': 594213659,
            'src_wid': 909659821,
            'src_x': -32653,
            'src_y': -7697,
            }
        self.req_bin_0 = b'\x28\x00\x04\x00' b'\xad\x4e\x38\x36' \
            b'\x1b\xfb\x6a\x23' b'\x73\x80\xef\xe1'

        self.reply_args_0 = {
            'child': 1591798213,
            'same_screen': 1,
            'sequence_number': 17356,
            'x': -14832,
            'y': -18863,
            }
        self.reply_bin_0 = b'\x01\x01\xcc\x43' b'\x00\x00\x00\x00' \
            b'\xc5\xe9\xe0\x5e' b'\x10\xc6\x51\xb6' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.TranslateCoords._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.TranslateCoords._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.TranslateCoords._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.TranslateCoords._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestWarpPointer(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'dst_window': 161645563,
            'dst_x': -13829,
            'dst_y': -27954,
            'src_height': 54738,
            'src_width': 35872,
            'src_window': 20830424,
            'src_x': -4056,
            'src_y': -3379,
            }
        self.req_bin_0 = b'\x29\x00\x06\x00' b'\xd8\xd8\x3d\x01' \
            b'\xfb\x83\xa2\x09' b'\x28\xf0\xcd\xf2' \
            b'\x20\x8c\xd2\xd5' b'\xfb\xc9\xce\x92'


    def testPackRequest0(self):
        bin = request.WarpPointer._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.WarpPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestSetInputFocus(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'focus': 662025099,
            'revert_to': 0,
            'time': 1930554666,
            }
        self.req_bin_0 = b'\x2a\x00\x03\x00' b'\x8b\xb3\x75\x27' \
            b'\x2a\xed\x11\x73'


    def testPackRequest0(self):
        bin = request.SetInputFocus._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetInputFocus._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetInputFocus(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x2b\x00\x01\x00'

        self.reply_args_0 = {
            'focus': 1930432580,
            'revert_to': 229,
            'sequence_number': 56442,
            }
        self.reply_bin_0 = b'\x01\xe5\x7a\xdc' b'\x00\x00\x00\x00' \
            b'\x44\x10\x10\x73' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetInputFocus._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetInputFocus._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetInputFocus._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetInputFocus._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestQueryKeymap(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x2c\x00\x01\x00'

        self.reply_args_0 = {
            'map': [154, 159, 141, 227, 241, 180, 207, 147, 247, 238, 252, 231, 240, 131, 222, 170, 247, 230, 238, 231, 162, 228, 141, 239, 237, 156, 232, 186, 167, 229, 157, 131],
            'sequence_number': 12863,
            }
        self.reply_bin_0 = b'\x01\x00\x3f\x32' b'\x02\x00\x00\x00' \
            b'\x9a\x9f\x8d\xe3' b'\xf1\xb4\xcf\x93' \
            b'\xf7\xee\xfc\xe7' b'\xf0\x83\xde\xaa' \
            b'\xf7\xe6\xee\xe7' b'\xa2\xe4\x8d\xef' \
            b'\xed\x9c\xe8\xba' b'\xa7\xe5\x9d\x83'


    def testPackRequest0(self):
        bin = request.QueryKeymap._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryKeymap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.QueryKeymap._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryKeymap._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestOpenFont(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'fid': 704981195,
            'name': 'foofont',
            }
        self.req_bin_0 = b'\x2d\x00\x05\x00' b'\xcb\x28\x05\x2a' \
            b'\x07\x00\x00\x00' b'\x66\x6f\x6f\x66' \
            b'\x6f\x6e\x74\x00'


    def testPackRequest0(self):
        bin = request.OpenFont._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.OpenFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCloseFont(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'font': 1856192698,
            }
        self.req_bin_0 = b'\x2e\x00\x02\x00' b'\xba\x40\xa3\x6e'


    def testPackRequest0(self):
        bin = request.CloseFont._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CloseFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestQueryFont(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'font': 2076380709,
            }
        self.req_bin_0 = b'\x2f\x00\x02\x00' b'\x25\x0e\xc3\x7b'

        self.reply_args_0 = {
            'all_chars_exist': 0,
            'char_infos': [{'descent': -29018, 'right_side_bearing': -868, 'character_width': -15335, 'left_side_bearing': -19774, 'attributes': 63603, 'ascent': -2231}, {'descent': -18640, 'right_side_bearing': -1474, 'character_width': -24137, 'left_side_bearing': -26963, 'attributes': 47815, 'ascent': -29244}, {'descent': -14022, 'right_side_bearing': -13059, 'character_width': -16141, 'left_side_bearing': -22570, 'attributes': 16884, 'ascent': -20245}],
            'default_char': 20446,
            'draw_direction': 180,
            'font_ascent': -19099,
            'font_descent': -2194,
            'max_bounds': {'descent': -22562, 'right_side_bearing': -30493, 'character_width': -11172, 'left_side_bearing': -20927, 'attributes': 55614, 'ascent': -22033},
            'max_byte1': 165,
            'max_char_or_byte2': 19861,
            'min_bounds': {'descent': -8645, 'right_side_bearing': -2675, 'character_width': -15262, 'left_side_bearing': -32714, 'attributes': 44034, 'ascent': -9378},
            'min_byte1': 179,
            'min_char_or_byte2': 47241,
            'properties': [{'name': 599463600, 'value': 1377595039}],
            'sequence_number': 46525,
            }
        self.reply_bin_0 = b'\x01\x00\xbd\xb5' b'\x12\x00\x00\x00' \
            b'\x36\x80\x8d\xf5' b'\x62\xc4\x5e\xdb' \
            b'\x3b\xde\x02\xac' b'\x00\x00\x00\x00' \
            b'\x41\xae\xe3\x88' b'\x5c\xd4\xef\xa9' \
            b'\xde\xa7\x3e\xd9' b'\x00\x00\x00\x00' \
            b'\x89\xb8\x95\x4d' b'\xde\x4f\x01\x00' \
            b'\xb4\xb3\xa5\x00' b'\x65\xb5\x6e\xf7' \
            b'\x03\x00\x00\x00' b'\xb0\x16\xbb\x23' \
            b'\x9f\x6e\x1c\x52' b'\xc2\xb2\x9c\xfc' \
            b'\x19\xc4\x49\xf7' b'\xa6\x8e\x73\xf8' \
            b'\xad\x96\x3e\xfa' b'\xb7\xa1\xc4\x8d' \
            b'\x30\xb7\xc7\xba' b'\xd6\xa7\xfd\xcc' \
            b'\xf3\xc0\xeb\xb0' b'\x3a\xc9\xf4\x41'


    def testPackRequest0(self):
        bin = request.QueryFont._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.QueryFont._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryFont._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestQueryTextExtents(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'font': 1454550358,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = b'\x30\x01\x04\x00' b'\x56\xad\xb2\x56' \
            b'\x00\x66\x00\x6f' b'\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'draw_direction': 243,
            'font_ascent': -22984,
            'font_descent': -14953,
            'overall_ascent': -32755,
            'overall_descent': -23440,
            'overall_left': -902013824,
            'overall_right': -741556933,
            'overall_width': -1224334048,
            'sequence_number': 40436,
            }
        self.reply_bin_0 = b'\x01\xf3\xf4\x9d' b'\x00\x00\x00\x00' \
            b'\x38\xa6\x97\xc5' b'\x0d\x80\x70\xa4' \
            b'\x20\x25\x06\xb7' b'\x80\x5c\x3c\xca' \
            b'\x3b\xbd\xcc\xd3' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryTextExtents._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryTextExtents._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.QueryTextExtents._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryTextExtents._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestListFonts(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'max_names': 30610,
            'pattern': 'bhazr',
            }
        self.req_bin_0 = b'\x31\x00\x04\x00' b'\x92\x77\x05\x00' \
            b'\x62\x68\x61\x7a' b'\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 29120,
            }
        self.reply_bin_0 = b'\x01\x00\xc0\x71' b'\x05\x00\x00\x00' \
            b'\x03\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x03\x66\x69\x65' b'\x05\x66\x75\x7a' \
            b'\x7a\x79\x08\x66' b'\x6f\x6f\x7a\x6f' \
            b'\x6f\x6f\x6d\x00'


    def testPackRequest0(self):
        bin = request.ListFonts._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ListFonts._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.ListFonts._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.ListFonts._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestListFontsWithInfo(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'max_names': 14206,
            'pattern': 'bhazr2',
            }
        self.req_bin_0 = b'\x32\x00\x04\x00' b'\x7e\x37\x06\x00' \
            b'\x62\x68\x61\x7a' b'\x72\x32\x00\x00'

        self.reply_args_0 = {
            'all_chars_exist': 1,
            'default_char': 5010,
            'draw_direction': 181,
            'font_ascent': -16695,
            'font_descent': -24836,
            'max_bounds': {'descent': -31974, 'right_side_bearing': -10894, 'character_width': -25465, 'left_side_bearing': -8347, 'attributes': 16239, 'ascent': -26294},
            'max_byte1': 152,
            'max_char_or_byte2': 55726,
            'min_bounds': {'descent': -21871, 'right_side_bearing': -30012, 'character_width': -16010, 'left_side_bearing': -27251, 'attributes': 53682, 'ascent': -12190},
            'min_byte1': 208,
            'min_char_or_byte2': 31272,
            'name': 'fontfont',
            'properties': [{'name': 1016194121, 'value': 1935277562}],
            'replies_hint': 1408896390,
            'sequence_number': 52220,
            }
        self.reply_bin_0 = b'\x01\x08\xfc\xcb' b'\x0b\x00\x00\x00' \
            b'\x8d\x95\xc4\x8a' b'\x76\xc1\x62\xd0' \
            b'\x91\xaa\xb2\xd1' b'\x00\x00\x00\x00' \
            b'\x65\xdf\x72\xd5' b'\x87\x9c\x4a\x99' \
            b'\x1a\x83\x6f\x3f' b'\x00\x00\x00\x00' \
            b'\x28\x7a\xae\xd9' b'\x92\x13\x01\x00' \
            b'\xb5\xd0\x98\x01' b'\xc9\xbe\xfc\x9e' \
            b'\x86\x0d\xfa\x53' b'\x49\xe4\x91\x3c' \
            b'\xfa\xfd\x59\x73' b'\x66\x6f\x6e\x74' \
            b'\x66\x6f\x6e\x74'


    def testPackRequest0(self):
        bin = request.ListFontsWithInfo._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ListFontsWithInfo._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.ListFontsWithInfo._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.ListFontsWithInfo._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestSetFontPath(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'path': ['foo', 'bar', 'gazonk'],
            }
        self.req_bin_0 = b'\x33\x00\x06\x00' b'\x03\x00\x00\x00' \
            b'\x03\x66\x6f\x6f' b'\x03\x62\x61\x72' \
            b'\x06\x67\x61\x7a' b'\x6f\x6e\x6b\x00'

        self.req_args_1 = {
            'path': [],
            }
        self.req_bin_1 = b'\x33\x00\x02\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetFontPath._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetFontPath._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackRequest1(self):
        bin = request.SetFontPath._request.to_binary(*(), **self.req_args_1)
        self.assertBinaryEqual(bin, self.req_bin_1)

    def testUnpackRequest1(self):
        args, remain = request.SetFontPath._request.parse_binary(self.req_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_1)


class TestGetFontPath(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x34\x00\x01\x00'

        self.reply_args_0 = {
            'paths': ['path1', 'path2232'],
            'sequence_number': 617,
            }
        self.reply_bin_0 = b'\x01\x00\x69\x02' b'\x04\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x05\x70\x61\x74' b'\x68\x31\x08\x70' \
            b'\x61\x74\x68\x32' b'\x32\x33\x32\x00'

        self.reply_args_1 = {
            'paths': [],
            'sequence_number': 49278,
            }
        self.reply_bin_1 = b'\x01\x00\x7e\xc0' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetFontPath._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetFontPath._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetFontPath._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetFontPath._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)

    def testPackReply1(self):
        bin = request.GetFontPath._reply.to_binary(*(), **self.reply_args_1)
        self.assertBinaryEqual(bin, self.reply_bin_1)

    def testUnpackReply1(self):
        args, remain = request.GetFontPath._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_1)


class TestCreatePixmap(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'depth': 226,
            'drawable': 913032172,
            'height': 62792,
            'pid': 228953027,
            'width': 11737,
            }
        self.req_bin_0 = b'\x35\xe2\x04\x00' b'\xc3\x8b\xa5\x0d' \
            b'\xec\xc3\x6b\x36' b'\xd9\x2d\x48\xf5'


    def testPackRequest0(self):
        bin = request.CreatePixmap._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CreatePixmap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestFreePixmap(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'pixmap': 1112337390,
            }
        self.req_bin_0 = b'\x36\x00\x02\x00' b'\xee\xeb\x4c\x42'


    def testPackRequest0(self):
        bin = request.FreePixmap._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.FreePixmap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCreateGC(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'stipple': 1544647467, 'background': 980279926, 'subwindow_mode': 1, 'fill_style': 3, 'font': 1176575685, 'graphics_exposures': 1, 'tile': 1315686229, 'tile_stipple_x_origin': -16228, 'dashes': 226, 'function': 0, 'foreground': 1821798372, 'clip_x_origin': -17214, 'cap_style': 3, 'tile_stipple_y_origin': -5552, 'join_style': 1, 'line_width': 59029, 'dash_offset': 53663, 'clip_y_origin': -24275, 'arc_mode': 1, 'line_style': 2, 'plane_mask': 535198434, 'clip_mask': 530992626, 'fill_rule': 1},
            'cid': 1345956480,
            'drawable': 589741066,
            }
        self.req_bin_0 = b'\x37\x00\x1b\x00' b'\x80\xaa\x39\x50' \
            b'\x0a\xbc\x26\x23' b'\xff\xff\x7f\x00' \
            b'\x00\x00\x00\x00' b'\xe2\x7a\xe6\x1f' \
            b'\xe4\x6f\x96\x6c' b'\x76\xe2\x6d\x3a' \
            b'\x95\xe6\x00\x00' b'\x02\x00\x00\x00' \
            b'\x03\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x03\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x55\xc7\x6b\x4e' b'\x2b\x73\x11\x5c' \
            b'\x9c\xc0\x00\x00' b'\x50\xea\x00\x00' \
            b'\xc5\x1e\x21\x46' b'\x01\x00\x00\x00' \
            b'\x01\x00\x00\x00' b'\xc2\xbc\x00\x00' \
            b'\x2d\xa1\x00\x00' b'\xf2\x4d\xa6\x1f' \
            b'\x9f\xd1\x00\x00' b'\xe2\x00\x00\x00' \
            b'\x01\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.CreateGC._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CreateGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestChangeGC(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'stipple': 1165278526, 'background': 686615653, 'subwindow_mode': 1, 'fill_style': 2, 'font': 902289335, 'graphics_exposures': 1, 'tile': 875351804, 'tile_stipple_x_origin': -19144, 'dashes': 128, 'function': 1, 'foreground': 583551477, 'clip_x_origin': -9978, 'cap_style': 0, 'tile_stipple_y_origin': -25991, 'join_style': 2, 'line_width': 50468, 'dash_offset': 45232, 'clip_y_origin': -4695, 'arc_mode': 0, 'line_style': 0, 'plane_mask': 613643341, 'clip_mask': 1644117194, 'fill_rule': 0},
            'gc': 1618091665,
            }
        self.req_bin_0 = b'\x38\x00\x1a\x00' b'\x91\x1e\x72\x60' \
            b'\xff\xff\x7f\x00' b'\x01\x00\x00\x00' \
            b'\x4d\x74\x93\x24' b'\xf5\x49\xc8\x22' \
            b'\x65\xec\xec\x28' b'\x24\xc5\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\xfc\xce\x2c\x34' \
            b'\x3e\xbd\x74\x45' b'\x38\xb5\x00\x00' \
            b'\x79\x9a\x00\x00' b'\xb7\xd7\xc7\x35' \
            b'\x01\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x06\xd9\x00\x00' b'\xa9\xed\x00\x00' \
            b'\xca\x3c\xff\x61' b'\xb0\xb0\x00\x00' \
            b'\x80\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangeGC._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCopyGC(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'dst_gc': 2047479112,
            'mask': 899879427,
            'src_gc': 1832775121,
            }
        self.req_bin_0 = b'\x39\x00\x04\x00' b'\xd1\xed\x3d\x6d' \
            b'\x48\x0d\x0a\x7a' b'\x03\x12\xa3\x35'


    def testPackRequest0(self):
        bin = request.CopyGC._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CopyGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestSetDashes(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'dash_offset': 11030,
            'dashes': [223, 197, 205, 156, 156, 183, 131, 171, 214],
            'gc': 868302473,
            }
        self.req_bin_0 = b'\x3a\x00\x06\x00' b'\x89\x3e\xc1\x33' \
            b'\x16\x2b\x09\x00' b'\xdf\xc5\xcd\x9c' \
            b'\x9c\xb7\x83\xab' b'\xd6\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetDashes._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetDashes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestSetClipRectangles(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'gc': 991525136,
            'ordering': 0,
            'rectangles': [{'y': -28619, 'x': -17572, 'height': 2016, 'width': 40876}, {'y': -14418, 'x': -19958, 'height': 42214, 'width': 2025}],
            'x_origin': -31134,
            'y_origin': -20443,
            }
        self.req_bin_0 = b'\x3b\x00\x07\x00' b'\x10\x79\x19\x3b' \
            b'\x62\x86\x25\xb0' b'\x5c\xbb\x35\x90' \
            b'\xac\x9f\xe0\x07' b'\x0a\xb2\xae\xc7' \
            b'\xe9\x07\xe6\xa4'

        self.req_args_1 = {
            'gc': 701940136,
            'ordering': 0,
            'rectangles': [],
            'x_origin': -8019,
            'y_origin': -20442,
            }
        self.req_bin_1 = b'\x3b\x00\x03\x00' b'\xa8\xc1\xd6\x29' \
            b'\xad\xe0\x26\xb0'


    def testPackRequest0(self):
        bin = request.SetClipRectangles._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetClipRectangles._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackRequest1(self):
        bin = request.SetClipRectangles._request.to_binary(*(), **self.req_args_1)
        self.assertBinaryEqual(bin, self.req_bin_1)

    def testUnpackRequest1(self):
        args, remain = request.SetClipRectangles._request.parse_binary(self.req_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_1)


class TestFreeGC(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'gc': 1614945050,
            }
        self.req_bin_0 = b'\x3c\x00\x02\x00' b'\x1a\x1b\x42\x60'


    def testPackRequest0(self):
        bin = request.FreeGC._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.FreeGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestClearArea(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'exposures': 1,
            'height': 65529,
            'width': 35469,
            'window': 541797992,
            'x': -30105,
            'y': -32138,
            }
        self.req_bin_0 = b'\x3d\x01\x04\x00' b'\x68\x2e\x4b\x20' \
            b'\x67\x8a\x76\x82' b'\x8d\x8a\xf9\xff'


    def testPackRequest0(self):
        bin = request.ClearArea._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ClearArea._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCopyArea(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'dst_drawable': 1396196736,
            'dst_x': -1894,
            'dst_y': -26287,
            'gc': 1677699535,
            'height': 10203,
            'src_drawable': 751576716,
            'src_x': -11578,
            'src_y': -8246,
            'width': 1586,
            }
        self.req_bin_0 = b'\x3e\x00\x07\x00' b'\x8c\x26\xcc\x2c' \
            b'\x80\x45\x38\x53' b'\xcf\xa9\xff\x63' \
            b'\xc6\xd2\xca\xdf' b'\x9a\xf8\x51\x99' \
            b'\x32\x06\xdb\x27'


    def testPackRequest0(self):
        bin = request.CopyArea._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CopyArea._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCopyPlane(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'bit_plane': 246015498,
            'dst_drawable': 1437673583,
            'dst_x': -7834,
            'dst_y': -27313,
            'gc': 1211144030,
            'height': 49080,
            'src_drawable': 271114743,
            'src_x': -25682,
            'src_y': -10027,
            'width': 39897,
            }
        self.req_bin_0 = b'\x3f\x00\x08\x00' b'\xf7\xe1\x28\x10' \
            b'\x6f\x28\xb1\x55' b'\x5e\x97\x30\x48' \
            b'\xae\x9b\xd5\xd8' b'\x66\xe1\x4f\x95' \
            b'\xd9\x9b\xb8\xbf' b'\x0a\xe6\xa9\x0e'


    def testPackRequest0(self):
        bin = request.CopyPlane._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CopyPlane._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolyPoint(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'coord_mode': 1,
            'drawable': 851848467,
            'gc': 1535501063,
            'points': [{'y': -1403, 'x': -6131}, {'y': -31934, 'x': -29254}, {'y': -10746, 'x': -22626}],
            }
        self.req_bin_0 = b'\x40\x01\x06\x00' b'\x13\x2d\xc6\x32' \
            b'\x07\xe3\x85\x5b' b'\x0d\xe8\x85\xfa' \
            b'\xba\x8d\x42\x83' b'\x9e\xa7\x06\xd6'


    def testPackRequest0(self):
        bin = request.PolyPoint._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyPoint._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolyLine(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'coord_mode': 0,
            'drawable': 919972239,
            'gc': 795836146,
            'points': [{'y': -10315, 'x': -30298}, {'y': -29455, 'x': -12375}, {'y': -5123, 'x': -7653}, {'y': -28833, 'x': -13247}, {'y': -7323, 'x': -781}],
            }
        self.req_bin_0 = b'\x41\x00\x08\x00' b'\x8f\xa9\xd5\x36' \
            b'\xf2\x7e\x6f\x2f' b'\xa6\x89\xb5\xd7' \
            b'\xa9\xcf\xf1\x8c' b'\x1b\xe2\xfd\xeb' \
            b'\x41\xcc\x5f\x8f' b'\xf3\xfc\x65\xe3'


    def testPackRequest0(self):
        bin = request.PolyLine._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyLine._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolySegment(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 226701618,
            'gc': 2063278158,
            'segments': [{'y1': -21674, 'x2': -5146, 'x1': -16318, 'y2': -6032}],
            }
        self.req_bin_0 = b'\x42\x00\x05\x00' b'\x32\x31\x83\x0d' \
            b'\x4e\x20\xfb\x7a' b'\x42\xc0\x56\xab' \
            b'\xe6\xeb\x70\xe8'


    def testPackRequest0(self):
        bin = request.PolySegment._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolySegment._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolyRectangle(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 576422975,
            'gc': 1829049801,
            'rectangles': [{'y': -5825, 'x': -12104, 'height': 28684, 'width': 46429}, {'y': -1378, 'x': -8911, 'height': 53015, 'width': 17886}, {'y': -17049, 'x': -15271, 'height': 47977, 'width': 28690}],
            }
        self.req_bin_0 = b'\x43\x00\x09\x00' b'\x3f\x84\x5b\x22' \
            b'\xc9\x15\x05\x6d' b'\xb8\xd0\x3f\xe9' \
            b'\x5d\xb5\x0c\x70' b'\x31\xdd\x9e\xfa' \
            b'\xde\x45\x17\xcf' b'\x59\xc4\x67\xbd' \
            b'\x12\x70\x69\xbb'


    def testPackRequest0(self):
        bin = request.PolyRectangle._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyRectangle._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolyArc(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'arcs': [{'height': 16175, 'width': 57808, 'angle1': -17659, 'angle2': -12925, 'y': -29951, 'x': -5759}, {'height': 12126, 'width': 55806, 'angle1': -25872, 'angle2': -6829, 'y': -31835, 'x': -20446}, {'height': 18290, 'width': 46029, 'angle1': -32438, 'angle2': -1944, 'y': -4147, 'x': -21703}],
            'drawable': 183912361,
            'gc': 1546366910,
            }
        self.req_bin_0 = b'\x44\x00\x0c\x00' b'\xa9\x47\xf6\x0a' \
            b'\xbe\xaf\x2b\x5c' b'\x81\xe9\x01\x8b' \
            b'\xd0\xe1\x2f\x3f' b'\x05\xbb\x83\xcd' \
            b'\x22\xb0\xa5\x83' b'\xfe\xd9\x5e\x2f' \
            b'\xf0\x9a\x53\xe5' b'\x39\xab\xcd\xef' \
            b'\xcd\xb3\x72\x47' b'\x4a\x81\x68\xf8'


    def testPackRequest0(self):
        bin = request.PolyArc._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyArc._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestFillPoly(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'coord_mode': 0,
            'drawable': 199889986,
            'gc': 475925659,
            'points': [{'y': -8118, 'x': -16883}, {'y': -11768, 'x': -10315}, {'y': -6988, 'x': -16810}],
            'shape': 2,
            }
        self.req_bin_0 = b'\x45\x00\x07\x00' b'\x42\x14\xea\x0b' \
            b'\x9b\x0c\x5e\x1c' b'\x02\x00\x00\x00' \
            b'\x0d\xbe\x4a\xe0' b'\xb5\xd7\x08\xd2' \
            b'\x56\xbe\xb4\xe4'


    def testPackRequest0(self):
        bin = request.FillPoly._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.FillPoly._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolyFillRectangle(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 539934343,
            'gc': 259164168,
            'rectangles': [{'y': -17381, 'x': -13860, 'height': 28032, 'width': 34914}, {'y': -22013, 'x': -8516, 'height': 17941, 'width': 46138}],
            }
        self.req_bin_0 = b'\x46\x00\x07\x00' b'\x87\xbe\x2e\x20' \
            b'\x08\x88\x72\x0f' b'\xdc\xc9\x1b\xbc' \
            b'\x62\x88\x80\x6d' b'\xbc\xde\x03\xaa' \
            b'\x3a\xb4\x15\x46'


    def testPackRequest0(self):
        bin = request.PolyFillRectangle._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyFillRectangle._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolyFillArc(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'arcs': [{'height': 50011, 'width': 35237, 'angle1': -26749, 'angle2': -25733, 'y': -28881, 'x': -26507}],
            'drawable': 1039842351,
            'gc': 1556052490,
            }
        self.req_bin_0 = b'\x47\x00\x06\x00' b'\x2f\xbc\xfa\x3d' \
            b'\x0a\x7a\xbf\x5c' b'\x75\x98\x2f\x8f' \
            b'\xa5\x89\x5b\xc3' b'\x83\x97\x7b\x9b'


    def testPackRequest0(self):
        bin = request.PolyFillArc._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyFillArc._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPutImage(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'data': 'bit map data',
            'depth': 196,
            'drawable': 1126680250,
            'dst_x': -25372,
            'dst_y': -26934,
            'format': 2,
            'gc': 607782076,
            'height': 12927,
            'left_pad': 129,
            'width': 6818,
            }
        self.req_bin_0 = b'\x48\x02\x09\x00' b'\xba\xc6\x27\x43' \
            b'\xbc\x04\x3a\x24' b'\xa2\x1a\x7f\x32' \
            b'\xe4\x9c\xca\x96' b'\x81\xc4\x00\x00' \
            b'\x62\x69\x74\x20' b'\x6d\x61\x70\x20' \
            b'\x64\x61\x74\x61'


    def testPackRequest0(self):
        bin = request.PutImage._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PutImage._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetImage(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 2092284116,
            'format': 1,
            'height': 56949,
            'plane_mask': 1054187334,
            'width': 8499,
            'x': -14777,
            'y': -10093,
            }
        self.req_bin_0 = b'\x49\x01\x05\x00' b'\xd4\xb8\xb5\x7c' \
            b'\x47\xc6\x93\xd8' b'\x33\x21\x75\xde' \
            b'\x46\x9f\xd5\x3e'

        self.reply_args_0 = {
            'data': 'this is real ly imag e b-map',
            'depth': 239,
            'sequence_number': 37730,
            'visual': 1008057036,
            }
        self.reply_bin_0 = b'\x01\xef\x62\x93' b'\x07\x00\x00\x00' \
            b'\xcc\xba\x15\x3c' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x74\x68\x69\x73' b'\x20\x69\x73\x20' \
            b'\x72\x65\x61\x6c' b'\x20\x6c\x79\x20' \
            b'\x69\x6d\x61\x67' b'\x20\x65\x20\x62' \
            b'\x2d\x6d\x61\x70'


    def testPackRequest0(self):
        bin = request.GetImage._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetImage._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetImage._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetImage._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestPolyText8(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 945936210,
            'gc': 395971420,
            'items': [{'string': 'zoo', 'delta': 2}, 16909060, {'string': 'ie', 'delta': 0}],
            'x': -31098,
            'y': -2172,
            }
        self.req_bin_0 = b'\x4a\x00\x08\x00' b'\x52\xd7\x61\x38' \
            b'\x5c\x0b\x9a\x17' b'\x86\x86\x84\xf7' \
            b'\x03\x02\x7a\x6f' b'\x6f\xff\x01\x02' \
            b'\x03\x04\x02\x00' b'\x69\x65\x00\x00'


    def testPackRequest0(self):
        bin = request.PolyText8._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyText8._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestPolyText16(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 1025949844,
            'gc': 1765491562,
            'items': [{'string': (4131, 18), 'delta': 2}, 16909060],
            'x': -19740,
            'y': -30360,
            }
        self.req_bin_0 = b'\x4b\x00\x07\x00' b'\x94\xc0\x26\x3d' \
            b'\x6a\x43\x3b\x69' b'\xe4\xb2\x68\x89' \
            b'\x02\x02\x10\x23' b'\x00\x12\xff\x01' \
            b'\x02\x03\x04\x00'


    def testPackRequest0(self):
        bin = request.PolyText16._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.PolyText16._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestImageText8(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 1351748646,
            'gc': 115186633,
            'string': 'showme',
            'x': -27918,
            'y': -14469,
            }
        self.req_bin_0 = b'\x4c\x06\x06\x00' b'\x26\x0c\x92\x50' \
            b'\xc9\x9b\xdd\x06' b'\xf2\x92\x7b\xc7' \
            b'\x73\x68\x6f\x77' b'\x6d\x65\x00\x00'


    def testPackRequest0(self):
        bin = request.ImageText8._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ImageText8._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestImageText16(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 652527416,
            'gc': 2134423313,
            'string': (115, 104, 111, 119, 109, 111, 114, 101),
            'x': -28917,
            'y': -7914,
            }
        self.req_bin_0 = b'\x4d\x08\x08\x00' b'\x38\xc7\xe4\x26' \
            b'\x11\xb7\x38\x7f' b'\x0b\x8f\x16\xe1' \
            b'\x00\x73\x00\x68' b'\x00\x6f\x00\x77' \
            b'\x00\x6d\x00\x6f' b'\x00\x72\x00\x65'


    def testPackRequest0(self):
        bin = request.ImageText16._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ImageText16._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCreateColormap(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'alloc': 1,
            'mid': 1698116715,
            'visual': 1122247262,
            'window': 484710181,
            }
        self.req_bin_0 = b'\x4e\x01\x04\x00' b'\x6b\x34\x37\x65' \
            b'\x25\x17\xe4\x1c' b'\x5e\x22\xe4\x42'


    def testPackRequest0(self):
        bin = request.CreateColormap._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CreateColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestFreeColormap(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 967508457,
            }
        self.req_bin_0 = b'\x4f\x00\x02\x00' b'\xe9\x01\xab\x39'


    def testPackRequest0(self):
        bin = request.FreeColormap._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.FreeColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCopyColormapAndFree(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'mid': 950772638,
            'src_cmap': 1847203012,
            }
        self.req_bin_0 = b'\x50\x00\x03\x00' b'\x9e\xa3\xab\x38' \
            b'\xc4\x14\x1a\x6e'


    def testPackRequest0(self):
        bin = request.CopyColormapAndFree._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CopyColormapAndFree._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestInstallColormap(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 2126076595,
            }
        self.req_bin_0 = b'\x51\x00\x02\x00' b'\xb3\x5a\xb9\x7e'


    def testPackRequest0(self):
        bin = request.InstallColormap._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.InstallColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestUninstallColormap(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 655844603,
            }
        self.req_bin_0 = b'\x52\x00\x02\x00' b'\xfb\x64\x17\x27'


    def testPackRequest0(self):
        bin = request.UninstallColormap._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.UninstallColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestListInstalledColormaps(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'window': 1333670852,
            }
        self.req_bin_0 = b'\x53\x00\x02\x00' b'\xc4\x33\x7e\x4f'

        self.reply_args_0 = {
            'cmaps': [1309197997, 1589346714],
            'sequence_number': 62114,
            }
        self.reply_bin_0 = b'\x01\x00\xa2\xf2' b'\x02\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xad\xc6\x08\x4e' b'\x9a\x81\xbb\x5e'


    def testPackRequest0(self):
        bin = request.ListInstalledColormaps._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ListInstalledColormaps._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.ListInstalledColormaps._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.ListInstalledColormaps._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestAllocColor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'blue': 10508,
            'cmap': 446273048,
            'green': 43368,
            'red': 14031,
            }
        self.req_bin_0 = b'\x54\x00\x04\x00' b'\x18\x96\x99\x1a' \
            b'\xcf\x36\x68\xa9' b'\x0c\x29\x00\x00'

        self.reply_args_0 = {
            'blue': 29664,
            'green': 430,
            'pixel': 1275226450,
            'red': 5156,
            'sequence_number': 11602,
            }
        self.reply_bin_0 = b'\x01\x00\x52\x2d' b'\x00\x00\x00\x00' \
            b'\x24\x14\xae\x01' b'\xe0\x73\x00\x00' \
            b'\x52\x69\x02\x4c' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.AllocColor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.AllocColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.AllocColor._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.AllocColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestAllocNamedColor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 625521008,
            'name': 'octarin',
            }
        self.req_bin_0 = b'\x55\x00\x05\x00' b'\x70\xb1\x48\x25' \
            b'\x07\x00\x00\x00' b'\x6f\x63\x74\x61' \
            b'\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'exact_blue': 45128,
            'exact_green': 29895,
            'exact_red': 46147,
            'pixel': 1518195288,
            'screen_blue': 41059,
            'screen_green': 51685,
            'screen_red': 60568,
            'sequence_number': 15366,
            }
        self.reply_bin_0 = b'\x01\x00\x06\x3c' b'\x00\x00\x00\x00' \
            b'\x58\xd2\x7d\x5a' b'\x43\xb4\xc7\x74' \
            b'\x48\xb0\x98\xec' b'\xe5\xc9\x63\xa0' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.AllocNamedColor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.AllocNamedColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.AllocNamedColor._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.AllocNamedColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestAllocColorCells(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 2005042093,
            'colors': 28009,
            'contiguous': 1,
            'planes': 35805,
            }
        self.req_bin_0 = b'\x56\x01\x03\x00' b'\xad\x83\x82\x77' \
            b'\x69\x6d\xdd\x8b'

        self.reply_args_0 = {
            'masks': [927811713, 692224741, 537710104],
            'pixels': [1390808070, 1950804725, 1775188259, 153412312, 356371138, 660636713, 1608390912, 1222391062, 619833140, 267104833, 1478945126, 1502686323, 2024385568, 1074788553, 1060450333, 172807825, 85663305],
            'sequence_number': 6217,
            }
        self.reply_bin_0 = b'\x01\x00\x49\x18' b'\x14\x00\x00\x00' \
            b'\x11\x00\x03\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x06\x0c\xe6\x52' b'\xf5\xea\x46\x74' \
            b'\x23\x39\xcf\x69' b'\xd8\xe2\x24\x09' \
            b'\xc2\xca\x3d\x15' b'\x29\x84\x60\x27' \
            b'\x00\x19\xde\x5f' b'\x16\x35\xdc\x48' \
            b'\x34\xe7\xf1\x24' b'\x41\xb2\xeb\x0f' \
            b'\x66\xe9\x26\x58' b'\x73\x2c\x91\x59' \
            b'\x20\xac\xa9\x78' b'\xc9\xf8\x0f\x40' \
            b'\x1d\x30\x35\x3f' b'\x91\xd6\x4c\x0a' \
            b'\x49\x1e\x1b\x05' b'\x81\x48\x4d\x37' \
            b'\xe5\x82\x42\x29' b'\x18\xce\x0c\x20'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 63049,
            }
        self.reply_bin_1 = b'\x01\x00\x49\xf6' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.AllocColorCells._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.AllocColorCells._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.AllocColorCells._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.AllocColorCells._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)

    def testPackReply1(self):
        bin = request.AllocColorCells._reply.to_binary(*(), **self.reply_args_1)
        self.assertBinaryEqual(bin, self.reply_bin_1)

    def testUnpackReply1(self):
        args, remain = request.AllocColorCells._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_1)


class TestAllocColorPlanes(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'blue': 17849,
            'cmap': 1235258520,
            'colors': 62323,
            'contiguous': 1,
            'green': 44142,
            'red': 65508,
            }
        self.req_bin_0 = b'\x57\x01\x04\x00' b'\x98\x8c\xa0\x49' \
            b'\x73\xf3\xe4\xff' b'\x6e\xac\xb9\x45'

        self.reply_args_0 = {
            'blue_mask': 1363213739,
            'green_mask': 1257012974,
            'pixels': [86459759, 1624090919, 1010427525, 1399128813],
            'red_mask': 389798617,
            'sequence_number': 60057,
            }
        self.reply_bin_0 = b'\x01\x00\x99\xea' b'\x04\x00\x00\x00' \
            b'\x04\x00\x00\x00' b'\xd9\xda\x3b\x17' \
            b'\xee\x7e\xec\x4a' b'\xab\xfd\x40\x51' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x6f\x45\x27\x05' b'\x27\xa9\xcd\x60' \
            b'\x85\xe6\x39\x3c' b'\xed\x02\x65\x53'


    def testPackRequest0(self):
        bin = request.AllocColorPlanes._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.AllocColorPlanes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.AllocColorPlanes._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.AllocColorPlanes._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestFreeColors(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1105118848,
            'pixels': [1056006429, 196001131, 747283410, 715818017, 1439122371, 1841977117, 708291896, 1489672946, 618989649, 2029791261, 1747131973, 1181352956, 976766929, 675465375, 694269519, 2083457789, 867998373],
            'plane_mask': 2121970633,
            }
        self.req_bin_0 = b'\x58\x00\x14\x00' b'\x80\xc6\xde\x41' \
            b'\xc9\xb3\x7a\x7e' b'\x1d\x61\xf1\x3e' \
            b'\x6b\xbd\xae\x0b' b'\xd2\xa3\x8a\x2c' \
            b'\x21\x84\xaa\x2a' b'\xc3\x43\xc7\x55' \
            b'\x1d\x57\xca\x6d' b'\x38\xad\x37\x2a' \
            b'\xf2\x9a\xca\x58' b'\x51\x08\xe5\x24' \
            b'\x1d\x28\xfc\x78' b'\x45\x1e\x23\x68' \
            b'\xfc\x03\x6a\x46' b'\xd1\x47\x38\x3a' \
            b'\x9f\xc8\x42\x28' b'\x4f\xb6\x61\x29' \
            b'\xfd\x0a\x2f\x7c' b'\xa5\x9a\xbc\x33'


    def testPackRequest0(self):
        bin = request.FreeColors._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.FreeColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestStoreColors(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 200224662,
            'items': [{'blue': 12501, 'flags': 174, 'green': 27232, 'pixel': 1412337360, 'red': 35676}, {'blue': 13544, 'flags': 198, 'green': 49868, 'pixel': 1624465264, 'red': 41082}, {'blue': 8182, 'flags': 252, 'green': 45837, 'pixel': 1992166823, 'red': 28856}, {'blue': 36214, 'flags': 198, 'green': 10594, 'pixel': 1307567581, 'red': 15877}],
            }
        self.req_bin_0 = b'\x59\x00\x0e\x00' b'\x96\x2f\xef\x0b' \
            b'\xd0\x8e\x2e\x54' b'\x5c\x8b\x60\x6a' \
            b'\xd5\x30\xae\x00' b'\x70\x5f\xd3\x60' \
            b'\x7a\xa0\xcc\xc2' b'\xe8\x34\xc6\x00' \
            b'\xa7\x0d\xbe\x76' b'\xb8\x70\x0d\xb3' \
            b'\xf6\x1f\xfc\x00' b'\xdd\xe5\xef\x4d' \
            b'\x05\x3e\x62\x29' b'\x76\x8d\xc6\x00'


    def testPackRequest0(self):
        bin = request.StoreColors._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.StoreColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestStoreNamedColor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1960507691,
            'flags': 255,
            'name': 'blue',
            'pixel': 990987101,
            }
        self.req_bin_0 = b'\x5a\xff\x05\x00' b'\x2b\xf9\xda\x74' \
            b'\x5d\x43\x11\x3b' b'\x04\x00\x00\x00' \
            b'\x62\x6c\x75\x65'


    def testPackRequest0(self):
        bin = request.StoreNamedColor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.StoreNamedColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestQueryColors(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 523457697,
            'pixels': [252314471, 1787024858, 1070286120, 1538912496, 1092826517, 587223111, 1792566854, 2105060613],
            }
        self.req_bin_0 = b'\x5b\x00\x0a\x00' b'\xa1\x54\x33\x1f' \
            b'\x67\x03\x0a\x0f' b'\xda\xd5\x83\x6a' \
            b'\x28\x45\xcb\x3f' b'\xf0\xf0\xb9\x5b' \
            b'\x95\x35\x23\x41' b'\x47\x50\x00\x23' \
            b'\x46\x66\xd8\x6a' b'\x05\xad\x78\x7d'

        self.reply_args_0 = {
            'colors': [{'blue': 33433, 'green': 60435, 'red': 25296}, {'blue': 18289, 'green': 56659, 'red': 57658}, {'blue': 61243, 'green': 27343, 'red': 51827}, {'blue': 18719, 'green': 53821, 'red': 33401}, {'blue': 65464, 'green': 38571, 'red': 19745}],
            'sequence_number': 32219,
            }
        self.reply_bin_0 = b'\x01\x00\xdb\x7d' b'\x0a\x00\x00\x00' \
            b'\x05\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xd0\x62\x13\xec' b'\x99\x82\x00\x00' \
            b'\x3a\xe1\x53\xdd' b'\x71\x47\x00\x00' \
            b'\x73\xca\xcf\x6a' b'\x3b\xef\x00\x00' \
            b'\x79\x82\x3d\xd2' b'\x1f\x49\x00\x00' \
            b'\x21\x4d\xab\x96' b'\xb8\xff\x00\x00'

        self.req_args_1 = {
            'cmap': 1183862146,
            'pixels': [],
            }
        self.req_bin_1 = b'\x5b\x00\x02\x00' b'\x82\x4d\x90\x46'


    def testPackRequest0(self):
        bin = request.QueryColors._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackRequest1(self):
        bin = request.QueryColors._request.to_binary(*(), **self.req_args_1)
        self.assertBinaryEqual(bin, self.req_bin_1)

    def testUnpackRequest1(self):
        args, remain = request.QueryColors._request.parse_binary(self.req_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_1)

    def testPackReply0(self):
        bin = request.QueryColors._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryColors._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestLookupColor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 319162028,
            'name': 'octarin',
            }
        self.req_bin_0 = b'\x5c\x00\x05\x00' b'\xac\x06\x06\x13' \
            b'\x07\x00\x00\x00' b'\x6f\x63\x74\x61' \
            b'\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'exact_blue': 35731,
            'exact_green': 36285,
            'exact_red': 22785,
            'screen_blue': 12571,
            'screen_green': 21261,
            'screen_red': 29980,
            'sequence_number': 35414,
            }
        self.reply_bin_0 = b'\x01\x00\x56\x8a' b'\x00\x00\x00\x00' \
            b'\x01\x59\xbd\x8d' b'\x93\x8b\x1c\x75' \
            b'\x0d\x53\x1b\x31' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.LookupColor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.LookupColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.LookupColor._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.LookupColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestCreateCursor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'back_blue': 25459,
            'back_green': 53224,
            'back_red': 46293,
            'cid': 1497886291,
            'fore_blue': 48870,
            'fore_green': 3105,
            'fore_red': 50883,
            'mask': 501621762,
            'source': 1227954148,
            'x': 43581,
            'y': 53834,
            }
        self.req_bin_0 = b'\x5d\x00\x08\x00' b'\x53\xee\x47\x59' \
            b'\xe4\x17\x31\x49' b'\x02\x24\xe6\x1d' \
            b'\xc3\xc6\x21\x0c' b'\xe6\xbe\xd5\xb4' \
            b'\xe8\xcf\x73\x63' b'\x3d\xaa\x4a\xd2'


    def testPackRequest0(self):
        bin = request.CreateCursor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CreateCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestCreateGlyphCursor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'back_blue': 47417,
            'back_green': 30084,
            'back_red': 34590,
            'cid': 2106292170,
            'fore_blue': 28999,
            'fore_green': 57323,
            'fore_red': 57030,
            'mask': 79562119,
            'mask_char': 38782,
            'source': 1063743249,
            'source_char': 33045,
            }
        self.req_bin_0 = b'\x5e\x00\x08\x00' b'\xca\x77\x8b\x7d' \
            b'\x11\x6f\x67\x3f' b'\x87\x05\xbe\x04' \
            b'\x15\x81\x7e\x97' b'\xc6\xde\xeb\xdf' \
            b'\x47\x71\x1e\x87' b'\x84\x75\x39\xb9'


    def testPackRequest0(self):
        bin = request.CreateGlyphCursor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.CreateGlyphCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestFreeCursor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'cursor': 880461049,
            }
        self.req_bin_0 = b'\x5f\x00\x02\x00' b'\xf9\xc4\x7a\x34'


    def testPackRequest0(self):
        bin = request.FreeCursor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.FreeCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestRecolorCursor(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'back_blue': 42677,
            'back_green': 45475,
            'back_red': 22357,
            'cursor': 1406154815,
            'fore_blue': 63525,
            'fore_green': 30904,
            'fore_red': 10332,
            }
        self.req_bin_0 = b'\x60\x00\x05\x00' b'\x3f\x38\xd0\x53' \
            b'\x5c\x28\xb8\x78' b'\x25\xf8\x55\x57' \
            b'\xa3\xb1\xb5\xa6'


    def testPackRequest0(self):
        bin = request.RecolorCursor._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.RecolorCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestQueryBestSize(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 1830398758,
            'height': 25063,
            'item_class': 2,
            'width': 56353,
            }
        self.req_bin_0 = b'\x61\x02\x03\x00' b'\x26\xab\x19\x6d' \
            b'\x21\xdc\xe7\x61'

        self.reply_args_0 = {
            'height': 49829,
            'sequence_number': 20927,
            'width': 47173,
            }
        self.reply_bin_0 = b'\x01\x00\xbf\x51' b'\x00\x00\x00\x00' \
            b'\x45\xb8\xa5\xc2' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryBestSize._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryBestSize._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.QueryBestSize._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryBestSize._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestQueryExtension(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'name': 'XTRA',
            }
        self.req_bin_0 = b'\x62\x00\x03\x00' b'\x04\x00\x00\x00' \
            b'\x58\x54\x52\x41'

        self.reply_args_0 = {
            'first_error': 245,
            'first_event': 208,
            'major_opcode': 136,
            'present': 0,
            'sequence_number': 57205,
            }
        self.reply_bin_0 = b'\x01\x00\x75\xdf' b'\x00\x00\x00\x00' \
            b'\x00\x88\xd0\xf5' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryExtension._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.QueryExtension._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.QueryExtension._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.QueryExtension._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestListExtensions(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x63\x00\x01\x00'

        self.reply_args_0 = {
            'names': ['XTRA', 'XTRA-II'],
            'sequence_number': 65367,
            }
        self.reply_bin_0 = b'\x01\x02\x57\xff' b'\x04\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x04\x58\x54\x52' b'\x41\x07\x58\x54' \
            b'\x52\x41\x2d\x49' b'\x49\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ListExtensions._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ListExtensions._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.ListExtensions._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.ListExtensions._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestChangeKeyboardMapping(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'first_keycode': 209,
            'keysyms': [[1603668560, 931946639, 211405004], [1360963098, 1873849632, 952792434], [1490356148, 1940088399, 98764853], [1709705072, 630002501, 804965110], [312608755, 1140670982, 1215321258], [1701922610, 365037106, 169583241], [1870113797, 1330817882, 517178039], [1960285384, 307342963, 990311897], [545412183, 548309930, 20180830], [1727936374, 1935332499, 1455158296], [339250065, 948607486, 742096527], [1261800628, 1372110414, 911196506], [537081847, 1815276355, 427815247], [826122461, 1037681409, 509395365], [1228194629, 1234399220, 2131789930], [634003216, 2100119788, 1413537765], [589442127, 1215323309, 1472743195], [1599164158, 105321726, 1302248027], [1066713724, 1941658701, 614597260], [1715539042, 1303662156, 756603491]],
            }
        self.req_bin_0 = b'\x64\x14\x3e\x00' b'\xd1\x03\x00\x00' \
            b'\x50\x0a\x96\x5f' b'\x8f\x60\x8c\x37' \
            b'\xcc\xc8\x99\x0c' b'\x1a\xa6\x1e\x51' \
            b'\x20\xad\xb0\x6f' b'\x72\x75\xca\x38' \
            b'\xb4\x07\xd5\x58' b'\x4f\x66\xa3\x73' \
            b'\x35\x08\xe3\x05' b'\x70\x07\xe8\x65' \
            b'\x45\x13\x8d\x25' b'\xf6\xca\xfa\x2f' \
            b'\xf3\x07\xa2\x12' b'\x06\x42\xfd\x43' \
            b'\xaa\x54\x70\x48' b'\x32\x47\x71\x65' \
            b'\x32\x06\xc2\x15' b'\x89\xa2\x1b\x0a' \
            b'\x05\xac\x77\x6f' b'\x5a\xab\x52\x4f' \
            b'\xb7\x82\xd3\x1e' b'\xc8\x94\xd7\x74' \
            b'\x73\xae\x51\x12' b'\xd9\xf5\x06\x3b' \
            b'\x57\x54\x82\x20' b'\xaa\x8b\xae\x20' \
            b'\x5e\xef\x33\x01' b'\x76\x37\xfe\x66' \
            b'\x93\xd4\x5a\x73' b'\x18\xf4\xbb\x56' \
            b'\x91\x8b\x38\x14' b'\xfe\x99\x8a\x38' \
            b'\x8f\x7e\x3b\x2c' b'\xb4\x8c\x35\x4b' \
            b'\x4e\xbe\xc8\x51' b'\x5a\xc1\x4f\x36' \
            b'\xf7\x37\x03\x20' b'\x43\xeb\x32\x6c' \
            b'\x4f\xf1\x7f\x19' b'\xdd\xa0\x3d\x31' \
            b'\x01\xc3\xd9\x3d' b'\xa5\xc1\x5c\x1e' \
            b'\x45\xc3\x34\x49' b'\xf4\x6f\x93\x49' \
            b'\x6a\x88\x10\x7f' b'\x10\x1f\xca\x25' \
            b'\xec\x48\x2d\x7d' b'\xe5\xdf\x40\x54' \
            b'\x4f\x2c\x22\x23' b'\xad\x5c\x70\x48' \
            b'\x1b\x47\xc8\x57' b'\xfe\x4e\x51\x5f' \
            b'\xfe\x14\x47\x06' b'\x5b\xba\x9e\x4d' \
            b'\x7c\xc2\x94\x3f' b'\x4d\x5c\xbb\x73' \
            b'\x8c\x02\xa2\x24' b'\x62\x0c\x41\x66' \
            b'\x4c\x4e\xb4\x4d' b'\x63\xda\x18\x2d'


    def testPackRequest0(self):
        bin = request.ChangeKeyboardMapping._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeKeyboardMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetKeyboardMapping(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'count': 214,
            'first_keycode': 207,
            }
        self.req_bin_0 = b'\x65\x00\x02\x00' b'\xcf\xd6\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[1548181899, 1415581578, 1800315249], [1349152528, 1940044681, 1388005887], [663428316, 946660592, 1244625269], [1572730625, 193559950, 633744868], [1605202933, 377184179, 283811004], [1158369341, 2086257988, 1139996791], [1961698339, 1783426369, 551839054], [1771007886, 1034760334, 1731920851], [1603223997, 727385468, 247325063], [2067797600, 302273387, 2075543394], [1847137865, 1555243546, 2104409941], [2077195964, 1727838808, 785495937], [1697976597, 29890084, 1152280257], [976645557, 1444887947, 1443840867], [1255333237, 1766127705, 2019261461], [232671482, 502128711, 53740025], [1898879870, 1205613172, 1965497096], [475382442, 135757562, 1769215894], [1952895082, 648948458, 876808673], [300168848, 2032081167, 653617967]],
            'sequence_number': 32414,
            }
        self.reply_bin_0 = b'\x01\x03\x9e\x7e' b'\x3c\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x8b\x61\x47\x5c' b'\x8a\x0f\x60\x54' \
            b'\x71\xa1\x4e\x6b' b'\x10\x6f\x6a\x50' \
            b'\x89\xbb\xa2\x73' b'\xff\x49\xbb\x52' \
            b'\xdc\x1c\x8b\x27' b'\xf0\xe4\x6c\x38' \
            b'\x75\x79\x2f\x4a' b'\x01\xf7\xbd\x5d' \
            b'\x8e\x7d\x89\x0b' b'\xe4\x2d\xc6\x25' \
            b'\xf5\x73\xad\x5f' b'\xb3\x5f\x7b\x16' \
            b'\xbc\x9c\xea\x10' b'\x3d\x50\x0b\x45' \
            b'\x44\xc5\x59\x7c' b'\x77\xf8\xf2\x43' \
            b'\x23\x24\xed\x74' b'\x41\xed\x4c\x6a' \
            b'\x4e\x65\xe4\x20' b'\x8e\x6f\x8f\x69' \
            b'\x8e\x30\xad\x3d' b'\xd3\x03\x3b\x67' \
            b'\xbd\x41\x8f\x5f' b'\x7c\x05\x5b\x2b' \
            b'\x87\xe1\xbd\x0e' b'\x60\x16\x40\x7b' \
            b'\x6b\x53\x04\x12' b'\x62\x47\xb6\x7b' \
            b'\x49\x16\x19\x6e' b'\x1a\x22\xb3\x5c' \
            b'\x55\xbf\x6e\x7d' b'\xbc\x7e\xcf\x7b' \
            b'\x58\xba\xfc\x66' b'\x81\xb7\xd1\x2e' \
            b'\x15\x11\x35\x65' b'\x24\x16\xc8\x01' \
            b'\xc1\x66\xae\x44' b'\xb5\x6d\x36\x3a' \
            b'\x8b\x3d\x1f\x56' b'\x63\x43\x0f\x56' \
            b'\x75\xdd\xd2\x4a' b'\x59\xf8\x44\x69' \
            b'\x15\x7c\x5b\x78' b'\xfa\x48\xde\x0d' \
            b'\x47\xe0\xed\x1d' b'\xf9\x01\x34\x03' \
            b'\x7e\x9b\x2e\x71' b'\x74\x32\xdc\x47' \
            b'\x08\x1b\x27\x75' b'\xaa\xc2\x55\x1c' \
            b'\xfa\x7e\x17\x08' b'\x96\x17\x74\x69' \
            b'\x6a\xd0\x66\x74' b'\xea\x2a\xae\x26' \
            b'\xe1\x09\x43\x34' b'\x90\x36\xe4\x11' \
            b'\x0f\x19\x1f\x79' b'\x2f\x6b\xf5\x26'


    def testPackRequest0(self):
        bin = request.GetKeyboardMapping._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetKeyboardMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetKeyboardMapping._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetKeyboardMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestChangeKeyboardControl(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'led': 213, 'auto_repeat_mode': 1, 'bell_pitch': -28323, 'bell_percent': -15, 'key_click_percent': -116, 'key': 249, 'bell_duration': -17904, 'led_mode': 1},
            }
        self.req_bin_0 = b'\x66\x00\x0a\x00' b'\xff\x00\x00\x00' \
            b'\x8c\x00\x00\x00' b'\xf1\x00\x00\x00' \
            b'\x5d\x91\x00\x00' b'\x10\xba\x00\x00' \
            b'\xd5\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\xf9\x00\x00\x00' b'\x01\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangeKeyboardControl._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeKeyboardControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetKeyboardControl(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x67\x00\x01\x00'

        self.reply_args_0 = {
            'auto_repeats': [223, 147, 181, 140, 190, 180, 249, 132, 175, 184, 249, 237, 140, 215, 197, 253, 173, 178, 152, 143, 236, 186, 212, 210, 204, 130, 228, 159, 144, 200, 136, 225],
            'bell_duration': 441,
            'bell_percent': 146,
            'bell_pitch': 59042,
            'global_auto_repeat': 0,
            'key_click_percent': 170,
            'led_mask': 1867665246,
            'sequence_number': 14353,
            }
        self.reply_bin_0 = b'\x01\x00\x11\x38' b'\x05\x00\x00\x00' \
            b'\x5e\x4f\x52\x6f' b'\xaa\x92\xa2\xe6' \
            b'\xb9\x01\x00\x00' b'\xdf\x93\xb5\x8c' \
            b'\xbe\xb4\xf9\x84' b'\xaf\xb8\xf9\xed' \
            b'\x8c\xd7\xc5\xfd' b'\xad\xb2\x98\x8f' \
            b'\xec\xba\xd4\xd2' b'\xcc\x82\xe4\x9f' \
            b'\x90\xc8\x88\xe1'


    def testPackRequest0(self):
        bin = request.GetKeyboardControl._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetKeyboardControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetKeyboardControl._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetKeyboardControl._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestBell(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'percent': -19,
            }
        self.req_bin_0 = b'\x68\xed\x01\x00'


    def testPackRequest0(self):
        bin = request.Bell._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.Bell._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestChangePointerControl(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'accel_denum': -28542,
            'accel_num': -28064,
            'do_accel': 0,
            'do_thresh': 1,
            'threshold': -24619,
            }
        self.req_bin_0 = b'\x69\x00\x03\x00' b'\x60\x92\x82\x90' \
            b'\xd5\x9f\x00\x01'


    def testPackRequest0(self):
        bin = request.ChangePointerControl._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangePointerControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetPointerControl(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x6a\x00\x01\x00'

        self.reply_args_0 = {
            'accel_denom': 51826,
            'accel_num': 1226,
            'sequence_number': 1938,
            'threshold': 15788,
            }
        self.reply_bin_0 = b'\x01\x00\x92\x07' b'\x00\x00\x00\x00' \
            b'\xca\x04\x72\xca' b'\xac\x3d\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetPointerControl._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetPointerControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetPointerControl._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetPointerControl._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestSetScreenSaver(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'allow_exposures': 2,
            'interval': -27103,
            'prefer_blank': 0,
            'timeout': -22242,
            }
        self.req_bin_0 = b'\x6b\x00\x03\x00' b'\x1e\xa9\x21\x96' \
            b'\x00\x02\x00\x00'


    def testPackRequest0(self):
        bin = request.SetScreenSaver._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestGetScreenSaver(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x6c\x00\x01\x00'

        self.reply_args_0 = {
            'allow_exposures': 1,
            'interval': 31345,
            'prefer_blanking': 1,
            'sequence_number': 34598,
            'timeout': 48933,
            }
        self.reply_bin_0 = b'\x01\x00\x26\x87' b'\x00\x00\x00\x00' \
            b'\x25\xbf\x71\x7a' b'\x01\x01\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetScreenSaver._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetScreenSaver._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetScreenSaver._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestChangeHosts(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'host': [141, 192, 249, 133],
            'host_family': 2,
            'mode': 1,
            }
        self.req_bin_0 = b'\x6d\x01\x03\x00' b'\x02\x00\x04\x00' \
            b'\x8d\xc0\xf9\x85'


    def testPackRequest0(self):
        bin = request.ChangeHosts._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ChangeHosts._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestListHosts(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x6e\x00\x01\x00'

        self.reply_args_0 = {
            'hosts': [{'name': [34, 23, 178, 12], 'family': 0}, {'name': [130, 236, 254, 15], 'family': 0}],
            'mode': 1,
            'sequence_number': 30157,
            }
        self.reply_bin_0 = b'\x01\x01\xcd\x75' b'\x04\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x04\x00' b'\x22\x17\xb2\x0c' \
            b'\x00\x00\x04\x00' b'\x82\xec\xfe\x0f'


    def testPackRequest0(self):
        bin = request.ListHosts._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ListHosts._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.ListHosts._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.ListHosts._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestSetAccessControl(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'mode': 1,
            }
        self.req_bin_0 = b'\x6f\x01\x01\x00'


    def testPackRequest0(self):
        bin = request.SetAccessControl._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetAccessControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestSetCloseDownMode(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'mode': 0,
            }
        self.req_bin_0 = b'\x70\x00\x01\x00'


    def testPackRequest0(self):
        bin = request.SetCloseDownMode._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetCloseDownMode._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestKillClient(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'resource': 1028639966,
            }
        self.req_bin_0 = b'\x71\x00\x02\x00' b'\xde\xcc\x4f\x3d'


    def testPackRequest0(self):
        bin = request.KillClient._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.KillClient._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestRotateProperties(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'delta': -15519,
            'properties': [862505702, 1473403724, 1052877752, 1953573572, 157880830, 173556470, 1306334440, 141112753, 590639874, 1359545959, 1177616073, 698374646],
            'window': 2135947192,
            }
        self.req_bin_0 = b'\x72\x00\x0f\x00' b'\xb8\xf7\x4f\x7f' \
            b'\x0c\x00\x61\xc3' b'\xe6\xca\x68\x33' \
            b'\x4c\x5b\xd2\x57' b'\xb8\xa3\xc1\x3e' \
            b'\xc4\x2a\x71\x74' b'\xfe\x11\x69\x09' \
            b'\xf6\x42\x58\x0a' b'\xe8\x14\xdd\x4d' \
            b'\xb1\x35\x69\x08' b'\x02\x73\x34\x23' \
            b'\x67\x06\x09\x51' b'\xc9\xfe\x30\x46' \
            b'\xf6\x59\xa0\x29'


    def testPackRequest0(self):
        bin = request.RotateProperties._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.RotateProperties._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestForceScreenSaver(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'mode': 0,
            }
        self.req_bin_0 = b'\x73\x00\x01\x00'


    def testPackRequest0(self):
        bin = request.ForceScreenSaver._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.ForceScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


class TestSetPointerMapping(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'map': [205, 140, 217, 237, 211],
            }
        self.req_bin_0 = b'\x74\x05\x03\x00' b'\xcd\x8c\xd9\xed' \
            b'\xd3\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 47312,
            'status': 226,
            }
        self.reply_bin_0 = b'\x01\xe2\xd0\xb8' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetPointerMapping._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetPointerMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.SetPointerMapping._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.SetPointerMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestGetPointerMapping(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x75\x00\x01\x00'

        self.reply_args_0 = {
            'map': [155, 185, 157, 171, 186],
            'sequence_number': 27411,
            }
        self.reply_bin_0 = b'\x01\x05\x13\x6b' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x9b\xb9\x9d\xab' b'\xba\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetPointerMapping._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetPointerMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetPointerMapping._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetPointerMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestSetModifierMapping(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'keycodes': [[24, 109], [170, 95], [39, 236], [17, 212], [23, 24], [189, 207], [142, 150], [143, 84]],
            }
        self.req_bin_0 = b'\x76\x02\x05\x00' b'\x18\x6d\xaa\x5f' \
            b'\x27\xec\x11\xd4' b'\x17\x18\xbd\xcf' \
            b'\x8e\x96\x8f\x54'

        self.reply_args_0 = {
            'sequence_number': 23338,
            'status': 143,
            }
        self.reply_bin_0 = b'\x01\x8f\x2a\x5b' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetModifierMapping._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.SetModifierMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.SetModifierMapping._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.SetModifierMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestGetModifierMapping(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x77\x00\x01\x00'

        self.reply_args_0 = {
            'keycodes': [[170, 192], [222, 184], [247, 153], [90, 147], [54, 168], [57, 27], [216, 94], [195, 146]],
            'sequence_number': 52951,
            }
        self.reply_bin_0 = b'\x01\x02\xd7\xce' b'\x04\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xaa\xc0\xde\xb8' b'\xf7\x99\x5a\x93' \
            b'\x36\xa8\x39\x1b' b'\xd8\x5e\xc3\x92'


    def testPackRequest0(self):
        bin = request.GetModifierMapping._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.GetModifierMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)

    def testPackReply0(self):
        bin = request.GetModifierMapping._reply.to_binary(*(), **self.reply_args_0)
        self.assertBinaryEqual(bin, self.reply_bin_0)

    def testUnpackReply0(self):
        args, remain = request.GetModifierMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_0)


class TestNoOperation(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x7f\x00\x01\x00'


    def testPackRequest0(self):
        bin = request.NoOperation._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.NoOperation._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


if __name__ == "__main__":
    unittest.main()
