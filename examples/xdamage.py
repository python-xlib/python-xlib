#!/usr/bin/python
#
# examples/xdamage.py -- demonstrate damage extension
#
#    Copyright (C) 2019 Mohit Garg <mrmohitgarg1990@gmail.com>
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

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib import display, X, threaded,Xutil
import time

try:
    import thread
except ModuleNotFoundError:
    import _thread as thread

from Xlib.ext import damage
from PIL import Image, ImageTk
import traceback

def redraw(win, gc):
    # win.clear_area()
    win.fill_rectangle(gc, 0, 0, 60, 60)

def blink(display, win, gc, cols):
    while 1:
        time.sleep(2)
        print('Changing color', cols[0])
        gc.change(foreground = cols[0])
        cols = (cols[1], cols[0])
        redraw(win, gc)
        display.flush()

def get_image_from_win(win, pt_w, pt_h, pt_x=0, pt_y=0):
    try:
        raw = win.get_image(pt_x, pt_y, pt_w, pt_h, X.ZPixmap, 0xffffffff)
        image = Image.frombytes("RGB", (pt_w, pt_h), raw.data, "raw", "BGRX")
        return image

    except Exception:
        traceback.print_exc()

def check_ext(disp):
    # Check for extension
    if not disp.has_extension('DAMAGE'):
        sys.stderr.write('server does not have the DAMAGE extension\n')
        sys.stderr.write("\n".join(disp.list_extensions()))
        
        if disp.query_extension('DAMAGE') is None:
            sys.exit(1)
    else:
        r = disp.damage_query_version()
        print('DAMAGE version {}.{}'.format(r.major_version, r.minor_version))
    
def main():
    d = display.Display()
    root = d.screen().root

    check_ext(d)
    colormap = d.screen().default_colormap

    red = colormap.alloc_named_color("red").pixel
    blue = colormap.alloc_named_color("blue").pixel
    background = colormap.alloc_named_color("white").pixel

    window1 = root.create_window(100, 100, 250, 100, 1,
                                X.CopyFromParent, X.InputOutput,
                                X.CopyFromParent,
                                background_pixel = background,
                                event_mask = X.StructureNotifyMask | X.ExposureMask)
    window1.set_wm_name('Changing Window')
    window1.map()
    gc = window1.create_gc(foreground = red)
    
    thread.start_new_thread(blink, (d, window1, gc, (blue, red)))
    
    window1.damage_create(damage.DamageReportRawRectangles)
    window1.set_wm_normal_hints(
            flags=(Xutil.PPosition | Xutil.PSize | Xutil.PMinSize),
            min_width=50,
            min_height=50
            )

    window2 = root.create_window(100, 250, 250, 100, 1,
                                X.CopyFromParent, X.InputOutput,
                                X.CopyFromParent,
                                background_pixel = background,
                                event_mask = X.StructureNotifyMask | X.ExposureMask)
    window2.set_wm_normal_hints(
            flags=(Xutil.PPosition | Xutil.PSize | Xutil.PMinSize),
            min_width=50,
            min_height=50
            )

    window2.set_wm_name('Tracking Window')
    window2.map()

    while 1:
        event = d.next_event()
        if event.type == X.Expose:
            if event.count == 0:
                redraw(window1, gc)
        elif event.type == d.extension_event.DamageNotify:
            image = get_image_from_win(window1, event.area.width, event.area.height, event.area.x, event.area.y)
            bgpm = window2.create_pixmap(image.width, image.height, d.screen().root_depth)
            bggc = window2.create_gc(foreground=0, background=0)
            bgpm.put_pil_image(bggc, 0, 0, image)
            window2.copy_area(bggc, bgpm, 0, 0, image.width, image.height, 0, 0)
            # bggc.free()
        elif event.type == X.DestroyNotify:
            sys.exit(0)

if __name__ == "__main__":
    main()
