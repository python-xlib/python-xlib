#!/usr/bin/python3
#
# examples/xfixes-selection-notify.py -- demonstrate the XFIXES extension
# SelectionNotify event.
#
#    Copyright (C) 2019
#      Tony Crisci <tony@dubstepdish.com>
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
from Xlib.ext import xfixes

def main(argv):
    if len(sys.argv) != 2:
        sys.exit('usage: {0} SELECTION\n\n'
                 'SELECTION is typically PRIMARY, SECONDARY or CLIPBOARD.\n'
                 .format(sys.argv[0]))

    display = Display()

    sel_name = sys.argv[1]
    sel_atom = display.get_atom(sel_name)

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

    mask = xfixes.XFixesSetSelectionOwnerNotifyMask | \
           xfixes.XFixesSelectionWindowDestroyNotifyMask | \
           xfixes.XFixesSelectionClientCloseNotifyMask

    display.xfixes_select_selection_input(screen.root, sel_atom, mask)

    while True:
        e = display.next_event()
        print(e)

        if (e.type, e.sub_code) == display.extension_event.SetSelectionOwnerNotify:
            print('SetSelectionOwner: owner=0x{0:08x}'.format(e.owner.id))
        elif (e.type, e.sub_code) == display.extension_event.SelectionWindowDestroyNotify:
            print('SelectionWindowDestroy: owner=0x{0:08x}'.format(e.owner.id))
        elif (e.type, e.sub_code) == display.extension_event.SelectionClientCloseNotify:
            print('SelectionClientClose: owner=0x{0:08x}'.format(e.owner.id))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
