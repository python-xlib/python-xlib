#!/usr/bin/env python
#
# examples/eventthread.py -- Tests multithreaded event handling
#
#    Copyright (C) 2010-2011 Outpost Embedded, LLC
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

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
from threading import Thread

from Xlib import Xatom, threaded
from Xlib.display import Display


class EventThread(Thread):
    display = None
    _stop = None

    def __init__(self, display):
        super(EventThread, self).__init__()
        self.display = display
        self.daemon = True

    def run(self):
        while True:
            event = self.display.next_event()
            print('event: %r' % event)


def main(argv):
    display = Display()

    thread = EventThread(display)
    thread.start()
    time.sleep(1)

    screen = display.screen()

    # The get_property call should not deadlock, despite the blocking next_event
    # call in the thread.
    atom = display.intern_atom('_XROOTPMAP_ID', True)
    response = screen.root.get_property(atom, Xatom.PIXMAP, 0, 1)
    print('get_property response: %r' % response)

    display.close()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
