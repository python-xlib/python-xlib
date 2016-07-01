# Xlib.ext.xfixes -- XFIXES extension module
#
#    Copyright (C) 2010-2011 Outpost Embedded, LLC
#      Forest Bond <forest.bond@rapidrollout.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA

'''
A partial implementation of the XFIXES extension.  Only the HideCursor and
ShowCursor requests are provided.
'''

from Xlib.protocol import rq

extname = 'XFIXES'


class QueryVersion(rq.ReplyRequest):
    _request = rq.Struct(rq.Card8('opcode'),
                         rq.Opcode(0),
                         rq.RequestLength(),
                         rq.Card32('major_version'),
                         rq.Card32('minor_version')
                         )
    _reply = rq.Struct(rq.ReplyCode(),
                       rq.Pad(1),
                       rq.Card16('sequence_number'),
                       rq.ReplyLength(),
                       rq.Card32('major_version'),
                       rq.Card32('minor_version'),
                       rq.Pad(16)
                       )


def query_version(self):
    return QueryVersion(display=self.display,
                        opcode=self.display.get_extension_major(extname),
                        major_version=4,
                        minor_version=0)


class HideCursor(rq.Request):
    _request = rq.Struct(rq.Card8('opcode'),
                         rq.Opcode(29),
                         rq.RequestLength(),
                         rq.Window('window')
                         )

def hide_cursor(self):
    HideCursor(display=self.display,
               opcode=self.display.get_extension_major(extname),
               window=self)


class ShowCursor(rq.Request):
    _request = rq.Struct(rq.Card8('opcode'),
                         rq.Opcode(30),
                         rq.RequestLength(),
                         rq.Window('window')
                         )


def show_cursor(self):
    ShowCursor(display=self.display,
               opcode=self.display.get_extension_major(extname),
               window=self)


def init(disp, info):
    disp.extension_add_method('display', 'xfixes_query_version', query_version)
    disp.extension_add_method('window', 'xfixes_hide_cursor', hide_cursor)
    disp.extension_add_method('window', 'xfixes_show_cursor', show_cursor)
