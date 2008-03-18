#!/usr/bin/python

import sys
import os

sys.path[1:1] = [os.path.join(sys.path[0], '..')]

from Xlib import display, X, threaded
import time
import thread

def redraw(win, gc):
    # win.clear_area()
    win.fill_rectangle(gc, 20, 20, 60, 60)

def blink(display, win, gc, cols):
    while 1:
        time.sleep(2)
        print 'Changing color', cols[0]
        gc.change(foreground = cols[0])
        cols = (cols[1], cols[0])
        redraw(win, gc)
        display.flush()

def main():
    d = display.Display()
    root = d.screen().root

    colormap = d.screen().default_colormap

    red = colormap.alloc_named_color("red").pixel
    blue = colormap.alloc_named_color("blue").pixel
    background = colormap.alloc_named_color("white").pixel

    window = root.create_window(100, 100, 100, 100, 1,
                                X.CopyFromParent, X.InputOutput,
                                X.CopyFromParent,
                                background_pixel = background,
                                event_mask = X.StructureNotifyMask | X.ExposureMask)
    window.map()

    gc = window.create_gc(foreground = red)

    thread.start_new_thread(blink, (d, window, gc, (blue, red)))

    while 1:
        event = d.next_event()
        if event.type == X.Expose:
            if event.count == 0:
                redraw(window, gc)
        elif event.type == X.DestroyNotify:
            sys.exit(0)

if __name__ == "__main__":
    main()
