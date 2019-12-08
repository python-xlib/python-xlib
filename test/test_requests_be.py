#!/usr/bin/env python2

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(__file__, '../..')))

import unittest
from Xlib.protocol import request, event
from . import BigEndianTest as EndianTest
from . import DummyDisplay

dummy_display = DummyDisplay()


class TestCreateWindow(EndianTest):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'cursor': 64054583, 'override_redirect': 0, 'bit_gravity': 3, 'event_mask': 1268138548, 'border_pixel': 1592533117, 'background_pixel': 239147199, 'save_under': 0, 'colormap': 68318329, 'do_not_propagate_mask': 906135756, 'backing_store': 0, 'win_gravity': 2, 'backing_planes': 299720948, 'border_pixmap': 53775720, 'backing_pixel': 1581625428, 'background_pixmap': 1373224142},
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
        self.req_bin_0 = b'\x01\x97\x00\x17' b'\x1b\xfd\x54\x45' \
            b'\x1d\xc8\xd5\x0c' b'\xc0\xaf\xcd\x0e' \
            b'\x07\xcb\x90\xad' b'\x33\xe7\x00\x02' \
            b'\x53\x30\x69\xc4' b'\x00\x00\x7f\xff' \
            b'\x51\xd9\xbc\xce' b'\x0e\x41\x18\xbf' \
            b'\x03\x34\x8d\x68' b'\x5e\xec\x20\x7d' \
            b'\x03\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x11\xdd\x60\xf4' \
            b'\x5e\x45\xb0\x54' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x4b\x96\x42\x34' \
            b'\x36\x02\x88\xcc' b'\x04\x12\x74\x79' \
            b'\x03\xd1\x65\x37'


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
            'attrs': {'cursor': 596789700, 'override_redirect': 0, 'bit_gravity': 6, 'event_mask': 1499308477, 'border_pixel': 473458160, 'background_pixel': 1170318459, 'save_under': 0, 'colormap': 730747963, 'do_not_propagate_mask': 907623048, 'backing_store': 1, 'win_gravity': 8, 'backing_planes': 1738304197, 'border_pixmap': 900977490, 'backing_pixel': 1866873765, 'background_pixmap': 1506149446},
            'window': 333955224,
            }
        self.req_bin_0 = b'\x02\x00\x00\x12' b'\x13\xe7\xc0\x98' \
            b'\x00\x00\x7f\xff' b'\x59\xc6\x04\x46' \
            b'\x45\xc1\xa4\x7b' b'\x35\xb3\xd3\x52' \
            b'\x1c\x38\x65\xf0' b'\x06\x00\x00\x00' \
            b'\x08\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x67\x9c\x6a\xc5' b'\x6f\x46\x3b\xa5' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x59\x5d\xa1\xbd' b'\x36\x19\x3a\x88' \
            b'\x2b\x8e\x54\x3b' b'\x23\x92\x49\xc4'


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
        self.req_bin_0 = b'\x03\x00\x00\x02' b'\x1b\x90\x66\xbd'

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
        self.reply_bin_0 = b'\x01\xd6\x1b\x2a' b'\x00\x00\x00\x03' \
            b'\x0b\xe0\x18\x88' b'\x62\x42\x98\xdb' \
            b'\x6c\x7b\xb2\x09' b'\x2c\x07\xbd\xb8' \
            b'\x01\x00\xf5\x00' b'\x7c\x90\x0e\xa6' \
            b'\x76\x0e\xc6\x50' b'\x30\x74\xd0\x89' \
            b'\x15\x2c\x00\x00'


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
        self.req_bin_0 = b'\x04\x00\x00\x02' b'\x46\xaa\x44\x78'


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
        self.req_bin_0 = b'\x05\x00\x00\x02' b'\x25\x87\xdd\xa0'


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
        self.req_bin_0 = b'\x06\x01\x00\x02' b'\x49\xe7\xac\xdf'


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
        self.req_bin_0 = b'\x07\x00\x00\x04' b'\x18\x9d\xe9\x96' \
            b'\x5a\x30\x68\xf8' b'\x88\xe7\x85\xdd'


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
        self.req_bin_0 = b'\x08\x00\x00\x02' b'\x54\xa5\x46\xcc'


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
        self.req_bin_0 = b'\x09\x00\x00\x02' b'\x1d\x2c\xc5\x47'


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
        self.req_bin_0 = b'\x0a\x00\x00\x02' b'\x62\xf4\xe7\x45'


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
        self.req_bin_0 = b'\x0b\x00\x00\x02' b'\x25\x0b\xaa\x26'


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
            'attrs': {'width': 39387, 'stack_mode': 2, 'height': 57679, 'sibling': 973756745, 'y': -17512, 'x': -27539, 'border_width': -14551},
            'window': 349362548,
            }
        self.req_bin_0 = b'\x0c\x00\x00\x0a' b'\x14\xd2\xd9\x74' \
            b'\x00\x7f\x00\x00' b'\x94\x6d\x00\x00' \
            b'\xbb\x98\x00\x00' b'\x99\xdb\x00\x00' \
            b'\xe1\x4f\x00\x00' b'\xc7\x29\x00\x00' \
            b'\x3a\x0a\x59\x49' b'\x02\x00\x00\x00'


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
        self.req_bin_0 = b'\x0d\x01\x00\x02' b'\x2d\x7a\x82\xa9'


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
        self.req_bin_0 = b'\x0e\x00\x00\x02' b'\x1a\xd2\x20\x57'

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
        self.reply_bin_0 = b'\x01\xc4\xb4\xaa' b'\x00\x00\x00\x00' \
            b'\x77\xe5\x4c\x24' b'\xd7\x7e\xd2\xf2' \
            b'\x13\x47\x9c\xf0' b'\xa3\x8d\x00\x00' \
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
        self.req_bin_0 = b'\x0f\x00\x00\x02' b'\x15\xe8\xdf\x00'

        self.reply_args_0 = {
            'children': [1147122179, 1565853418, 525792997, 350969719, 992761785, 814939899, 579774073],
            'parent': 1374454548,
            'root': 1987327953,
            'sequence_number': 65105,
            }
        self.reply_bin_0 = b'\x01\x00\xfe\x51' b'\x00\x00\x00\x07' \
            b'\x76\x74\x37\xd1' b'\x51\xec\x83\x14' \
            b'\x00\x07\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x44\x5f\xb2\x03' b'\x5d\x55\x06\xea' \
            b'\x1f\x56\xf6\xe5' b'\x14\xeb\x5f\x77' \
            b'\x3b\x2c\x57\xb9' b'\x30\x92\xfe\xfb' \
            b'\x22\x8e\xa6\x79'


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
        self.req_bin_0 = b'\x10\x00\x00\x05' b'\x00\x0a\x00\x00' \
            b'\x66\x75\x7a\x7a' b'\x79\x5f\x70\x72' \
            b'\x6f\x70\x00\x00'

        self.reply_args_0 = {
            'atom': 696457407,
            'sequence_number': 45122,
            }
        self.reply_bin_0 = b'\x01\x00\xb0\x42' b'\x00\x00\x00\x00' \
            b'\x29\x83\x18\xbf' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x11\x00\x00\x02' b'\x6b\xe3\x92\x52'

        self.reply_args_0 = {
            'name': 'WM_CLASS',
            'sequence_number': 50608,
            }
        self.reply_bin_0 = b'\x01\x00\xc5\xb0' b'\x00\x00\x00\x02' \
            b'\x00\x08\x00\x00' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x12\x00\x00\x06' b'\x1d\x52\x72\x7c' \
            b'\x69\x31\xd3\xd5' b'\x04\x1c\xdc\x51' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_1 = {
            'data': (8, b'foo'),
            'mode': 1,
            'property': 575034703,
            'type': 142204480,
            'window': 861560365,
            }
        self.req_bin_1 = b'\x12\x01\x00\x07' b'\x33\x5a\x5e\x2d' \
            b'\x22\x46\x55\x4f' b'\x08\x79\xde\x40' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x03' \
            b'\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'data': (8, b'zoom'),
            'mode': 0,
            'property': 2024948722,
            'type': 1218075423,
            'window': 1961010416,
            }
        self.req_bin_2 = b'\x12\x00\x00\x07' b'\x74\xe2\xa4\xf0' \
            b'\x78\xb2\x43\xf2' b'\x48\x9a\x5b\x1f' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x04' \
            b'\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'data': (16, []),
            'mode': 2,
            'property': 456677559,
            'type': 1407609354,
            'window': 675831147,
            }
        self.req_bin_3 = b'\x12\x02\x00\x06' b'\x28\x48\x5d\x6b' \
            b'\x1b\x38\x58\xb7' b'\x53\xe6\x6a\x0a' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_4 = {
            'data': (16, [1, 2, 3]),
            'mode': 1,
            'property': 1899908134,
            'type': 1964041522,
            'window': 849678568,
            }
        self.req_bin_4 = b'\x12\x01\x00\x08' b'\x32\xa5\x10\xe8' \
            b'\x71\x3e\x4c\x26' b'\x75\x10\xe5\x32' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x03' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x00'

        self.req_args_5 = {
            'data': (16, [1, 2, 3, 4]),
            'mode': 2,
            'property': 306879937,
            'type': 568891375,
            'window': 985442388,
            }
        self.req_bin_5 = b'\x12\x02\x00\x08' b'\x3a\xbc\xa8\x54' \
            b'\x12\x4a\x9d\xc1' b'\x21\xe8\x97\xef' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x04' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x04'

        self.req_args_6 = {
            'data': (32, []),
            'mode': 0,
            'property': 1599917196,
            'type': 1205594429,
            'window': 529694076,
            }
        self.req_bin_6 = b'\x12\x00\x00\x06' b'\x1f\x92\x7d\x7c' \
            b'\x5f\x5c\xcc\x8c' b'\x47\xdb\xe9\x3d' \
            b'\x20\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_7 = {
            'data': (32, [1, 2, 3]),
            'mode': 2,
            'property': 1604265475,
            'type': 1255454396,
            'window': 564298846,
            }
        self.req_bin_7 = b'\x12\x02\x00\x09' b'\x21\xa2\x84\x5e' \
            b'\x5f\x9f\x26\x03' b'\x4a\xd4\xb6\xbc' \
            b'\x20\x00\x00\x00' b'\x00\x00\x00\x03' \
            b'\x00\x00\x00\x01' b'\x00\x00\x00\x02' \
            b'\x00\x00\x00\x03'


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
        self.req_bin_0 = b'\x13\x00\x00\x03' b'\x36\xd7\xeb\x63' \
            b'\x72\xec\xdc\x3a'


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
        self.req_bin_0 = b'\x14\x01\x00\x06' b'\x2e\x56\xe6\x4b' \
            b'\x1c\x13\xb3\xdc' b'\x7f\xa9\x5e\xf2' \
            b'\x7f\xb0\x4f\xf8' b'\x11\xb5\xda\xc2'

        self.reply_args_0 = {
            'bytes_after': 195292012,
            'property_type': 1059882735,
            'sequence_number': 33648,
            'value': (8, b''),
            }
        self.reply_bin_0 = b'\x01\x08\x83\x70' b'\x00\x00\x00\x00' \
            b'\x3f\x2c\x86\xef' b'\x0b\xa3\xeb\x6c' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_1 = {
            'bytes_after': 1849269963,
            'property_type': 101247178,
            'sequence_number': 49786,
            'value': (8, b'foo'),
            }
        self.reply_bin_1 = b'\x01\x08\xc2\x7a' b'\x00\x00\x00\x01' \
            b'\x06\x08\xe8\xca' b'\x6e\x39\x9e\xcb' \
            b'\x00\x00\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'bytes_after': 1347495650,
            'property_type': 328289775,
            'sequence_number': 7441,
            'value': (8, b'zoom'),
            }
        self.reply_bin_2 = b'\x01\x08\x1d\x11' b'\x00\x00\x00\x01' \
            b'\x13\x91\x4d\xef' b'\x50\x51\x26\xe2' \
            b'\x00\x00\x00\x04' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'bytes_after': 1461387818,
            'property_type': 1701043014,
            'sequence_number': 10740,
            'value': (16, []),
            }
        self.reply_bin_3 = b'\x01\x10\x29\xf4' b'\x00\x00\x00\x00' \
            b'\x65\x63\xdb\x46' b'\x57\x1b\x02\x2a' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_4 = {
            'bytes_after': 136490248,
            'property_type': 1280844186,
            'sequence_number': 27922,
            'value': (16, [1, 2, 3]),
            }
        self.reply_bin_4 = b'\x01\x10\x6d\x12' b'\x00\x00\x00\x02' \
            b'\x4c\x58\x21\x9a' b'\x08\x22\xad\x08' \
            b'\x00\x00\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x00'

        self.reply_args_5 = {
            'bytes_after': 1279726180,
            'property_type': 819586705,
            'sequence_number': 25472,
            'value': (16, [1, 2, 3, 4]),
            }
        self.reply_bin_5 = b'\x01\x10\x63\x80' b'\x00\x00\x00\x02' \
            b'\x30\xd9\xe6\x91' b'\x4c\x47\x12\x64' \
            b'\x00\x00\x00\x04' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x04'

        self.reply_args_6 = {
            'bytes_after': 539973238,
            'property_type': 1136329940,
            'sequence_number': 30930,
            'value': (32, []),
            }
        self.reply_bin_6 = b'\x01\x20\x78\xd2' b'\x00\x00\x00\x00' \
            b'\x43\xbb\x04\xd4' b'\x20\x2f\x56\x76' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_7 = {
            'bytes_after': 1848575862,
            'property_type': 1188109101,
            'sequence_number': 63896,
            'value': (32, [1, 2, 3]),
            }
        self.reply_bin_7 = b'\x01\x20\xf9\x98' b'\x00\x00\x00\x03' \
            b'\x46\xd1\x1b\x2d' b'\x6e\x2f\x07\x76' \
            b'\x00\x00\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x01' b'\x00\x00\x00\x02' \
            b'\x00\x00\x00\x03'


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
        self.req_bin_0 = b'\x15\x00\x00\x02' b'\x78\xa2\x93\x17'

        self.reply_args_0 = {
            'atoms': [24720840, 1460963027, 1547803868, 246063525, 1464027403, 1900134270, 1153200538, 1612563336, 573068260, 1650618737, 1376520521, 730586807, 239622004, 630352260, 933716813, 339706725, 974429777, 7034796, 2048369638, 1550746425, 1880945398, 1545568005, 565689201],
            'sequence_number': 63949,
            }
        self.reply_bin_0 = b'\x01\x00\xf9\xcd' b'\x00\x00\x00\x17' \
            b'\x00\x17\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x01\x79\x35\xc8' b'\x57\x14\x86\xd3' \
            b'\x5c\x41\x9c\xdc' b'\x0e\xaa\xa1\xa5' \
            b'\x57\x43\x49\x0b' b'\x71\x41\xbf\x7e' \
            b'\x44\xbc\x71\x9a' b'\x60\x1d\xc3\x88' \
            b'\x22\x28\x53\xe4' b'\x62\x62\x71\x71' \
            b'\x52\x0c\x09\x49' b'\x2b\x8b\xde\xb7' \
            b'\x0e\x48\x57\x74' b'\x25\x92\x69\x84' \
            b'\x37\xa7\x63\x4d' b'\x14\x3f\x83\x65' \
            b'\x3a\x14\x9e\x51' b'\x00\x6b\x57\xac' \
            b'\x7a\x17\xa3\xe6' b'\x5c\x6e\x83\x39' \
            b'\x70\x1c\xf2\xf6' b'\x5c\x1f\x7f\x05' \
            b'\x21\xb7\xbb\x71'


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
        self.req_bin_0 = b'\x16\x00\x00\x04' b'\x40\x14\x34\xaf' \
            b'\x61\x88\xfa\x37' b'\x16\xdf\x10\x9a'


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
        self.req_bin_0 = b'\x17\x00\x00\x02' b'\x40\xfc\xb6\x8e'

        self.reply_args_0 = {
            'owner': 228581038,
            'sequence_number': 60065,
            }
        self.reply_bin_0 = b'\x01\x00\xea\xa1' b'\x00\x00\x00\x00' \
            b'\x0d\x9f\xde\xae' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x18\x00\x00\x06' b'\x6f\x6e\x27\x0b' \
            b'\x50\x0a\xd6\x37' b'\x26\x34\x70\x54' \
            b'\x6b\xbc\xd2\x3b' b'\x51\xca\x18\xd3'


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
        self.req_bin_0 = b'\x19\x00\x00\x0b' b'\x45\x0b\x5f\x31' \
            b'\x7a\x0d\x47\x9f' b'\x0c\x00\x00\x00' \
            b'\x40\xfc\x18\xea' b'\x9c\xe5\x33\xeb' \
            b'\x28\x20\x60\xb8' b'\xc4\x33\x00\x00' \
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
        self.req_bin_0 = b'\x1a\x00\x00\x06' b'\x4c\xab\x37\x5a' \
            b'\x53\xfb\x01\x00' b'\x0e\x52\xae\x7d' \
            b'\x76\xed\xb4\x18' b'\x2e\x77\x27\x5a'

        self.reply_args_0 = {
            'sequence_number': 15948,
            'status': 206,
            }
        self.reply_bin_0 = b'\x01\xce\x3e\x4c' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x1b\x00\x00\x02' b'\x07\x6b\x17\x8d'


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
        self.req_bin_0 = b'\x1c\x00\x00\x06' b'\x70\x63\x9e\x5c' \
            b'\x92\x3e\x00\x00' b'\x5d\xb0\x25\xe7' \
            b'\x3e\x35\xef\x70' b'\x91\x00\xfb\x5d'


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
        self.req_bin_0 = b'\x1d\xa0\x00\x03' b'\x10\x70\x21\xae' \
            b'\xa9\xe5\x00\x00'


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
        self.req_bin_0 = b'\x1e\x00\x00\x04' b'\x3c\xd7\x0d\x8f' \
            b'\x79\x33\x56\x66' b'\x8d\xbf\x00\x00'


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
        self.req_bin_0 = b'\x1f\x00\x00\x04' b'\x21\xee\x60\x21' \
            b'\x43\x8b\xd0\x81' b'\x01\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 46979,
            'status': 179,
            }
        self.reply_bin_0 = b'\x01\xb3\xb7\x83' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x20\x00\x00\x02' b'\x27\xe7\x51\xcd'


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
        self.req_bin_0 = b'\x21\x01\x00\x04' b'\x7f\x62\x0d\xdf' \
            b'\xac\xf3\xdf\x01' b'\x01\x00\x00\x00'


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
        self.req_bin_0 = b'\x22\x9e\x00\x03' b'\x1f\xbc\x5f\x0e' \
            b'\x3a\x85\x00\x00'


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
        self.req_bin_0 = b'\x23\x01\x00\x02' b'\x2b\x47\x63\x4d'


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
        self.req_bin_0 = b'\x24\x00\x00\x01'


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
        self.req_bin_0 = b'\x25\x00\x00\x01'


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
        self.req_bin_0 = b'\x26\x00\x00\x02' b'\x02\xb2\x40\x2c'

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
        self.reply_bin_0 = b'\x01\x00\x97\xa4' b'\x00\x00\x00\x00' \
            b'\x1c\x31\x15\x5b' b'\x00\xec\xa1\x2b' \
            b'\x89\x16\xda\x9a' b'\xd0\xc7\x87\x89' \
            b'\x3b\x9b\x00\x00' b'\x00\x00\x00\x00'


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
        self.req_bin_0 = b'\x27\x00\x00\x04' b'\x08\xa1\x92\xe3' \
            b'\x73\xe5\xcd\x93' b'\x04\x06\x56\xfd'

        self.reply_args_0 = {
            'events': [{'y': -30447, 'x': -21941, 'time': 1846118496}, {'y': -23643, 'x': -24970, 'time': 1104207400}, {'y': -25748, 'x': -16862, 'time': 1436684371}, {'y': -9066, 'x': -28433, 'time': 1158061593}, {'y': -14057, 'x': -3855, 'time': 2009067067}],
            'sequence_number': 38018,
            }
        self.reply_bin_0 = b'\x01\x00\x94\x82' b'\x00\x00\x00\x0a' \
            b'\x00\x00\x00\x05' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x6e\x09\x88\x60' b'\xaa\x4b\x89\x11' \
            b'\x41\xd0\xde\x28' b'\x9e\x76\xa3\xa5' \
            b'\x55\xa2\x10\x53' b'\xbe\x22\x9b\x6c' \
            b'\x45\x06\x9e\x19' b'\x90\xef\xdc\x96' \
            b'\x77\xbf\xee\x3b' b'\xf0\xf1\xc9\x17'


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
        self.req_bin_0 = b'\x28\x00\x00\x04' b'\x3c\x81\x7b\xfc' \
            b'\x1f\x1b\x88\x94' b'\xe4\x6e\xbc\x8a'

        self.reply_args_0 = {
            'child': 202628650,
            'same_screen': 1,
            'sequence_number': 12734,
            'x': -29592,
            'y': -11175,
            }
        self.reply_bin_0 = b'\x01\x01\x31\xbe' b'\x00\x00\x00\x00' \
            b'\x0c\x13\xde\x2a' b'\x8c\x68\xd4\x59' \
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
        self.req_bin_0 = b'\x29\x00\x00\x06' b'\x37\x2d\xaf\x69' \
            b'\x2d\x5a\x9f\x6f' b'\xb6\x37\xb4\x9e' \
            b'\x78\x8e\xde\x24' b'\xdd\x52\x86\xef'


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
        self.req_bin_0 = b'\x2a\x02\x00\x03' b'\x53\xa5\x6d\xe7' \
            b'\x7d\xfa\x20\x28'


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
        self.req_bin_0 = b'\x2b\x00\x00\x01'

        self.reply_args_0 = {
            'focus': 864688157,
            'revert_to': 153,
            'sequence_number': 4228,
            }
        self.reply_bin_0 = b'\x01\x99\x10\x84' b'\x00\x00\x00\x00' \
            b'\x33\x8a\x18\x1d' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x2c\x00\x00\x01'

        self.reply_args_0 = {
            'map': [214, 155, 191, 177, 176, 242, 163, 236, 174, 199, 246, 191, 147, 241, 153, 140, 131, 151, 188, 170, 232, 252, 251, 182, 230, 143, 170, 225, 128, 227, 195, 244],
            'sequence_number': 18950,
            }
        self.reply_bin_0 = b'\x01\x00\x4a\x06' b'\x00\x00\x00\x02' \
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
        self.req_bin_0 = b'\x2d\x00\x00\x05' b'\x36\x26\x1b\xf5' \
            b'\x00\x07\x00\x00' b'\x66\x6f\x6f\x66' \
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
        self.req_bin_0 = b'\x2e\x00\x00\x02' b'\x59\x2a\xe9\x0c'


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
        self.req_bin_0 = b'\x2f\x00\x00\x02' b'\x7a\x8a\x62\x61'

        self.reply_args_0 = {
            'all_chars_exist': 0,
            'char_infos': [{'descent': -16821, 'right_side_bearing': -14557, 'character_width': -11080, 'left_side_bearing': -7099, 'attributes': 10400, 'ascent': -9228}, {'descent': -30852, 'right_side_bearing': -23046, 'character_width': -25635, 'left_side_bearing': -26546, 'attributes': 38213, 'ascent': -1026}, {'descent': -22492, 'right_side_bearing': -15002, 'character_width': -30771, 'left_side_bearing': -8660, 'attributes': 4002, 'ascent': -8259}],
            'default_char': 39252,
            'draw_direction': 145,
            'font_ascent': -1914,
            'font_descent': -3596,
            'max_bounds': {'descent': -30143, 'right_side_bearing': -30905, 'character_width': -1286, 'left_side_bearing': -27610, 'attributes': 56049, 'ascent': -16128},
            'max_byte1': 231,
            'max_char_or_byte2': 4746,
            'min_bounds': {'descent': -4827, 'right_side_bearing': -17145, 'character_width': -16291, 'left_side_bearing': -13626, 'attributes': 35063, 'ascent': -2642},
            'min_byte1': 188,
            'min_char_or_byte2': 12434,
            'properties': [{'name': 1568813755, 'value': 2137719486}],
            'sequence_number': 3542,
            }
        self.reply_bin_0 = b'\x01\x00\x0d\xd6' b'\x00\x00\x00\x12' \
            b'\xca\xc6\xbd\x07' b'\xc0\x5d\xf5\xae' \
            b'\xed\x25\x88\xf7' b'\x00\x00\x00\x00' \
            b'\x94\x26\x87\x47' b'\xfa\xfa\xc1\x00' \
            b'\x8a\x41\xda\xf1' b'\x00\x00\x00\x00' \
            b'\x30\x92\x12\x8a' b'\x99\x54\x00\x01' \
            b'\x91\xbc\xe7\x00' b'\xf8\x86\xf1\xf4' \
            b'\x00\x00\x00\x03' b'\x5d\x82\x32\xbb' \
            b'\x7f\x6b\x02\xbe' b'\xe4\x45\xc7\x23' \
            b'\xd4\xb8\xdb\xf4' b'\xbe\x4b\x28\xa0' \
            b'\x98\x4e\xa5\xfa' b'\x9b\xdd\xfb\xfe' \
            b'\x87\x7c\x95\x45' b'\xde\x2c\xc5\x66' \
            b'\x87\xcd\xdf\xbd' b'\xa8\x24\x0f\xa2'


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
        self.req_bin_0 = b'\x30\x01\x00\x04' b'\x48\xec\x1f\xbc' \
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
        self.reply_bin_0 = b'\x01\xbf\x95\x34' b'\x00\x00\x00\x00' \
            b'\xcc\x19\x85\x16' b'\xcf\x47\x8a\x7e' \
            b'\xb5\xa9\x29\x72' b'\xd4\x24\xcd\xca' \
            b'\xca\xb5\xc6\x07' b'\x00\x00\x00\x00'


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
        self.req_bin_0 = b'\x31\x00\x00\x04' b'\x91\xb2\x00\x05' \
            b'\x62\x68\x61\x7a' b'\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 34517,
            }
        self.reply_bin_0 = b'\x01\x00\x86\xd5' b'\x00\x00\x00\x05' \
            b'\x00\x03\x00\x00' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x32\x00\x00\x04' b'\x51\xfd\x00\x06' \
            b'\x62\x68\x61\x7a' b'\x72\x32\x00\x00'

        self.reply_args_0 = {
            'all_chars_exist': 0,
            'default_char': 61580,
            'draw_direction': 146,
            'font_ascent': -30368,
            'font_descent': -15151,
            'max_bounds': {'descent': -17786, 'right_side_bearing': -10759, 'character_width': -11617, 'left_side_bearing': -28480, 'attributes': 20976, 'ascent': -22938},
            'max_byte1': 245,
            'max_char_or_byte2': 49530,
            'min_bounds': {'descent': -24065, 'right_side_bearing': -9300, 'character_width': -22473, 'left_side_bearing': -10823, 'attributes': 26194, 'ascent': -24947},
            'min_byte1': 130,
            'min_char_or_byte2': 61140,
            'name': 'fontfont',
            'properties': [{'name': 2007331946, 'value': 560055601}],
            'replies_hint': 457810933,
            'sequence_number': 13642,
            }
        self.reply_bin_0 = b'\x01\x08\x35\x4a' b'\x00\x00\x00\x0b' \
            b'\xd5\xb9\xdb\xac' b'\xa8\x37\x9e\x8d' \
            b'\xa1\xff\x66\x52' b'\x00\x00\x00\x00' \
            b'\x90\xc0\xd5\xf9' b'\xd2\x9f\xa6\x66' \
            b'\xba\x86\x51\xf0' b'\x00\x00\x00\x00' \
            b'\xee\xd4\xc1\x7a' b'\xf0\x8c\x00\x01' \
            b'\x92\x82\xf5\x00' b'\x89\x60\xc4\xd1' \
            b'\x1b\x49\xa3\xf5' b'\x77\xa5\x74\x6a' \
            b'\x21\x61\xc5\x31' b'\x66\x6f\x6e\x74' \
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
        self.req_bin_0 = b'\x33\x00\x00\x06' b'\x00\x03\x00\x00' \
            b'\x03\x66\x6f\x6f' b'\x03\x62\x61\x72' \
            b'\x06\x67\x61\x7a' b'\x6f\x6e\x6b\x00'

        self.req_args_1 = {
            'path': [],
            }
        self.req_bin_1 = b'\x33\x00\x00\x02' b'\x00\x00\x00\x00'


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
        self.req_bin_0 = b'\x34\x00\x00\x01'

        self.reply_args_0 = {
            'paths': ['path1', 'path2232'],
            'sequence_number': 33409,
            }
        self.reply_bin_0 = b'\x01\x00\x82\x81' b'\x00\x00\x00\x04' \
            b'\x00\x02\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x05\x70\x61\x74' b'\x68\x31\x08\x70' \
            b'\x61\x74\x68\x32' b'\x32\x33\x32\x00'

        self.reply_args_1 = {
            'paths': [],
            'sequence_number': 17636,
            }
        self.reply_bin_1 = b'\x01\x00\x44\xe4' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x35\xa1\x00\x04' b'\x77\x76\x0b\x1f' \
            b'\x2c\xad\x52\x4c' b'\xe2\x80\x12\x9c'


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
        self.req_bin_0 = b'\x36\x00\x00\x02' b'\x70\x8c\xed\x61'


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
            'attrs': {'stipple': 1424681955, 'background': 338824284, 'subwindow_mode': 0, 'fill_style': 0, 'font': 568001783, 'graphics_exposures': 0, 'tile': 2000996399, 'tile_stipple_x_origin': -25980, 'dashes': 215, 'function': 7, 'foreground': 612071305, 'clip_x_origin': -22581, 'cap_style': 2, 'tile_stipple_y_origin': -23968, 'join_style': 2, 'line_width': 61484, 'dash_offset': 46571, 'clip_y_origin': -14920, 'arc_mode': 0, 'line_style': 2, 'plane_mask': 793618921, 'clip_mask': 605132525, 'fill_rule': 1},
            'cid': 1476454377,
            'drawable': 1362081172,
            }
        self.req_bin_0 = b'\x37\x00\x00\x1b' b'\x58\x00\xe7\xe9' \
            b'\x51\x2f\xb5\x94' b'\x00\x7f\xff\xff' \
            b'\x07\x00\x00\x00' b'\x2f\x4d\xa9\xe9' \
            b'\x24\x7b\x77\x89' b'\x14\x32\x0c\x5c' \
            b'\xf0\x2c\x00\x00' b'\x02\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x77\x44\xc8\x2f' b'\x54\xea\xeb\xe3' \
            b'\x9a\x84\x00\x00' b'\xa2\x60\x00\x00' \
            b'\x21\xdb\x04\xf7' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\xa7\xcb\x00\x00' \
            b'\xc5\xb8\x00\x00' b'\x24\x11\x96\xed' \
            b'\xb5\xeb\x00\x00' b'\xd7\x00\x00\x00' \
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
            'attrs': {'stipple': 1656031462, 'background': 539344312, 'subwindow_mode': 1, 'fill_style': 0, 'font': 347060191, 'graphics_exposures': 1, 'tile': 716372747, 'tile_stipple_x_origin': -24195, 'dashes': 137, 'function': 8, 'foreground': 1049179696, 'clip_x_origin': -32135, 'cap_style': 3, 'tile_stipple_y_origin': -15601, 'join_style': 1, 'line_width': 36097, 'dash_offset': 42536, 'clip_y_origin': -25437, 'arc_mode': 1, 'line_style': 0, 'plane_mask': 1085423224, 'clip_mask': 161650480, 'fill_rule': 0},
            'gc': 1250995304,
            }
        self.req_bin_0 = b'\x38\x00\x00\x1a' b'\x4a\x90\xac\x68' \
            b'\x00\x7f\xff\xff' b'\x08\x00\x00\x00' \
            b'\x40\xb2\x3e\x78' b'\x3e\x89\x36\x30' \
            b'\x20\x25\xbd\xb8' b'\x8d\x01\x00\x00' \
            b'\x00\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x01\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x2a\xb2\xfb\x0b' \
            b'\x62\xb5\x08\xe6' b'\xa1\x7d\x00\x00' \
            b'\xc3\x0f\x00\x00' b'\x14\xaf\xb7\xdf' \
            b'\x01\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x82\x79\x00\x00' b'\x9c\xa3\x00\x00' \
            b'\x09\xa2\x97\x30' b'\xa6\x28\x00\x00' \
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
        self.req_bin_0 = b'\x39\x00\x00\x04' b'\x46\xba\x24\x71' \
            b'\x12\xf5\xbc\xbb' b'\x37\x04\x40\x4b'


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
        self.req_bin_0 = b'\x3a\x00\x00\x06' b'\x2d\x46\x57\x65' \
            b'\xc8\xb5\x00\x09' b'\xa0\x8a\xce\xdd' \
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
            'rectangles': [{'y': -3797, 'x': -14422, 'height': 26888, 'width': 57581}, {'y': -12431, 'x': -858, 'height': 10384, 'width': 49373}],
            'x_origin': -27444,
            'y_origin': -780,
            }
        self.req_bin_0 = b'\x3b\x01\x00\x07' b'\x6e\xac\x66\x4a' \
            b'\x94\xcc\xfc\xf4' b'\xc7\xaa\xf1\x2b' \
            b'\xe0\xed\x69\x08' b'\xfc\xa6\xcf\x71' \
            b'\xc0\xdd\x28\x90'

        self.req_args_1 = {
            'gc': 1892892424,
            'ordering': 1,
            'rectangles': [],
            'x_origin': -19258,
            'y_origin': -31956,
            }
        self.req_bin_1 = b'\x3b\x01\x00\x03' b'\x70\xd3\x3f\x08' \
            b'\xb4\xc6\x83\x2c'


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
        self.req_bin_0 = b'\x3c\x00\x00\x02' b'\x16\xf6\x4a\x49'


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
        self.req_bin_0 = b'\x3d\x01\x00\x04' b'\x64\x26\x3d\x94' \
            b'\xf7\x24\xb4\xb3' b'\xce\x5f\xac\x7f'


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
        self.req_bin_0 = b'\x3e\x00\x00\x07' b'\x6e\x9a\xa6\x63' \
            b'\x5e\x17\x5d\x86' b'\x67\xc7\xa2\x35' \
            b'\x9f\xc3\xa2\x26' b'\x94\x60\xe4\xc8' \
            b'\xb4\x86\x1c\xac'


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
        self.req_bin_0 = b'\x3f\x00\x00\x08' b'\x30\xf8\x20\x8d' \
            b'\x6f\xa4\x29\x48' b'\x04\xf5\xed\x85' \
            b'\xed\xe6\xbc\x3f' b'\x9c\x78\x99\x8b' \
            b'\xd2\x0b\xec\x1f' b'\x3a\xec\x37\x6a'


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
            'points': [{'y': -22768, 'x': -21311}, {'y': -6707, 'x': -5881}, {'y': -25311, 'x': -4217}],
            }
        self.req_bin_0 = b'\x40\x00\x00\x06' b'\x03\x08\x6f\xad' \
            b'\x54\x7c\xf7\xad' b'\xac\xc1\xa7\x10' \
            b'\xe9\x07\xe5\xcd' b'\xef\x87\x9d\x21'


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
            'points': [{'y': -19712, 'x': -26440}, {'y': -23639, 'x': -22012}, {'y': -30494, 'x': -4445}, {'y': -7428, 'x': -1085}, {'y': -21262, 'x': -23622}],
            }
        self.req_bin_0 = b'\x41\x01\x00\x08' b'\x56\xfb\x73\x16' \
            b'\x7d\x97\x50\x12' b'\x98\xb8\xb3\x00' \
            b'\xaa\x04\xa3\xa9' b'\xee\xa3\x88\xe2' \
            b'\xfb\xc3\xe2\xfc' b'\xa3\xba\xac\xf2'


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
            'segments': [{'y1': -15198, 'x2': -21917, 'x1': -5123, 'y2': -1992}],
            }
        self.req_bin_0 = b'\x42\x00\x00\x05' b'\x03\x89\x6a\x18' \
            b'\x0e\xc4\x84\xb3' b'\xeb\xfd\xc4\xa2' \
            b'\xaa\x63\xf8\x38'


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
            'rectangles': [{'y': -970, 'x': -4030, 'height': 11958, 'width': 17374}, {'y': -1228, 'x': -13744, 'height': 17653, 'width': 64713}, {'y': -29216, 'x': -31515, 'height': 28735, 'width': 39352}],
            }
        self.req_bin_0 = b'\x43\x00\x00\x09' b'\x2c\x40\x79\xa2' \
            b'\x5d\x41\xf6\xec' b'\xf0\x42\xfc\x36' \
            b'\x43\xde\x2e\xb6' b'\xca\x50\xfb\x34' \
            b'\xfc\xc9\x44\xf5' b'\x84\xe5\x8d\xe0' \
            b'\x99\xb8\x70\x3f'


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
            'arcs': [{'height': 39984, 'width': 28855, 'angle1': -517, 'angle2': -16010, 'y': -22490, 'x': -6999}, {'height': 38043, 'width': 59205, 'angle1': -26540, 'angle2': -24422, 'y': -20146, 'x': -28979}, {'height': 366, 'width': 28833, 'angle1': -15732, 'angle2': -2439, 'y': -9543, 'x': -31314}],
            'drawable': 1732034432,
            'gc': 1156382390,
            }
        self.req_bin_0 = b'\x44\x00\x00\x0c' b'\x67\x3c\xbf\x80' \
            b'\x44\xec\xfe\xb6' b'\xe4\xa9\xa8\x26' \
            b'\x70\xb7\x9c\x30' b'\xfd\xfb\xc1\x76' \
            b'\x8e\xcd\xb1\x4e' b'\xe7\x45\x94\x9b' \
            b'\x98\x54\xa0\x9a' b'\x85\xae\xda\xb9' \
            b'\x70\xa1\x01\x6e' b'\xc2\x8c\xf6\x79'


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
            'points': [{'y': -9194, 'x': -10262}, {'y': -8456, 'x': -1958}, {'y': -10793, 'x': -8617}],
            'shape': 1,
            }
        self.req_bin_0 = b'\x45\x00\x00\x07' b'\x19\x39\x72\x7d' \
            b'\x2e\x9f\xcf\x2b' b'\x01\x00\x00\x00' \
            b'\xd7\xea\xdc\x16' b'\xf8\x5a\xde\xf8' \
            b'\xde\x57\xd5\xd7'


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
            'rectangles': [{'y': -11003, 'x': -1676, 'height': 21895, 'width': 60599}, {'y': -22482, 'x': -12349, 'height': 55831, 'width': 43731}],
            }
        self.req_bin_0 = b'\x46\x00\x00\x07' b'\x0f\xf4\xb8\xeb' \
            b'\x5c\x21\xe8\x50' b'\xf9\x74\xd5\x05' \
            b'\xec\xb7\x55\x87' b'\xcf\xc3\xa8\x2e' \
            b'\xaa\xd3\xda\x17'


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
            'arcs': [{'height': 20525, 'width': 33490, 'angle1': -10916, 'angle2': -19386, 'y': -22928, 'x': -3276}],
            'drawable': 700537986,
            'gc': 864213787,
            }
        self.req_bin_0 = b'\x47\x00\x00\x06' b'\x29\xc1\x5c\x82' \
            b'\x33\x82\xdb\x1b' b'\xf3\x34\xa6\x70' \
            b'\x82\xd2\x50\x2d' b'\xd5\x5c\xb4\x46'


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
        self.req_bin_0 = b'\x48\x02\x00\x09' b'\x25\xd9\x07\x90' \
            b'\x46\xf7\xfc\xfd' b'\x21\x95\x32\x1c' \
            b'\xb5\xd1\xd5\x1c' b'\xe1\xac\x00\x00' \
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
        self.req_bin_0 = b'\x49\x02\x00\x05' b'\x33\xfb\x45\x6a' \
            b'\xc6\x22\xea\xb7' b'\x01\x1a\x4e\xca' \
            b'\x24\xba\x96\xb6'

        self.reply_args_0 = {
            'data': b'\xeb?:\xa7\xc6\x8b\xc2\x96o-S\xe6\xd6z6\x94\xd7v\xd2R.\xa2\xeaw\t\x13\x95\x85',
            'depth': 181,
            'sequence_number': 28429,
            'visual': 1687469773,
            }
        self.reply_bin_0 = b'\x01\xb5\x6f\x0d' b'\x00\x00\x00\x07' \
            b'\x64\x94\xbe\xcd' b'\x00\x00\x00\x00' \
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
            'items': [{'string': 'zoo', 'delta': 2}, 16909060, {'string': 'ie', 'delta': 0}],
            'x': -11315,
            'y': -22209,
            }
        self.req_bin_0 = b'\x4a\x00\x00\x08' b'\x4a\x3d\xf0\xf3' \
            b'\x4d\xa8\x16\x12' b'\xd3\xcd\xa9\x3f' \
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
            'items': [{'string': (4131, 18), 'delta': 2}, 16909060],
            'x': -18280,
            'y': -10630,
            }
        self.req_bin_0 = b'\x4b\x00\x00\x07' b'\x3b\x85\xbb\xa4' \
            b'\x38\x8d\x71\xb2' b'\xb8\x98\xd6\x7a' \
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
        self.req_bin_0 = b'\x4c\x06\x00\x06' b'\x1b\x5b\x91\x4d' \
            b'\x41\x6f\x26\x47' b'\xbc\x91\xe5\x99' \
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
        self.req_bin_0 = b'\x4d\x08\x00\x08' b'\x73\x5a\xe4\xa2' \
            b'\x7a\xdc\xc6\x63' b'\xe5\xe4\xde\x33' \
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
        self.req_bin_0 = b'\x4e\x00\x00\x04' b'\x54\x56\x38\xac' \
            b'\x0a\xdb\x94\x84' b'\x24\x54\x1c\xe8'


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
        self.req_bin_0 = b'\x4f\x00\x00\x02' b'\x41\xfb\x54\xd4'


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
        self.req_bin_0 = b'\x50\x00\x00\x03' b'\x54\xfa\x29\x9b' \
            b'\x51\x05\x34\xbb'


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
        self.req_bin_0 = b'\x51\x00\x00\x02' b'\x4f\x44\xf0\x26'


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
        self.req_bin_0 = b'\x52\x00\x00\x02' b'\x2a\xe8\x72\xed'


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
        self.req_bin_0 = b'\x53\x00\x00\x02' b'\x0b\xf5\x1c\x95'

        self.reply_args_0 = {
            'cmaps': [1757616530, 2044469232],
            'sequence_number': 49482,
            }
        self.reply_bin_0 = b'\x01\x00\xc1\x4a' b'\x00\x00\x00\x02' \
            b'\x00\x02\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x68\xc3\x19\x92' b'\x79\xdc\x1f\xf0'


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
        self.req_bin_0 = b'\x54\x00\x00\x04' b'\x1e\x11\x2c\x97' \
            b'\xad\x3c\x50\x77' b'\x3a\x82\x00\x00'

        self.reply_args_0 = {
            'blue': 1856,
            'green': 9912,
            'pixel': 99308744,
            'red': 13306,
            'sequence_number': 53114,
            }
        self.reply_bin_0 = b'\x01\x00\xcf\x7a' b'\x00\x00\x00\x00' \
            b'\x33\xfa\x26\xb8' b'\x07\x40\x00\x00' \
            b'\x05\xeb\x54\xc8' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x55\x00\x00\x05' b'\x1f\x58\x00\x19' \
            b'\x00\x07\x00\x00' b'\x6f\x63\x74\x61' \
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
        self.reply_bin_0 = b'\x01\x00\xfc\xe3' b'\x00\x00\x00\x00' \
            b'\x3c\xd2\x44\x81' b'\x9d\x7c\xda\x88' \
            b'\xc5\xbb\x13\xa4' b'\x75\x96\x6b\x18' \
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
        self.req_bin_0 = b'\x56\x00\x00\x03' b'\x5b\xf3\xc2\x40' \
            b'\xb3\x44\x63\x4c'

        self.reply_args_0 = {
            'masks': [1726878301, 2057281944, 1494524694],
            'pixels': [1061732426, 858313521, 524018138, 316972578, 1408939380, 1476723430, 11972931, 1917037904, 1612749468, 1847847580, 1653727126, 1901587588, 228960010, 1671710636, 913060041, 470023299, 377779303],
            'sequence_number': 34200,
            }
        self.reply_bin_0 = b'\x01\x00\x85\x98' b'\x00\x00\x00\x14' \
            b'\x00\x11\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x3f\x48\xc0\x4a' b'\x33\x28\xd3\x31' \
            b'\x1f\x3b\xe1\xda' b'\x12\xe4\x9e\x22' \
            b'\x53\xfa\xb5\x74' b'\x58\x05\x02\xe6' \
            b'\x00\xb6\xb1\x43' b'\x72\x43\xad\x50' \
            b'\x60\x20\x9a\x9c' b'\x6e\x23\xea\x9c' \
            b'\x62\x91\xdf\x96' b'\x71\x57\xec\x84' \
            b'\x0d\xa5\xa7\x0a' b'\x63\xa4\x47\xac' \
            b'\x36\x6c\x30\xc9' b'\x1c\x03\xfc\x83' \
            b'\x16\x84\x74\x67' b'\x66\xee\x12\x5d' \
            b'\x7a\x9f\xa1\x98' b'\x59\x14\xa3\x16'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 30700,
            }
        self.reply_bin_1 = b'\x01\x00\x77\xec' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x57\x00\x00\x04' b'\x47\x5a\x12\xbc' \
            b'\x40\xcb\xeb\xdf' b'\xda\x2c\x20\x11'

        self.reply_args_0 = {
            'blue_mask': 1200348460,
            'green_mask': 2121548418,
            'pixels': [980309855, 286409072, 1721094583, 997879295],
            'red_mask': 1140662566,
            'sequence_number': 44006,
            }
        self.reply_bin_0 = b'\x01\x00\xab\xe6' b'\x00\x00\x00\x04' \
            b'\x00\x04\x00\x00' b'\x43\xfd\x21\x26' \
            b'\x7e\x74\x42\x82' b'\x47\x8b\xdd\x2c' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x3a\x6e\x57\x5f' b'\x11\x12\x41\x70' \
            b'\x66\x95\xd1\xb7' b'\x3b\x7a\x6d\xff'


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
        self.req_bin_0 = b'\x58\x00\x00\x14' b'\x14\x60\x49\x44' \
            b'\x5f\x31\x19\xfb' b'\x4c\x38\xc8\x12' \
            b'\x28\x9e\x38\x29' b'\x79\x9b\xe5\xd1' \
            b'\x60\xad\x08\x49' b'\x72\x1b\x3e\xa8' \
            b'\x38\xa7\x3e\xfa' b'\x4e\x6c\x64\x29' \
            b'\x68\x53\x22\x19' b'\x5c\x12\x2b\x44' \
            b'\x72\x2e\xb8\x97' b'\x40\x9d\x92\x21' \
            b'\x36\xa0\x70\xee' b'\x6a\x51\x17\x29' \
            b'\x74\x14\xd0\xdc' b'\x46\x21\xab\x0d' \
            b'\x39\x14\xb2\x73' b'\x72\xd8\xb7\x1c'


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
            'items': [{'blue': 17242, 'flags': 191, 'green': 29751, 'pixel': 1850111768, 'red': 31364}, {'blue': 50444, 'flags': 252, 'green': 18429, 'pixel': 1803657350, 'red': 42045}, {'blue': 29083, 'flags': 147, 'green': 18252, 'pixel': 1345997556, 'red': 15935}, {'blue': 18063, 'flags': 213, 'green': 15623, 'pixel': 1532391469, 'red': 18981}],
            }
        self.req_bin_0 = b'\x59\x00\x00\x0e' b'\x28\xed\x3e\x32' \
            b'\x6e\x46\x77\x18' b'\x7a\x84\x74\x37' \
            b'\x43\x5a\xbf\x00' b'\x6b\x81\xa0\x86' \
            b'\xa4\x3d\x47\xfd' b'\xc5\x0c\xfc\x00' \
            b'\x50\x3a\x4a\xf4' b'\x3e\x3f\x47\x4c' \
            b'\x71\x9b\x93\x00' b'\x5b\x56\x70\x2d' \
            b'\x4a\x25\x3d\x07' b'\x46\x8f\xd5\x00'


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
        self.req_bin_0 = b'\x5a\x94\x00\x05' b'\x11\xb7\x3d\xc3' \
            b'\x13\x4f\x6b\x4b' b'\x00\x04\x00\x00' \
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
        self.req_bin_0 = b'\x5b\x00\x00\x0a' b'\x34\x2d\x37\x5d' \
            b'\x1d\x9a\xf9\xec' b'\x31\x08\x4c\xe9' \
            b'\x58\xd4\x58\xf8' b'\x13\x90\x1f\x71' \
            b'\x5a\x6c\xf1\x47' b'\x1b\x63\xce\xd6' \
            b'\x08\x39\xa6\xa8' b'\x35\x1b\x64\x2a'

        self.reply_args_0 = {
            'colors': [{'blue': 27504, 'green': 30790, 'red': 35816}, {'blue': 54840, 'green': 13811, 'red': 4336}, {'blue': 59555, 'green': 25780, 'red': 27790}, {'blue': 62257, 'green': 38534, 'red': 50705}, {'blue': 56402, 'green': 1536, 'red': 45837}],
            'sequence_number': 57970,
            }
        self.reply_bin_0 = b'\x01\x00\xe2\x72' b'\x00\x00\x00\x0a' \
            b'\x00\x05\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x8b\xe8\x78\x46' b'\x6b\x70\x00\x00' \
            b'\x10\xf0\x35\xf3' b'\xd6\x38\x00\x00' \
            b'\x6c\x8e\x64\xb4' b'\xe8\xa3\x00\x00' \
            b'\xc6\x11\x96\x86' b'\xf3\x31\x00\x00' \
            b'\xb3\x0d\x06\x00' b'\xdc\x52\x00\x00'

        self.req_args_1 = {
            'cmap': 710627905,
            'pixels': [],
            }
        self.req_bin_1 = b'\x5b\x00\x00\x02' b'\x2a\x5b\x52\x41'


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
        self.req_bin_0 = b'\x5c\x00\x00\x05' b'\x62\x00\x00\xc1' \
            b'\x00\x07\x00\x00' b'\x6f\x63\x74\x61' \
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
        self.reply_bin_0 = b'\x01\x00\x94\x60' b'\x00\x00\x00\x00' \
            b'\x62\x60\x7b\x1b' b'\x02\x82\xf2\x57' \
            b'\x5b\x0c\x4d\x71' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x5d\x00\x00\x08' b'\x60\x72\xdf\x7e' \
            b'\x31\xec\x15\x1c' b'\x6d\x3e\xc8\x4a' \
            b'\xe5\x42\xf5\x14' b'\xd6\xf2\x6c\x44' \
            b'\x8a\xc8\xc0\x5d' b'\xbd\x10\x8c\xcf'


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
        self.req_bin_0 = b'\x5e\x00\x00\x08' b'\x66\x63\x14\x81' \
            b'\x4d\x38\x61\x7a' b'\x72\xec\x7b\x73' \
            b'\x39\x75\x7d\xfc' b'\x39\x2c\x46\xdf' \
            b'\x70\x92\x7d\x53' b'\x08\x6e\x64\x8c'


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
        self.req_bin_0 = b'\x5f\x00\x00\x02' b'\x2b\x07\x4a\xf7'


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
        self.req_bin_0 = b'\x60\x00\x00\x05' b'\x55\x9e\xa6\x9b' \
            b'\xae\xdc\xcd\x53' b'\x68\x81\xba\x63' \
            b'\x2b\x40\xd8\x2b'


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
        self.req_bin_0 = b'\x61\x01\x00\x03' b'\x75\xb4\x8a\x35' \
            b'\x21\xac\xfc\x10'

        self.reply_args_0 = {
            'height': 2023,
            'sequence_number': 41036,
            'width': 35260,
            }
        self.reply_bin_0 = b'\x01\x00\xa0\x4c' b'\x00\x00\x00\x00' \
            b'\x89\xbc\x07\xe7' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x62\x00\x00\x03' b'\x00\x04\x00\x00' \
            b'\x58\x54\x52\x41'

        self.reply_args_0 = {
            'first_error': 237,
            'first_event': 149,
            'major_opcode': 134,
            'present': 1,
            'sequence_number': 59692,
            }
        self.reply_bin_0 = b'\x01\x00\xe9\x2c' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x63\x00\x00\x01'

        self.reply_args_0 = {
            'names': ['XTRA', 'XTRA-II'],
            'sequence_number': 9149,
            }
        self.reply_bin_0 = b'\x01\x02\x23\xbd' b'\x00\x00\x00\x04' \
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
        self.req_bin_0 = b'\x64\x14\x00\x3e' b'\x9d\x03\x00\x00' \
            b'\x6e\xf4\xfc\x31' b'\x3b\x18\xef\x4e' \
            b'\x17\x42\xe5\x90' b'\x06\x6f\xba\x15' \
            b'\x21\x4c\xcd\x52' b'\x30\x86\x79\xb9' \
            b'\x29\xe6\xb1\x34' b'\x1b\x17\xaf\x2e' \
            b'\x3a\x33\x96\x6c' b'\x29\xd6\x15\x5c' \
            b'\x2b\x33\x37\xcf' b'\x61\x6f\xf9\x9a' \
            b'\x70\x98\x0b\x0b' b'\x30\x87\x35\x32' \
            b'\x23\x9d\xe9\xac' b'\x60\x41\xdb\x9d' \
            b'\x79\xc1\x0e\x7e' b'\x6a\x7c\x7e\xb9' \
            b'\x35\xf5\xd6\x18' b'\x20\x4a\x6e\xf6' \
            b'\x6a\xde\x5c\x68' b'\x0a\x7b\xe7\x46' \
            b'\x3c\x33\x03\xb2' b'\x02\x7b\x26\xc3' \
            b'\x5f\xe0\x06\xe4' b'\x45\x0b\xae\xff' \
            b'\x06\xaa\xbd\xb0' b'\x7f\xfc\xfa\xc2' \
            b'\x79\xd8\x81\x2d' b'\x2c\xcb\x80\x21' \
            b'\x1c\xb3\x4f\xd3' b'\x53\x37\xeb\xfb' \
            b'\x08\xc8\x7c\x9c' b'\x63\xff\x71\xcf' \
            b'\x7a\x88\x55\xa9' b'\x53\x6c\xb2\x51' \
            b'\x05\x27\x2d\xb8' b'\x60\x8a\xb6\xb6' \
            b'\x03\xf8\xca\x7c' b'\x79\x8c\xe0\x92' \
            b'\x1f\xa6\xfa\xb0' b'\x19\x84\xa6\x9a' \
            b'\x6b\x6b\xd9\xdc' b'\x02\x9b\xcf\xfb' \
            b'\x4f\x87\xed\x46' b'\x13\x81\x43\xc5' \
            b'\x1e\x88\xa4\x01' b'\x10\x28\x02\x4a' \
            b'\x3c\x9d\xa6\x19' b'\x55\xb0\xd3\xd8' \
            b'\x0e\xa4\x50\x38' b'\x48\x30\x27\xb1' \
            b'\x79\x50\x1a\x2c' b'\x1b\xe6\x43\x1d' \
            b'\x3b\x86\x3b\xcc' b'\x59\x88\x11\x78' \
            b'\x20\xcc\x97\xef' b'\x62\x29\xb7\x8e' \
            b'\x2f\x37\xf5\x03' b'\x15\x7a\x1d\x5b'


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
        self.req_bin_0 = b'\x65\x00\x00\x02' b'\xa9\xcf\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[232140298, 1242716010, 55143985], [1994770011, 669923085, 1236514049], [1454592222, 1949971307, 2057660497], [805965556, 851808913, 2021792706], [1535482384, 425909956, 163201187], [1271520474, 1483083165, 1783638995], [1346992789, 521515080, 218831382], [1497210568, 1658890074, 647643874], [1825990828, 1469435098, 1289374120], [1729858135, 259963764, 1709884923], [2112789657, 1215330896, 1680696611], [88195295, 745614404, 1144061708], [919934772, 1420606257, 795794911], [148083460, 1086542523, 1390588550], [732788374, 27170279, 1824449766], [902069278, 1765942198, 1052700150], [226642993, 930984408, 2063275595], [777792886, 1364908620, 1914642756], [1779635393, 987282730, 1518933756], [328545991, 935201525, 378251236]],
            'sequence_number': 48346,
            }
        self.reply_bin_0 = b'\x01\x03\xbc\xda' b'\x00\x00\x00\x3c' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x0d\xd6\x2e\x0a' b'\x4a\x12\x57\x6a' \
            b'\x03\x49\x6e\x31' b'\x76\xe5\xc6\x5b' \
            b'\x27\xee\x37\x0d' b'\x49\xb3\xb5\x01' \
            b'\x56\xb3\x50\xde' b'\x74\x3a\x33\x6b' \
            b'\x7a\xa5\x68\x51' b'\x30\x0a\x0e\xf4' \
            b'\x32\xc5\x92\x91' b'\x78\x82\x1b\xc2' \
            b'\x5b\x85\x9a\x10' b'\x19\x62\xde\xc4' \
            b'\x09\xba\x40\xa3' b'\x4b\xc9\xdc\xda' \
            b'\x58\x66\x0d\x9d' b'\x6a\x50\x2b\xd3' \
            b'\x50\x49\x7a\x95' b'\x1f\x15\xb0\x48' \
            b'\x0d\x0b\x1a\x16' b'\x59\x3d\x9e\xc8' \
            b'\x62\xe0\xa7\x5a' b'\x26\x9a\x42\xe2' \
            b'\x6c\xd6\x68\xac' b'\x57\x95\xcc\xda' \
            b'\x4c\xda\x49\xa8' b'\x67\x1b\x8a\x57' \
            b'\x0f\x7e\xbb\x74' b'\x65\xea\xc5\xfb' \
            b'\x7d\xee\x9c\x99' b'\x48\x70\x7a\x50' \
            b'\x64\x2d\x65\x23' b'\x05\x41\xc0\xdf' \
            b'\x2c\x71\x2c\x44' b'\x44\x30\xff\x0c' \
            b'\x36\xd5\x17\x34' b'\x54\xac\xbb\x31' \
            b'\x2f\x6e\xdd\xdf' b'\x08\xd3\x93\x04' \
            b'\x40\xc3\x52\xbb' b'\x52\xe2\xb2\x86' \
            b'\x2b\xad\x76\x96' b'\x01\x9e\x95\xe7' \
            b'\x6c\xbe\xe4\xe6' b'\x35\xc4\x7c\x1e' \
            b'\x69\x42\x23\xb6' b'\x3e\xbe\xed\xf6' \
            b'\x0d\x82\x4c\x31' b'\x37\x7d\xb1\xd8' \
            b'\x7a\xfb\x16\x4b' b'\x2e\x5c\x2d\x76' \
            b'\x51\x5a\xda\x4c' b'\x72\x1f\x21\x44' \
            b'\x6a\x13\x14\xc1' b'\x3a\xd8\xbd\x2a' \
            b'\x5a\x89\x16\xfc' b'\x13\x95\x36\xc7' \
            b'\x37\xbe\x0a\xf5' b'\x16\x8b\xa7\xe4'


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
            'attrs': {'led': 196, 'auto_repeat_mode': 0, 'bell_pitch': -2303, 'bell_percent': -5, 'key_click_percent': -59, 'key': 190, 'bell_duration': -4223, 'led_mode': 1},
            }
        self.req_bin_0 = b'\x66\x00\x00\x0a' b'\x00\x00\x00\xff' \
            b'\xc5\x00\x00\x00' b'\xfb\x00\x00\x00' \
            b'\xf7\x01\x00\x00' b'\xef\x81\x00\x00' \
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
        self.req_bin_0 = b'\x67\x00\x00\x01'

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
        self.reply_bin_0 = b'\x01\x00\x4f\x63' b'\x00\x00\x00\x05' \
            b'\x54\xfd\xa4\x59' b'\xde\xf9\x8e\xb0' \
            b'\x88\xea\x00\x00' b'\xc7\xf3\xbe\xf6' \
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
        self.req_bin_0 = b'\x68\xd8\x00\x01'


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
        self.req_bin_0 = b'\x69\x00\x00\x03' b'\xb6\x76\xdf\x7a' \
            b'\xc6\x73\x01\x01'


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
        self.req_bin_0 = b'\x6a\x00\x00\x01'

        self.reply_args_0 = {
            'accel_denom': 18010,
            'accel_num': 29992,
            'sequence_number': 46318,
            'threshold': 20350,
            }
        self.reply_bin_0 = b'\x01\x00\xb4\xee' b'\x00\x00\x00\x00' \
            b'\x75\x28\x46\x5a' b'\x4f\x7e\x00\x00' \
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
        self.req_bin_0 = b'\x6b\x00\x00\x03' b'\xa0\x2d\x9d\x82' \
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
        self.req_bin_0 = b'\x6c\x00\x00\x01'

        self.reply_args_0 = {
            'allow_exposures': 0,
            'interval': 8091,
            'prefer_blanking': 0,
            'sequence_number': 12877,
            'timeout': 20935,
            }
        self.reply_bin_0 = b'\x01\x00\x32\x4d' b'\x00\x00\x00\x00' \
            b'\x51\xc7\x1f\x9b' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x6d\x00\x00\x03' b'\x00\x00\x00\x04' \
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
        self.req_bin_0 = b'\x6e\x00\x00\x01'

        self.reply_args_0 = {
            'hosts': [{'name': [34, 23, 178, 12], 'family': 0}, {'name': [130, 236, 254, 15], 'family': 0}],
            'mode': 1,
            'sequence_number': 15164,
            }
        self.reply_bin_0 = b'\x01\x01\x3b\x3c' b'\x00\x00\x00\x04' \
            b'\x00\x02\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x04' b'\x22\x17\xb2\x0c' \
            b'\x00\x00\x00\x04' b'\x82\xec\xfe\x0f'


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
        self.req_bin_0 = b'\x6f\x01\x00\x01'


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
        self.req_bin_0 = b'\x70\x00\x00\x01'


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
        self.req_bin_0 = b'\x71\x00\x00\x02' b'\x26\xb1\xb4\x5e'


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
        self.req_bin_0 = b'\x72\x00\x00\x0f' b'\x10\x2a\xed\x21' \
            b'\x00\x0c\xd1\xa5' b'\x01\xd0\x9d\x12' \
            b'\x5a\xa1\x59\x87' b'\x44\x5f\x89\xe8' \
            b'\x10\x34\xde\xd6' b'\x23\x1d\xa2\x3d' \
            b'\x05\xd4\x75\x5c' b'\x7c\xb6\xb2\x45' \
            b'\x06\xfb\xb5\x63' b'\x46\xd5\x77\x72' \
            b'\x25\x65\xbb\xc6' b'\x59\x45\xf9\x12' \
            b'\x78\xd8\xed\xb2'


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
        self.req_bin_0 = b'\x73\x01\x00\x01'


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
        self.req_bin_0 = b'\x74\x05\x00\x03' b'\x9a\x83\xc8\xf8' \
            b'\xfa\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 22584,
            'status': 240,
            }
        self.reply_bin_0 = b'\x01\xf0\x58\x38' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x75\x00\x00\x01'

        self.reply_args_0 = {
            'map': [175, 141, 192, 250, 157],
            'sequence_number': 54134,
            }
        self.reply_bin_0 = b'\x01\x05\xd3\x76' b'\x00\x00\x00\x02' \
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
        self.req_bin_0 = b'\x76\x02\x00\x05' b'\x21\xcd\xfb\x25' \
            b'\x1b\x4d\x4c\x9b' b'\x2b\x7f\x3c\xd5' \
            b'\x73\xc2\xe6\xe2'

        self.reply_args_0 = {
            'sequence_number': 56627,
            'status': 204,
            }
        self.reply_bin_0 = b'\x01\xcc\xdd\x33' b'\x00\x00\x00\x00' \
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
        self.req_bin_0 = b'\x77\x00\x00\x01'

        self.reply_args_0 = {
            'keycodes': [[219, 156], [30, 50], [106, 108], [135, 41], [80, 122], [88, 38], [80, 1], [209, 230]],
            'sequence_number': 45434,
            }
        self.reply_bin_0 = b'\x01\x02\xb1\x7a' b'\x00\x00\x00\x04' \
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
        self.req_bin_0 = b'\x7f\x00\x00\x01'


    def testPackRequest0(self):
        bin = request.NoOperation._request.to_binary(*(), **self.req_args_0)
        self.assertBinaryEqual(bin, self.req_bin_0)

    def testUnpackRequest0(self):
        args, remain = request.NoOperation._request.parse_binary(self.req_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_0)


if __name__ == "__main__":
    unittest.main()
