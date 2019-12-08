#!/usr/bin/env python

import sys
import os

sys.path.insert(0, os.path.normpath(os.path.join(__file__, '../../..')))

import struct
from random import randint, choice, seed

from Xlib.protocol import request, structs, rq, event
from Xlib import X



seed(42)

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
    global event_defs

    request_defs = {}
    mini_request_defs = {}
    resource_request_defs = {}
    reply_defs = {}
    struct_defs = {}
    event_defs = {}

    for line in sys.stdin.readlines():
        parts = line.strip().split()

        fields = []
        for f in parts[2:]:
            fields.append(f.split(':'))

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
        elif parts[0] == 'EVENT':
            event_defs[parts[1]] = fields


def build():
    if struct.unpack('BB', struct.pack('H', 0x0100))[0]:
        endian = 'be'
    else:
        endian = 'le'

    read_defs()

    build_request(endian)
    build_event(endian)


def build_request(endian):
    fc = open('genrequest.c', 'w')

    fc.write(C_HEADER)

    reqlist = list(request.major_codes.items())
    reqlist.sort(key=lambda x: x[0])

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
            if type(vardefs) is not list:
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
                if type(vardefs) is not list:
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
        parts = line.strip().split()
        if parts[0] == 'REQUEST':
            req_bins[parts[1]] = parts[2]
        elif parts[0] == 'REPLY':
            reply_bins[parts[1]] = parts[2]

    fpy = open('../test_requests_%s.py' % endian, 'w')
    os.chmod('../test_requests_%s.py' % endian, 0o755)

    if endian == 'be':
        e = 'BigEndian'
        v = 1
    else:
        e = 'LittleEndian'
        v = 0

    fpy.write(PY_HEADER % { 'endname': e, 'endvalue': v })

    for code, req in reqlist:
        name = req.__name__

        fpy.write('\n\nclass Test%s(EndianTest):\n' % name)
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
        bin = request.%(req)s._request.to_binary(*(), **self.req_args_%(n)d)
        self.assertBinaryEqual(bin, self.req_bin_%(n)d)

    def testUnpackRequest%(n)d(self):
        args, remain = request.%(req)s._request.parse_binary(self.req_bin_%(n)d, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.req_args_%(n)d)
''' % { 'req': req.__name__, 'n': i })

        for i in range(0, replies + 1):
            fpy.write('''
    def testPackReply%(n)d(self):
        bin = request.%(req)s._reply.to_binary(*(), **self.reply_args_%(n)d)
        self.assertBinaryEqual(bin, self.reply_bin_%(n)d)

    def testUnpackReply%(n)d(self):
        args, remain = request.%(req)s._reply.parse_binary(self.reply_bin_%(n)d, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.reply_args_%(n)d)
''' % { 'req': req.__name__, 'n': i })

    fpy.write('''

if __name__ == "__main__":
    unittest.main()
''')


def build_event(endian):
    fc = open('genevent.c', 'w')

    fc.write(C_HEADER)

    evtlist = list(event.event_class.items())
    evtlist.sort(key=lambda x: x[0])

    genfuncs = []
    evt_args = {}

    for code, evt in evtlist:

        # skip events that does not subclass rq.Event immediately,
        # since those are specializations of the more general ones we
        # test.

        if evt.__bases__ != (rq.Event, ):
            continue

        # special handling of KeymapNotify, since that
        # event is so different
        if evt == event.KeymapNotify:
            evt_args['KeymapNotify'] = gen_func(fc,
                                                'genevent_KeymapNotify',
                                                'xKeymapEvent',
                                                'EVENT KeymapNotify',
                                                evt._fields,
                                                (('BYTE', 'type'), ),
                                                (31, ))
            genfuncs.append('genevent_KeymapNotify')
            continue

        name = evt.__name__

        cdefs = event_defs.get(name)
        if cdefs is None:
            sys.stderr.write('missing def for event: %s\n' % name)
        else:
            vardefs = event_var_defs.get(name, [()])
            if type(vardefs) is not list:
                vardefs = [vardefs]

            i = 0
            for v in vardefs:
                if i > 0:
                    uname = name + str(i)
                else:
                    uname = name

                try:
                    evt_args[uname] = gen_func(fc,
                                               'genevent_' + uname,
                                               'xEvent',
                                               'EVENT ' + uname,
                                               evt._fields,
                                               cdefs,
                                               v)
                except:
                    sys.stderr.write('Error in %s event\n' % uname)
                    raise

                genfuncs.append('genevent_' + uname)
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
    os.system('gcc -Wall -g genevent.c -o genevent')

    evt_bins = {}
    pc = os.popen('./genevent', 'r')
    for line in pc.readlines():
        parts = line.strip().split()
        if parts[0] == 'EVENT':
            evt_bins[parts[1]] = parts[2]

    fpy = open('../test_events_%s.py' % endian, 'w')
    os.chmod('../test_events_%s.py' % endian, 0o755)

    if endian == 'be':
        e = 'BigEndian'
        v = 1
    else:
        e = 'LittleEndian'
        v = 0

    fpy.write(PY_HEADER % { 'endname': e, 'endvalue': v })

    for code, evt in evtlist:
        if evt.__bases__ != (rq.Event, ):
            continue

        name = evt.__name__

        fpy.write('\n\nclass Test%s(EndianTest):\n' % name)
        fpy.write('    def setUp(self):\n')

        i = 0
        evts = -1
        while 1:
            if i > 0:
                uname = name + str(i)
            else:
                uname = name

            evtbin = evt_bins.get(uname)

            if evtbin is None:
                break

            evts = i
            fpy.write('        self.evt_args_%d = %s\n'
                      % (i, build_args(evt_args[uname])))
            fpy.write('        self.evt_bin_%d = %s\n\n'
                      % (i, build_bin(evtbin)))
            i = i + 1

        for i in range(0, evts + 1):
            fpy.write('''
    def testPack%(n)d(self):
        bin = event.%(evt)s._fields.to_binary(*(), **self.evt_args_%(n)d)
        self.assertBinaryEqual(bin, self.evt_bin_%(n)d)

    def testUnpack%(n)d(self):
        args, remain = event.%(evt)s._fields.parse_binary(self.evt_bin_%(n)d, dummy_display, 1)
        self.assertBinaryEmpty(remain)
        self.assertEqual(args, self.evt_args_%(n)d)
''' % { 'evt': evt.__name__, 'n': i })

    fpy.write('''

if __name__ == "__main__":
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

                vfdata = list(map(rand, range(0, vflen)))

                #
                # Special case for a few in-line coded lists
                #
                if structname in ('xGetKeyboardControlReply',
                                  'xQueryKeymapReply',
                                  'xKeymapEvent'):
                    extra_vars.append('%s %s_def[%d] = { %s };'
                                      % (ctype, f.name, vflen,
                                         ', '.join(map(str, vfdata))))
                    varfs[f.name] = ('memcpy(data.xstruct.map, %s_def, sizeof(%s_def));'
                                     % (f.name, f.name),
                                     vflen, 0)
                else:
                    fc.write('%s %s[%d];\n      '
                             % (ctype, f.name, deflen))
                    extra_vars.append('%s %s_def[%d] = { %s };'
                                      % (ctype, f.name, vflen,
                                         ', '.join(map(str, vfdata))))
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
                                     ', '.join(cdata)))

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
                    defdata.append('{ ' + ', '.join(map(str, d)) + ' }')

                fc.write('x%s %s[%d];\n        ' % (vfname, f.name, vflen))

                extra_vars.append('x%s %s_def[%d] = { %s };'
                                  % (vfname, f.name, vflen,
                                     ', '.join(defdata)))
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
        elif isinstance(f, (rq.String8, rq.Binary)):
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

            varfs[f.name] = (' '.join(vlcode), 0, 0)
            args[f.name] = vlargs

        #
        # Text/font list, hardwire since they are so rare
        #
        elif isinstance(f, rq.TextElements8):
            if isinstance(f, rq.TextElements16):
                vfstr = b'\x02\x02\x10\x23\x00\x12\xff\x01\x02\x03\x04'
                ret = [{'delta': 2, 'string': (0x1023, 0x0012)},
                       0x01020304]
            else:
                vfstr = b'\x03\x02zoo\xff\x01\x02\x03\x04\x02\x00ie'
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
                                 ', '.join(cdata)))
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
                cdata = ', '.join(map(str, data))
            elif format == 32:
                ctype = 'CARD32'
                clen = length
                cdata = ', '.join(map(str, data))

            if not isinstance(f, rq.FixedPropertyData):
                fc.write('%s %s[%d];\n        ' %
                         (ctype, f.name, clen))

            extra_vars.append('%s %s_def[%d] = { %s };'
                              % (ctype, f.name, length, cdata))

            if not isinstance(f, rq.FixedPropertyData):
                varfs[f.name] = ('memcpy(data.%s, %s_def, sizeof(%s_def));'
                                 % (f.name, f.name, f.name),
                                 length, format)
            else:
                varfs[f.name] = ('assert(sizeof(%s_def) == 20); memcpy(data.xstruct.u.clientMessage.u.b.bytes, %s_def, sizeof(%s_def));'
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
                     % (t, ', '.join(map(str, d))))
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
    if not isinstance(s, bytes):
        s = s.encode('ascii')
    return '"' + ''.join('\\x%x' % c for c in s) + '"'


def build_args(args):
    kwlist = []
    for kw, val in sorted(args.items(), key=lambda i: i[0]):
        if isinstance(val, rq.Event):
            members = list(val._data.keys())
            members.remove('send_event')
            kwlist.append("            '%s': event.%s(%s),\n" % (
                kw, val.__class__.__name__,
                ', '.join('%s=%s' % (m, val._data[m])
                          for m in sorted(members)),
            ))
        else:
            kwlist.append("            '%s': %s,\n" % (kw, repr(val)))

    return '{\n' + ''.join(kwlist) + '            }'

def build_bin(bin):
    bins = []
    for i in range(0, len(bin), 16):
        bins.append(bin[i:i+16])

    bins2 = []
    for i in range(0, len(bins), 2):
        try:
            bins2.append("b'%s' b'%s'" % (bins[i], bins[i + 1]))
        except IndexError:
            bins2.append("b'%s'" % bins[i])

    return ' \\\n            '.join(bins2)


request_var_defs = {
    'InternAtom': ('fuzzy_prop', ),
    'ChangeProperty': [((8, b''), ),
                       ((8, b'foo'), ),
                       ((8, b'zoom'), ),
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
    'PutImage': (b'\xe9\x10\xf2o\x7f{\xae-\xe6\x18\xce\x83', ),
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
    'GetProperty': [((8, b''), ),
                       ((8, b'foo'), ),
                       ((8, b'zoom'), ),
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
    'GetImage': (b'\xeb?:\xa7\xc6\x8b\xc2\x96o-S\xe6\xd6z6\x94\xd7v\xd2R.\xa2\xeaw\t\x13\x95\x85',),
    'ListInstalledColormaps': (2, ),
    'AllocColorCells': [(17, 3),
                        (0, 0) ],
    'AllocColorPlanes': (4, ),
    'QueryColors': (('rgb', 5), ),
    'ListExtensions': (['XTRA', 'XTRA-II'], ),
    'GetKeyboardControl': (32, ),
    'GetPointerMapping': (5, ),
#    '': (, ),
    }

event_var_defs = {
    'ClientMessage': [((8, b'01234567890123456789'), ),
                      ((16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), ),
                      ((32, [1, 2, 3, 4, 5]), ) ],
    }

structcode_defs = {
    'b': ('INT8', -128, -1, 1),
    'B': ('CARD8', 128, 255, 1),
    'h': ('INT16', -32768, -1, 2),
    'H': ('CARD16', 32768, 65536, 2),
    'l': ('INT32', -2147483647, -1, 4),
    'L': ('CARD32', 65536, 2147483646, 4),
    }

C_HEADER = r'''
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>
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

'''

PY_HEADER = r'''#!/usr/bin/env python2

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(__file__, '../..')))

import unittest
from Xlib.protocol import request, event
from . import %(endname)sTest as EndianTest
from . import DummyDisplay

dummy_display = DummyDisplay()
'''

if __name__ == '__main__':
    build()
