#!/usr/bin/python3
#
# examples/xfixes-cursor-notify.py -- demonstrate the XFIXES extension
# CursorNotify event.
#
#    Copyright (C) 2022
#      Dan Isla <dan.isla@gmail.com>
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
from Xlib.display import Display
from Xlib.ext import xfixes

def main():
    display = Display()

    if not display.has_extension('XFIXES'):
        if display.query_extension('XFIXES') is None:
            print('XFIXES extension not supported')
            return 1

    xfixes_version = display.xfixes_query_version()
    print('Found XFIXES version {}.{}'.format(
        xfixes_version.major_version,
        xfixes_version.minor_version
    ))

    screen = display.screen()

    display.xfixes_select_cursor_input(screen.root, xfixes.XFixesDisplayCursorNotifyMask)

    cursor_cache = {}
  
    while True:
        e = display.next_event()
        print(e)

        if (e.type, e.sub_code) == display.extension_event.DisplayCursorNotify:
            print("DisplayCursorNotify: cursor_serial={}".format(e.cursor_serial))
            image = display.xfixes_get_cursor_image(screen.root)
            cached = False
            if cursor_cache.get(image.cursor_serial):
                cached = True
            else:
                cursor_cache[image.cursor_serial] = image.cursor_image

            print("Cursor position={},{}, size={}x{}, xyhot={},{}, cursor_serial={}, cached={}".format(
                image.x, image.y, image.width,image.height, image.xhot, image.yhot, image.cursor_serial, cached
            ))


if __name__ == "__main__":
    sys.exit(main())
