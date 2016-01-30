#!/usr/bin/env python

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from Xlib.protocol import rq

class Custom(rq.Card32):
    def check_value(self, value):
        return int(value)
    def parse_value(self, value, display):
        return str(value)

CustomObj = Custom(None)


class TestNestedStruct(unittest.TestCase):
    def setUp(self):
        self.s1 = rq.Struct(rq.Card32('a1'), rq.Card32('a2'))
        self.s2 = rq.Struct(rq.Object('b1', self.s1), rq.Object('b2', self.s1))
        self.s3 = rq.Struct(rq.Object('c1', self.s2), rq.Object('c2', self.s2))

    def testToBinary1(self):
        self.s1.to_binary(1, 2)

    def testToBinary2(self):
        self.s2.to_binary((1, 2), (3, 4))

    def testToBinary3(self):
        self.s3.to_binary(((1, 2), (3, 4)), ((5, 6), (7, 8)))

class TestNestedStructWithFancyValue(unittest.TestCase):
    def setUp(self):
        self.s1 = rq.Struct(Custom('a1'), Custom('a2'))
        self.s2 = rq.Struct(rq.Object('b1', self.s1), rq.Object('b2', self.s1))
        self.s3 = rq.Struct(rq.Object('c1', self.s2), rq.Object('c2', self.s2))

    def testToBinary1(self):
        self.s1.to_binary('1', '2')

    def testToBinary2(self):
        self.s2.to_binary(('1', '2'), ('3', '4'))

    def testToBinary3(self):
        self.s3.to_binary((('1', '2'), ('3', '4')), (('5', '6'), ('7', '8')))

class TestListWithFancyValue(unittest.TestCase):
    def setUp(self):
        self.s1 = rq.Struct(rq.LengthOf('l', 4), rq.List('l', CustomObj))

    def testToBinary1(self):
        self.s1.to_binary(['1', '2', '3'])

if __name__ == '__main__':
    unittest.main()
