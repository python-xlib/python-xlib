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
            'attrs': {'background_pixmap': 1373224142, 'background_pixel': 239147199, 'border_pixmap': 53775720, 'border_pixel': 1592533117, 'bit_gravity': 3, 'win_gravity': 2, 'backing_store': 0, 'backing_planes': 299720948, 'backing_pixel': 1581625428, 'override_redirect': 0, 'save_under': 0, 'event_mask': 1268138548, 'do_not_propagate_mask': 906135756, 'colormap': 68318329, 'cursor': 64054583},
            'border_width': 13287,
            'depth': 151,
            'height': 37037,
            'parent': 499701004,
            'visual': 1395681732,
            'wid': 469587013,
            'width': 1995,
            'window_class': 2,
            'x': -16209,
            'y': -13042,
            }
        self.req_bin_0 = b'\x01\x97\x17\x00' b'\x45\x54\xfd\x1b' \
            b'\x0c\xd5\xc8\x1d' b'\xaf\xc0\x0e\xcd' \
            b'\xcb\x07\xad\x90' b'\xe7\x33\x02\x00' \
            b'\xc4\x69\x30\x53' b'\xff\x7f\x00\x00' \
            b'\xce\xbc\xd9\x51' b'\xbf\x18\x41\x0e' \
            b'\x68\x8d\x34\x03' b'\x7d\x20\xec\x5e' \
            b'\x03\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\xf4\x60\xdd\x11' \
            b'\x54\xb0\x45\x5e' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x34\x42\x96\x4b' \
            b'\xcc\x88\x02\x36' b'\x79\x74\x12\x04' \
            b'\x37\x65\xd1\x03'


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
            'attrs': {'background_pixmap': 1506149446, 'background_pixel': 1170318459, 'border_pixmap': 900977490, 'border_pixel': 473458160, 'bit_gravity': 6, 'win_gravity': 8, 'backing_store': 1, 'backing_planes': 1738304197, 'backing_pixel': 1866873765, 'override_redirect': 0, 'save_under': 0, 'event_mask': 1499308477, 'do_not_propagate_mask': 907623048, 'colormap': 730747963, 'cursor': 596789700},
            'window': 333955224,
            }
        self.req_bin_0 = b'\x02\x00\x12\x00' b'\x98\xc0\xe7\x13' \
            b'\xff\x7f\x00\x00' b'\x46\x04\xc6\x59' \
            b'\x7b\xa4\xc1\x45' b'\x52\xd3\xb3\x35' \
            b'\xf0\x65\x38\x1c' b'\x06\x00\x00\x00' \
            b'\x08\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\xc5\x6a\x9c\x67' b'\xa5\x3b\x46\x6f' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xbd\xa1\x5d\x59' b'\x88\x3a\x19\x36' \
            b'\x3b\x54\x8e\x2b' b'\xc4\x49\x92\x23'


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
            'window': 462448317,
            }
        self.req_bin_0 = b'\x03\x00\x02\x00' b'\xbd\x66\x90\x1b'

        self.reply_args_0 = {
            'all_event_masks': 1980679760,
            'backing_bit_planes': 1820045833,
            'backing_pixel': 738704824,
            'backing_store': 214,
            'bit_gravity': 152,
            'colormap': 2089815718,
            'do_not_propagate_mask': 5420,
            'map_is_installed': 0,
            'map_state': 245,
            'override_redirect': 0,
            'save_under': 1,
            'sequence_number': 6954,
            'visual': 199235720,
            'win_class': 25154,
            'win_gravity': 219,
            'your_event_mask': 812961929,
            }
        self.reply_bin_0 = b'\x01\xd6\x2a\x1b' b'\x03\x00\x00\x00' \
            b'\x88\x18\xe0\x0b' b'\x42\x62\x98\xdb' \
            b'\x09\xb2\x7b\x6c' b'\xb8\xbd\x07\x2c' \
            b'\x01\x00\xf5\x00' b'\xa6\x0e\x90\x7c' \
            b'\x50\xc6\x0e\x76' b'\x89\xd0\x74\x30' \
            b'\x2c\x15\x00\x00'


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
            'window': 1185563768,
            }
        self.req_bin_0 = b'\x04\x00\x02\x00' b'\x78\x44\xaa\x46'


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
            'window': 629661088,
            }
        self.req_bin_0 = b'\x05\x00\x02\x00' b'\xa0\xdd\x87\x25'


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
            'window': 1239919839,
            }
        self.req_bin_0 = b'\x06\x01\x02\x00' b'\xdf\xac\xe7\x49'


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
            'parent': 1513122040,
            'window': 413002134,
            'x': -30489,
            'y': -31267,
            }
        self.req_bin_0 = b'\x07\x00\x04\x00' b'\x96\xe9\x9d\x18' \
            b'\xf8\x68\x30\x5a' b'\xe7\x88\xdd\x85'


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
            'window': 1420117708,
            }
        self.req_bin_0 = b'\x08\x00\x02\x00' b'\xcc\x46\xa5\x54'


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
            'window': 489473351,
            }
        self.req_bin_0 = b'\x09\x00\x02\x00' b'\x47\xc5\x2c\x1d'


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
            'window': 1660217157,
            }
        self.req_bin_0 = b'\x0a\x00\x02\x00' b'\x45\xe7\xf4\x62'


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
            'window': 621521446,
            }
        self.req_bin_0 = b'\x0b\x00\x02\x00' b'\x26\xaa\x0b\x25'


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
            'attrs': {'x': -27539, 'y': -17512, 'width': 39387, 'height': 57679, 'border_width': -14551, 'sibling': 973756745, 'stack_mode': 2},
            'window': 349362548,
            }
        self.req_bin_0 = b'\x0c\x00\x0a\x00' b'\x74\xd9\xd2\x14' \
            b'\x7f\x00\x00\x00' b'\x6d\x94\x00\x00' \
            b'\x98\xbb\x00\x00' b'\xdb\x99\x00\x00' \
            b'\x4f\xe1\x00\x00' b'\x29\xc7\x00\x00' \
            b'\x49\x59\x0a\x3a' b'\x02\x00\x00\x00'


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
            'direction': 1,
            'window': 763003561,
            }
        self.req_bin_0 = b'\x0d\x01\x02\x00' b'\xa9\x82\x7a\x2d'


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
            'drawable': 449978455,
            }
        self.req_bin_0 = b'\x0e\x00\x02\x00' b'\x57\x20\xd2\x1a'

        self.reply_args_0 = {
            'border_width': 41869,
            'depth': 196,
            'height': 40176,
            'root': 2011515940,
            'sequence_number': 46250,
            'width': 4935,
            'x': -10370,
            'y': -11534,
            }
        self.reply_bin_0 = b'\x01\xc4\xaa\xb4' b'\x00\x00\x00\x00' \
            b'\x24\x4c\xe5\x77' b'\x7e\xd7\xf2\xd2' \
            b'\x47\x13\xf0\x9c' b'\x8d\xa3\x00\x00' \
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
            'window': 367582976,
            }
        self.req_bin_0 = b'\x0f\x00\x02\x00' b'\x00\xdf\xe8\x15'

        self.reply_args_0 = {
            'children': [1147122179, 1565853418, 525792997, 350969719, 992761785, 814939899, 579774073],
            'parent': 1374454548,
            'root': 1987327953,
            'sequence_number': 65105,
            }
        self.reply_bin_0 = b'\x01\x00\x51\xfe' b'\x07\x00\x00\x00' \
            b'\xd1\x37\x74\x76' b'\x14\x83\xec\x51' \
            b'\x07\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x03\xb2\x5f\x44' b'\xea\x06\x55\x5d' \
            b'\xe5\xf6\x56\x1f' b'\x77\x5f\xeb\x14' \
            b'\xb9\x57\x2c\x3b' b'\xfb\xfe\x92\x30' \
            b'\x79\xa6\x8e\x22'


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
            'atom': 696457407,
            'sequence_number': 45122,
            }
        self.reply_bin_0 = b'\x01\x00\x42\xb0' b'\x00\x00\x00\x00' \
            b'\xbf\x18\x83\x29' b'\x00\x00\x00\x00' \
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
            'atom': 1810076242,
            }
        self.req_bin_0 = b'\x11\x00\x02\x00' b'\x52\x92\xe3\x6b'

        self.reply_args_0 = {
            'name': 'WM_CLASS',
            'sequence_number': 50608,
            }
        self.reply_bin_0 = b'\x01\x00\xb0\xc5' b'\x02\x00\x00\x00' \
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
            'data': (8, b''),
            'mode': 0,
            'property': 1764873173,
            'type': 69000273,
            'window': 491942524,
            }
        self.req_bin_0 = b'\x12\x00\x06\x00' b'\x7c\x72\x52\x1d' \
            b'\xd5\xd3\x31\x69' b'\x51\xdc\x1c\x04' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_1 = {
            'data': (8, b'foo'),
            'mode': 1,
            'property': 575034703,
            'type': 142204480,
            'window': 861560365,
            }
        self.req_bin_1 = b'\x12\x01\x07\x00' b'\x2d\x5e\x5a\x33' \
            b'\x4f\x55\x46\x22' b'\x40\xde\x79\x08' \
            b'\x08\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'data': (8, b'zoom'),
            'mode': 0,
            'property': 2024948722,
            'type': 1218075423,
            'window': 1961010416,
            }
        self.req_bin_2 = b'\x12\x00\x07\x00' b'\xf0\xa4\xe2\x74' \
            b'\xf2\x43\xb2\x78' b'\x1f\x5b\x9a\x48' \
            b'\x08\x00\x00\x00' b'\x04\x00\x00\x00' \
            b'\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'data': (16, []),
            'mode': 2,
            'property': 456677559,
            'type': 1407609354,
            'window': 675831147,
            }
        self.req_bin_3 = b'\x12\x02\x06\x00' b'\x6b\x5d\x48\x28' \
            b'\xb7\x58\x38\x1b' b'\x0a\x6a\xe6\x53' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_4 = {
            'data': (16, [1, 2, 3]),
            'mode': 1,
            'property': 1899908134,
            'type': 1964041522,
            'window': 849678568,
            }
        self.req_bin_4 = b'\x12\x01\x08\x00' b'\xe8\x10\xa5\x32' \
            b'\x26\x4c\x3e\x71' b'\x32\xe5\x10\x75' \
            b'\x10\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x00\x00'

        self.req_args_5 = {
            'data': (16, [1, 2, 3, 4]),
            'mode': 2,
            'property': 306879937,
            'type': 568891375,
            'window': 985442388,
            }
        self.req_bin_5 = b'\x12\x02\x08\x00' b'\x54\xa8\xbc\x3a' \
            b'\xc1\x9d\x4a\x12' b'\xef\x97\xe8\x21' \
            b'\x10\x00\x00\x00' b'\x04\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x04\x00'

        self.req_args_6 = {
            'data': (32, []),
            'mode': 0,
            'property': 1599917196,
            'type': 1205594429,
            'window': 529694076,
            }
        self.req_bin_6 = b'\x12\x00\x06\x00' b'\x7c\x7d\x92\x1f' \
            b'\x8c\xcc\x5c\x5f' b'\x3d\xe9\xdb\x47' \
            b'\x20\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_7 = {
            'data': (32, [1, 2, 3]),
            'mode': 2,
            'property': 1604265475,
            'type': 1255454396,
            'window': 564298846,
            }
        self.req_bin_7 = b'\x12\x02\x09\x00' b'\x5e\x84\xa2\x21' \
            b'\x03\x26\x9f\x5f' b'\xbc\xb6\xd4\x4a' \
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
            'property': 1928125498,
            'window': 920120163,
            }
        self.req_bin_0 = b'\x13\x00\x03\x00' b'\x63\xeb\xd7\x36' \
            b'\x3a\xdc\xec\x72'


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
            'delete': 1,
            'long_length': 297130690,
            'long_offset': 2142261240,
            'property': 471053276,
            'type': 2141806322,
            'window': 777446987,
            }
        self.req_bin_0 = b'\x14\x01\x06\x00' b'\x4b\xe6\x56\x2e' \
            b'\xdc\xb3\x13\x1c' b'\xf2\x5e\xa9\x7f' \
            b'\xf8\x4f\xb0\x7f' b'\xc2\xda\xb5\x11'

        self.reply_args_0 = {
            'bytes_after': 195292012,
            'property_type': 1059882735,
            'sequence_number': 33648,
            'value': (8, b''),
            }
        self.reply_bin_0 = b'\x01\x08\x70\x83' b'\x00\x00\x00\x00' \
            b'\xef\x86\x2c\x3f' b'\x6c\xeb\xa3\x0b' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_1 = {
            'bytes_after': 1849269963,
            'property_type': 101247178,
            'sequence_number': 49786,
            'value': (8, b'foo'),
            }
        self.reply_bin_1 = b'\x01\x08\x7a\xc2' b'\x01\x00\x00\x00' \
            b'\xca\xe8\x08\x06' b'\xcb\x9e\x39\x6e' \
            b'\x03\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'bytes_after': 1347495650,
            'property_type': 328289775,
            'sequence_number': 7441,
            'value': (8, b'zoom'),
            }
        self.reply_bin_2 = b'\x01\x08\x11\x1d' b'\x01\x00\x00\x00' \
            b'\xef\x4d\x91\x13' b'\xe2\x26\x51\x50' \
            b'\x04\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'bytes_after': 1461387818,
            'property_type': 1701043014,
            'sequence_number': 10740,
            'value': (16, []),
            }
        self.reply_bin_3 = b'\x01\x10\xf4\x29' b'\x00\x00\x00\x00' \
            b'\x46\xdb\x63\x65' b'\x2a\x02\x1b\x57' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_4 = {
            'bytes_after': 136490248,
            'property_type': 1280844186,
            'sequence_number': 27922,
            'value': (16, [1, 2, 3]),
            }
        self.reply_bin_4 = b'\x01\x10\x12\x6d' b'\x02\x00\x00\x00' \
            b'\x9a\x21\x58\x4c' b'\x08\xad\x22\x08' \
            b'\x03\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x00\x00'

        self.reply_args_5 = {
            'bytes_after': 1279726180,
            'property_type': 819586705,
            'sequence_number': 25472,
            'value': (16, [1, 2, 3, 4]),
            }
        self.reply_bin_5 = b'\x01\x10\x80\x63' b'\x02\x00\x00\x00' \
            b'\x91\xe6\xd9\x30' b'\x64\x12\x47\x4c' \
            b'\x04\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x01\x00\x02\x00' b'\x03\x00\x04\x00'

        self.reply_args_6 = {
            'bytes_after': 539973238,
            'property_type': 1136329940,
            'sequence_number': 30930,
            'value': (32, []),
            }
        self.reply_bin_6 = b'\x01\x20\xd2\x78' b'\x00\x00\x00\x00' \
            b'\xd4\x04\xbb\x43' b'\x76\x56\x2f\x20' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_7 = {
            'bytes_after': 1848575862,
            'property_type': 1188109101,
            'sequence_number': 63896,
            'value': (32, [1, 2, 3]),
            }
        self.reply_bin_7 = b'\x01\x20\x98\xf9' b'\x03\x00\x00\x00' \
            b'\x2d\x1b\xd1\x46' b'\x76\x07\x2f\x6e' \
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
            'window': 2023920407,
            }
        self.req_bin_0 = b'\x15\x00\x02\x00' b'\x17\x93\xa2\x78'

        self.reply_args_0 = {
            'atoms': [24720840, 1460963027, 1547803868, 246063525, 1464027403, 1900134270, 1153200538, 1612563336, 573068260, 1650618737, 1376520521, 730586807, 239622004, 630352260, 933716813, 339706725, 974429777, 7034796, 2048369638, 1550746425, 1880945398, 1545568005, 565689201],
            'sequence_number': 63949,
            }
        self.reply_bin_0 = b'\x01\x00\xcd\xf9' b'\x17\x00\x00\x00' \
            b'\x17\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xc8\x35\x79\x01' b'\xd3\x86\x14\x57' \
            b'\xdc\x9c\x41\x5c' b'\xa5\xa1\xaa\x0e' \
            b'\x0b\x49\x43\x57' b'\x7e\xbf\x41\x71' \
            b'\x9a\x71\xbc\x44' b'\x88\xc3\x1d\x60' \
            b'\xe4\x53\x28\x22' b'\x71\x71\x62\x62' \
            b'\x49\x09\x0c\x52' b'\xb7\xde\x8b\x2b' \
            b'\x74\x57\x48\x0e' b'\x84\x69\x92\x25' \
            b'\x4d\x63\xa7\x37' b'\x65\x83\x3f\x14' \
            b'\x51\x9e\x14\x3a' b'\xac\x57\x6b\x00' \
            b'\xe6\xa3\x17\x7a' b'\x39\x83\x6e\x5c' \
            b'\xf6\xf2\x1c\x70' b'\x05\x7f\x1f\x5c' \
            b'\x71\xbb\xb7\x21'


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
            'selection': 1636366903,
            'time': 383717530,
            'window': 1075066031,
            }
        self.req_bin_0 = b'\x16\x00\x04\x00' b'\xaf\x34\x14\x40' \
            b'\x37\xfa\x88\x61' b'\x9a\x10\xdf\x16'


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
            'selection': 1090303630,
            }
        self.req_bin_0 = b'\x17\x00\x02\x00' b'\x8e\xb6\xfc\x40'

        self.reply_args_0 = {
            'owner': 228581038,
            'sequence_number': 60065,
            }
        self.reply_bin_0 = b'\x01\x00\xa1\xea' b'\x00\x00\x00\x00' \
            b'\xae\xde\x9f\x0d' b'\x00\x00\x00\x00' \
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
            'property': 1807536699,
            'requestor': 1869489931,
            'selection': 1342887479,
            'target': 640970836,
            'time': 1372199123,
            }
        self.req_bin_0 = b'\x18\x00\x06\x00' b'\x0b\x27\x6e\x6f' \
            b'\x37\xd6\x0a\x50' b'\x54\x70\x34\x26' \
            b'\x3b\xd2\xbc\x6b' b'\xd3\x18\xca\x51'


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
            'destination': 1158373169,
            'event': event.Expose(count=50227, height=24760, sequence_number=0, type=12, width=10272, window=1090263274, x=40165, y=13291),
            'event_mask': 2047690655,
            'propagate': 0,
            }
        self.req_bin_0 = b'\x19\x00\x0b\x00' b'\x31\x5f\x0b\x45' \
            b'\x9f\x47\x0d\x7a' b'\x0c\x00\x00\x00' \
            b'\xea\x18\xfc\x40' b'\xe5\x9c\xeb\x33' \
            b'\x20\x28\xb8\x60' b'\x33\xc4\x00\x00' \
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
            'confine_to': 240299645,
            'cursor': 1995289624,
            'event_mask': 21499,
            'grab_window': 1286289242,
            'keyboard_mode': 0,
            'owner_events': 0,
            'pointer_mode': 1,
            'time': 779560794,
            }
        self.req_bin_0 = b'\x1a\x00\x06\x00' b'\x5a\x37\xab\x4c' \
            b'\xfb\x53\x01\x00' b'\x7d\xae\x52\x0e' \
            b'\x18\xb4\xed\x76' b'\x5a\x27\x77\x2e'

        self.reply_args_0 = {
            'sequence_number': 15948,
            'status': 206,
            }
        self.reply_bin_0 = b'\x01\xce\x4c\x3e' b'\x00\x00\x00\x00' \
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
            'time': 124458893,
            }
        self.req_bin_0 = b'\x1b\x00\x02\x00' b'\x8d\x17\x6b\x07'


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
            'button': 145,
            'confine_to': 1571825127,
            'cursor': 1043722096,
            'event_mask': 37438,
            'grab_window': 1885576796,
            'keyboard_mode': 0,
            'modifiers': 64349,
            'owner_events': 0,
            'pointer_mode': 0,
            }
        self.req_bin_0 = b'\x1c\x00\x06\x00' b'\x5c\x9e\x63\x70' \
            b'\x3e\x92\x00\x00' b'\xe7\x25\xb0\x5d' \
            b'\x70\xef\x35\x3e' b'\x91\x00\x5d\xfb'


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
            'button': 160,
            'grab_window': 275784110,
            'modifiers': 43493,
            }
        self.req_bin_0 = b'\x1d\xa0\x03\x00' b'\xae\x21\x70\x10' \
            b'\xe5\xa9\x00\x00'


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
            'cursor': 1020726671,
            'event_mask': 36287,
            'time': 2033407590,
            }
        self.req_bin_0 = b'\x1e\x00\x04\x00' b'\x8f\x0d\xd7\x3c' \
            b'\x66\x56\x33\x79' b'\xbf\x8d\x00\x00'


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
            'grab_window': 569270305,
            'keyboard_mode': 0,
            'owner_events': 0,
            'pointer_mode': 1,
            'time': 1133236353,
            }
        self.req_bin_0 = b'\x1f\x00\x04\x00' b'\x21\x60\xee\x21' \
            b'\x81\xd0\x8b\x43' b'\x01\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 46979,
            'status': 179,
            }
        self.reply_bin_0 = b'\x01\xb3\x83\xb7' b'\x00\x00\x00\x00' \
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
            'time': 669471181,
            }
        self.req_bin_0 = b'\x20\x00\x02\x00' b'\xcd\x51\xe7\x27'


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
            'grab_window': 2137132511,
            'key': 223,
            'keyboard_mode': 1,
            'modifiers': 44275,
            'owner_events': 1,
            'pointer_mode': 1,
            }
        self.req_bin_0 = b'\x21\x01\x04\x00' b'\xdf\x0d\x62\x7f' \
            b'\xf3\xac\xdf\x01' b'\x01\x00\x00\x00'


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
            'grab_window': 532438798,
            'key': 158,
            'modifiers': 14981,
            }
        self.req_bin_0 = b'\x22\x9e\x03\x00' b'\x0e\x5f\xbc\x1f' \
            b'\x85\x3a\x00\x00'


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
            'time': 726098765,
            }
        self.req_bin_0 = b'\x23\x01\x02\x00' b'\x4d\x63\x47\x2b'


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
            'window': 45236268,
            }
        self.req_bin_0 = b'\x26\x00\x02\x00' b'\x2c\x40\xb2\x02'

        self.reply_args_0 = {
            'child': 15507755,
            'mask': 15259,
            'root': 472978779,
            'root_x': -30442,
            'root_y': -9574,
            'same_screen': 0,
            'sequence_number': 38820,
            'win_x': -12089,
            'win_y': -30839,
            }
        self.reply_bin_0 = b'\x01\x00\xa4\x97' b'\x00\x00\x00\x00' \
            b'\x5b\x15\x31\x1c' b'\x2b\xa1\xec\x00' \
            b'\x16\x89\x9a\xda' b'\xc7\xd0\x89\x87' \
            b'\x9b\x3b\x00\x00' b'\x00\x00\x00\x00'


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
            'start': 1944440211,
            'stop': 67524349,
            'window': 144806627,
            }
        self.req_bin_0 = b'\x27\x00\x04\x00' b'\xe3\x92\xa1\x08' \
            b'\x93\xcd\xe5\x73' b'\xfd\x56\x06\x04'

        self.reply_args_0 = {
            'events': [{'time': 1846118496, 'x': -21941, 'y': -30447}, {'time': 1104207400, 'x': -24970, 'y': -23643}, {'time': 1436684371, 'x': -16862, 'y': -25748}, {'time': 1158061593, 'x': -28433, 'y': -9066}, {'time': 2009067067, 'x': -3855, 'y': -14057}],
            'sequence_number': 38018,
            }
        self.reply_bin_0 = b'\x01\x00\x82\x94' b'\x0a\x00\x00\x00' \
            b'\x05\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x60\x88\x09\x6e' b'\x4b\xaa\x11\x89' \
            b'\x28\xde\xd0\x41' b'\x76\x9e\xa5\xa3' \
            b'\x53\x10\xa2\x55' b'\x22\xbe\x6c\x9b' \
            b'\x19\x9e\x06\x45' b'\xef\x90\x96\xdc' \
            b'\x3b\xee\xbf\x77' b'\xf1\xf0\x17\xc9'


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
            'dst_wid': 521898132,
            'src_wid': 1015118844,
            'src_x': -7058,
            'src_y': -17270,
            }
        self.req_bin_0 = b'\x28\x00\x04\x00' b'\xfc\x7b\x81\x3c' \
            b'\x94\x88\x1b\x1f' b'\x6e\xe4\x8a\xbc'

        self.reply_args_0 = {
            'child': 202628650,
            'same_screen': 1,
            'sequence_number': 12734,
            'x': -29592,
            'y': -11175,
            }
        self.reply_bin_0 = b'\x01\x01\xbe\x31' b'\x00\x00\x00\x00' \
            b'\x2a\xde\x13\x0c' b'\x68\x8c\x59\xd4' \
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
            'dst_window': 760913775,
            'dst_x': -8878,
            'dst_y': -30993,
            'src_height': 56868,
            'src_width': 30862,
            'src_window': 925740905,
            'src_x': -18889,
            'src_y': -19298,
            }
        self.req_bin_0 = b'\x29\x00\x06\x00' b'\x69\xaf\x2d\x37' \
            b'\x6f\x9f\x5a\x2d' b'\x37\xb6\x9e\xb4' \
            b'\x8e\x78\x24\xde' b'\x52\xdd\xef\x86'


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
            'focus': 1403350503,
            'revert_to': 2,
            'time': 2113544232,
            }
        self.req_bin_0 = b'\x2a\x02\x03\x00' b'\xe7\x6d\xa5\x53' \
            b'\x28\x20\xfa\x7d'


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
            'focus': 864688157,
            'revert_to': 153,
            'sequence_number': 4228,
            }
        self.reply_bin_0 = b'\x01\x99\x84\x10' b'\x00\x00\x00\x00' \
            b'\x1d\x18\x8a\x33' b'\x00\x00\x00\x00' \
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
            'map': [214, 155, 191, 177, 176, 242, 163, 236, 174, 199, 246, 191, 147, 241, 153, 140, 131, 151, 188, 170, 232, 252, 251, 182, 230, 143, 170, 225, 128, 227, 195, 244],
            'sequence_number': 18950,
            }
        self.reply_bin_0 = b'\x01\x00\x06\x4a' b'\x02\x00\x00\x00' \
            b'\xd6\x9b\xbf\xb1' b'\xb0\xf2\xa3\xec' \
            b'\xae\xc7\xf6\xbf' b'\x93\xf1\x99\x8c' \
            b'\x83\x97\xbc\xaa' b'\xe8\xfc\xfb\xb6' \
            b'\xe6\x8f\xaa\xe1' b'\x80\xe3\xc3\xf4'


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
            'fid': 908467189,
            'name': 'foofont',
            }
        self.req_bin_0 = b'\x2d\x00\x05\x00' b'\xf5\x1b\x26\x36' \
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
            'font': 1495984396,
            }
        self.req_bin_0 = b'\x2e\x00\x02\x00' b'\x0c\xe9\x2a\x59'


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
            'font': 2055889505,
            }
        self.req_bin_0 = b'\x2f\x00\x02\x00' b'\x61\x62\x8a\x7a'

        self.reply_args_0 = {
            'all_chars_exist': 0,
            'char_infos': [{'left_side_bearing': -7099, 'right_side_bearing': -14557, 'character_width': -11080, 'ascent': -9228, 'descent': -16821, 'attributes': 10400}, {'left_side_bearing': -26546, 'right_side_bearing': -23046, 'character_width': -25635, 'ascent': -1026, 'descent': -30852, 'attributes': 38213}, {'left_side_bearing': -8660, 'right_side_bearing': -15002, 'character_width': -30771, 'ascent': -8259, 'descent': -22492, 'attributes': 4002}],
            'default_char': 39252,
            'draw_direction': 145,
            'font_ascent': -1914,
            'font_descent': -3596,
            'max_bounds': {'left_side_bearing': -27610, 'right_side_bearing': -30905, 'character_width': -1286, 'ascent': -16128, 'descent': -30143, 'attributes': 56049},
            'max_byte1': 231,
            'max_char_or_byte2': 4746,
            'min_bounds': {'left_side_bearing': -13626, 'right_side_bearing': -17145, 'character_width': -16291, 'ascent': -2642, 'descent': -4827, 'attributes': 35063},
            'min_byte1': 188,
            'min_char_or_byte2': 12434,
            'properties': [{'name': 1568813755, 'value': 2137719486}],
            'sequence_number': 3542,
            }
        self.reply_bin_0 = b'\x01\x00\xd6\x0d' b'\x12\x00\x00\x00' \
            b'\xc6\xca\x07\xbd' b'\x5d\xc0\xae\xf5' \
            b'\x25\xed\xf7\x88' b'\x00\x00\x00\x00' \
            b'\x26\x94\x47\x87' b'\xfa\xfa\x00\xc1' \
            b'\x41\x8a\xf1\xda' b'\x00\x00\x00\x00' \
            b'\x92\x30\x8a\x12' b'\x54\x99\x01\x00' \
            b'\x91\xbc\xe7\x00' b'\x86\xf8\xf4\xf1' \
            b'\x03\x00\x00\x00' b'\xbb\x32\x82\x5d' \
            b'\xbe\x02\x6b\x7f' b'\x45\xe4\x23\xc7' \
            b'\xb8\xd4\xf4\xdb' b'\x4b\xbe\xa0\x28' \
            b'\x4e\x98\xfa\xa5' b'\xdd\x9b\xfe\xfb' \
            b'\x7c\x87\x45\x95' b'\x2c\xde\x66\xc5' \
            b'\xcd\x87\xbd\xdf' b'\x24\xa8\xa2\x0f'


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
            'font': 1223434172,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = b'\x30\x01\x04\x00' b'\xbc\x1f\xec\x48' \
            b'\x00\x66\x00\x6f' b'\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'draw_direction': 191,
            'font_ascent': -13287,
            'font_descent': -31466,
            'overall_ascent': -12473,
            'overall_descent': -30082,
            'overall_left': -735785526,
            'overall_right': -894056953,
            'overall_width': -1247205006,
            'sequence_number': 38196,
            }
        self.reply_bin_0 = b'\x01\xbf\x34\x95' b'\x00\x00\x00\x00' \
            b'\x19\xcc\x16\x85' b'\x47\xcf\x7e\x8a' \
            b'\x72\x29\xa9\xb5' b'\xca\xcd\x24\xd4' \
            b'\x07\xc6\xb5\xca' b'\x00\x00\x00\x00'


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
            'max_names': 37298,
            'pattern': 'bhazr',
            }
        self.req_bin_0 = b'\x31\x00\x04\x00' b'\xb2\x91\x05\x00' \
            b'\x62\x68\x61\x7a' b'\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 34517,
            }
        self.reply_bin_0 = b'\x01\x00\xd5\x86' b'\x05\x00\x00\x00' \
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
            'max_names': 20989,
            'pattern': 'bhazr2',
            }
        self.req_bin_0 = b'\x32\x00\x04\x00' b'\xfd\x51\x06\x00' \
            b'\x62\x68\x61\x7a' b'\x72\x32\x00\x00'

        self.reply_args_0 = {
            'all_chars_exist': 0,
            'default_char': 61580,
            'draw_direction': 146,
            'font_ascent': -30368,
            'font_descent': -15151,
            'max_bounds': {'left_side_bearing': -28480, 'right_side_bearing': -10759, 'character_width': -11617, 'ascent': -22938, 'descent': -17786, 'attributes': 20976},
            'max_byte1': 245,
            'max_char_or_byte2': 49530,
            'min_bounds': {'left_side_bearing': -10823, 'right_side_bearing': -9300, 'character_width': -22473, 'ascent': -24947, 'descent': -24065, 'attributes': 26194},
            'min_byte1': 130,
            'min_char_or_byte2': 61140,
            'name': 'fontfont',
            'properties': [{'name': 2007331946, 'value': 560055601}],
            'replies_hint': 457810933,
            'sequence_number': 13642,
            }
        self.reply_bin_0 = b'\x01\x08\x4a\x35' b'\x0b\x00\x00\x00' \
            b'\xb9\xd5\xac\xdb' b'\x37\xa8\x8d\x9e' \
            b'\xff\xa1\x52\x66' b'\x00\x00\x00\x00' \
            b'\xc0\x90\xf9\xd5' b'\x9f\xd2\x66\xa6' \
            b'\x86\xba\xf0\x51' b'\x00\x00\x00\x00' \
            b'\xd4\xee\x7a\xc1' b'\x8c\xf0\x01\x00' \
            b'\x92\x82\xf5\x00' b'\x60\x89\xd1\xc4' \
            b'\xf5\xa3\x49\x1b' b'\x6a\x74\xa5\x77' \
            b'\x31\xc5\x61\x21' b'\x66\x6f\x6e\x74' \
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
            'sequence_number': 33409,
            }
        self.reply_bin_0 = b'\x01\x00\x81\x82' b'\x04\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x05\x70\x61\x74' b'\x68\x31\x08\x70' \
            b'\x61\x74\x68\x32' b'\x32\x33\x32\x00'

        self.reply_args_1 = {
            'paths': [],
            'sequence_number': 17636,
            }
        self.reply_bin_1 = b'\x01\x00\xe4\x44' b'\x00\x00\x00\x00' \
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
            'depth': 161,
            'drawable': 749556300,
            'height': 4764,
            'pid': 2004224799,
            'width': 57984,
            }
        self.req_bin_0 = b'\x35\xa1\x04\x00' b'\x1f\x0b\x76\x77' \
            b'\x4c\x52\xad\x2c' b'\x80\xe2\x9c\x12'


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
            'pixmap': 1888284001,
            }
        self.req_bin_0 = b'\x36\x00\x02\x00' b'\x61\xed\x8c\x70'


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
            'attrs': {'function': 7, 'plane_mask': 793618921, 'foreground': 612071305, 'background': 338824284, 'line_width': 61484, 'line_style': 2, 'cap_style': 2, 'join_style': 2, 'fill_style': 0, 'fill_rule': 1, 'tile': 2000996399, 'stipple': 1424681955, 'tile_stipple_x_origin': -25980, 'tile_stipple_y_origin': -23968, 'font': 568001783, 'subwindow_mode': 0, 'graphics_exposures': 0, 'clip_x_origin': -22581, 'clip_y_origin': -14920, 'clip_mask': 605132525, 'dash_offset': 46571, 'dashes': 215, 'arc_mode': 0},
            'cid': 1476454377,
            'drawable': 1362081172,
            }
        self.req_bin_0 = b'\x37\x00\x1b\x00' b'\xe9\xe7\x00\x58' \
            b'\x94\xb5\x2f\x51' b'\xff\xff\x7f\x00' \
            b'\x07\x00\x00\x00' b'\xe9\xa9\x4d\x2f' \
            b'\x89\x77\x7b\x24' b'\x5c\x0c\x32\x14' \
            b'\x2c\xf0\x00\x00' b'\x02\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x2f\xc8\x44\x77' b'\xe3\xeb\xea\x54' \
            b'\x84\x9a\x00\x00' b'\x60\xa2\x00\x00' \
            b'\xf7\x04\xdb\x21' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\xcb\xa7\x00\x00' \
            b'\xb8\xc5\x00\x00' b'\xed\x96\x11\x24' \
            b'\xeb\xb5\x00\x00' b'\xd7\x00\x00\x00' \
            b'\x00\x00\x00\x00'


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
            'attrs': {'function': 8, 'plane_mask': 1085423224, 'foreground': 1049179696, 'background': 539344312, 'line_width': 36097, 'line_style': 0, 'cap_style': 3, 'join_style': 1, 'fill_style': 0, 'fill_rule': 0, 'tile': 716372747, 'stipple': 1656031462, 'tile_stipple_x_origin': -24195, 'tile_stipple_y_origin': -15601, 'font': 347060191, 'subwindow_mode': 1, 'graphics_exposures': 1, 'clip_x_origin': -32135, 'clip_y_origin': -25437, 'clip_mask': 161650480, 'dash_offset': 42536, 'dashes': 137, 'arc_mode': 1},
            'gc': 1250995304,
            }
        self.req_bin_0 = b'\x38\x00\x1a\x00' b'\x68\xac\x90\x4a' \
            b'\xff\xff\x7f\x00' b'\x08\x00\x00\x00' \
            b'\x78\x3e\xb2\x40' b'\x30\x36\x89\x3e' \
            b'\xb8\xbd\x25\x20' b'\x01\x8d\x00\x00' \
            b'\x00\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x01\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x0b\xfb\xb2\x2a' \
            b'\xe6\x08\xb5\x62' b'\x7d\xa1\x00\x00' \
            b'\x0f\xc3\x00\x00' b'\xdf\xb7\xaf\x14' \
            b'\x01\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x79\x82\x00\x00' b'\xa3\x9c\x00\x00' \
            b'\x30\x97\xa2\x09' b'\x28\xa6\x00\x00' \
            b'\x89\x00\x00\x00' b'\x01\x00\x00\x00'


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
            'dst_gc': 318094523,
            'mask': 923025483,
            'src_gc': 1186604145,
            }
        self.req_bin_0 = b'\x39\x00\x04\x00' b'\x71\x24\xba\x46' \
            b'\xbb\xbc\xf5\x12' b'\x4b\x40\x04\x37'


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
            'dash_offset': 51381,
            'dashes': [160, 138, 206, 221, 138, 219, 181, 191, 154],
            'gc': 759584613,
            }
        self.req_bin_0 = b'\x3a\x00\x06\x00' b'\x65\x57\x46\x2d' \
            b'\xb5\xc8\x09\x00' b'\xa0\x8a\xce\xdd' \
            b'\x8a\xdb\xb5\xbf' b'\x9a\x00\x00\x00'


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
            'gc': 1856792138,
            'ordering': 1,
            'rectangles': [{'x': -14422, 'y': -3797, 'width': 57581, 'height': 26888}, {'x': -858, 'y': -12431, 'width': 49373, 'height': 10384}],
            'x_origin': -27444,
            'y_origin': -780,
            }
        self.req_bin_0 = b'\x3b\x01\x07\x00' b'\x4a\x66\xac\x6e' \
            b'\xcc\x94\xf4\xfc' b'\xaa\xc7\x2b\xf1' \
            b'\xed\xe0\x08\x69' b'\xa6\xfc\x71\xcf' \
            b'\xdd\xc0\x90\x28'

        self.req_args_1 = {
            'gc': 1892892424,
            'ordering': 1,
            'rectangles': [],
            'x_origin': -19258,
            'y_origin': -31956,
            }
        self.req_bin_1 = b'\x3b\x01\x03\x00' b'\x08\x3f\xd3\x70' \
            b'\xc6\xb4\x2c\x83'


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
            'gc': 385239625,
            }
        self.req_bin_0 = b'\x3c\x00\x02\x00' b'\x49\x4a\xf6\x16'


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
            'height': 44159,
            'width': 52831,
            'window': 1680227732,
            'x': -2268,
            'y': -19277,
            }
        self.req_bin_0 = b'\x3d\x01\x04\x00' b'\x94\x3d\x26\x64' \
            b'\x24\xf7\xb3\xb4' b'\x5f\xce\x7f\xac'


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
            'dst_drawable': 1578589574,
            'dst_x': -27552,
            'dst_y': -6968,
            'gc': 1741136437,
            'height': 7340,
            'src_drawable': 1855628899,
            'src_x': -24637,
            'src_y': -24026,
            'width': 46214,
            }
        self.req_bin_0 = b'\x3e\x00\x07\x00' b'\x63\xa6\x9a\x6e' \
            b'\x86\x5d\x17\x5e' b'\x35\xa2\xc7\x67' \
            b'\xc3\x9f\x26\xa2' b'\x60\x94\xc8\xe4' \
            b'\x86\xb4\xac\x1c'


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
            'bit_plane': 988559210,
            'dst_drawable': 1873029448,
            'dst_x': -25480,
            'dst_y': -26229,
            'gc': 83225989,
            'height': 60447,
            'src_drawable': 821567629,
            'src_x': -4634,
            'src_y': -17345,
            'width': 53771,
            }
        self.req_bin_0 = b'\x3f\x00\x08\x00' b'\x8d\x20\xf8\x30' \
            b'\x48\x29\xa4\x6f' b'\x85\xed\xf5\x04' \
            b'\xe6\xed\x3f\xbc' b'\x78\x9c\x8b\x99' \
            b'\x0b\xd2\x1f\xec' b'\x6a\x37\xec\x3a'


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
            'coord_mode': 0,
            'drawable': 50884525,
            'gc': 1417476013,
            'points': [{'x': -21311, 'y': -22768}, {'x': -5881, 'y': -6707}, {'x': -4217, 'y': -25311}],
            }
        self.req_bin_0 = b'\x40\x00\x06\x00' b'\xad\x6f\x08\x03' \
            b'\xad\xf7\x7c\x54' b'\xc1\xac\x10\xa7' \
            b'\x07\xe9\xcd\xe5' b'\x87\xef\x21\x9d'


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
            'coord_mode': 1,
            'drawable': 1459319574,
            'gc': 2107068434,
            'points': [{'x': -26440, 'y': -19712}, {'x': -22012, 'y': -23639}, {'x': -4445, 'y': -30494}, {'x': -1085, 'y': -7428}, {'x': -23622, 'y': -21262}],
            }
        self.req_bin_0 = b'\x41\x01\x08\x00' b'\x16\x73\xfb\x56' \
            b'\x12\x50\x97\x7d' b'\xb8\x98\x00\xb3' \
            b'\x04\xaa\xa9\xa3' b'\xa3\xee\xe2\x88' \
            b'\xc3\xfb\xfc\xe2' b'\xba\xa3\xf2\xac'


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
            'drawable': 59337240,
            'gc': 247760051,
            'segments': [{'x1': -5123, 'y1': -15198, 'x2': -21917, 'y2': -1992}],
            }
        self.req_bin_0 = b'\x42\x00\x05\x00' b'\x18\x6a\x89\x03' \
            b'\xb3\x84\xc4\x0e' b'\xfd\xeb\xa2\xc4' \
            b'\x63\xaa\x38\xf8'


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
            'drawable': 742422946,
            'gc': 1564604140,
            'rectangles': [{'x': -4030, 'y': -970, 'width': 17374, 'height': 11958}, {'x': -13744, 'y': -1228, 'width': 64713, 'height': 17653}, {'x': -31515, 'y': -29216, 'width': 39352, 'height': 28735}],
            }
        self.req_bin_0 = b'\x43\x00\x09\x00' b'\xa2\x79\x40\x2c' \
            b'\xec\xf6\x41\x5d' b'\x42\xf0\x36\xfc' \
            b'\xde\x43\xb6\x2e' b'\x50\xca\x34\xfb' \
            b'\xc9\xfc\xf5\x44' b'\xe5\x84\xe0\x8d' \
            b'\xb8\x99\x3f\x70'


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
            'arcs': [{'x': -6999, 'y': -22490, 'width': 28855, 'height': 39984, 'angle1': -517, 'angle2': -16010}, {'x': -28979, 'y': -20146, 'width': 59205, 'height': 38043, 'angle1': -26540, 'angle2': -24422}, {'x': -31314, 'y': -9543, 'width': 28833, 'height': 366, 'angle1': -15732, 'angle2': -2439}],
            'drawable': 1732034432,
            'gc': 1156382390,
            }
        self.req_bin_0 = b'\x44\x00\x0c\x00' b'\x80\xbf\x3c\x67' \
            b'\xb6\xfe\xec\x44' b'\xa9\xe4\x26\xa8' \
            b'\xb7\x70\x30\x9c' b'\xfb\xfd\x76\xc1' \
            b'\xcd\x8e\x4e\xb1' b'\x45\xe7\x9b\x94' \
            b'\x54\x98\x9a\xa0' b'\xae\x85\xb9\xda' \
            b'\xa1\x70\x6e\x01' b'\x8c\xc2\x79\xf6'


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
            'drawable': 423195261,
            'gc': 782225195,
            'points': [{'x': -10262, 'y': -9194}, {'x': -1958, 'y': -8456}, {'x': -8617, 'y': -10793}],
            'shape': 1,
            }
        self.req_bin_0 = b'\x45\x00\x07\x00' b'\x7d\x72\x39\x19' \
            b'\x2b\xcf\x9f\x2e' b'\x01\x00\x00\x00' \
            b'\xea\xd7\x16\xdc' b'\x5a\xf8\xf8\xde' \
            b'\x57\xde\xd7\xd5'


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
            'drawable': 267696363,
            'gc': 1545726032,
            'rectangles': [{'x': -1676, 'y': -11003, 'width': 60599, 'height': 21895}, {'x': -12349, 'y': -22482, 'width': 43731, 'height': 55831}],
            }
        self.req_bin_0 = b'\x46\x00\x07\x00' b'\xeb\xb8\xf4\x0f' \
            b'\x50\xe8\x21\x5c' b'\x74\xf9\x05\xd5' \
            b'\xb7\xec\x87\x55' b'\xc3\xcf\x2e\xa8' \
            b'\xd3\xaa\x17\xda'


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
            'arcs': [{'x': -3276, 'y': -22928, 'width': 33490, 'height': 20525, 'angle1': -10916, 'angle2': -19386}],
            'drawable': 700537986,
            'gc': 864213787,
            }
        self.req_bin_0 = b'\x47\x00\x06\x00' b'\x82\x5c\xc1\x29' \
            b'\x1b\xdb\x82\x33' b'\x34\xf3\x70\xa6' \
            b'\xd2\x82\x2d\x50' b'\x5c\xd5\x46\xb4'


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
            'data': b'\xe9\x10\xf2o\x7f{\xae-\xe6\x18\xce\x83',
            'depth': 172,
            'drawable': 634980240,
            'dst_x': -18991,
            'dst_y': -10980,
            'format': 2,
            'gc': 1190657277,
            'height': 12828,
            'left_pad': 225,
            'width': 8597,
            }
        self.req_bin_0 = b'\x48\x02\x09\x00' b'\x90\x07\xd9\x25' \
            b'\xfd\xfc\xf7\x46' b'\x95\x21\x1c\x32' \
            b'\xd1\xb5\x1c\xd5' b'\xe1\xac\x00\x00' \
            b'\xe9\x10\xf2\x6f' b'\x7f\x7b\xae\x2d' \
            b'\xe6\x18\xce\x83'


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
            'drawable': 872105322,
            'format': 2,
            'height': 20170,
            'plane_mask': 616208054,
            'width': 282,
            'x': -14814,
            'y': -5449,
            }
        self.req_bin_0 = b'\x49\x02\x05\x00' b'\x6a\x45\xfb\x33' \
            b'\x22\xc6\xb7\xea' b'\x1a\x01\xca\x4e' \
            b'\xb6\x96\xba\x24'

        self.reply_args_0 = {
            'data': b'\xeb?:\xa7\xc6\x8b\xc2\x96o-S\xe6\xd6z6\x94\xd7v\xd2R.\xa2\xeaw\t\x13\x95\x85',
            'depth': 181,
            'sequence_number': 28429,
            'visual': 1687469773,
            }
        self.reply_bin_0 = b'\x01\xb5\x0d\x6f' b'\x07\x00\x00\x00' \
            b'\xcd\xbe\x94\x64' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xeb\x3f\x3a\xa7' b'\xc6\x8b\xc2\x96' \
            b'\x6f\x2d\x53\xe6' b'\xd6\x7a\x36\x94' \
            b'\xd7\x76\xd2\x52' b'\x2e\xa2\xea\x77' \
            b'\x09\x13\x95\x85'


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
            'drawable': 1245573363,
            'gc': 1302861330,
            'items': [{'delta': 2, 'string': 'zoo'}, 16909060, {'delta': 0, 'string': 'ie'}],
            'x': -11315,
            'y': -22209,
            }
        self.req_bin_0 = b'\x4a\x00\x08\x00' b'\xf3\xf0\x3d\x4a' \
            b'\x12\x16\xa8\x4d' b'\xcd\xd3\x3f\xa9' \
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
            'drawable': 998620068,
            'gc': 948793778,
            'items': [{'delta': 2, 'string': (4131, 18)}, 16909060],
            'x': -18280,
            'y': -10630,
            }
        self.req_bin_0 = b'\x4b\x00\x07\x00' b'\xa4\xbb\x85\x3b' \
            b'\xb2\x71\x8d\x38' b'\x98\xb8\x7a\xd6' \
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
            'drawable': 458985805,
            'gc': 1097803335,
            'string': 'showme',
            'x': -17263,
            'y': -6759,
            }
        self.req_bin_0 = b'\x4c\x06\x06\x00' b'\x4d\x91\x5b\x1b' \
            b'\x47\x26\x6f\x41' b'\x91\xbc\x99\xe5' \
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
            'drawable': 1935336610,
            'gc': 2061289059,
            'string': (115, 104, 111, 119, 109, 111, 114, 101),
            'x': -6684,
            'y': -8653,
            }
        self.req_bin_0 = b'\x4d\x08\x08\x00' b'\xa2\xe4\x5a\x73' \
            b'\x63\xc6\xdc\x7a' b'\xe4\xe5\x33\xde' \
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
            'alloc': 0,
            'mid': 1414936748,
            'visual': 609492200,
            'window': 182162564,
            }
        self.req_bin_0 = b'\x4e\x00\x04\x00' b'\xac\x38\x56\x54' \
            b'\x84\x94\xdb\x0a' b'\xe8\x1c\x54\x24'


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
            'cmap': 1106990292,
            }
        self.req_bin_0 = b'\x4f\x00\x02\x00' b'\xd4\x54\xfb\x41'


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
            'mid': 1425680795,
            'src_cmap': 1359295675,
            }
        self.req_bin_0 = b'\x50\x00\x03\x00' b'\x9b\x29\xfa\x54' \
            b'\xbb\x34\x05\x51'


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
            'cmap': 1329917990,
            }
        self.req_bin_0 = b'\x51\x00\x02\x00' b'\x26\xf0\x44\x4f'


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
            'cmap': 719876845,
            }
        self.req_bin_0 = b'\x52\x00\x02\x00' b'\xed\x72\xe8\x2a'


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
            'window': 200613013,
            }
        self.req_bin_0 = b'\x53\x00\x02\x00' b'\x95\x1c\xf5\x0b'

        self.reply_args_0 = {
            'cmaps': [1757616530, 2044469232],
            'sequence_number': 49482,
            }
        self.reply_bin_0 = b'\x01\x00\x4a\xc1' b'\x02\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x92\x19\xc3\x68' b'\xf0\x1f\xdc\x79'


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
            'blue': 14978,
            'cmap': 504442007,
            'green': 20599,
            'red': 44348,
            }
        self.req_bin_0 = b'\x54\x00\x04\x00' b'\x97\x2c\x11\x1e' \
            b'\x3c\xad\x77\x50' b'\x82\x3a\x00\x00'

        self.reply_args_0 = {
            'blue': 1856,
            'green': 9912,
            'pixel': 99308744,
            'red': 13306,
            'sequence_number': 53114,
            }
        self.reply_bin_0 = b'\x01\x00\x7a\xcf' b'\x00\x00\x00\x00' \
            b'\xfa\x33\xb8\x26' b'\x40\x07\x00\x00' \
            b'\xc8\x54\xeb\x05' b'\x00\x00\x00\x00' \
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
            'cmap': 525860889,
            'name': 'octarin',
            }
        self.req_bin_0 = b'\x55\x00\x05\x00' b'\x19\x00\x58\x1f' \
            b'\x07\x00\x00\x00' b'\x6f\x63\x74\x61' \
            b'\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'exact_blue': 50619,
            'exact_green': 55944,
            'exact_red': 40316,
            'pixel': 1020413057,
            'screen_blue': 27416,
            'screen_green': 30102,
            'screen_red': 5028,
            'sequence_number': 64739,
            }
        self.reply_bin_0 = b'\x01\x00\xe3\xfc' b'\x00\x00\x00\x00' \
            b'\x81\x44\xd2\x3c' b'\x7c\x9d\x88\xda' \
            b'\xbb\xc5\xa4\x13' b'\x96\x75\x18\x6b' \
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
            'cmap': 1542701632,
            'colors': 45892,
            'contiguous': 0,
            'planes': 25420,
            }
        self.req_bin_0 = b'\x56\x00\x03\x00' b'\x40\xc2\xf3\x5b' \
            b'\x44\xb3\x4c\x63'

        self.reply_args_0 = {
            'masks': [1726878301, 2057281944, 1494524694],
            'pixels': [1061732426, 858313521, 524018138, 316972578, 1408939380, 1476723430, 11972931, 1917037904, 1612749468, 1847847580, 1653727126, 1901587588, 228960010, 1671710636, 913060041, 470023299, 377779303],
            'sequence_number': 34200,
            }
        self.reply_bin_0 = b'\x01\x00\x98\x85' b'\x14\x00\x00\x00' \
            b'\x11\x00\x03\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x4a\xc0\x48\x3f' b'\x31\xd3\x28\x33' \
            b'\xda\xe1\x3b\x1f' b'\x22\x9e\xe4\x12' \
            b'\x74\xb5\xfa\x53' b'\xe6\x02\x05\x58' \
            b'\x43\xb1\xb6\x00' b'\x50\xad\x43\x72' \
            b'\x9c\x9a\x20\x60' b'\x9c\xea\x23\x6e' \
            b'\x96\xdf\x91\x62' b'\x84\xec\x57\x71' \
            b'\x0a\xa7\xa5\x0d' b'\xac\x47\xa4\x63' \
            b'\xc9\x30\x6c\x36' b'\x83\xfc\x03\x1c' \
            b'\x67\x74\x84\x16' b'\x5d\x12\xee\x66' \
            b'\x98\xa1\x9f\x7a' b'\x16\xa3\x14\x59'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 30700,
            }
        self.reply_bin_1 = b'\x01\x00\xec\x77' b'\x00\x00\x00\x00' \
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
            'blue': 8209,
            'cmap': 1197085372,
            'colors': 16587,
            'contiguous': 0,
            'green': 55852,
            'red': 60383,
            }
        self.req_bin_0 = b'\x57\x00\x04\x00' b'\xbc\x12\x5a\x47' \
            b'\xcb\x40\xdf\xeb' b'\x2c\xda\x11\x20'

        self.reply_args_0 = {
            'blue_mask': 1200348460,
            'green_mask': 2121548418,
            'pixels': [980309855, 286409072, 1721094583, 997879295],
            'red_mask': 1140662566,
            'sequence_number': 44006,
            }
        self.reply_bin_0 = b'\x01\x00\xe6\xab' b'\x04\x00\x00\x00' \
            b'\x04\x00\x00\x00' b'\x26\x21\xfd\x43' \
            b'\x82\x42\x74\x7e' b'\x2c\xdd\x8b\x47' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x5f\x57\x6e\x3a' b'\x70\x41\x12\x11' \
            b'\xb7\xd1\x95\x66' b'\xff\x6d\x7a\x3b'


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
            'cmap': 341854532,
            'pixels': [1278789650, 681457705, 2040260049, 1621952585, 1914388136, 950484730, 1315726377, 1750278681, 1544694596, 1915664535, 1084068385, 916484334, 1783699241, 1947521244, 1176611597, 957657715, 1926805276],
            'plane_mask': 1597053435,
            }
        self.req_bin_0 = b'\x58\x00\x14\x00' b'\x44\x49\x60\x14' \
            b'\xfb\x19\x31\x5f' b'\x12\xc8\x38\x4c' \
            b'\x29\x38\x9e\x28' b'\xd1\xe5\x9b\x79' \
            b'\x49\x08\xad\x60' b'\xa8\x3e\x1b\x72' \
            b'\xfa\x3e\xa7\x38' b'\x29\x64\x6c\x4e' \
            b'\x19\x22\x53\x68' b'\x44\x2b\x12\x5c' \
            b'\x97\xb8\x2e\x72' b'\x21\x92\x9d\x40' \
            b'\xee\x70\xa0\x36' b'\x29\x17\x51\x6a' \
            b'\xdc\xd0\x14\x74' b'\x0d\xab\x21\x46' \
            b'\x73\xb2\x14\x39' b'\x1c\xb7\xd8\x72'


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
            'cmap': 686636594,
            'items': [{'pixel': 1850111768, 'red': 31364, 'green': 29751, 'blue': 17242, 'flags': 191}, {'pixel': 1803657350, 'red': 42045, 'green': 18429, 'blue': 50444, 'flags': 252}, {'pixel': 1345997556, 'red': 15935, 'green': 18252, 'blue': 29083, 'flags': 147}, {'pixel': 1532391469, 'red': 18981, 'green': 15623, 'blue': 18063, 'flags': 213}],
            }
        self.req_bin_0 = b'\x59\x00\x0e\x00' b'\x32\x3e\xed\x28' \
            b'\x18\x77\x46\x6e' b'\x84\x7a\x37\x74' \
            b'\x5a\x43\xbf\x00' b'\x86\xa0\x81\x6b' \
            b'\x3d\xa4\xfd\x47' b'\x0c\xc5\xfc\x00' \
            b'\xf4\x4a\x3a\x50' b'\x3f\x3e\x4c\x47' \
            b'\x9b\x71\x93\x00' b'\x2d\x70\x56\x5b' \
            b'\x25\x4a\x07\x3d' b'\x8f\x46\xd5\x00'


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
            'cmap': 297221571,
            'flags': 148,
            'name': 'blue',
            'pixel': 323971915,
            }
        self.req_bin_0 = b'\x5a\x94\x05\x00' b'\xc3\x3d\xb7\x11' \
            b'\x4b\x6b\x4f\x13' b'\x04\x00\x00\x00' \
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
            'cmap': 875378525,
            'pixels': [496695788, 822627561, 1490311416, 328212337, 1517089095, 459525846, 137995944, 890987562],
            }
        self.req_bin_0 = b'\x5b\x00\x0a\x00' b'\x5d\x37\x2d\x34' \
            b'\xec\xf9\x9a\x1d' b'\xe9\x4c\x08\x31' \
            b'\xf8\x58\xd4\x58' b'\x71\x1f\x90\x13' \
            b'\x47\xf1\x6c\x5a' b'\xd6\xce\x63\x1b' \
            b'\xa8\xa6\x39\x08' b'\x2a\x64\x1b\x35'

        self.reply_args_0 = {
            'colors': [{'red': 35816, 'green': 30790, 'blue': 27504}, {'red': 4336, 'green': 13811, 'blue': 54840}, {'red': 27790, 'green': 25780, 'blue': 59555}, {'red': 50705, 'green': 38534, 'blue': 62257}, {'red': 45837, 'green': 1536, 'blue': 56402}],
            'sequence_number': 57970,
            }
        self.reply_bin_0 = b'\x01\x00\x72\xe2' b'\x0a\x00\x00\x00' \
            b'\x05\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xe8\x8b\x46\x78' b'\x70\x6b\x00\x00' \
            b'\xf0\x10\xf3\x35' b'\x38\xd6\x00\x00' \
            b'\x8e\x6c\xb4\x64' b'\xa3\xe8\x00\x00' \
            b'\x11\xc6\x86\x96' b'\x31\xf3\x00\x00' \
            b'\x0d\xb3\x00\x06' b'\x52\xdc\x00\x00'

        self.req_args_1 = {
            'cmap': 710627905,
            'pixels': [],
            }
        self.req_bin_1 = b'\x5b\x00\x02\x00' b'\x41\x52\x5b\x2a'


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
            'cmap': 1644167361,
            'name': 'octarin',
            }
        self.req_bin_0 = b'\x5c\x00\x05\x00' b'\xc1\x00\x00\x62' \
            b'\x07\x00\x00\x00' b'\x6f\x63\x74\x61' \
            b'\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'exact_blue': 642,
            'exact_green': 31515,
            'exact_red': 25184,
            'screen_blue': 19825,
            'screen_green': 23308,
            'screen_red': 62039,
            'sequence_number': 37984,
            }
        self.reply_bin_0 = b'\x01\x00\x60\x94' b'\x00\x00\x00\x00' \
            b'\x60\x62\x1b\x7b' b'\x82\x02\x57\xf2' \
            b'\x0c\x5b\x71\x4d' b'\x00\x00\x00\x00' \
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
            'back_blue': 49245,
            'back_green': 35528,
            'back_red': 27716,
            'cid': 1618141054,
            'fore_blue': 55026,
            'fore_green': 62740,
            'fore_red': 58690,
            'mask': 1832831050,
            'source': 837555484,
            'x': 48400,
            'y': 36047,
            }
        self.req_bin_0 = b'\x5d\x00\x08\x00' b'\x7e\xdf\x72\x60' \
            b'\x1c\x15\xec\x31' b'\x4a\xc8\x3e\x6d' \
            b'\x42\xe5\x14\xf5' b'\xf2\xd6\x44\x6c' \
            b'\xc8\x8a\x5d\xc0' b'\x10\xbd\xcf\x8c'


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
            'back_blue': 25740,
            'back_green': 2158,
            'back_red': 32083,
            'cid': 1717769345,
            'fore_blue': 28818,
            'fore_green': 18143,
            'fore_red': 14636,
            'mask': 1928100723,
            'mask_char': 32252,
            'source': 1295540602,
            'source_char': 14709,
            }
        self.req_bin_0 = b'\x5e\x00\x08\x00' b'\x81\x14\x63\x66' \
            b'\x7a\x61\x38\x4d' b'\x73\x7b\xec\x72' \
            b'\x75\x39\xfc\x7d' b'\x2c\x39\xdf\x46' \
            b'\x92\x70\x53\x7d' b'\x6e\x08\x8c\x64'


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
            'cursor': 721898231,
            }
        self.req_bin_0 = b'\x5f\x00\x02\x00' b'\xf7\x4a\x07\x2b'


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
            'back_blue': 55339,
            'back_green': 11072,
            'back_red': 47715,
            'cursor': 1436460699,
            'fore_blue': 26753,
            'fore_green': 52563,
            'fore_red': 44764,
            }
        self.req_bin_0 = b'\x60\x00\x05\x00' b'\x9b\xa6\x9e\x55' \
            b'\xdc\xae\x53\xcd' b'\x81\x68\x63\xba' \
            b'\x40\x2b\x2b\xd8'


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
            'drawable': 1974766133,
            'height': 64528,
            'item_class': 1,
            'width': 8620,
            }
        self.req_bin_0 = b'\x61\x01\x03\x00' b'\x35\x8a\xb4\x75' \
            b'\xac\x21\x10\xfc'

        self.reply_args_0 = {
            'height': 2023,
            'sequence_number': 41036,
            'width': 35260,
            }
        self.reply_bin_0 = b'\x01\x00\x4c\xa0' b'\x00\x00\x00\x00' \
            b'\xbc\x89\xe7\x07' b'\x00\x00\x00\x00' \
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
            'first_error': 237,
            'first_event': 149,
            'major_opcode': 134,
            'present': 1,
            'sequence_number': 59692,
            }
        self.reply_bin_0 = b'\x01\x00\x2c\xe9' b'\x00\x00\x00\x00' \
            b'\x01\x86\x95\xed' b'\x00\x00\x00\x00' \
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
            'sequence_number': 9149,
            }
        self.reply_bin_0 = b'\x01\x02\xbd\x23' b'\x04\x00\x00\x00' \
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
            'first_keycode': 157,
            'keysyms': [[1861549105, 991489870, 390260112], [107985429, 558681426, 814119353], [702984500, 454537006, 976459372], [701896028, 724776911, 1634728346], [1889012491, 814167346, 597551532], [1614928797, 2042695294, 1786543801], [905303576, 541748982, 1792957544], [175892294, 1009976242, 41625283], [1608517348, 1158393599, 111852976], [2147285698, 2044231981, 751534113], [481513427, 1396173819, 147356828], [1677685199, 2055755177, 1399632465], [86453688, 1619703478, 66636412], [2039275666, 531036848, 428123802], [1802230236, 43765755, 1334308166], [327238597, 512271361, 271057482], [1016964633, 1437651928, 245649464], [1211115441, 2035292716, 468075293], [998652876, 1502089592, 550279151], [1646901134, 792196355, 360324443]],
            }
        self.req_bin_0 = b'\x64\x14\x3e\x00' b'\x9d\x03\x00\x00' \
            b'\x31\xfc\xf4\x6e' b'\x4e\xef\x18\x3b' \
            b'\x90\xe5\x42\x17' b'\x15\xba\x6f\x06' \
            b'\x52\xcd\x4c\x21' b'\xb9\x79\x86\x30' \
            b'\x34\xb1\xe6\x29' b'\x2e\xaf\x17\x1b' \
            b'\x6c\x96\x33\x3a' b'\x5c\x15\xd6\x29' \
            b'\xcf\x37\x33\x2b' b'\x9a\xf9\x6f\x61' \
            b'\x0b\x0b\x98\x70' b'\x32\x35\x87\x30' \
            b'\xac\xe9\x9d\x23' b'\x9d\xdb\x41\x60' \
            b'\x7e\x0e\xc1\x79' b'\xb9\x7e\x7c\x6a' \
            b'\x18\xd6\xf5\x35' b'\xf6\x6e\x4a\x20' \
            b'\x68\x5c\xde\x6a' b'\x46\xe7\x7b\x0a' \
            b'\xb2\x03\x33\x3c' b'\xc3\x26\x7b\x02' \
            b'\xe4\x06\xe0\x5f' b'\xff\xae\x0b\x45' \
            b'\xb0\xbd\xaa\x06' b'\xc2\xfa\xfc\x7f' \
            b'\x2d\x81\xd8\x79' b'\x21\x80\xcb\x2c' \
            b'\xd3\x4f\xb3\x1c' b'\xfb\xeb\x37\x53' \
            b'\x9c\x7c\xc8\x08' b'\xcf\x71\xff\x63' \
            b'\xa9\x55\x88\x7a' b'\x51\xb2\x6c\x53' \
            b'\xb8\x2d\x27\x05' b'\xb6\xb6\x8a\x60' \
            b'\x7c\xca\xf8\x03' b'\x92\xe0\x8c\x79' \
            b'\xb0\xfa\xa6\x1f' b'\x9a\xa6\x84\x19' \
            b'\xdc\xd9\x6b\x6b' b'\xfb\xcf\x9b\x02' \
            b'\x46\xed\x87\x4f' b'\xc5\x43\x81\x13' \
            b'\x01\xa4\x88\x1e' b'\x4a\x02\x28\x10' \
            b'\x19\xa6\x9d\x3c' b'\xd8\xd3\xb0\x55' \
            b'\x38\x50\xa4\x0e' b'\xb1\x27\x30\x48' \
            b'\x2c\x1a\x50\x79' b'\x1d\x43\xe6\x1b' \
            b'\xcc\x3b\x86\x3b' b'\x78\x11\x88\x59' \
            b'\xef\x97\xcc\x20' b'\x8e\xb7\x29\x62' \
            b'\x03\xf5\x37\x2f' b'\x5b\x1d\x7a\x15'


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
            'count': 207,
            'first_keycode': 169,
            }
        self.req_bin_0 = b'\x65\x00\x02\x00' b'\xa9\xcf\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[232140298, 1242716010, 55143985], [1994770011, 669923085, 1236514049], [1454592222, 1949971307, 2057660497], [805965556, 851808913, 2021792706], [1535482384, 425909956, 163201187], [1271520474, 1483083165, 1783638995], [1346992789, 521515080, 218831382], [1497210568, 1658890074, 647643874], [1825990828, 1469435098, 1289374120], [1729858135, 259963764, 1709884923], [2112789657, 1215330896, 1680696611], [88195295, 745614404, 1144061708], [919934772, 1420606257, 795794911], [148083460, 1086542523, 1390588550], [732788374, 27170279, 1824449766], [902069278, 1765942198, 1052700150], [226642993, 930984408, 2063275595], [777792886, 1364908620, 1914642756], [1779635393, 987282730, 1518933756], [328545991, 935201525, 378251236]],
            'sequence_number': 48346,
            }
        self.reply_bin_0 = b'\x01\x03\xda\xbc' b'\x3c\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x0a\x2e\xd6\x0d' b'\x6a\x57\x12\x4a' \
            b'\x31\x6e\x49\x03' b'\x5b\xc6\xe5\x76' \
            b'\x0d\x37\xee\x27' b'\x01\xb5\xb3\x49' \
            b'\xde\x50\xb3\x56' b'\x6b\x33\x3a\x74' \
            b'\x51\x68\xa5\x7a' b'\xf4\x0e\x0a\x30' \
            b'\x91\x92\xc5\x32' b'\xc2\x1b\x82\x78' \
            b'\x10\x9a\x85\x5b' b'\xc4\xde\x62\x19' \
            b'\xa3\x40\xba\x09' b'\xda\xdc\xc9\x4b' \
            b'\x9d\x0d\x66\x58' b'\xd3\x2b\x50\x6a' \
            b'\x95\x7a\x49\x50' b'\x48\xb0\x15\x1f' \
            b'\x16\x1a\x0b\x0d' b'\xc8\x9e\x3d\x59' \
            b'\x5a\xa7\xe0\x62' b'\xe2\x42\x9a\x26' \
            b'\xac\x68\xd6\x6c' b'\xda\xcc\x95\x57' \
            b'\xa8\x49\xda\x4c' b'\x57\x8a\x1b\x67' \
            b'\x74\xbb\x7e\x0f' b'\xfb\xc5\xea\x65' \
            b'\x99\x9c\xee\x7d' b'\x50\x7a\x70\x48' \
            b'\x23\x65\x2d\x64' b'\xdf\xc0\x41\x05' \
            b'\x44\x2c\x71\x2c' b'\x0c\xff\x30\x44' \
            b'\x34\x17\xd5\x36' b'\x31\xbb\xac\x54' \
            b'\xdf\xdd\x6e\x2f' b'\x04\x93\xd3\x08' \
            b'\xbb\x52\xc3\x40' b'\x86\xb2\xe2\x52' \
            b'\x96\x76\xad\x2b' b'\xe7\x95\x9e\x01' \
            b'\xe6\xe4\xbe\x6c' b'\x1e\x7c\xc4\x35' \
            b'\xb6\x23\x42\x69' b'\xf6\xed\xbe\x3e' \
            b'\x31\x4c\x82\x0d' b'\xd8\xb1\x7d\x37' \
            b'\x4b\x16\xfb\x7a' b'\x76\x2d\x5c\x2e' \
            b'\x4c\xda\x5a\x51' b'\x44\x21\x1f\x72' \
            b'\xc1\x14\x13\x6a' b'\x2a\xbd\xd8\x3a' \
            b'\xfc\x16\x89\x5a' b'\xc7\x36\x95\x13' \
            b'\xf5\x0a\xbe\x37' b'\xe4\xa7\x8b\x16'


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
            'attrs': {'key_click_percent': -59, 'bell_percent': -5, 'bell_pitch': -2303, 'bell_duration': -4223, 'led': 196, 'led_mode': 1, 'key': 190, 'auto_repeat_mode': 0},
            }
        self.req_bin_0 = b'\x66\x00\x0a\x00' b'\xff\x00\x00\x00' \
            b'\xc5\x00\x00\x00' b'\xfb\x00\x00\x00' \
            b'\x01\xf7\x00\x00' b'\x81\xef\x00\x00' \
            b'\xc4\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\xbe\x00\x00\x00' b'\x00\x00\x00\x00'


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
            'auto_repeats': [199, 243, 190, 246, 225, 214, 135, 254, 211, 174, 252, 182, 218, 194, 215, 199, 198, 130, 176, 149, 189, 232, 253, 189, 249, 253, 242, 132, 151, 203, 184, 231],
            'bell_duration': 35050,
            'bell_percent': 249,
            'bell_pitch': 36528,
            'global_auto_repeat': 0,
            'key_click_percent': 222,
            'led_mask': 1425908825,
            'sequence_number': 20323,
            }
        self.reply_bin_0 = b'\x01\x00\x63\x4f' b'\x05\x00\x00\x00' \
            b'\x59\xa4\xfd\x54' b'\xde\xf9\xb0\x8e' \
            b'\xea\x88\x00\x00' b'\xc7\xf3\xbe\xf6' \
            b'\xe1\xd6\x87\xfe' b'\xd3\xae\xfc\xb6' \
            b'\xda\xc2\xd7\xc7' b'\xc6\x82\xb0\x95' \
            b'\xbd\xe8\xfd\xbd' b'\xf9\xfd\xf2\x84' \
            b'\x97\xcb\xb8\xe7'


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
            'percent': -40,
            }
        self.req_bin_0 = b'\x68\xd8\x01\x00'


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
            'accel_denum': -8326,
            'accel_num': -18826,
            'do_accel': 1,
            'do_thresh': 1,
            'threshold': -14733,
            }
        self.req_bin_0 = b'\x69\x00\x03\x00' b'\x76\xb6\x7a\xdf' \
            b'\x73\xc6\x01\x01'


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
            'accel_denom': 18010,
            'accel_num': 29992,
            'sequence_number': 46318,
            'threshold': 20350,
            }
        self.reply_bin_0 = b'\x01\x00\xee\xb4' b'\x00\x00\x00\x00' \
            b'\x28\x75\x5a\x46' b'\x7e\x4f\x00\x00' \
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
            'interval': -25214,
            'prefer_blank': 0,
            'timeout': -24531,
            }
        self.req_bin_0 = b'\x6b\x00\x03\x00' b'\x2d\xa0\x82\x9d' \
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
            'allow_exposures': 0,
            'interval': 8091,
            'prefer_blanking': 0,
            'sequence_number': 12877,
            'timeout': 20935,
            }
        self.reply_bin_0 = b'\x01\x00\x4d\x32' b'\x00\x00\x00\x00' \
            b'\xc7\x51\x9b\x1f' b'\x00\x00\x00\x00' \
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
            'host': [183, 251, 198, 200],
            'host_family': 0,
            'mode': 0,
            }
        self.req_bin_0 = b'\x6d\x00\x03\x00' b'\x00\x00\x04\x00' \
            b'\xb7\xfb\xc6\xc8'


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
            'hosts': [{'family': 0, 'name': [34, 23, 178, 12]}, {'family': 0, 'name': [130, 236, 254, 15]}],
            'mode': 1,
            'sequence_number': 15164,
            }
        self.reply_bin_0 = b'\x01\x01\x3c\x3b' b'\x04\x00\x00\x00' \
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
            'resource': 649180254,
            }
        self.req_bin_0 = b'\x71\x00\x02\x00' b'\x5e\xb4\xb1\x26'


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
            'delta': -11867,
            'properties': [30448914, 1520523655, 1147111912, 271900374, 589144637, 97809756, 2092347973, 117159267, 1188394866, 627424198, 1497757970, 2027482546],
            'window': 271248673,
            }
        self.req_bin_0 = b'\x72\x00\x0f\x00' b'\x21\xed\x2a\x10' \
            b'\x0c\x00\xa5\xd1' b'\x12\x9d\xd0\x01' \
            b'\x87\x59\xa1\x5a' b'\xe8\x89\x5f\x44' \
            b'\xd6\xde\x34\x10' b'\x3d\xa2\x1d\x23' \
            b'\x5c\x75\xd4\x05' b'\x45\xb2\xb6\x7c' \
            b'\x63\xb5\xfb\x06' b'\x72\x77\xd5\x46' \
            b'\xc6\xbb\x65\x25' b'\x12\xf9\x45\x59' \
            b'\xb2\xed\xd8\x78'


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
            'mode': 1,
            }
        self.req_bin_0 = b'\x73\x01\x01\x00'


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
            'map': [154, 131, 200, 248, 250],
            }
        self.req_bin_0 = b'\x74\x05\x03\x00' b'\x9a\x83\xc8\xf8' \
            b'\xfa\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 22584,
            'status': 240,
            }
        self.reply_bin_0 = b'\x01\xf0\x38\x58' b'\x00\x00\x00\x00' \
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
            'map': [175, 141, 192, 250, 157],
            'sequence_number': 54134,
            }
        self.reply_bin_0 = b'\x01\x05\x76\xd3' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xaf\x8d\xc0\xfa' b'\x9d\x00\x00\x00'


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
            'keycodes': [[33, 205], [251, 37], [27, 77], [76, 155], [43, 127], [60, 213], [115, 194], [230, 226]],
            }
        self.req_bin_0 = b'\x76\x02\x05\x00' b'\x21\xcd\xfb\x25' \
            b'\x1b\x4d\x4c\x9b' b'\x2b\x7f\x3c\xd5' \
            b'\x73\xc2\xe6\xe2'

        self.reply_args_0 = {
            'sequence_number': 56627,
            'status': 204,
            }
        self.reply_bin_0 = b'\x01\xcc\x33\xdd' b'\x00\x00\x00\x00' \
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
            'keycodes': [[219, 156], [30, 50], [106, 108], [135, 41], [80, 122], [88, 38], [80, 1], [209, 230]],
            'sequence_number': 45434,
            }
        self.reply_bin_0 = b'\x01\x02\x7a\xb1' b'\x04\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xdb\x9c\x1e\x32' b'\x6a\x6c\x87\x29' \
            b'\x50\x7a\x58\x26' b'\x50\x01\xd1\xe6'


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
