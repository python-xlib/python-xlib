#!/usr/bin/env python2

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(__file__, '../..')))

import unittest
from Xlib.protocol import request, event
from . import LittleEndianTest as EndianTest
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
        self.evt_bin_0 = b'\xee\x00\x0a\xbd' b'\x63\xd5\x42\x29' \
            b'\x8c\x9b\x18\x41' b'\x9f\x07\x61\x18' \
            b'\x9a\x3b\x00\x00' b'\x00\x00\x00\x00' \
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
        self.evt_bin_0 = b'\x85\x00\xc7\xc4' b'\xaa\x52\x0e\x56' \
            b'\x48\xd3\xfe\x45' b'\x84\x94\x4c\x0b' \
            b'\x5b\xc4\x9a\xc2' b'\xac\x00\x00\x00' \
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
        self.evt_bin_0 = b'\xf8\x00\xda\x85' b'\xbf\xa9\x65\x53' \
            b'\x35\x72\xc7\x00' b'\x00\x00\x00\x00' \
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
        self.evt_bin_0 = b'\xae\x00\xd8\x96' b'\x41\x14\xcc\x37' \
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
        self.evt_bin_0 = b'\x97\x00\x52\x79' b'\xe9\xfc\x8a\x2c' \
            b'\x1f\xc0\x45\x34' b'\xa9\xaa\x18\xa9' \
            b'\x8d\xac\xc7\x1b' b'\x94\xdc\x00\x00' \
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
        self.evt_bin_0 = b'\xd4\x00\x61\x6a' b'\x85\x4c\xcb\x58' \
            b'\x6b\x87\x6c\x3f' b'\x00\x00\x00\x00' \
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
        self.evt_bin_0 = b'\xc9\x00\x9f\xaa' b'\x1f\x1a\xfd\x78' \
            b'\xf1\x04\x43\x33' b'\x00\x00\x00\x00' \
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
        self.evt_bin_0 = b'\xf4\x00\x8b\x17' b'\x21\x19\x43\x28' \
            b'\x01\x9b\x4f\x20' b'\x01\x00\x00\x00' \
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
        self.evt_bin_0 = b'\x9d\x00\x5e\xf9' b'\xbd\xd9\xe3\x62' \
            b'\x1d\x02\xbd\x33' b'\x00\x00\x00\x00' \
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
        self.evt_bin_0 = b'\x80\x00\x5c\xa9' b'\x05\x6f\x48\x6f' \
            b'\xf6\xb4\x74\x45' b'\x7e\x0a\x23\x3b' \
            b'\xe5\xb4\xf0\x86' b'\x00\x00\x00\x00' \
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
        self.evt_bin_0 = b'\xdc\x00\x64\xa0' b'\x1d\x21\xd4\x60' \
            b'\x32\x9f\xcf\x3f' b'\xc9\x64\x0e\x50' \
            b'\x94\xb8\x47\xe1' b'\x36\x0e\x1c\x35' \
            b'\x5d\x45\x00\x00' b'\x00\x00\x00\x00'


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
        self.evt_bin_0 = b'\xc9\xf0\x7f\xe2' b'\xca\x41\x61\x59' \
            b'\x46\x09\x0c\x3e' b'\xdb\xe3\x8b\x0f' \
            b'\xb1\x83\x90\xfc' b'\x49\xa2\xdf\x9c' \
            b'\x9f\xcd\x42\x3e' b'\x00\x00\x00\x00'


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
        self.evt_bin_0 = b'\xa8\x00\x8d\x50' b'\x8f\xe4\x82\x46' \
            b'\xb8\x15\xc1\x01' b'\xb0\xc6\x39\xb4' \
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
        self.evt_bin_0 = b'\x97\x00\x85\x3a' b'\x2c\x48\x03\x7f' \
            b'\x66\xd8\xb5\xea' b'\x00\x00\x00\x00' \
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
        self.evt_bin_0 = b'\x9d\x00\x21\x77' b'\x5b\x49\x3a\x79' \
            b'\x71\x21\x0a\x0f' b'\xa9\x26\xe9\x52' \
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
        self.evt_bin_0 = b'\xff\x00\xc2\xef' b'\x65\xa8\xba\x5b' \
            b'\x37\xb8\x5c\x25' b'\xda\xb7\x23\x41' \
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
        self.evt_bin_0 = b'\xc5\x00\x5d\x6b' b'\xf0\x3b\xd9\x6a' \
            b'\xcd\x8b\xc3\x3d' b'\xf8\xa7\x79\x7d' \
            b'\xa5\xb2\x72\x3c' b'\x01\x93\x33\x1f' \
            b'\xa2\xfa\x78\x3a' b'\x00\x00\x00\x00'


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
        self.evt_bin_0 = b'\xa5\x00\x32\x63' b'\xaa\xeb\x66\x18' \
            b'\x8a\xc6\x00\x76' b'\xb0\x67\xb9\x4c' \
            b'\x9b\x09\x0f\x41' b'\x9e\x83\x87\x5f' \
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
        self.evt_bin_0 = b'\xa2\x00\x30\xde' b'\x6b\x89\xf0\x08' \
            b'\x2c\x13\x5d\x23' b'\x01\xd7\x00\x00' \
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
        self.evt_bin_0 = b'\xc4\x08\x0f\xd3' b'\xf4\x0e\x55\x00' \
            b'\x5c\x11\x35\x24' b'\x30\x31\x32\x33' \
            b'\x34\x35\x36\x37' b'\x38\x39\x30\x31' \
            b'\x32\x33\x34\x35' b'\x36\x37\x38\x39'

        self.evt_args_1 = {
            'client_type': 1245441508,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'sequence_number': 55140,
            'type': 204,
            'window': 1260504694,
            }
        self.evt_bin_1 = b'\xcc\x10\x64\xd7' b'\x76\xc6\x21\x4b' \
            b'\xe4\xed\x3b\x4a' b'\x01\x00\x02\x00' \
            b'\x03\x00\x04\x00' b'\x05\x00\x06\x00' \
            b'\x07\x00\x08\x00' b'\x09\x00\x0a\x00'

        self.evt_args_2 = {
            'client_type': 959018764,
            'data': (32, [1, 2, 3, 4, 5]),
            'sequence_number': 56961,
            'type': 253,
            'window': 319171761,
            }
        self.evt_bin_2 = b'\xfd\x20\x81\xde' b'\xb1\x2c\x06\x13' \
            b'\x0c\x77\x29\x39' b'\x01\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x04\x00\x00\x00' b'\x05\x00\x00\x00'


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
        self.evt_bin_0 = b'\xfb\x00\x5a\x59' b'\xd5\xe0\xf4\x00' \
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
