#!/usr/bin/python
#
# examples/record_demo.py -- demonstrate record extension
#
#    Copyright (C) 2006 Alex Badea <vamposdecampos@gmail.com>
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
Simple demo for the RECORD extension

Not very much unlike the xmacrorec2 program in the xmacro package.
'''


# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq

local_dpy = display.Display()
record_dpy = display.Display()

def lookup_keysym(keysym):
    for name in dir(XK):
        if name[:3] == "XK_" and getattr(XK, name) == keysym:
            return name[3:]
    return "[%d]" % keysym

def record_callback(reply):
    if reply.category != record.FromServer:
        return
    if reply.client_swapped:
        print("* received swapped protocol data, cowardly ignored")
        return
    if not len(reply.data) or reply.data[0] < 2:
        # not an event
        return

    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)

        if event.type in [X.KeyPress, X.KeyRelease]:
            pr = event.type == X.KeyPress and "Press" or "Release"

            keysym = local_dpy.keycode_to_keysym(event.detail, 0)
            if not keysym:
                print("KeyCode%s" % pr, event.detail)
            else:
                print("KeyStr%s" % pr, lookup_keysym(keysym))

            if event.type == X.KeyPress and keysym == XK.XK_Escape:
                local_dpy.record_disable_context(ctx)
                local_dpy.flush()
                return
        elif event.type == X.ButtonPress:
            print("ButtonPress", event.detail)
        elif event.type == X.ButtonRelease:
            print("ButtonRelease", event.detail)
        elif event.type == X.MotionNotify:
            print("MotionNotify", event.root_x, event.root_y)


# Check if the extension is present
if not record_dpy.has_extension("RECORD"):
    print("RECORD extension not found")
    sys.exit(1)
r = record_dpy.record_get_version(0, 0)
print("RECORD extension version %d.%d" % (r.major_version, r.minor_version))

# Create a recording context; we only want key and mouse events
ctx = record_dpy.record_create_context(
        0,
        [record.AllClients],
        [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': (X.KeyPress, X.MotionNotify),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
        }])

# Enable the context; this only returns after a call to record_disable_context,
# while calling the callback function in the meantime
record_dpy.record_enable_context(ctx, record_callback)

# Finally free the context
record_dpy.record_free_context(ctx)
