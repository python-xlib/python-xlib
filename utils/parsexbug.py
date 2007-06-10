#!/usr/bin/python

import sys
import os
import pprint
import struct


# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))

def dummy_buffer(str, x, y = sys.maxint):
    return str[x:y]

__builtins__.buffer = dummy_buffer

from Xlib.protocol import display, request, rq, event
from Xlib import error

# We don't want any fancy dictwrapper, just plain mappings
rq.DictWrapper = lambda x: x

class BugFile:
    def __init__(self, file):
        self.file = file
        self.cbuf = self.sbuf = ''

    def read_client(self, bytes):
        while len(self.cbuf) < bytes and self.file:
            self.read_next()

        d = self.cbuf[:bytes]
        self.cbuf = self.cbuf[bytes:]

        return d

    def read_server(self, bytes):
        while len(self.sbuf) < bytes and self.file:
            self.read_next()

        d = self.sbuf[:bytes]
        self.sbuf = self.sbuf[bytes:]

        return d

    def read_next(self):
        line = self.file.readline()
        if line == '':
            self.file = None
            return

        src = line[0]
        length = int(line[1:-1])
        data = self.file.read(length)
        if src == 'C':
            self.cbuf = self.cbuf + data
        elif src == 'S':
            self.sbuf = self.sbuf + data
        else:
            raise ValueError('Bad control line: %s' % line)


class ParseString:
    def __init__(self, datafunc):
        self.get_data = datafunc
        self.data = ''

    def __getitem__(self, i):
        if i < 0:
            raise ValueError('bad string index: %d' % i)

        if len(self.data) <= i:
            if not self.get_data:
                raise RuntimeError('attempt to allocate more data after returning a new ParseString')

            self.data = self.data + self.get_data(i - len(self.data) + 1)

        return self.data[i]

    def __getslice__(self, i, j):
        if j == sys.maxint:
            if self.get_data:
                ps = ParseString(self.get_data)
                self.get_data = None
                return ps
            else:
                raise RuntimeError('attempt to allocate another ParseString')


        if i < 0 or j < 0 or i > j:
            raise ValueError('bad slice indices: [%d:%d]' % (i, j))

        if len(self.data) < j:
            if not self.get_data:
                raise RuntimeError('attempt to allocate more data after returning a new ParseString')

            self.data = self.data + self.get_data(j - len(self.data))

        return self.data[i:j]

class DummyDisplay:
    def get_resource_class(self, name):
        return None

class ParseXbug:
    def __init__(self, infile = sys.stdin, outfile = sys.stdout):
        bf = BugFile(infile)
        self.cdata = ParseString(bf.read_client)
        sdata = ParseString(bf.read_server)

        self.outfile = outfile
        self.xpprint = pprint.PrettyPrinter(indent = 2, stream = outfile)

        self.disp = DummyDisplay()

        # Parse client setup request
        r, self.cdata = display.ConnectionSetupRequest._request.parse_binary(self.cdata, self.disp)

        self.print_xbug('request', 'ConnectionSetup', r)

        # Parse server reply
        r, sdata = display.ConnectionSetupRequest._reply.parse_binary(sdata, self.disp)

        extra = r['additional_length'] * 4
        del r['additional_length']

        extradata = sdata[:extra]
        sdata = sdata[extra:]

        if r['status'] == 0:
            r['reason'] = extradata[:r['reason_length']]
            del r['status']
            del r['reason_length']
            self.print_xbug('error', 'ConnectionSetup', r)
            return

        elif r['status'] == 1:
            r2, d = display.ConnectionSetupRequest._success_reply.parse_binary(extradata, self.disp)
            del r['status']
            del r['reason_length']
            r.update(r2)
            del r2
            self.print_xbug('reply', 'ConnectionSetup', r)

        else:
            raise ValueError('bad connection setup reply status: %d' % r['status'])


        self.last_serial = 0
        self.last_request = None

        while 1:
            # Get next server item, always at least 32 bytes
            d = sdata[:32]
            if len(d) != 32:
                # Print out remaining requests
                try:
                    self.get_requests(sys.maxint)
                except ValueError:
                    pass
                return

            sdata = sdata[32:]

            # Check type
            t = ord(d[0])

            # Error
            if t == 0:
                # Code is second byte
                code = ord(d[1])
                # Fetch error class
                estruct = error.xerror_class.get(code, error.XError)
                r, d = estruct._fields.parse_binary(d, self.disp)
                del r['type']

                self.get_requests(r['sequence_number'])
                self.print_xbug('error', estruct.__name__, r)

            # Reply
            elif t == 1:
                # Get sequence number, and read corresponding request
                sno = struct.unpack('=H', d[2:4])[0]
                self.get_requests(sno)

                # Get entire reply length
                rlen = int(struct.unpack('=L', d[4:8])[0]) * 4
                d = d + sdata[:rlen]
                sdata = sdata[rlen:]

                if self.last_request:
                    r, d = self.last_request._reply.parse_binary(d, self.disp)
                    self.print_xbug('reply', self.last_request.__name__, r)
                else:
                    self.print_xbug('reply', 'Unknown',
                                    { 'sequence_number': sno })

            # Some event
            else:
                estruct = event.event_class.get(t, event.AnyEvent)
                r, d = estruct._fields.parse_binary(d, self.disp)

                self.get_requests(r['sequence_number'])
                self.print_xbug('event', estruct.__name__, r)

    def get_requests(self, serial):
        # Get request length
        while self.last_serial < serial:
            d = self.cdata[2:4]
            if len(d) != 2:
                raise ValueError('client request missing')

            rlen = struct.unpack('=H', d)[0] * 4
            d = self.cdata[:rlen]
            if len(d) != rlen:
                raise ValueError('client request missing')

            self.cdata = self.cdata[rlen:]

            opcode = ord(d[0])
            self.last_request = request.major_codes.get(opcode)
            self.last_serial = self.last_serial + 1

            if self.last_request:
                r, d = self.last_request._request.parse_binary(d, self.disp)
                r['sequence_number'] = self.last_serial
                self.print_xbug('request', self.last_request.__name__, r)

            else:
                self.print_xbug('request', 'Unknown (%d)' % opcode,
                                { 'sequence_number': self.last_serial })



    def print_xbug(self, rtype, name, data):
        self.outfile.write('%-8s %s\n' % (rtype + ':', name))
        self.xpprint.pprint(data)
        self.outfile.write('\n')

if __name__ == '__main__':
    ParseXbug()
