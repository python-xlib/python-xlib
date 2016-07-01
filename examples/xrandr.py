#!/usr/bin/python
#
# examples/xrandr.py -- demonstrate the RandR extension
#
#    Copyright (C) 2009 David H. Bronke <whitelynx@gmail.com>
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


# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os
import pprint

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib import X, display, Xutil
from Xlib.ext import randr

# Application window (only one)
class Window(object):
    def __init__(self, display):
        self.d = display

        # Check for extension
        if not self.d.has_extension('RANDR'):
            sys.stderr.write('%s: server does not have the RANDR extension\n'
                             % sys.argv[0])
            print(self.d.query_extension('RANDR'))
            sys.stderr.write("\n".join(self.d.list_extensions()))
            if self.d.query_extension('RANDR') is None:
                sys.exit(1)

        # print(version)
        r = self.d.xrandr_query_version()
        print('RANDR version %d.%d' % (r.major_version, r.minor_version))


        # Grab the current screen
        self.screen = self.d.screen()

        self.window = self.screen.root.create_window(
            50, 50, 300, 200, 2,
            self.screen.root_depth,
            X.InputOutput,
            X.CopyFromParent,

            # special attribute values
            background_pixel = self.screen.white_pixel,
            event_mask = (X.ExposureMask |
                          X.StructureNotifyMask |
                          X.ButtonPressMask |
                          X.ButtonReleaseMask |
                          X.Button1MotionMask),
            colormap = X.CopyFromParent,
            )

        self.gc = self.window.create_gc(
            foreground = self.screen.black_pixel,
            background = self.screen.white_pixel,
            )

        # Set some WM info

        self.WM_DELETE_WINDOW = self.d.intern_atom('WM_DELETE_WINDOW')
        self.WM_PROTOCOLS = self.d.intern_atom('WM_PROTOCOLS')

        self.window.set_wm_name('Xlib example: xrandr.py')
        self.window.set_wm_icon_name('xrandr.py')
        self.window.set_wm_class('xrandr', 'XlibExample')

        self.window.set_wm_protocols([self.WM_DELETE_WINDOW])
        self.window.set_wm_hints(flags = Xutil.StateHint,
                                 initial_state = Xutil.NormalState)

        self.window.set_wm_normal_hints(flags = (Xutil.PPosition | Xutil.PSize
                                                 | Xutil.PMinSize),
                                        min_width = 20,
                                        min_height = 20)

        # Map the window, making it visible
        self.window.map()

        # Enable all RandR events.
        self.window.xrandr_select_input(
            randr.RRScreenChangeNotifyMask
            | randr.RRCrtcChangeNotifyMask
            | randr.RROutputChangeNotifyMask
            | randr.RROutputPropertyNotifyMask
            )

        self.pp = pprint.PrettyPrinter(indent=4)

        print("Screen info:")
        self.pp.pprint(self.window.xrandr_get_screen_info()._data)

        print("Screen size range:")
        self.pp.pprint(self.window.xrandr_get_screen_size_range()._data)

        print("Primary output:")
        self.pp.pprint(self.window.xrandr_get_output_primary()._data)

        resources = self.window.xrandr_get_screen_resources()._data

        print("Modes:")
        for mode_id, mode in self.parseModes(resources['mode_names'], resources['modes']).items():
            print("    %d: %s" % (mode_id, mode['name']))

        for output in resources['outputs']:
            print("Output %d info:" % (output, ))
            self.pp.pprint(self.d.xrandr_get_output_info(output, resources['config_timestamp'])._data)

        for crtc in resources['crtcs']:
            print("CRTC %d info:" % (crtc, ))
            self.pp.pprint(self.d.xrandr_get_crtc_info(crtc, resources['config_timestamp'])._data)

        print("Raw screen resources:")
        self.pp.pprint(resources)

    def parseModes(self, mode_names, modes):
        lastIdx = 0
        modedatas = dict()
        for mode in modes:
            modedata = dict(mode._data)
            modedata['name'] = mode_names[lastIdx:lastIdx + modedata['name_length']]
            modedatas[modedata['id']] = modedata
            lastIdx += modedata['name_length']
        return modedatas

    # Main loop, handling events
    def loop(self):
        current = None
        while 1:
            e = self.d.next_event()

            # Window has been destroyed, quit
            if e.type == X.DestroyNotify:
                sys.exit(0)

            # Screen information has changed
            elif e.__class__.__name__ == randr.ScreenChangeNotify.__name__:
                print('Screen change')
                print(self.pp.pprint(e._data))

            # check if we're getting one of the RandR event types with subcodes
            elif e.type == self.d.extension_event.CrtcChangeNotify[0]:
                # yes, check the subcodes

                # CRTC information has changed
                if (e.type, e.sub_code) == self.d.extension_event.CrtcChangeNotify:
                    print('CRTC change')
                    #e = randr.CrtcChangeNotify(display=display.display, binarydata = e._binary)
                    print(self.pp.pprint(e._data))

                # Output information has changed
                elif (e.type, e.sub_code) == self.d.extension_event.OutputChangeNotify:
                    print('Output change')
                    #e = randr.OutputChangeNotify(display=display.display, binarydata = e._binary)
                    print(self.pp.pprint(e._data))

                # Output property information has changed
                elif (e.type, e.sub_code) == self.d.extension_event.OutputPropertyNotify:
                    print('Output property change')
                    #e = randr.OutputPropertyNotify(display=display.display, binarydata = e._binary)
                    print(self.pp.pprint(e._data))
                else:
                    print("Unrecognised subcode", e.sub_code)

            # Somebody wants to tell us something
            elif e.type == X.ClientMessage:
                if e.client_type == self.WM_PROTOCOLS:
                    fmt, data = e.data
                    if fmt == 32 and data[0] == self.WM_DELETE_WINDOW:
                        sys.exit(0)


if __name__ == '__main__':
    Window(display.Display()).loop()
