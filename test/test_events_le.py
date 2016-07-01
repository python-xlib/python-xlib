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
            'data': [236, 252, 232, 206, 210, 131, 246, 234, 162, 151, 217, 167, 171, 128, 239, 200, 179, 146, 209, 131, 223, 155, 181, 171, 175, 220, 227, 200, 138, 134, 148],
            'type': 207,
            }
        self.evt_bin_0 = b'\xcf\xec\xfc\xe8' b'\xce\xd2\x83\xf6' \
            b'\xea\xa2\x97\xd9' b'\xa7\xab\x80\xef' \
            b'\xc8\xb3\x92\xd1' b'\x83\xdf\x9b\xb5' \
            b'\xab\xaf\xdc\xe3' b'\xc8\x8a\x86\x94'


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
            'count': 7686,
            'height': 49538,
            'sequence_number': 18018,
            'type': 214,
            'width': 18088,
            'window': 1421524673,
            'x': 31959,
            'y': 29112,
            }
        self.evt_bin_0 = b'\xd6\x00\x62\x46' b'\xc1\xbe\xba\x54' \
            b'\xd7\x7c\xb8\x71' b'\xa8\x46\x82\xc1' \
            b'\x06\x1e\x00\x00' b'\x00\x00\x00\x00' \
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
            'count': 757,
            'drawable': 1457059207,
            'height': 26058,
            'major_event': 166,
            'minor_event': 39379,
            'sequence_number': 18746,
            'type': 183,
            'width': 3220,
            'x': 32023,
            'y': 43806,
            }
        self.evt_bin_0 = b'\xb7\x00\x3a\x49' b'\x87\xf5\xd8\x56' \
            b'\x17\x7d\x1e\xab' b'\x94\x0c\xca\x65' \
            b'\xd3\x99\xf5\x02' b'\xa6\x00\x00\x00' \
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
            'major_event': 128,
            'minor_event': 21675,
            'sequence_number': 9214,
            'type': 155,
            'window': 548772746,
            }
        self.evt_bin_0 = b'\x9b\x00\xfe\x23' b'\x8a\x9b\xb5\x20' \
            b'\xab\x54\x80\x00' b'\x00\x00\x00\x00' \
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
            'sequence_number': 11725,
            'state': 218,
            'type': 223,
            'window': 816529890,
            }
        self.evt_bin_0 = b'\xdf\x00\xcd\x2d' b'\xe2\x41\xab\x30' \
            b'\xda\x00\x00\x00' b'\x00\x00\x00\x00' \
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
            'border_width': 56534,
            'height': 60389,
            'override': 1,
            'parent': 1731314417,
            'sequence_number': 54657,
            'type': 192,
            'width': 1479,
            'window': 154841762,
            'x': -4750,
            'y': -31393,
            }
        self.evt_bin_0 = b'\xc0\x00\x81\xd5' b'\xf1\xc2\x31\x67' \
            b'\xa2\xb2\x3a\x09' b'\x72\xed\x5f\x85' \
            b'\xc7\x05\xe5\xeb' b'\xd6\xdc\x01\x00' \
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
            'event': 897029110,
            'sequence_number': 46572,
            'type': 201,
            'window': 247390922,
            }
        self.evt_bin_0 = b'\xc9\x00\xec\xb5' b'\xf6\x93\x77\x35' \
            b'\xca\xe2\xbe\x0e' b'\x00\x00\x00\x00' \
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
            'event': 1720839242,
            'from_configure': 1,
            'sequence_number': 21456,
            'type': 130,
            'window': 1327438921,
            }
        self.evt_bin_0 = b'\x82\x00\xd0\x53' b'\x4a\xec\x91\x66' \
            b'\x49\x1c\x1f\x4f' b'\x01\x00\x00\x00' \
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
            'event': 1813526544,
            'override': 1,
            'sequence_number': 6009,
            'type': 245,
            'window': 522567740,
            }
        self.evt_bin_0 = b'\xf5\x00\x79\x17' b'\x10\x38\x18\x6c' \
            b'\x3c\xc0\x25\x1f' b'\x01\x00\x00\x00' \
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
            'parent': 666354749,
            'sequence_number': 26091,
            'type': 195,
            'window': 729142504,
            }
        self.evt_bin_0 = b'\xc3\x00\xeb\x65' b'\x3d\xc4\xb7\x27' \
            b'\xe8\xd4\x75\x2b' b'\x00\x00\x00\x00' \
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
            'event': 1096286586,
            'override': 1,
            'parent': 1095145830,
            'sequence_number': 11231,
            'type': 170,
            'window': 244928407,
            'x': -3314,
            'y': -21409,
            }
        self.evt_bin_0 = b'\xaa\x00\xdf\x2b' b'\x7a\x01\x58\x41' \
            b'\x97\x4f\x99\x0e' b'\x66\x99\x46\x41' \
            b'\x0e\xf3\x5f\xac' b'\x01\x00\x00\x00' \
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
            'above_sibling': 423690578,
            'border_width': 50707,
            'event': 507433541,
            'height': 11820,
            'override': 0,
            'sequence_number': 53461,
            'type': 232,
            'width': 43047,
            'window': 314542502,
            'x': -13183,
            'y': -8052,
            }
        self.evt_bin_0 = b'\xe8\x00\xd5\xd0' b'\x45\xd2\x3e\x1e' \
            b'\xa6\x89\xbf\x12' b'\x52\x01\x41\x19' \
            b'\x81\xcc\x8c\xe0' b'\x27\xa8\x2c\x2e' \
            b'\x13\xc6\x00\x00' b'\x00\x00\x00\x00'


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
            'border_width': 4713,
            'height': 10110,
            'parent': 1984611127,
            'sequence_number': 29560,
            'sibling': 1364316652,
            'stack_mode': 225,
            'type': 224,
            'value_mask': 29123,
            'width': 41200,
            'window': 1212265415,
            'x': -12463,
            'y': -4669,
            }
        self.evt_bin_0 = b'\xe0\xe1\x78\x73' b'\x37\xc3\x4a\x76' \
            b'\xc7\xb3\x41\x48' b'\xec\xd1\x51\x51' \
            b'\x51\xcf\xc3\xed' b'\xf0\xa0\x7e\x27' \
            b'\x69\x12\xc3\x71' b'\x00\x00\x00\x00'


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
            'event': 120690564,
            'sequence_number': 18186,
            'type': 166,
            'window': 1089529951,
            'x': -22676,
            'y': -18075,
            }
        self.evt_bin_0 = b'\xa6\x00\x0a\x47' b'\x84\x97\x31\x07' \
            b'\x5f\xe8\xf0\x40' b'\x6c\xa7\x65\xb9' \
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
            'height': 56089,
            'sequence_number': 54549,
            'type': 135,
            'width': 56674,
            'window': 164839077,
            }
        self.evt_bin_0 = b'\x87\x00\x15\xd5' b'\xa5\x3e\xd3\x09' \
            b'\x62\xdd\x19\xdb' b'\x00\x00\x00\x00' \
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
            'atom': 1190414551,
            'sequence_number': 33357,
            'state': 242,
            'time': 1700429414,
            'type': 206,
            'window': 993700932,
            }
        self.evt_bin_0 = b'\xce\x00\x4d\x82' b'\x44\xac\x3a\x3b' \
            b'\xd7\x48\xf4\x46' b'\x66\x7e\x5a\x65' \
            b'\xf2\x00\x00\x00' b'\x00\x00\x00\x00' \
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
            'atom': 1021439924,
            'sequence_number': 53120,
            'time': 1399833091,
            'type': 185,
            'window': 690517929,
            }
        self.evt_bin_0 = b'\xb9\x00\x80\xcf' b'\x03\xc2\x6f\x53' \
            b'\xa9\x77\x28\x29' b'\xb4\xef\xe1\x3c' \
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
            'owner': 1930866783,
            'property': 370621667,
            'requestor': 737570035,
            'selection': 1533999683,
            'sequence_number': 4295,
            'target': 1083543199,
            'time': 222327341,
            'type': 147,
            }
        self.evt_bin_0 = b'\x93\x00\xc7\x10' b'\x2d\x72\x40\x0d' \
            b'\x5f\xb0\x16\x73' b'\xf3\x6c\xf6\x2b' \
            b'\x43\xfa\x6e\x5b' b'\x9f\x8e\x95\x40' \
            b'\xe3\x3c\x17\x16' b'\x00\x00\x00\x00'


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
            'property': 607556330,
            'requestor': 1122624134,
            'selection': 340960018,
            'sequence_number': 28832,
            'target': 800734635,
            'time': 943687849,
            'type': 159,
            }
        self.evt_bin_0 = b'\x9f\x00\xa0\x70' b'\xa9\x88\x3f\x38' \
            b'\x86\xe2\xe9\x42' b'\x12\xa3\x52\x14' \
            b'\xab\x3d\xba\x2f' b'\xea\x92\x36\x24' \
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
            'colormap': 1694865742,
            'new': 1,
            'sequence_number': 22344,
            'state': 136,
            'type': 180,
            'window': 1283976465,
            }
        self.evt_bin_0 = b'\xb4\x00\x48\x57' b'\x11\xed\x87\x4c' \
            b'\x4e\x99\x05\x65' b'\x01\x88\x00\x00' \
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
            'client_type': 1554224294,
            'data': (8, '01234567890123456789'),
            'sequence_number': 44540,
            'type': 140,
            'window': 610247893,
            }
        self.evt_bin_0 = b'\x8c\x08\xfc\xad' b'\xd5\xa4\x5f\x24' \
            b'\xa6\x94\xa3\x5c' b'\x30\x31\x32\x33' \
            b'\x34\x35\x36\x37' b'\x38\x39\x30\x31' \
            b'\x32\x33\x34\x35' b'\x36\x37\x38\x39'

        self.evt_args_1 = {
            'client_type': 715933209,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'sequence_number': 59422,
            'type': 212,
            'window': 1875362098,
            }
        self.evt_bin_1 = b'\xd4\x10\x1e\xe8' b'\x32\xc1\xc7\x6f' \
            b'\x19\x46\xac\x2a' b'\x01\x00\x02\x00' \
            b'\x03\x00\x04\x00' b'\x05\x00\x06\x00' \
            b'\x07\x00\x08\x00' b'\x09\x00\x0a\x00'

        self.evt_args_2 = {
            'client_type': 2078114542,
            'data': (32, [1, 2, 3, 4, 5]),
            'sequence_number': 9488,
            'type': 202,
            'window': 751277030,
            }
        self.evt_bin_2 = b'\xca\x20\x10\x25' b'\xe6\x93\xc7\x2c' \
            b'\xee\x82\xdd\x7b' b'\x01\x00\x00\x00' \
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
            'count': 167,
            'first_keycode': 248,
            'request': 204,
            'sequence_number': 25843,
            'type': 217,
            }
        self.evt_bin_0 = b'\xd9\x00\xf3\x64' b'\xcc\xf8\xa7\x00' \
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
