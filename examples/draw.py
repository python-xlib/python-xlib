#!/usr/bin/python
#
# examples/draw.py -- high-level xlib test application.
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


import sys
import os

# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Xlib import X, display, Xutil

# Application window (only one)
class Window:
    def __init__(self, display):
        self.d = display
        self.objects = []

        # Find which screen to open the window on
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

        self.window.set_wm_name('Xlib example: draw.py')
        self.window.set_wm_icon_name('draw.py')
        self.window.set_wm_class('draw', 'XlibExample')

        self.window.set_wm_protocols([self.WM_DELETE_WINDOW])
        self.window.set_wm_hints(flags = Xutil.StateHint,
                                 initial_state = Xutil.NormalState)

        self.window.set_wm_normal_hints(flags = (Xutil.PPosition | Xutil.PSize
                                                 | Xutil.PMinSize),
                                        min_width = 20,
                                        min_height = 20)

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

            # Some part of the window has been exposed,
            # redraw all the objects.
            if e.type == X.Expose:
                for o in self.objects:
                    o.expose(e)

            # Left button pressed, start to draw
            if e.type == X.ButtonPress and e.detail == 1:
                current = Movement(self, e)
                self.objects.append(current)

            # Left button released, finish drawing
            if e.type == X.ButtonRelease and e.detail == 1 and current:
                current.finish(e)
                current = None

            # Mouse movement with button pressed, draw
            if e.type == X.MotionNotify and current:
                current.motion(e)

            if e.type == X.ClientMessage:
                if e.client_type == self.WM_PROTOCOLS:
                    fmt, data = e.data
                    if fmt == 32 and data[0] == self.WM_DELETE_WINDOW:
                        sys.exit(0)

# A drawed objects, consisting of either a single
# romboid, or two romboids connected by a winding line

class Movement:
    def __init__(self, win, ev):
        self.win = win

        self.left = ev.event_x - 5
        self.right = ev.event_x + 5
        self.top = ev.event_y - 5
        self.bottom = ev.event_y + 5

        self.time = ev.time
        self.lines = [(ev.event_x, ev.event_y)]

        self.first = Romboid(self.win, ev)
        self.last = None

    def motion(self, ev):
        # Find all the mouse coordinates since the
        # last event received

        events = self.win.window.get_motion_events(self.time, ev.time)
        self.time = ev.time

        # Record the previous last coordinate, and append
        # the new coordinates
        firstline = len(self.lines) - 1

        if events:
            # Discard the first coordinate if that is identical to
            # the last recorded coordinate

            pos = events[0]
            if (pos.x, pos.y) == self.lines[-1]:
                events = events[1:]

            # Append all coordinates
            for pos in events:
                x = pos.x
                y = pos.y

                if x < self.left:
                    self.left = x
                if x > self.right:
                    self.right = x

                if y < self.top:
                    self.top = y
                if y > self.bottom:
                    self.bottom = y

                self.lines.append((x, y))

        # Append the event coordinate, if that is different from the
        # last movement coordinate
        if (ev.event_x, ev.event_y) != self.lines[-1]:
            self.lines.append((ev.event_x, ev.event_y))

        # Draw a line between the new coordinates
        self.win.window.poly_line(self.win.gc,
                                  X.CoordModeOrigin,
                                  self.lines[firstline:])


    def finish(self, ev):
        self.motion(ev)
        if len(self.lines) > 1:
            self.last = Romboid(self.win, ev)

            self.left = min(ev.event_x - 5, self.left)
            self.right = max(ev.event_x + 5, self.right)
            self.top = min(ev.event_y - 5, self.top)
            self.bottom = max(ev.event_y + 5, self.bottom)

    def expose(self, ev):
        # We should check if this object is in the exposed
        # area, but I can't be bothered right now, so just
        # redraw on the last Expose in every batch

        if ev.count == 0:
            self.first.draw()
            if self.last:
                # Redraw all the lines
                self.win.window.poly_line(self.win.gc,
                                          X.CoordModeOrigin,
                                          self.lines)
                self.last.draw()


# A romboid, drawed around the Movement endpoints
class Romboid:
    def __init__(self, win, ev):
        self.win = win
        self.x = ev.event_x
        self.y = ev.event_y
        self.draw()

    def draw(self):
        # Draw the segments of the romboid
        self.win.window.poly_line(self.win.gc, X.CoordModePrevious,
                                  [(self.x, self.y - 5),
                                   (5, 5),
                                   (-5, 5),
                                   (-5, -5),
                                   (5, -5)])


if __name__ == '__main__':
    Window(display.Display()).loop()
