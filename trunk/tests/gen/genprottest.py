#!/usr/bin/python

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import types
import string
import struct
from whrandom import randint, choice

from Xlib.protocol import request, structs, rq, event
from Xlib import X, XK

MINI_DEF = (('CARD8', 'reqType'),
	    ('BYTE', 'pad'),
	    ('CARD16', 'length'))

RESOURCE_DEF = (('CARD8', 'reqType'),
		('BYTE', 'pad'),
		('CARD16', 'length'),
		('CARD32', 'id'))

def read_defs():
    global request_defs, reply_defs, struct_defs
    global mini_request_defs, resource_request_defs

    request_defs = {}
    mini_request_defs = {}
    resource_request_defs = {}
    reply_defs = {}
    struct_defs = {}

    for line in sys.stdin.readlines():
	parts = string.split(string.strip(line))

	fields = []
	for f in parts[2:]:
	    fields.append(string.split(f, ':'))
	
	if parts[0] == 'REQUEST':
	    request_defs[parts[1]] = fields
	elif parts[0] == 'MINIREQUEST':
	    mini_request_defs[parts[1]] = MINI_DEF
	elif parts[0] == 'RESOURCEREQUEST':
	    resource_request_defs[parts[1]] = RESOURCE_DEF
	elif parts[0] == 'REPLY':
	    reply_defs[parts[1]] = fields
	elif parts[0] == 'STRUCT':
	    struct_defs[parts[1]] = fields
	    
    
def build():
    if struct.unpack('BB', struct.pack('H', 0x0100))[0]:
	endian = 'be'
    else:
	endian = 'le'
	
    read_defs()
    
    fc = open('genrequest.c', 'w')

    fc.write(r'''
    #include <stdio.h>
    #include <assert.h>
    #include <ctype.h>
    #include <X11/Xproto.h>

    void output(char *name, void *data, int length)
    {
        unsigned char *d = (unsigned char *) data;
	
	printf("%s ", name);

	while (length-- > 0) {
	  if (0 && isgraph(*d))
	    putchar(*d);
          else
	    printf("\\x%02x", *d);
          d++;
        }

	putchar('\n');
    }
	  
    ''')

    reqlist = request.major_codes.items()
    reqlist.sort(lambda x, y: cmp(x[0], y[0]))

    genfuncs = []
    req_args = {}
    reply_args = {}
    
    for code, req in reqlist:
	name = req.__name__
	creqname = name
	
	cdefs = request_defs.get(name)
	if cdefs is None:
	    cdefs = mini_request_defs.get(name)
	    creqname = ''
	if cdefs is None:
	    cdefs = resource_request_defs.get(name)
	    creqname = 'Resource'

	creqname = 'x%sReq' % creqname
	
	if cdefs is None:
	    sys.stderr.write('missing def for request: %s\n' % name)
	else:
	    vardefs = request_var_defs.get(name, [()])
	    if type(vardefs) is not types.ListType:
		vardefs = [vardefs]

	    i = 0
	    for v in vardefs:
		if i > 0:
		    uname = name + str(i)
		else:
		    uname = name

		try:
		    req_args[uname] = gen_func(fc,
					      'genrequest_' + uname,
					      creqname,
					      'REQUEST ' + uname,
					      req._request,
					      cdefs,
					      v)
		except:
		    sys.stderr.write('Error in %s request\n' % uname)
		    raise

		genfuncs.append('genrequest_' + uname)
		i = i + 1

	if issubclass(req, rq.ReplyRequest):
	    cdefs = reply_defs.get(name)

	    if cdefs is None:
		sys.stderr.write('missing def for reply: %s\n' % name)
	    else:
		vardefs = reply_var_defs.get(name, ())
		if type(vardefs) is not types.ListType:
		    vardefs = [vardefs]

		i = 0
		for v in vardefs:
		    if i > 0:
			uname = name + str(i)
		    else:
			uname = name
			
		    try:
			reply_args[uname] = gen_func(fc,
						     'genreply_' + uname,
						     'x%sReply' % name,
						     'REPLY ' + uname,
						     req._reply,
						     cdefs,
						     v)
		    except:
			sys.stderr.write('Error in %s reply\n' % uname)
			raise

		    genfuncs.append('genreply_' + uname)
		    i = i + 1


    fc.write('''

    int main(void)
    {
    ''')

    for gf in genfuncs:
	fc.write('      %s();\n' % gf)

    fc.write('''
      return 0;
    }
    ''')

    fc.close()
    os.system('gcc -Wall -g genrequest.c -o genrequest')

    req_bins = {}
    reply_bins = {}
    pc = os.popen('./genrequest', 'r')
    for line in pc.readlines():
	parts = string.split(string.strip(line))
	if parts[0] == 'REQUEST':
	    req_bins[parts[1]] = parts[2]
	elif parts[0] == 'REPLY':
	    reply_bins[parts[1]] = parts[2]

    fpy = open('test_requests_%s.py' % endian, 'w')

    fpy.write(PY_HEADER)

    fpy.write('def check_endian():\n')
    if endian == 'be':
	e = 'Big-endian'
	v = 1
    else:
	e = 'Little-endian'
	v = 0

    fpy.write("    if struct.unpack('BB', struct.pack('H', 0x0100))[0] != %d:\n" % v)
    fpy.write("        sys.stderr.write('%s tests, skipping on this system.\\n')\n" % e)
    fpy.write("        sys.exit(0)\n\n")

	
    for code, req in reqlist:
        name = req.__name__
	
	fpy.write('\n\nclass Test%s(unittest.TestCase):\n' % name)
	fpy.write('    def setUp(self):\n')

	i = 0
	reqs = -1
	replies = -1
	while 1:
	    if i > 0:
		uname = name + str(i)
	    else:
		uname = name

	    reqbin = req_bins.get(uname)
	    replybin = reply_bins.get(uname)

	    if reqbin is None and replybin is None:
		break

	    if reqbin:
		reqs = i
		fpy.write('        self.req_args_%d = %s\n'
			  % (i, build_args(req_args[uname])))
		fpy.write('        self.req_bin_%d = %s\n\n'
			  % (i, build_bin(reqbin)))
	    if replybin:
		replies = i
		fpy.write('        self.reply_args_%d = %s\n'
			  % (i, build_args(reply_args[uname])))
		fpy.write('        self.reply_bin_%d = %s\n\n'
			  % (i, build_bin(replybin)))

	    i = i + 1
	    
	for i in range(0, reqs + 1):
	    fpy.write('''
    def testPackRequest%(n)d(self):
	bin = apply(request.%(req)s._request.to_binary, (), self.req_args_%(n)d)
	try:
	    assert bin == self.req_bin_%(n)d
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackRequest%(n)d(self):
	args, remain = request.%(req)s._request.parse_binary(self.req_bin_%(n)d, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.req_args_%(n)d
	except AssertionError:
	    raise AssertionError(args)
''' % { 'req': req.__name__, 'n': i })

	for i in range(0, replies + 1):
	    fpy.write('''
    def testPackReply%(n)d(self):
	bin = apply(request.%(req)s._reply.to_binary, (), self.reply_args_%(n)d)
	try:
	    assert bin == self.reply_bin_%(n)d
	except AssertionError:
	    raise AssertionError(tohex(bin))

    def testUnpackReply%(n)d(self):
	args, remain = request.%(req)s._reply.parse_binary(self.reply_bin_%(n)d, dummy_display, 1)
	try:
	    assert len(remain) == 0
	except AssertionError:
	    raise AssertionError(tohex(remain))
	try:
	    assert args == self.reply_args_%(n)d
	except AssertionError:
	    raise AssertionError(args)
''' % { 'req': req.__name__, 'n': i })

    fpy.write('''

if __name__ == "__main__":
    check_endian()
    unittest.main()
''')

    
def gen_func(fc, funcname, structname, outputname, pydef, cdef, vardefs):
    fc.write('''void %s(void)
    {
      struct {
        %s xstruct;
        ''' % (funcname, structname))

    args = {}
    varfs = {}
    extra_vars = []
    flags = None
    
    # structure fields etc
    i = 0
    for f in pydef.var_fields:
	#
	# List of something
	#
	if isinstance(f, rq.List):
	    #
	    # List of short strings
	    #
	    if f.type is rq.Str:
		vfstrings = vardefs[i]
		vflen = 0
		vfdata = ''
		for s in vfstrings:
		    vflen = vflen + 1 + len(s)
		    vfdata = vfdata + chr(len(s)) + s

		fc.write('unsigned char %s[%d];\n      '
			 % (f.name, pad4(vflen)))
		varfs[f.name] = ('memcpy(data.%s, %s, %d);'
				 % (f.name, cstring(vfdata), vflen),
				 len(vfstrings), 0)
		args[f.name] = vfstrings

	    #
	    # List of scalars
	    #
	    elif isinstance(f.type, rq.ScalarObj) \
		 or isinstance(f.type, rq.ResourceObj):

		vflen = vardefs[i]

		if f.type.structcode == 'B':
		    rmin = 128
		    rmax = 255
		    deflen = pad4(vflen)
		    ctype = 'CARD8'
		elif f.type.structcode == 'H':
		    rmin = 32768
		    rmax = 65536
		    deflen = vflen + vflen % 2
		    ctype = 'CARD16'
		elif f.type.structcode == 'L':
		    rmin = 65536
		    rmax = 2147483646
		    deflen = vflen
		    ctype = 'CARD32'
		else:
		    RuntimeError('oops: %s' % f.type.structcode)
		    
		def rand(x, rmin = rmin, rmax = rmax):
		    return randint(rmin, rmax)

		vfdata = map(rand, range(0, vflen))

		#
		# Special case for a few in-line coded lists
		#
		if structname in ('xGetKeyboardControlReply',
				  'xQueryKeymapReply'):
		    extra_vars.append('%s %s_def[%d] = { %s };'
				      % (ctype, f.name, vflen,
					 string.join(map(str, vfdata), ', ')))
		    varfs[f.name] = ('memcpy(data.xstruct.map, %s_def, sizeof(%s_def));'
				     % (f.name, f.name),
				     vflen, 0)
		else:
		    fc.write('%s %s[%d];\n      '
			     % (ctype, f.name, deflen))
		    extra_vars.append('%s %s_def[%d] = { %s };'
				      % (ctype, f.name, vflen,
					 string.join(map(str, vfdata), ', ')))
		    varfs[f.name] = ('memcpy(data.%s, %s_def, sizeof(%s_def));'
				     % (f.name, f.name, f.name),
				     vflen, 0)

		args[f.name] = vfdata
		
	    #
	    # Special handling of unique Host case
	    #
	    elif f.type is structs.Host:
		pydata = [{ 'family': X.FamilyInternet,
			    'name': [ 34, 23, 178, 12 ] },
			  { 'family': X.FamilyInternet,
			    'name': [ 130, 236, 254, 15 ] }, ]

		cdata = []
		for p in pydata:
		    cdata.append("{ { %d, 0, 4 }, { %d, %d, %d, %d } }"
				 % ((p['family'], ) + tuple(p['name'])))
		    
		fc.write('struct { xHostEntry e; CARD8 name[4]; } %s[2];\n      ' % f.name)

		extra_vars.append('struct { xHostEntry e; CARD8 name[4]; } %s_def[%d] = { %s };'
				  % (f.name, len(pydata),
				     string.join(cdata, ', ')))

		varfs[f.name] = ('memcpy(data.%s, %s_def, sizeof(%s_def));'
				 % (f.name, f.name, f.name),
				 len(pydata), 0)

		args[f.name] = pydata
		
			  
	    #
	    # List of structures
	    #
	    elif isinstance(f.type, rq.Struct):
		vfname, vflen = vardefs[i]
		vfdef = struct_defs[vfname]

		pydata = []
		defdata = []
		for si in range(0, vflen):
		    d = []
		    for t, cf in vfdef:
			if cf[:3] != 'pad':
			    d.append(gen_value(t))

		    pyd = {}
		    for sj in range(0, len(d)):
			pyd[f.type.fields[sj].name] = d[sj]
			
		    pydata.append(pyd)
		    defdata.append('{ ' + string.join(map(str, d), ', ') + ' }')
		
		fc.write('x%s %s[%d];\n        ' % (vfname, f.name, vflen))

		extra_vars.append('x%s %s_def[%d] = { %s };'
				  % (vfname, f.name, vflen,
				     string.join(defdata, ', ')))
		varfs[f.name] = ('memcpy(data.%s, %s_def, sizeof(%s_def));'
				 % (f.name, f.name, f.name),
				 vflen, 0)
		args[f.name] = pydata

	#
	# wide-char string
	#
	elif isinstance(f, rq.String16):
	    vfstr = vardefs[i]
	    vflen = len(vfstr)
	    
	    fc.write('unsigned char %s[%d];\n        ' %
		     (f.name, (vflen + vflen % 2) * 2))

	    s = ''
	    for c in vfstr:
		s = s + '\0' + c
		
	    varfs[f.name] = ('memcpy(data.%s, %s, %d);'
			     % (f.name, cstring(s), vflen * 2),
			     vflen, 0)
	    args[f.name] = tuple(map(ord, vfstr))

	#
	# byte-char string
	#
	elif isinstance(f, rq.String8):
	    vfstr = vardefs[i]
	    vflen = len(vfstr)
	    
	    fc.write('unsigned char %s[%d];\n        ' %
		     (f.name, (vflen + (4 - vflen % 4) % 4)))
	    varfs[f.name] = ('memcpy(data.%s, %s, %d);'
			     % (f.name, cstring(vfstr), vflen),
			     vflen, 0)
	    args[f.name] = vfstr

	#
	# List of optional values
	#
	elif isinstance(f, rq.ValueList):
	    vlcode = []
	    vlargs = {}
	    flags = 0
	    for vlf, flag in f.fields:
		ctype, rmin, rmax, clen = structcode_defs[vlf.structcode]
		fc.write('%s %s_%s;\n      '
			 % (ctype, f.name, vlf.name))
		if clen < 4:
		    fc.write('unsigned char %s_%s_pad[%d];\n      '
			     % (f.name, vlf.name, 4 - clen))

		if isinstance(vlf, rq.Set):
		    val = choice(vlf.values)
		elif isinstance(vlf, rq.Bool):
		    val = choice((0, 1))
		else:
		    val = randint(rmin, rmax)
		vlargs[vlf.name] = val
		vlcode.append('data.%s_%s = %d;' % (f.name, vlf.name, val))
		flags = flags | flag

	    # vlcode.append('data.%s_flags = %d;' % (f.name, flags))

	    varfs[f.name] = (string.join(vlcode, ' '), 0, 0)
	    args[f.name] = vlargs

	#
	# Text/font list, hardwire since they are so rare
	#
	elif isinstance(f, rq.TextElements8):
	    if isinstance(f, rq.TextElements16):
		vfstr = '\x02\x02\x10\x23\x00\x12\xff\x01\x02\x03\x04'
		ret = [{'delta': 2, 'string': (0x1023, 0x0012)},
		       0x01020304]
	    else:
		vfstr = '\x03\x02zoo\xff\x01\x02\x03\x04\x02\x00ie'
		ret = [{'delta': 2, 'string': 'zoo'},
		       0x01020304,
		       { 'delta': 0, 'string': 'ie'}]
	    
	    fc.write('unsigned char %s[%d];\n      '
		     % (f.name, len(vfstr)))
	    varfs[f.name] = ('memcpy(data.%s, %s, %d);'
			     % (f.name, cstring(vfstr), len(vfstr)),
			     0, 0)
	    args[f.name] = ret

	#
	# Keyboard/modifier mappings
	#
	elif isinstance(f, rq.KeyboardMapping) \
	     or isinstance(f, rq.ModifierMapping):

	    if isinstance(f, rq.KeyboardMapping):
		rmin = 0
		rmax = 2147483646
		length = 20
		format = 3
		ctype = 'CARD32'
	    else:
		rmin = 0
		rmax = 255
		length = 8
		format = 2
		ctype = 'CARD8'

	    pydata = []
	    cdata = []
	    for i in range(0, length):
		x = []
		for j in range(0, format):
		    v = randint(rmin, rmax)
		    x.append(v)
		    cdata.append(str(v))
		pydata.append(x)

	    fc.write('%s %s[%d];\n      ' % (ctype, f.name, len(cdata)))
	    extra_vars.append('%s %s_def[%d] = { %s };'
			      % (ctype, f.name, len(cdata),
				 string.join(cdata, ', ')))
	    varfs[f.name] = ('memcpy(data.%s, %s_def, sizeof(%s_def));'
			     % (f.name, f.name, f.name),
			     length, format)
	    args[f.name] = pydata
	    
	#
	# property data
	#
	elif isinstance(f, rq.PropertyData):
	    format, data = vardefs[i]
	    length = len(data)

	    if format == 8:
		ctype = 'CARD8'
		clen = pad4(length)
		cdata = cstring(data)
	    elif format == 16:
		ctype = 'CARD16'
		clen = length + length % 2
		cdata = string.join(map(str, data), ', ')
	    elif format == 32:
		ctype = 'CARD32'
		clen = length
		cdata = string.join(map(str, data), ', ')
		
	    fc.write('%s %s[%d];\n        ' %
		     (ctype, f.name, clen))
	    extra_vars.append('%s %s_def[%d] = { %s };'
			      % (ctype, f.name, length, cdata))
	    varfs[f.name] = ('memcpy(data.%s, %s_def, sizeof(%s_def));'
			     % (f.name, f.name, f.name),
		     length, format)

	    args[f.name] = (format, data)
	    
	#
	# Event
	#
	elif isinstance(f, rq.EventField):
	    ev = event.Expose(window = gen_value('CARD32'),
			      x = gen_value('CARD16'),
			      y =  gen_value('CARD16'),
			      width = gen_value('CARD16'),
			      height = gen_value('CARD16'),
			      count = gen_value('CARD16'))
	    cdata = cstring(ev._binary)
	    
	    # fc.write('unsigned char %s[32];\n        ' % f.name)
	    extra_vars.append('unsigned char %s_def[32] = %s;'
			      % (f.name, cdata))
	    varfs[f.name] = ('memcpy(&data.xstruct.event, %s_def, sizeof(%s_def));'
			     % (f.name, f.name),
			     0, 0)

	    args[f.name] = ev
	
	else:
	    raise RuntimeError('oops: %s.%s' % (funcname, f.name))
	
	i = i + 1

    
    fc.write('\n      } data;\n')

    
    for v in extra_vars:
	fc.write('      %s\n' % v)

    fc.write('''
      memset(&data, 0, sizeof(data));
    
    ''')

    pyi = 0
    ci = 0

    while ci < len(cdef):
	try:
	    pyf = pydef.fields[pyi]
	except IndexError:
	    pyf = None
	    
	cf = cdef[ci]
	t, f = cf
	
	pyi = pyi + 1
	ci = ci + 1
	
	if f[:3] == 'pad' or f[:6] == 'walign':
	    if not isinstance(pyf, rq.Pad):
		pyi = pyi - 1

	# special case for value list mask
	elif (f == 'mask' or f == 'valueMask') and flags is not None:
	    fc.write('      data.xstruct.%s = %d;\n' % (f, flags))
	    
	elif isinstance(pyf, rq.ConstantField):
	    fc.write('      data.xstruct.%s = %d;\n' % (f, pyf.value))

	elif isinstance(pyf, rq.RequestLength):
	    assert f == 'length'
	    
	    fc.write('      assert(sizeof(data) % 4 == 0);\n')
	    fc.write('      data.xstruct.length = sizeof(data) / 4;\n')

	elif isinstance(pyf, rq.ReplyLength):
	    assert f == 'length'
	    
	    fc.write('      assert(sizeof(data) % 4 == 0);\n')
	    fc.write('      assert(sizeof(data) >= 32);\n')
	    fc.write('      data.xstruct.length = (sizeof(data) - 32) / 4;\n')
	    
	elif isinstance(pyf, rq.LengthOf):
	    fc.write('      data.xstruct.%s = %d;\n' % (f, varfs[pyf.name][1]))

	elif isinstance(pyf, rq.OddLength):
	    fc.write('      data.xstruct.%s = %d;\n' % (f, varfs[pyf.name][1] % 2))
	    
	elif isinstance(pyf, rq.Format):
	    fc.write('      data.xstruct.%s = %d;\n' % (f, varfs[pyf.name][2]))

	elif isinstance(pyf, rq.Set):
	    val = choice(pyf.values)
	    fc.write('      data.xstruct.%s = %d;\n' % (f, val))
	    args[pyf.name] = val

	elif t == 'xCharInfo':
	    d = []
	    for ct, cf in struct_defs['CharInfo']:
		if cf[:3] != 'pad':
		    d.append(gen_value(ct))

	    pyd = {}
	    for sj in range(0, len(d)):
		pyd[pyf.type.fields[sj].name] = d[sj]
			
	    fc.write('{ %s def = { %s };\n      '
		     % (t, string.join(map(str, d), ', ')))
	    fc.write('memcpy(&data.xstruct.%s, &def, sizeof(def)); }\n        ' % f)
	    args[pyf.name] = pyd
	    
	else:
	    val = gen_value(t)
	    fc.write('      data.xstruct.%s = %d;\n' % (f, val))
	    args[pyf.name] = val

    for code, length, format in varfs.values():
	fc.write('      %s\n' % code);
	
    fc.write('''
      output("%s", &data, sizeof(data));
    }
    
    ''' % outputname)

    return args

    
def gen_value(t):
    if t == 'INT8':
	val = randint(-128, -1)
    elif t == 'INT16':
	val = randint(-32768, -256)
    elif t == 'INT32':
	val = randint(-2147483647, -65536)
    elif t == 'CARD8' or t == 'BYTE':
	val = randint(128, 255)
    elif t == 'CARD16':
	val = randint(256, 65535)
    elif t == 'CARD32':
	val = randint(65536, 2147483646)
    elif t == 'BOOL':
	val = randint(0, 1)
    else:
	raise RuntimeError('unknown type: %s' % t)
    return val

	
def pad4(l):
    return l + (4 - l % 4) % 4

def cstring(s):
    return '"' + string.join(map(lambda c: '\\x%x' % ord(c), s), '') + '"'


def build_args(args):
    kwlist = []
    for kw, val in args.items():
	kwlist.append("            '%s': %s,\n" % (kw, repr(val)))
	
    return '{\n' + string.join(kwlist, '') + '            }'

def build_bin(bin):
    bins = []
    for i in range(0, len(bin), 16):
	bins.append(bin[i:i+16])

    bins2 = []
    for i in range(0, len(bins), 2):
	try:
	    bins2.append("'%s' '%s'" % (bins[i], bins[i + 1]))
	except IndexError:
	    bins2.append("'%s'" % bins[i])

    return string.join(bins2, ' \\\n            ')

    
request_var_defs = {
    'InternAtom': ('fuzzy_prop', ),
    'ChangeProperty': [((8, ''), ),
		       ((8, 'foo'), ),
		       ((8, 'zoom'), ),
		       ((16, []), ),
		       ((16, [1, 2, 3]), ),
		       ((16, [1, 2, 3, 4]), ),
		       ((32, []), ),
		       ((32, [1, 2, 3]), ) ],
    'OpenFont': ('foofont', ),
    'QueryTextExtents': ('foo', ),
    'ListFonts': ('bhazr', ),
    'ListFontsWithInfo': ('bhazr2', ),
    'SetFontPath': [(['foo', 'bar', 'gazonk'], ),
		    ([], ) ],
    'SetDashes': (9, ),
    'SetClipRectangles': [(('Rectangle', 2), ),
			  (('Rectangle', 0), ) ],
    'PolyPoint': (('Point', 3), ),
    'PolyLine': (('Point', 5), ),
    'PolySegment': (('Segment', 1), ),
    'PolyRectangle': (('Rectangle', 3), ),
    'PolyArc': (('Arc', 3), ),
    'FillPoly': (('Point', 3), ),
    'PolyFillRectangle': (('Rectangle', 2), ),
    'PolyFillArc': (('Arc', 1), ),
    'PutImage': ('bit map data', ),
    'ImageText8': ('showme', ),
    'ImageText16': ('showmore', ),
    'AllocNamedColor': ('octarin', ),
    'FreeColors': (17, ),
    'StoreColors': (('ColorItem', 4), ),
    'StoreNamedColor': ('blue', ),
    'QueryColors': [(8, ), (0, ) ],
    'LookupColor': ('octarin', ),
    'QueryExtension': ('XTRA', ),
    'ChangeHosts': (4, ),
    'RotateProperties': (12, ),
    'SetPointerMapping': (5, ),
    }

reply_var_defs = {
    'QueryTree': (7, ),
    'GetAtomName': ('WM_CLASS', ),
    'GetProperty': [((8, ''), ),
		       ((8, 'foo'), ),
		       ((8, 'zoom'), ),
		       ((16, []), ),
		       ((16, [1, 2, 3]), ),
		       ((16, [1, 2, 3, 4]), ),
		       ((32, []), ),
		       ((32, [1, 2, 3]), ) ],
    'ListProperties': (23, ),
    'GetMotionEvents': (('Timecoord', 5), ),
    'QueryKeymap': (32, ),
    'QueryFont': (('FontProp', 1), ('CharInfo', 3)),
    'ListFonts': (['fie', 'fuzzy', 'foozooom'], ),
    'ListFontsWithInfo': (('FontProp', 1), 'fontfont'),
    'GetFontPath': [(['path1', 'path2232'], ),
		    ([], ) ],
    'GetImage': ('this is real ly imag e b-map', ),
    'ListInstalledColormaps': (2, ),
    'AllocColorCells': [(17, 3),
			(0, 0) ],
    'AllocColorPlanes': (4, ),
    'QueryColors': (('rgb', 5), ),
    'ListExtensions': (['XTRA', 'XTRA-II'], ),
    'GetKeyboardControl': (8, ),
    'GetPointerMapping': (5, ),
#    '': (, ),
    }

structcode_defs = {
    'b': ('INT8', -128, -1, 1),
    'B': ('CARD8', 128, 255, 1),
    'h': ('INT16', -32768, -1, 2),
    'H': ('CARD16', 32768, 65536, 2),
    'l': ('INT32', -2147483647, -1, 4),
    'L': ('CARD32', 65536, 2147483646, 4),
    }

PY_HEADER = r'''
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import string
import unittest
from Xlib.protocol import request, rq
import Xlib.protocol.event

import struct
import array

class CmpArray:
    def __init__(self, *args, **kws):
	self.array = apply(array.array, args, kws)

    def __len__(self):
	return len(self.array)
    
    def __getslice__(self, x, y):
	return list(self.array[x:y])
    
    def __getattr__(self, attr):
	return getattr(self.array, attr)
    
    def __cmp__(self, other):
	return cmp(self.array.tolist(), other)

rq.array = CmpArray

def tohex(bin):
    bin = string.join(map(lambda c: '\x%02x' % ord(c), bin), '')

    bins = []
    for i in range(0, len(bin), 16):
	bins.append(bin[i:i+16])

    bins2 = []
    for i in range(0, len(bins), 2):
	try:
	    bins2.append("'%s' '%s'" % (bins[i], bins[i + 1]))
	except IndexError:
	    bins2.append("'%s'" % bins[i])

    return string.join(bins2, ' \\\n            ')

class DummyDisplay:
    def get_resource_class(self, x):
	return None

    event_classes = Xlib.protocol.event.event_class
dummy_display = DummyDisplay()

'''

if __name__ == '__main__':
    build()
