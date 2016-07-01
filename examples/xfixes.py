#!/usr/bin/python
#
# examples/xfixes.py -- demonstrate the XFIXES extension
#
#    Copyright (C) 2011 Outpost Embedded, LLC
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

# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os
import time

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib.display import Display


def main(argv):
    display = Display()

    if not display.has_extension('XFIXES'):
        if display.query_extension('XFIXES') is None:
            print('XFIXES extension not supported', file=sys.stderr)
            return 1

    xfixes_version = display.xfixes_query_version()
    print('Found XFIXES version %s.%s' % (
      xfixes_version.major_version,
      xfixes_version.minor_version,
    ), file=sys.stderr)

    screen = display.screen()

    print('Hiding cursor ...', file=sys.stderr)
    screen.root.xfixes_hide_cursor()
    display.sync()

    time.sleep(5)

    print('Showing cursor ...', file=sys.stderr)
    screen.root.xfixes_hide_cursor()
    display.sync()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
