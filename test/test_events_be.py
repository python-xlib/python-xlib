#!/usr/bin/env python2

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(__file__, '../..')))

import unittest
from Xlib.protocol import request, event
from . import BigEndianTest as EndianTest
from . import DummyDisplay

dummy_display = DummyDisplay()


class TestKeymapNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'data': [248, 202, 136, 187, 201, 200, 244, 146, 187, 195, 178, 236, 157, 185, 166, 196, 164, 146, 143, 170, 206, 201, 240, 159, 247, 205, 231, 197, 254, 240, 148],
            'type': 138,
            }
        self.evt_bin_0 = b'\x8a\xf8\xca\x88' b'\xbb\xc9\xc8\xf4' \
            b'\x92\xbb\xc3\xb2' b'\xec\x9d\xb9\xa6' \
            b'\xc4\xa4\x92\x8f' b'\xaa\xce\xc9\xf0' \
            b'\x9f\xf7\xcd\xe7' b'\xc5\xfe\xf0\x94'


    def testPack0(self):
        bin = event.KeymapNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.KeymapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestExpose(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'count': 15258,
            'height': 6241,
            'sequence_number': 48394,
            'type': 238,
            'width': 1951,
            'window': 692245859,
            'x': 39820,
            'y': 16664,
            }
        self.evt_bin_0 = b'\xee\x00\xbd\x0a' b'\x29\x42\xd5\x63' \
            b'\x9b\x8c\x41\x18' b'\x07\x9f\x18\x61' \
            b'\x3b\x9a\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.Expose._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.Expose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestGraphicsExpose(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'count': 49818,
            'drawable': 1443779242,
            'height': 2892,
            'major_event': 172,
            'minor_event': 50267,
            'sequence_number': 50375,
            'type': 133,
            'width': 38020,
            'x': 54088,
            'y': 17918,
            }
        self.evt_bin_0 = b'\x85\x00\xc4\xc7' b'\x56\x0e\x52\xaa' \
            b'\xd3\x48\x45\xfe' b'\x94\x84\x0b\x4c' \
            b'\xc4\x5b\xc2\x9a' b'\xac\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.GraphicsExpose._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.GraphicsExpose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestNoExpose(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'major_event': 199,
            'minor_event': 29237,
            'sequence_number': 34266,
            'type': 248,
            'window': 1399171519,
            }
        self.evt_bin_0 = b'\xf8\x00\x85\xda' b'\x53\x65\xa9\xbf' \
            b'\x72\x35\xc7\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.NoExpose._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.NoExpose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestVisibilityNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 38616,
            'state': 253,
            'type': 174,
            'window': 936121409,
            }
        self.evt_bin_0 = b'\xae\x00\x96\xd8' b'\x37\xcc\x14\x41' \
            b'\xfd\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.VisibilityNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.VisibilityNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestCreateNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'border_width': 56468,
            'height': 7111,
            'override': 0,
            'parent': 747306217,
            'sequence_number': 31058,
            'type': 151,
            'width': 44173,
            'window': 876986399,
            'x': -21847,
            'y': -22248,
            }
        self.evt_bin_0 = b'\x97\x00\x79\x52' b'\x2c\x8a\xfc\xe9' \
            b'\x34\x45\xc0\x1f' b'\xaa\xa9\xa9\x18' \
            b'\xac\x8d\x1b\xc7' b'\xdc\x94\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.CreateNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.CreateNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestDestroyNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'event': 1489718405,
            'sequence_number': 27233,
            'type': 212,
            'window': 1064077163,
            }
        self.evt_bin_0 = b'\xd4\x00\x6a\x61' b'\x58\xcb\x4c\x85' \
            b'\x3f\x6c\x87\x6b' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.DestroyNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.DestroyNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestUnmapNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'event': 2029853215,
            'from_configure': 0,
            'sequence_number': 43679,
            'type': 201,
            'window': 860030193,
            }
        self.evt_bin_0 = b'\xc9\x00\xaa\x9f' b'\x78\xfd\x1a\x1f' \
            b'\x33\x43\x04\xf1' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.UnmapNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.UnmapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestMapNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'event': 675485985,
            'override': 1,
            'sequence_number': 6027,
            'type': 244,
            'window': 542087937,
            }
        self.evt_bin_0 = b'\xf4\x00\x17\x8b' b'\x28\x43\x19\x21' \
            b'\x20\x4f\x9b\x01' b'\x01\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MapNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.MapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestMapRequest(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'parent': 1659099581,
            'sequence_number': 63838,
            'type': 157,
            'window': 868024861,
            }
        self.evt_bin_0 = b'\x9d\x00\xf9\x5e' b'\x62\xe3\xd9\xbd' \
            b'\x33\xbd\x02\x1d' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MapRequest._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.MapRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestReparentNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'event': 1867017989,
            'override': 0,
            'parent': 992152190,
            'sequence_number': 43356,
            'type': 128,
            'window': 1165276406,
            'x': -19227,
            'y': -30992,
            }
        self.evt_bin_0 = b'\x80\x00\xa9\x5c' b'\x6f\x48\x6f\x05' \
            b'\x45\x74\xb4\xf6' b'\x3b\x23\x0a\x7e' \
            b'\xb4\xe5\x86\xf0' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ReparentNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.ReparentNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestConfigureNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'above_sibling': 1343120585,
            'border_width': 17757,
            'event': 1624514845,
            'height': 13596,
            'override': 0,
            'sequence_number': 41060,
            'type': 220,
            'width': 3638,
            'window': 1070571314,
            'x': -18284,
            'y': -7865,
            }
        self.evt_bin_0 = b'\xdc\x00\xa0\x64' b'\x60\xd4\x21\x1d' \
            b'\x3f\xcf\x9f\x32' b'\x50\x0e\x64\xc9' \
            b'\xb8\x94\xe1\x47' b'\x0e\x36\x35\x1c' \
            b'\x45\x5d\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ConfigureNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.ConfigureNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestConfigureRequest(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'border_width': 52639,
            'height': 40159,
            'parent': 1499546058,
            'sequence_number': 57983,
            'sibling': 260826075,
            'stack_mode': 240,
            'type': 201,
            'value_mask': 15938,
            'width': 41545,
            'window': 1040976198,
            'x': -31823,
            'y': -880,
            }
        self.evt_bin_0 = b'\xc9\xf0\xe2\x7f' b'\x59\x61\x41\xca' \
            b'\x3e\x0c\x09\x46' b'\x0f\x8b\xe3\xdb' \
            b'\x83\xb1\xfc\x90' b'\xa2\x49\x9c\xdf' \
            b'\xcd\x9f\x3e\x42' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ConfigureRequest._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.ConfigureRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestGravityNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'event': 1182983311,
            'sequence_number': 20621,
            'type': 168,
            'window': 29431224,
            'x': -14672,
            'y': -19399,
            }
        self.evt_bin_0 = b'\xa8\x00\x50\x8d' b'\x46\x82\xe4\x8f' \
            b'\x01\xc1\x15\xb8' b'\xc6\xb0\xb4\x39' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.GravityNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.GravityNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestResizeRequest(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'height': 60085,
            'sequence_number': 14981,
            'type': 151,
            'width': 55398,
            'window': 2130921516,
            }
        self.evt_bin_0 = b'\x97\x00\x3a\x85' b'\x7f\x03\x48\x2c' \
            b'\xd8\x66\xea\xb5' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ResizeRequest._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.ResizeRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestPropertyNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'atom': 252322161,
            'sequence_number': 30497,
            'state': 167,
            'time': 1391011497,
            'type': 157,
            'window': 2033863003,
            }
        self.evt_bin_0 = b'\x9d\x00\x77\x21' b'\x79\x3a\x49\x5b' \
            b'\x0f\x0a\x21\x71' b'\x52\xe9\x26\xa9' \
            b'\xa7\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.PropertyNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.PropertyNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestSelectionClear(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'atom': 1092859866,
            'sequence_number': 61378,
            'time': 1538959461,
            'type': 255,
            'window': 626833463,
            }
        self.evt_bin_0 = b'\xff\x00\xef\xc2' b'\x5b\xba\xa8\x65' \
            b'\x25\x5c\xb8\x37' b'\x41\x23\xb7\xda' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionClear._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.SelectionClear._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestSelectionRequest(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'owner': 1036225485,
            'property': 981007010,
            'requestor': 2105124856,
            'selection': 1014149797,
            'sequence_number': 27485,
            'target': 523473665,
            'time': 1792621552,
            'type': 197,
            }
        self.evt_bin_0 = b'\xc5\x00\x6b\x5d' b'\x6a\xd9\x3b\xf0' \
            b'\x3d\xc3\x8b\xcd' b'\x7d\x79\xa7\xf8' \
            b'\x3c\x72\xb2\xa5' b'\x1f\x33\x93\x01' \
            b'\x3a\x78\xfa\xa2' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionRequest._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.SelectionRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestSelectionNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'property': 1602716574,
            'requestor': 1979762314,
            'selection': 1287219120,
            'sequence_number': 25394,
            'target': 1091504539,
            'time': 409398186,
            'type': 165,
            }
        self.evt_bin_0 = b'\xa5\x00\x63\x32' b'\x18\x66\xeb\xaa' \
            b'\x76\x00\xc6\x8a' b'\x4c\xb9\x67\xb0' \
            b'\x41\x0f\x09\x9b' b'\x5f\x87\x83\x9e' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.SelectionNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestColormapNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'colormap': 593302316,
            'new': 1,
            'sequence_number': 56880,
            'state': 215,
            'type': 162,
            'window': 149981547,
            }
        self.evt_bin_0 = b'\xa2\x00\xde\x30' b'\x08\xf0\x89\x6b' \
            b'\x23\x5d\x13\x2c' b'\x01\xd7\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ColormapNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.ColormapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


class TestClientMessage(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'client_type': 607457628,
            'data': (8, b'01234567890123456789'),
            'sequence_number': 54031,
            'type': 196,
            'window': 5574388,
            }
        self.evt_bin_0 = b'\xc4\x08\xd3\x0f' b'\x00\x55\x0e\xf4' \
            b'\x24\x35\x11\x5c' b'\x30\x31\x32\x33' \
            b'\x34\x35\x36\x37' b'\x38\x39\x30\x31' \
            b'\x32\x33\x34\x35' b'\x36\x37\x38\x39'

        self.evt_args_1 = {
            'client_type': 1245441508,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'sequence_number': 55140,
            'type': 204,
            'window': 1260504694,
            }
        self.evt_bin_1 = b'\xcc\x10\xd7\x64' b'\x4b\x21\xc6\x76' \
            b'\x4a\x3b\xed\xe4' b'\x00\x01\x00\x02' \
            b'\x00\x03\x00\x04' b'\x00\x05\x00\x06' \
            b'\x00\x07\x00\x08' b'\x00\x09\x00\x0a'

        self.evt_args_2 = {
            'client_type': 959018764,
            'data': (32, [1, 2, 3, 4, 5]),
            'sequence_number': 56961,
            'type': 253,
            'window': 319171761,
            }
        self.evt_bin_2 = b'\xfd\x20\xde\x81' b'\x13\x06\x2c\xb1' \
            b'\x39\x29\x77\x0c' b'\x00\x00\x00\x01' \
            b'\x00\x00\x00\x02' b'\x00\x00\x00\x03' \
            b'\x00\x00\x00\x04' b'\x00\x00\x00\x05'


    def testPack0(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)

    def testPack1(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_1)
        self.assertBinaryEqual(bin, self.evt_bin_1)

    def testUnpack1(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_1, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_1)

    def testPack2(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_2)
        self.assertBinaryEqual(bin, self.evt_bin_2)

    def testUnpack2(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_2, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_2)


class TestMappingNotify(EndianTest):
    def setUp(self):
        self.evt_args_0 = {
            'count': 244,
            'first_keycode': 224,
            'request': 213,
            'sequence_number': 22874,
            'type': 251,
            }
        self.evt_bin_0 = b'\xfb\x00\x59\x5a' b'\xd5\xe0\xf4\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MappingNotify._fields.to_binary(*(), **self.evt_args_0)
        self.assertBinaryEqual(bin, self.evt_bin_0)

    def testUnpack0(self):
        args, remain = event.MappingNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_0)


if __name__ == "__main__":
    unittest.main()
