#!/usr/bin/python
#
# examples/draw.py -- protocol test application.
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

from Xlib import X
from Xlib.protocol import display
from Xlib.protocol.request import *

# Application window (only one)
class Window:
    def __init__(self, display):
        self.d = display
        self.objects = []

        # Find which screen to open the window on
        self.screen = self.d.info.roots[self.d.default_screen]

        # Allocate ids to the window and gc
        self.window = self.d.allocate_resource_id()
        self.gc = self.d.allocate_resource_id()

        # Create a window
        CreateWindow(self.d, None,
                     self.screen.root_depth,
                     self.window,
                     self.screen.root,
                     50, 50, 300, 200, 2,
                     X.InputOutput,
                     X.CopyFromParent,

                     # special attribute values
                     background_pixel = self.screen.white_pixel,
                     event_mask = (X.ExposureMask |
                                   X.StructureNotifyMask |
                                   X.ButtonPressMask |
                                   X.ButtonReleaseMask |
                                   X.Button1MotionMask),
                     colormap = X.CopyFromParent)

        # Create a gc for drawing
        CreateGC(self.d, None,
                 self.gc,
                 self.window,

                 # special attribute values
                 foreground = self.screen.black_pixel,
                 background = self.screen.white_pixel)

        # Map the window, making it visible
        MapWindow(self.d, None, self.window)

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

        r = GetMotionEvents(self.win.d,
                            window = self.win.window,
                            start = self.time,
                            stop = ev.time)

        # Record the previous last coordinate, and append
        # the new coordinates

        firstline = len(self.lines) - 1

        if r.events:
            # Discard the first coordinate if that is identical to
            # the last recorded coordinate

            pos = r.events[0]
            if (pos.x, pos.y) == self.lines[-1]:
                events = r.events[1:]
            else:
                events = r.events

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
        PolyLine(self.win.d, None,
                 X.CoordModeOrigin,
                 self.win.window,
                 self.win.gc,
                 self.lines[firstline:])

        self.time = ev.time

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
                PolyLine(self.win.d, None,
                         X.CoordModeOrigin,
                         self.win.window,
                         self.win.gc,
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
        PolyLine(self.win.d, None,
                 X.CoordModePrevious,
                 self.win.window,
                 self.win.gc,
                 [(self.x, self.y - 5),
                  (5, 5),
                  (-5, 5),
                  (-5, -5),
                  (5, -5)])


if __name__ == '__main__':
    Window(display.Display()).loop()
