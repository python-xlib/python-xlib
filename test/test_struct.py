
from collections import OrderedDict
from functools import partial
import struct
import types
import re

from six import binary_type, iterbytes

from Xlib.protocol import rq
from . import DummyDisplay, TestCase


dummy_display = DummyDisplay()

def pack(format, *args):
    return struct.pack('=' + format, *args)

def packstr(s, padding=0):
    return s.encode() + (b'\0' * padding)


class StructTest(object):
    """ Test class helper for rq.Struct packing/unpacking support. """

    struct = None
    values_in = None
    binary = None
    values_out = None

    def test_pack_value_dict(self):
        self.assertBinaryEqual(self.struct.pack_value(dict(self.values_in)), self.binary)

    def test_pack_value_tuple(self):
        self.assertBinaryEqual(self.struct.pack_value(tuple(self.values_in.values())), self.binary)

    def test_to_binary_args(self):
        self.assertBinaryEqual(self.struct.to_binary(*self.values_in.values()), self.binary)

    def test_to_binary_kwargs(self):
        self.assertBinaryEqual(self.struct.to_binary(**dict(self.values_in)), self.binary)

    def test_parse_binary(self):
        values, remain = self.struct.parse_binary(self.binary, dummy_display)
        self.assertEqual(values, rq.DictWrapper(dict(self.values_out)))
        self.assertBinaryEmpty(remain)


def _struct_test(name, fields):
    """ Generate a new Struct packing/unpacking test.

    <fields> is a list of (field_name, field_type, field_value, field_binary):
        - field_name:
            name of the field, None if it's not a named field (e.g. LengthOf)
        - field_type:
            factory for the field type, taking one parameter only, the name of
            the field and returning a rq.Field subclass instance
        - field_value_in:
            the raw value passed in when packing and expected output on unpacking
        - field_binary:
            the binary representation of the field value or a function to
            convert it to binary for creating the expected result of packing
            the struct
        - field_value_out:
            the raw value passed expected on output on unpacking
            (optional, <field_value_in> is used if not specified)
    """

    class_name = ''.join([part.capitalize() for part in re.sub(r'[^\w]+', ' ', name).split()])
    class_name += 'StructTest'
    struct_layout = []
    values_in = OrderedDict()
    binary = b''
    values_out = OrderedDict()
    for field_params in fields:
        assert 4 <= len(field_params) <= 5
        field_name, field_type, field_value_in, field_binary = field_params[0:4]
        if len(field_params) == 5:
            field_value_out = field_params[4]
        else:
            field_value_out = field_value_in
        struct_layout.append(field_type(field_name))
        if field_name is not None:
            if field_value_in is not None:
                values_in[field_name] = field_value_in
            if field_value_out is not None:
                values_out[field_name] = field_value_out
        if isinstance(field_binary, binary_type):
            binary += field_binary
        elif isinstance(field_binary, (types.FunctionType, types.LambdaType, partial)):
            binary += field_binary(field_value_in)
        else:
            raise ValueError('unsupported type for binary: {data} [{type}]'.format(
                data=str(field_binary), type=type(field_binary))
            )
    class_dict = {
        'struct': rq.Struct(*struct_layout),
        'values_in': values_in,
        'binary': binary,
        'values_out': values_out,
    }
    globals()[class_name] = type(class_name, (StructTest, TestCase), class_dict)


_struct_test('card', (
    ('c8' , rq.Card8 , 0x42      , partial(pack, 'B')),
    ('c16', rq.Card16, 0x666     , partial(pack, 'H')),
    ('c32', rq.Card32, 0xdeadbeef, partial(pack, 'L')),
))

_struct_test('int', (
    ('i8' , rq.Int8 , -42        , partial(pack, 'b')),
    ('i16', rq.Int16, -666       , partial(pack, 'h')),
    ('i32', rq.Int32, -2147483648, partial(pack, 'l')),
))

_struct_test('list', (
    (None   , lambda name: rq.LengthOf('lc8', 1)          , None                                   , pack('B', 2)              ),
    (None   , lambda name: rq.LengthOf('lc16', 2)         , None                                   , pack('H', 3)              ),
    (None   , lambda name: rq.LengthOf('lc32', 4)         , None                                   , pack('L', 5)              ),
    ('lc8'  , lambda name: rq.List(name, rq.Card8 , pad=0), [0x42, 0xc3]                           , lambda v: pack('2B'  , *v)),
    ('lc16' , lambda name: rq.List(name, rq.Card16, pad=0), [666, 1, 60143]                        , lambda v: pack('3H'  , *v)),
    ('lc32' , lambda name: rq.List(name, rq.Card32, pad=0), [0xf02facb, 666, 1, 0x1043, 0xdeadbeef], lambda v: pack('5L'  , *v)),
))

_struct_test('list pad', (
    (None   , lambda name: rq.LengthOf('lc8', 1)          , None                                   , pack('B', 2)              ),
    (None   , lambda name: rq.LengthOf('lc16', 2)         , None                                   , pack('H', 3)              ),
    (None   , lambda name: rq.LengthOf('lc32', 4)         , None                                   , pack('L', 5)              ),
    ('lc8'  , lambda name: rq.List(name, rq.Card8 , pad=1), [0x42, 0xc3]                           , lambda v: pack('2B2x', *v)),
    ('lc16' , lambda name: rq.List(name, rq.Card16, pad=1), [666, 1, 60143]                        , lambda v: pack('3H2x', *v)),
    ('lc32' , lambda name: rq.List(name, rq.Card32, pad=1), [0xf02facb, 666, 1, 0x1043, 0xdeadbeef], lambda v: pack('5L'  , *v)),
))

_struct_test('fixed list', (
    ('lc8'  , lambda name: rq.FixedList(name, 2, rq.Card8 , pad=0), [0x42, 0xc3]                           , lambda v: pack('2B'  , *v)),
    ('lc16' , lambda name: rq.FixedList(name, 3, rq.Card16, pad=0), [666, 1, 60143]                        , lambda v: pack('3H'  , *v)),
    ('lc32' , lambda name: rq.FixedList(name, 5, rq.Card32, pad=0), [0xf02facb, 666, 1, 0x1043, 0xdeadbeef], lambda v: pack('5L'  , *v)),
))

_struct_test('fixed list pad', (
    ('lc8p' , lambda name: rq.FixedList(name, 2, rq.Card8 , pad=1), [0x42, 0xc3]                           , lambda v: pack('2B2x', *v)),
    ('lc16p', lambda name: rq.FixedList(name, 3, rq.Card16, pad=1), [666, 1, 60143]                        , lambda v: pack('3H2x', *v)),
    ('lc32p', lambda name: rq.FixedList(name, 5, rq.Card32, pad=1), [0xf02facb, 666, 1, 0x1043, 0xdeadbeef], lambda v: pack('5L'  , *v)),
))

_struct_test('string8', (
    (None, lambda name: rq.LengthOf('s1', 1)   , None                                , pack('B', 7) ),
    (None, lambda name: rq.LengthOf('s2', 2)   , None                                , pack('H', 13)),
    (None, lambda name: rq.LengthOf('s3', 4)   , None                                , pack('L', 34)),
    ('s1', lambda name: rq.String8(name, pad=0), "testing"                           , packstr      ),
    ('s2', lambda name: rq.String8(name, pad=0), "one two three"                     , packstr      ),
    ('s3', lambda name: rq.String8(name, pad=0), "supercalifragilisticexpialidocious", packstr      ),
))

_struct_test('string8 pad', (
    (None, lambda name: rq.LengthOf('s1', 1)   , None                                , pack('B', 7)               ),
    (None, lambda name: rq.LengthOf('s2', 2)   , None                                , pack('H', 13)              ),
    (None, lambda name: rq.LengthOf('s3', 4)   , None                                , pack('L', 34)              ),
    ('s1', lambda name: rq.String8(name, pad=1), "testing"                           , partial(packstr, padding=1)),
    ('s2', lambda name: rq.String8(name, pad=1), "one two three"                     , partial(packstr, padding=3)),
    ('s3', lambda name: rq.String8(name, pad=1), "supercalifragilisticexpialidocious", partial(packstr, padding=2)),
))

_struct_test('simple string16', (
    (None, lambda name: rq.LengthOf('s1', 1)   , None            , pack('B', 3) ),
    (None, lambda name: rq.LengthOf('s2', 2)   , None            , pack('H', 3) ),
    ('s1', lambda name: rq.String16(name, pad=0), (0, 1, 2), lambda s: struct.pack('>' + 'H' * len(s), *s)),
    # An 8-bits string is also allowed on input.
    ('s2', lambda name: rq.String16(name, pad=0), b'\x03\x04\x05', lambda s: struct.pack('>' + 'H' * len(s), *iterbytes(s)), (3, 4, 5)),
))

_struct_test('binary', (
    (None, lambda name: rq.LengthOf('s1', 1)  , None                                 , pack('B', 7) ),
    (None, lambda name: rq.LengthOf('s2', 2)  , None                                 , pack('H', 13)),
    (None, lambda name: rq.LengthOf('s3', 4)  , None                                 , pack('L', 34)),
    ('s1', lambda name: rq.Binary(name, pad=0), b"testing"                           , lambda v: v),
    ('s2', lambda name: rq.Binary(name, pad=0), b"one two three"                     , lambda v: v),
    ('s3', lambda name: rq.Binary(name, pad=0), b"supercalifragilisticexpialidocious", lambda v: v),
))

_struct_test('binary pad', (
    (None, lambda name: rq.LengthOf('s1', 1)  , None                                 , pack('B', 7) ),
    (None, lambda name: rq.LengthOf('s2', 2)  , None                                 , pack('H', 13)),
    (None, lambda name: rq.LengthOf('s3', 4)  , None                                 , pack('L', 34)),
    ('s1', lambda name: rq.Binary(name, pad=1), b"testing"                           , lambda v: v + b'\0' * 1),
    ('s2', lambda name: rq.Binary(name, pad=1), b"one two three"                     , lambda v: v + b'\0' * 3),
    ('s3', lambda name: rq.Binary(name, pad=1), b"supercalifragilisticexpialidocious", lambda v: v + b'\0' * 2),
))

_struct_test('fixed binary', (
    ('s1', lambda name: rq.FixedBinary(name, 7 ), b"testing"                           , lambda v: v),
    ('s2', lambda name: rq.FixedBinary(name, 13), b"one two three"                     , lambda v: v),
    ('s3', lambda name: rq.FixedBinary(name, 34), b"supercalifragilisticexpialidocious", lambda v: v),
    # Make sure fixed binary fields are handled as static fields.
    ('c8', rq.Card8, 0x42, partial(pack, 'B')),
))
