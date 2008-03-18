#!/usr/bin/python
#
# examples/shapewin.py -- demonstrate shape extension
#
#    Copyright (C) 2002 Peter Liljenberg <petli@ctrl-c.liu.se>
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


import sys
import os

# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Xlib import X, display, Xutil
from Xlib.ext import shape

# Application window (only one)
class Window:
    def __init__(self, display):
        self.d = display

        # Check for extension
        if not self.d.has_extension('SHAPE'):
            sys.stderr.write('%s: server does not have SHAPE extension\n'
                             % sys.argv[1])
            sys.exit(1)

        # print version
        r = self.d.shape_query_version()
        print 'SHAPE version %d.%d' % (r.major_version, r.minor_version)


        # Find which screen to open the window on
        self.screen = self.d.screen()

        # background pattern
        bgsize = 20

        bgpm = self.screen.root.create_pixmap(bgsize, bgsize, self.screen.root_depth)

        bggc = self.screen.root.create_gc(foreground = self.screen.black_pixel,
                                          background = self.screen.black_pixel)

        bgpm.fill_rectangle(bggc, 0, 0, bgsize, bgsize)

        bggc.change(foreground = self.screen.white_pixel)

        bgpm.arc(bggc, -bgsize / 2, 0, bgsize, bgsize, 0, 360 * 64)
        bgpm.arc(bggc, bgsize / 2, 0, bgsize, bgsize, 0, 360 * 64)
        bgpm.arc(bggc, 0, -bgsize / 2, bgsize, bgsize, 0, 360 * 64)
        bgpm.arc(bggc, 0, bgsize / 2, bgsize, bgsize, 0, 360 * 64)

        # Actual window
        self.window = self.screen.root.create_window(
            100, 100, 400, 300, 0,
            self.screen.root_depth,
            X.InputOutput,
            X.CopyFromParent,

            # special attribute values
            background_pixmap = bgpm,
            event_mask = (X.StructureNotifyMask |
                          X.ButtonReleaseMask),
            colormap = X.CopyFromParent,
            )

        # Set some WM info

        self.WM_DELETE_WINDOW = self.d.intern_atom('WM_DELETE_WINDOW')
        self.WM_PROTOCOLS = self.d.intern_atom('WM_PROTOCOLS')

        self.window.set_wm_name('Xlib example: shapewin.py')
        self.window.set_wm_icon_name('shapewin.py')
        self.window.set_wm_class('shapewin', 'XlibExample')

        self.window.set_wm_protocols([self.WM_DELETE_WINDOW])
        self.window.set_wm_hints(flags = Xutil.StateHint,
                                 initial_state = Xutil.NormalState)

        self.window.set_wm_normal_hints(flags = (Xutil.PPosition | Xutil.PSize
                                                 | Xutil.PMinSize),
                                        min_width = 50,
                                        min_height = 50)

        # The add and subtract shapes
        self.add_size = 60

        self.add_pm = self.window.create_pixmap(self.add_size, self.add_size, 1)
        gc = self.add_pm.create_gc(foreground = 0, background = 0)
        self.add_pm.fill_rectangle(gc, 0, 0, self.add_size, self.add_size)
        gc.change(foreground = 1)
        self.add_pm.fill_arc(gc, 0, 0, self.add_size, self.add_size, 0, 360 * 64)
        gc.free()

        self.sub_size = 59
        self.sub_pm = self.window.create_pixmap(self.sub_size, self.sub_size, 1)
        gc = self.sub_pm.create_gc(foreground = 0, background = 0)
        self.sub_pm.fill_rectangle(gc, 0, 0, self.sub_size, self.sub_size)
        gc.change(foreground = 1)
        self.sub_pm.fill_poly(gc, X.Convex, X.CoordModeOrigin,
                              [(self.sub_size / 2, 0),
                               (self.sub_size, self.sub_size / 2),
                               (self.sub_size / 2, self.sub_size),
                               (0, self.sub_size / 2)])
        gc.free()

        # Set initial mask
        self.window.shape_mask(shape.ShapeSet, shape.ShapeBounding,
                               0, 0, self.add_pm)
        self.window.shape_mask(shape.ShapeUnion, shape.ShapeBounding,
                               400 - self.add_size, 0, self.add_pm)
        self.window.shape_mask(shape.ShapeUnion, shape.ShapeBounding,
                               0, 300 - self.add_size, self.add_pm)
        self.window.shape_mask(shape.ShapeUnion, shape.ShapeBounding,
                               400 - self.add_size, 300 - self.add_size,
                               self.add_pm)

        # Tell X server to send us mask events
        self.window.shape_select_input(1)

        # Map the window, making it visible
        self.window.map()


    # Main loop, handling events
    def loop(self):
        current = None
        while 1:
            e = self.d.next_event()

            # Window has been destroyed, quit
            if e.type == X.DestroyNotify:
                sys.exit(0)

            # Button released, add or subtract
            elif e.type == X.ButtonRelease:
                if e.detail == 1:
                    self.window.shape_mask(shape.ShapeUnion,
                                           shape.ShapeBounding,
                                           e.event_x - self.add_size / 2,
                                           e.event_y - self.add_size / 2,
                                           self.add_pm)
                elif e.detail == 3:
                    self.window.shape_mask(shape.ShapeSubtract,
                                           shape.ShapeBounding,
                                           e.event_x - self.sub_size / 2,
                                           e.event_y - self.sub_size / 2,
                                           self.sub_pm)

            # Shape has changed
            elif e.type == self.d.extension_event.ShapeNotify:
                print 'Shape change'

            # Somebody wants to tell us something
            elif e.type == X.ClientMessage:
                if e.client_type == self.WM_PROTOCOLS:
                    fmt, data = e.data
                    if fmt == 32 and data[0] == self.WM_DELETE_WINDOW:
                        sys.exit(0)


if __name__ == '__main__':
    Window(display.Display()).loop()
