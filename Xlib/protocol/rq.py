# $Id: rq.py,v 1.6 2000-12-01 10:18:10 petli Exp $
#
# Xlib.protocol.rq -- structure primitives for request, events and errors
#
#    Copyright (C) 2000 Peter Liljenberg <petli@ctrl-c.liu.se>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


# Standard modules
import sys
import traceback
import struct
import string
import array
import types

# Xlib modules
from Xlib import X
from Xlib.support import lock

class BadDataError(Exception): pass

unsigned_codes = { 1: 'b',
		   2: 'h',
		   4: 'l'
		   }

unsigned_codes = { 1: 'B',
		   2: 'H',
		   4: 'L'
		   }


class Field:
    """Field objects represent the data fields of a Struct.

    Field objects must have the following methods:
    
      f.get_name()
      f.get_binary_value()


    They must also have the attribute `structcode', which should be set to
    an appropriate code or codes from the module struct.

    If `structcode' is set to one or more codes the attribute `structvalues'
    must be set to the number of values `structcode' encodes; i.e. the
    lengt of the tuple that struct.pack(f.structcode, data) would return.
    It must also have the method f.parse_value().

    If `structcode' isn't set the Field must have the method
    f.parse_binary_value() instead.
    """
    
    structcode = None
    structvalues = 0
    
    def __init__(self):
	pass
    
    def get_name(self):
	"""name = f.get_name()

	Return the name of this field, or None if it doesn't have one.
	"""
	
	return None

    def get_binary_value(self, keys):
	"""data [, len [, fmt]] = f.get_binary_value(keys)

	Fetch the value for this field from the mapping KEYS.
	Encode it as the string DATA for transmitting.  If this value
	encodes a sequence of any kind, the length of that sequence
	should be returned as LEN.  If the value might be of different
	formats, the format should be returned as LEN.

	If any of LEN and FMT are returned, they will be available to
	corresponding LengthField and FormatField objects.
	"""
	
	return ''

    def parse_value(self, value, display):
	"""newval = f.parse_value(value, display)

	Called when extracting values from recieved data.
	VALUE is the unpacked value according to f.structcode, and
	the method should return a possible modified value as NEWVAL.

	DISPLAY is the display involved, which is really only used by
	the Resource fields.
	
	If f.structvalues is 1, VALUE will be a single object (typically
	a number).  If f.structvalues is greater than 1, VALUE will be
	a tuple of that length.
	"""
	
	return value


    def parse_binary_value(self, data, display, length, format):
	"""value, remaindata = f.parse_binary_value(data, display, length, format)

	Decode a value for this field from the binary string DATA.
	If there are a LengthField and/or a FormatField connected to this
	field, their values will be LENGTH and FORMAT, respectively.  If
	there are no such fields the parameters will be None.

	DISPLAY is the display involved, which is really only used by
	the Resource fields.

	The decoded value is returned as VALUE, and the remaining part
	of DATA shold be returned as REMAINDATA.
	"""
	
	raise RuntimeError('Neither structcode or parse_binary_value provided for %s'
			   % self)
    
    
class Pad(Field):
    def __init__(self, size):
	self.size = size
	self.value = '\0' * size
	self.structcode = '%dx' % size
	self.structvalues = 0
	
    def get_binary_value(self, keys):
	return self.value

    
class ConstantField(Field):
    def __init__(self, value):
	self.value = value

    def get_binary_value(self, keys):
	val = struct.pack(self.structcode, self.value)
	return val


class Opcode(ConstantField):
    structcode = 'B'
    structvalues = 1

    
class LengthField(Field):
    """A LengthField stores the length of some other Field whose size
    may vary, e.g. List and String8.

    Its name should be the same as the name of the field whose size
    it stores.
    
    The lf.get_binary_value() method of LengthFields is not used, instead
    a lf.get_binary_length() should be provided.

    Unless LengthField.get_binary_length() is overridden in child classes,
    there should also be a lf.calc_length().
    """

    structcode = 'L'
    structvalues = 1

    def get_binary_length(self, length):
	"""data = lf.get_binary_length(length)

	Pack LENGTH, an integer, in a string for transmitting and return
	it as DATA.
	"""
	
	return struct.pack(self.structcode, self.calc_length(length))

    def calc_length(self, length):
	"""newlen = lf.calc_length(length)

	Return a new length NEWLEN based on the provided LENGTH.
	"""
	
	return length

	
class RequestLength(LengthField):
    structcode = 'H'
    structvalues = 1

    def calc_length(self, length):
	return length / 4 + 1


class LengthOf(LengthField):
    def __init__(self, name, size):
	self.name = name
	self.structcode = unsigned_codes[size]

    def get_name(self):
	return self.name


class OddLength(LengthField):
    structcode = 'B'
    structvalues = 1
    
    def __init__(self, name):
	self.name = name

    def get_name(self):
	return self.name

    def calc_length(self, length):
	return length % 2


class FormatField(Field):
    """A FormatField encodes the format of some other field, in a manner
    similar to LengthFields.

    The ff.get_binary_value() method is not used, replaced by
    ff.get_binary_format().
    """
    
    structvalues = 1
    
    def __init__(self, name, size):
	self.name = name
	self.structcode = unsigned_codes[size]
	
    def get_name(self):
	return self.name

    def get_binary_format(self, format):
	"""data = lf.get_binary_format(format)

	Pack FORMAT, an integer, in a string for transmitting and return
	it as DATA.
	"""
	
	return struct.pack(self.structcode, format)

Format = FormatField

    
class ValueField(Field):
    def __init__(self, name):
	self.name = name

    def get_name(self):
	return self.name

    def get_binary_value(self, keys):
	try:
	    val = keys[self.name]
	    val = self.check_value(val)
	    return self.pack_value(val)
	except KeyError:
	    raise TypeError('missing argument for field "%s"' % self.name)

    def check_value(self, val):
	return val

    def pack_value(self, value):
	val = struct.pack(self.structcode, value)
	return val
	
class Int8(ValueField):
    structcode = 'b'
    structvalues = 1

class Int16(ValueField):
    structcode = 'h'
    structvalues = 1

class Int32(ValueField):
    structcode = 'l'
    structvalues = 1

class Card8(ValueField):
    structcode = 'B'
    structvalues = 1

class Card16(ValueField):
    structcode = 'H'
    structvalues = 1

class Card32(ValueField):
    structcode = 'L'
    structvalues = 1


class Resource(Card32):
    cast_function = '__resource__'
    class_name = 'resource'

    def __init__(self, name, codes = ()):
	Card32.__init__(self, name)
	self.codes = codes
    
    def check_value(self, value):
	if type(value) is types.InstanceType:
	    return getattr(value, self.cast_function)()
	else:
	    return value

    def parse_value(self, value, display):
	if value in self.codes:
	    return value
	
	c = display.get_resource_class(self.class_name)
	if c:
	    return c(display, value)
	else:
	    return value
	
class Window(Resource):
    cast_function = '__window__'
    class_name = 'window'
    
class Pixmap(Resource):
    cast_function = '__pixmap__'
    class_name = 'pixmap'

class Drawable(Resource):
    cast_function = '__drawable__'
    class_name = 'drawable'

class Fontable(Resource):
    cast_function = '__fontable__'
    class_name = 'fontable'
    
class Font(Resource):
    cast_function = '__font__'
    class_name = 'font'

class GC(Resource):
    cast_function = '__gc__'
    class_name = 'gc'

class Colormap(Resource):
    cast_function = '__colormap__'
    class_name = 'colormap'

class Cursor(Resource):
    cast_function = '__cursor__'
    class_name = 'cursor'


class Bool(ValueField):
    structvalues = 1
    structcode = 'B'
    
    def check_value(self, value):
	return not not value
    
class Set(ValueField):
    structvalues = 1

    def __init__(self, name, size, values):
	ValueField.__init__(self, name)
	self.structcode = unsigned_codes[size]
	self.values = values

    def check_value(self, val):
	if val not in self.values:
	    raise ValueError('field %s: argument %s not in %s'
			     % (self.name, val, self.values))
	return val
    
class Gravity(Set):
    def __init__(self, name):
	Set.__init__(self, name, 1, (X.ForgetGravity, X.StaticGravity,
				    X.NorthWestGravity, X.NorthGravity,
				    X.NorthEastGravity, X.WestGravity,
				    X.CenterGravity, X.EastGravity,
				    X.SouthWestGravity, X.SouthGravity,
				    X.SouthEastGravity))


class FixedString(ValueField):
    structvalues = 1
    
    def __init__(self, name, size):
	ValueField.__init__(self, name)
	self.structcode = '%ds' % size

	
class String8(ValueField):
    structcode = None

    def __init__(self, name, pad = 1):
	ValueField.__init__(self, name)
	self.pad = pad
	
    def pack_value(self, val):
	slen = len(val)

	if self.pad:
	    return val + '\0' * ((4 - slen % 4) % 4), slen
	else:
	    return val, slen

    def parse_binary_value(self, data, display, length, format):
	if self.pad:
	    slen = length + ((4 - length % 4) % 4)
	else:
	    slen = length
	    
	return data[:length], data[slen:]


class String16(ValueField):
    structcode = None
    
    def __init__(self, name, pad = 1):
	ValueField.__init__(self, name)
	self.pad = pad
	
    def pack_value(self, val):
	# Convert 8-byte string into 16-byte list
	if type(val) is types.StringType:
	    val = map(lambda c: ord(c), val)
			      
	slen = len(val)

	if self.pad:
	    pad = '\0\0' * (slen % 2)
	else:
	    pad = ''
	    
	return apply(struct.pack, ('>' + 'H' * slen, ) + tuple(val)) + pad, slen

    def parse_binary_value(self, data, display, length, format):
	if self.pad:
	    slen = length + (length % 2)
	else:
	    slen = length
	    
	return struct.unpack('>' + 'H' * length, data[:length]), data[slen:]



class List(ValueField):
    """The List, FixedList and Object fields store compound data objects.
    The type of data objects must be provided as an object with the
    following attributes and methods:

    ...
       
    """
    
    structcode = None

    def __init__(self, name, type):
	ValueField.__init__(self, name)
	self.type = type
	
    def parse_binary_value(self, data, display, length, format):
	if length is None:
	    ret = []
	    if self.type.structcode is None:
		while data:
		    val, data = self.type.parse_binary(data, display)
		    ret.append(val)
	    else:
		scode = '=' + self.type.structcode
		slen = struct.calcsize(scode)
		pos = 0
		while pos + slen <= len(data):
		    v = struct.unpack(scode, data[pos: pos + slen])

		    if self.type.structvalues == 1:
			v = v[0]
			
		    ret.append(self.type.parse_value(v, display))
		    pos = pos + slen

		data = data[pos:]
		
	else:
	    ret = [None] * int(length)

	    if self.type.structcode is None:
		for i in range(0, length):
		    ret[i], data = self.type.parse_binary(data, display)
	    else:
		scode = '=' + self.type.structcode
		slen = struct.calcsize(scode)
		pos = 0
		for i in range(0, length):
		    v = struct.unpack(scode, data[pos: pos + slen])

		    if self.type.structvalues == 1:
			v = v[0]
			
		    ret[i] = self.type.parse_value(v, display)
		    pos = pos + slen

		data = data[pos:]

	data = data[len(data) % 4:]
	
	return ret, data

    def pack_value(self, val):
	# Single-char values, we'll assume that means integer lists.
	if self.type.structcode and len(self.type.structcode) == 1:
	    data = array.array(self.type.structcode, val).tostring()
	else:
	    data = []
	    for v in val:
		data.append(self.type.pack_value(v))
		
	    data = string.join(data, '')

	dlen = len(data)
	data = data + '\0' * ((4 - dlen % 4) % 4)
	    
	return data, len(val)
	

class FixedList(List):
    def __init__(self, name, size, type):
	List.__init__(self, name, type)
	self.size = size

    def parse_binary_value(self, data, display, length, format):
	return List.parse_binary_value(self, data, display, self.size, format)

    def pack_value(self, val):
	if len(val) != self.size:
	    raise BadDataError('length mismatch for FixedList %s' % self.name)
	return List.pack_value(self, val)


class Object(ValueField):
    structcode = None

    def __init__(self, name, type):
	ValueField.__init__(self, name)
	self.type = type
	self.structcode = self.type.structcode
	self.structvalues = self.type.structvalues
	
    def parse_binary_value(self, data, display, length, format):
	if self.type.structcode is None:
	    return self.type.parse_binary(data, display)
	
	else:
	    scode = '=' + self.type.structcode
	    slen = struct.calcsize(scode)

	    v = struct.unpack(scode, data[:slen])
	    if self.type.structvalues == 1:
		v = v[0]

	    return self.type.parse_value(v, display), data[slen:]

    def parse_value(self, val, display):
	return self.type.parse_value(val, display)
    
    def pack_value(self, val):
	# Single-char values, we'll assume that mean an integer
	if self.type.structcode and len(self.type.structcode) == 1:
	    return struct.pack('=' + self.type.structcode, val)
	else:
	    return self.type.pack_value(val)
    
class PropertyData(ValueField):
    structcode = None

    def parse_binary_value(self, data, display, length, format):
	if length is None:
	    length = len(data) / (format / 8)
	else:
	    length = int(length)

	if format == 0:
	    ret = None
	    
	elif format == 8:
	    ret = (8, data[:length])
	    data = data[length + ((4 - length % 4) % 4):]

	elif format == 16:
	    ret = (16, array.array('H', data[:2 * length]))
	    data = data[2 * (length + length % 2):]

	elif format == 32:
	    ret = (32, array.array('L', data[:4 * length]))
	    data = data[4 * length:]

	return ret, data

    def pack_value(self, value):
	fmt, val = value

	if fmt not in (8, 16, 32):
	    raise BadDataError('Invalid property data format %s' % format)
	
	if type(val) is types.StringType:
	    size = fmt / 8
	    vlen = len(val)
	    if vlen % size:
		vlen = vlen - vlen % size
		data = val[:vlen]
	    else:
		data = val
		
	    dlen = vlen / size
	
	else:
	    size = fmt / 8
	    data =  array.array(unsigned_codes[size], val).tostring()
	    dlen = len(val)

	dl = len(data)
	data = data + '\0' * ((4 - dl % 4) % 4)

	return data, dlen, fmt
	

class FixedPropertyData(PropertyData):
    def __init__(self, name, size):
	PropertyData.__init__(self, name)
	self.size = size
	
    def parse_binary_value(self, data, display, length, format):
	return PropertyData.parse_binary_value(self, data, display,
					       self.size / (format / 8), format)

    def pack_value(self, value):
	data, dlen, fmt = PropertyData.pack_value(self, value)

	if len(data) != self.size:
	    raise BadDataError('Wrong data length for FixedPropertyData: %s'
			       % (value, ))
	
	return data, dlen, fmt
	
    
class ValueList(Field):
    structcode = None
    
    def __init__(self, name, mask, pad, *fields):
	self.name = name
	self.maskcode = '=%s%dx' % (unsigned_codes[mask], pad)
	self.maskcodelen = struct.calcsize(self.maskcode)
	self.fields = []
	
	flag = 1
	for f in fields:
	    name = f.get_name()
	    if name:
		self.fields.append((f, flag))
		flag = flag << 1

    def get_name(self):
	return self.name
    
    def get_binary_value(self, keys):
	mask = 0
	data = ''

	keys = keys.get(self.name, keys)
	
	for field, flag in self.fields:
	    name = field.get_name()
	    if keys.has_key(name):
		mask = mask | flag
		d = field.get_binary_value(keys)
		if type(d) is types.TupleType:
		    d = d[0]
		    
		data = data + d + '\0' * (4 - len(d))

	return struct.pack(self.maskcode, mask) + data

    def parse_binary_value(self, data, display, length, format):
	r = {}
	
	mask = int(struct.unpack(self.maskcode, data[:self.maskcodelen])[0])
	data = data[self.maskcodelen:]

	for field, flag in self.fields:
	    if mask & flag:
		if field.structcode:
		    vals = struct.unpack(field.structcode,
					 data[:struct.calcsize(field.structcode)])
		    if field.structvalues == 1:
			vals = field.parse_value(vals[0], display)
		    else:
			vals = field.parse_value(vals, display)
		else:
		    vals, d = field.parse_binary_value(data[:4], display, None, None)
		    
		r[field.get_name()] = vals
		data = data[4:]

	return DictWrapper(r), data
		
	
class KeyboardMapping(ValueField):
    structcode = None

    def parse_binary_value(self, data, display, length, format):
	if length is None:
	    dlen = len(data)
	else:
	    dlen = length * format
	    
	a = array.array('L', data[:dlen])

	ret = []
	for i in range(0, len(a), format):
	    ret.append(a[i : i + format])

	return ret, data[dlen:]
    
    def pack_value(self, value):
	keycodes = 0
	for v in value:
	    keycodes = max(keycodes, len(v))

	a = array.array('L')
	
	for v in value:
	    for k in v:
		a.append(k)
	    for i in range(len(v), keycodes):
		a.append(X.NoSymbol)

	return a.tostring(), len(value), keycodes


class ModifierMapping(ValueField):
    structcode = None

    def parse_binary_value(self, data, display, length, format):
	a = array.array('B', data[:8 * format])

	ret = []
	for i in range(0, 8):
	    ret.append(a[i * format : (i + 1) * format])

	return ret, data[8 * format:]
    
    def pack_value(self, value):
	if len(value) != 8:
	    raise BadDataError('ModifierMapping list should have eight elements')
	
	keycodes = 0
	for v in value:
	    keycodes = max(keycodes, len(v))

	a = array.array('B')
	
	for v in value:
	    for k in v:
		a.append(k)
	    for i in range(len(v), keycodes):
		a.append(0)

	return a.tostring(), len(value), keycodes

class EventField(ValueField):
    structcode = None

    def pack_value(self, value):
	if not isinstance(value, Event):
	    raise BadDataError('%s is not an Event for field %s' % (value, self.name))

	return value._binary


#
# Objects usable for List and FixedList fields.
# Struct is also usable.
#

class ScalarObj:
    def __init__(self, code):
	self.structcode = code
	self.structvalues = 1
	
    def parse_value(self, value, display):
	return value
    
Card8Obj  = ScalarObj('B')
Card16Obj = ScalarObj('H')
Card32Obj = ScalarObj('L')

class ResourceObj:
    structcode = 'L'
    structvalues = 1
    
    def __init__(self, class_name):
	self.class_name = class_name
	
    def parse_value(self, value, display):
	c = display.get_resource_class(self.class_name)
	if c:
	    return c(display, value)
	else:
	    return value

WindowObj = ResourceObj('window')
ColormapObj = ResourceObj('colormap')

class StrClass:
    structcode = None

    def pack_value(self, val):
	return chr(len(val)) + val

    def parse_binary(self, data, display):
	slen = ord(data[0]) + 1
	return data[1:slen], data[slen:]

Str = StrClass()

class Struct:
    def __init__(self, *fields):
	self.fields = fields

	# Structures for build_from_args
	self.data_fields = []
	self.length_fields = []
	self.format_fields = []
	self.field_args = []
	self.total_length_field = None

	# Structures for parse_binary
	self.static_codes = '='
	self.static_values = 0
	self.static_fields = []
	self.static_size = None
	self.var_fields = []

	length_names = {}
	format_names = {}
	i = 0
	
	for f in self.fields:
	    name = f.get_name()

	    # If this is a length field, remember it until we
	    # find its corresponding data field
	    if isinstance(f, LengthField):
		length_names[name] = i

	    elif isinstance(f, FormatField):
		format_names[name] = i

	    # Just a data field
	    else:
		self.data_fields.append(i)
		
		if name:
		    self.field_args.append(name)

		    # If this is the data field of a length field which we
		    # already have got, group them together.
		    if length_names.has_key(name):
			self.length_fields.append((i, length_names[name]))
			del length_names[name]

		    # Similar for format fields
		    if format_names.has_key(name):
			self.format_fields.append((i, format_names[name]))
			del format_names[name]
		    
	    # Append structcode if there is one and we haven't
	    # got any varsize fields yet
	    if not self.var_fields and f.structcode is not None:
		self.static_codes = self.static_codes + f.structcode
		self.static_values = self.static_values + f.structvalues
		
	    # If we have got one varsize field, all the rest must
	    # also be varsize fields.
	    if self.var_fields:
		self.var_fields.append(f)

	    # If this field has no structcode, it is a varsize field
	    elif f.structcode is None:
		self.var_fields.append(f)

	    # Otherwise it is a static field if it has any values
	    elif f.structvalues:
		self.static_fields.append(f)

	    i = i + 1

	self.static_size = struct.calcsize(self.static_codes)
	if self.var_fields:
	    self.structcode = None
	    self.structvalues = 0
	else:
	    self.structcode = self.static_codes[1:]
	    self.structvalues = self.static_values
	    
	# Check for a total length field
	if length_names.has_key(None):
	    self.total_length_field = length_names[None]
	    del length_names[None]

	# If there are any length or format fields left without
	# corresponding data fields, scream and shout.
	if length_names:
	    raise ValueError('Missing data fields for lengths: %s'
			     % (length_names.keys(), ))

	if format_names:
	    raise ValueError('Missing data fields for formats: %s'
			     % (format_names.keys(), ))

    def build_from_args(self, args, keys):
	if args:
	    if len(args) > len(self.field_args):
		raise TypeError('too many arguments')
	    
	    for i in range(0, len(args)):
		keys[self.field_args[i]] = args[i]

	values = [None] * len(self.fields)
	lengths = [None] * len(self.fields)
	formats = [None] * len(self.fields)
	length = 0
	
	for i in self.data_fields:
	    ret = self.fields[i].get_binary_value(keys)

	    if type(ret) is types.StringType:
		values[i] = ret
		length = length + len(ret)
	    else:
		val = ret[0]
		length = length + len(val)
		values[i] = val

		try:
		    lengths[i] = ret[1]
		    formats[i] = ret[2]
		except IndexError:
		    pass
	    
	    
	for di, li in self.length_fields:
	    val = self.fields[li].get_binary_length(lengths[di])
	    values[li] = val
	    length = length + len(val)

	for di, fi in self.format_fields:
	    val = self.fields[fi].get_binary_format(formats[di])
	    values[fi] = val
	    length = length + len(val)
	
	if self.total_length_field is not None:
	    values[self.total_length_field] = self.fields[self.total_length_field].get_binary_length(length)
	    
	return string.join(values, '')

    def pack_value(self, value):
	if type(value) is types.TupleType:
	    return self.build_from_args(value, {})
	elif type(value) is types.DictionaryType:
	    return self.build_from_args((), value)
	else:
	    raise BadDataError('%s is not a tuple or a list' % (value))
	
    def parse_value(self, values, display, rawdict = 0):
	ret = {}
	i = 0
	for f in self.static_fields:
	    name = f.get_name()
	    if name:
		if f.structvalues == 1:
		    ret[name] = f.parse_value(values[i], display)
		else:
		    ret[name] = f.parse_value(values[i:i + f.structvalues], display)
		
	    i = i + f.structvalues

	if rawdict:
	    return ret
	else:
	    return DictWrapper(ret)
	
    def parse_binary(self, data, display, rawdict = 0):
	ret = {}
	lengths = {}
	formats = {}
	i = 0

	# Parse all static fields first
	values = struct.unpack(self.static_codes, data[:self.static_size])
	for f in self.static_fields:
	    if f.structvalues == 1:
		val = values[i]
	    else:
		val = values[i:i + f.structvalues]

	    name = f.get_name()
	    if name:
		# If it is a length field, remember its length in
		# wait for its varsize data field
		if isinstance(f, LengthField):
		    lengths[name] = f.parse_value(val, display)

		# Similar for formats
		elif isinstance(f, FormatField):
		    formats[name] = f.parse_value(val, display)

		# Else use field value directly
		else:
		    ret[name] = f.parse_value(val, display)

	    i = i + f.structvalues

	# Now parse all varsize fields
	data = data[self.static_size:]
	for f in self.var_fields:
	    name = f.get_name()
	    ret[name], data = f.parse_binary_value(data, display,
						   lengths.get(name, None),
						   formats.get(name, None))

	if not rawdict:
	    ret = DictWrapper(ret)
	    
	return ret, data


class TextElements8(ValueField):
    string_textitem = Struct( LengthOf('string', 1),
			      Int8('delta'),
			      String8('string', pad = 0) )

    def pack_value(self, value):
	data = ''
	args = {}
	
	for v in value:
	    # Let values be simple strings, meaning a delta of 0
	    if type(v) is types.StringType:
		v = (0, v)

	    # A tuple, it should be (delta, string)
	    # Encode it as one or more textitems
	    
	    if type(v) is types.TupleType:
		delta, str = v
		while delta or str:
		    args['delta'] = delta 
		    args['string'] = str[:254]
		    
		    data = data + self.string_textitem.build_from_args((), args)

		    delta = 0
		    str = str[254:]

	    # Else an integer, i.e. a font change
	    else:
		# Use fontable cast function if instance
		if type(v) is types.InstanceType:
		    v = v.__fontable__()
		    
		data = data + struct.pack('>BL', 255, v)

	# Pad out to four byte length
	dlen = len(data)
	return data + '\0' * ((4 - dlen % 4) % 4)

    def parse_binary_value(self, data, display, length, format):
	values = []
	while 1:
	    d = data[:2]
	    if len(d) != 2:
		break
	    
	    if ord(data[0]) == 255:
		values.append(struct.unpack('>L', data[1:5])[0])
		data = data[5:]

	    else:
		v, data = self.string_textitem.parse_binary(data, display)
		values.append(v)

	return v, ''
			      
		
	
class TextElements16(ValueField):
    string_textitem = Struct( LengthOf('string', 1),
			      Int8('delta'),
			      String16('string', pad = 0) )

		    

class GetAttrData:
    def __getattr__(self, attr):
	try:
	    if self._data:
		return self._data[attr]
	    else:
		raise AttributeError(attr)
	except KeyError:
	    raise AttributeError(attr)

class DictWrapper(GetAttrData):
    def __init__(self, dict):
	self._data = dict

    def __getitem__(self, key):
	return self._data[key]

    def __str__(self):
	return str(self._data)
    
    def __repr__(self):
	return '%s(%s)' % (self.__class__, repr(self._data))
    
class Request:
    def __init__(self, display, onerror = None, *args, **keys):
	self._errorhandler = onerror
	self._binary = self._request.build_from_args(args, keys)
	self._serial = None
	display.send_request(self, onerror is not None)

    def _set_error(self, error):
	if self._errorhandler is not None:
	    return call_error_handler(self._errorhandler, error, self)
	else:
	    return 0
    
class ReplyRequest(GetAttrData):
    def __init__(self, display, defer = 0, *args, **keys):
	self._display = display
	self._binary = self._request.build_from_args(args, keys)
	self._serial = None
	self._data = None
	self._error = None

	self._response_lock = lock.allocate_lock()
	
	self._display.send_request(self, 1)
	if not defer:
	    self.reply()
	    
    def reply(self):
	# Send request and wait for reply if we hasn't
	# already got one.  This means that reply() can safely
	# be called more than one time.

	self._response_lock.acquire()
	while self._data is None and self._error is None:
	    self._display.send_recv_lock.acquire()
	    self._response_lock.release()
	    
	    self._display.send_and_recv(request = self._serial)
	    self._response_lock.acquire()

	self._response_lock.release()
	self._display = None
	    
	# If error has been set, raise it
	if self._error:
	    raise self._error

    def _parse_response(self, data):
	self._response_lock.acquire()
	self._data, d = self._reply.parse_binary(data, self._display, rawdict = 1)
	self._response_lock.release()

    def _set_error(self, error):
	self._response_lock.acquire()
	self._error = error
	self._response_lock.release()
	return 1
    
    def __repr__(self):
	return '<%s serial = %s, data = %s, error = %s>' % (self.__class__, self._serial, self._data, self._error)
    
	
class Event(GetAttrData):
    def __init__(self, binarydata = None, display = None, **keys):
	if binarydata:
	    self._binary = binarydata
	    self._data, data = self._fields.parse_binary(binarydata, display,
							 rawdict = 1)
	else:
	    if self._code:
		keys['type'] = self._code

	    keys['sequence_number'] = 0
	    
	    self._binary = self._fields.build_from_args((), keys)
	    self._data = keys
	    
    def __repr__(self):
	return '<%s data = %s>' % (self.__class__, self._data)
    

def call_error_handler(handler, error, request):
    try:
	return handler(error, request)
    except:
	sys.stderr.write('Exception raised by error handler.\n')
	traceback.print_exc()
	return 0
