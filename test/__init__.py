
import unittest
import binascii
import difflib
import struct
import array

import Xlib.protocol.event
import Xlib.protocol.rq


class CmpArray(object):

    def __init__(self, *args, **kws):
        self.array = array.array(*args, **kws)

    def __len__(self):
        return len(self.array)

    def __getitem__(self, key):
        if isinstance(key, slice):
            x = key.start
            y = key.stop
            return list(self.array[x:y])
        else:
            return self.array[key]

    def __getattr__(self, attr):
        return getattr(self.array, attr)

    def __eq__(self, other):
        return self.array.tolist() == other

Xlib.protocol.rq.array = CmpArray


class DummyDisplay(object):

    def get_resource_class(self, x):
        return None

    event_classes = Xlib.protocol.event.event_class


class TestCase(unittest.TestCase):

    def assertBinaryEqual(self, bin1, bin2):
        if bin1 != bin2:
            self.fail('binary contents differ:\n' + bindiff(bin1, bin2))

    def assertBinaryEmpty(self, bin):
        if len(bin) != 0:
            self.fail('binary content not empty:\n' + ''.join(tohex(bin)))

class BigEndianTest(TestCase):

    @classmethod
    def setUpClass(cls):
        if struct.unpack('BB', struct.pack('H', 0x0100))[0] != 1:
            raise unittest.SkipTest('big-endian tests, skipping on this system')

class LittleEndianTest(TestCase):

    @classmethod
    def setUpClass(cls):
        if struct.unpack('BB', struct.pack('H', 0x0100))[0] != 0:
            raise unittest.SkipTest('little-endian tests, skipping on this system')


def tohex(bin):
    hex = []
    for i in range(0, len(bin), 16):
        hex.append(str(binascii.hexlify(bin[i:i+16])) + '\n')
    return hex

def bindiff(bin1, bin2):
    hex1 = tohex(bin1)
    hex2 = tohex(bin2)
    return ''.join(difflib.ndiff(hex1, hex2))
