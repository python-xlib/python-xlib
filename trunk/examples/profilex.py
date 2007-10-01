#!/usr/bin/python
#
# Program to generate profiling data.  Run with one argument,
# the profile stats file to generate.

import sys
import os

# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Xlib import X, display, Xatom

import profile

def dostuff():
    d = display.Display()
    r = d.screen().root
    cm = d.screen().default_colormap

    for i in xrange(0, 1000):
        if i % 50 == 0:
            print 'Iteration', i

        r.delete_property(Xatom.WM_NORMAL_HINTS)
        r.delete_property(Xatom.WM_NORMAL_HINTS)
        r.get_geometry()
        r.get_geometry()
        r.delete_property(Xatom.WM_NORMAL_HINTS)
        r.delete_property(Xatom.WM_NORMAL_HINTS)
        r.change_property(Xatom.WM_NORMAL_HINTS, Xatom.STRING, 32, [1, 2, 3, 4])
        r.query_tree()
        cm.query_colors([0, 1, 2, 3, 4, 5, 6, 7])

def main(filename):
    profile.run('dostuff()', filename)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print sys.argv[0], "<filename to write profile output to>"
