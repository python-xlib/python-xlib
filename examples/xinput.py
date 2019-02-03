#!/usr/bin/python
#
# examples/xinput.py -- demonstrate the XInput extension
#
#    Copyright (C) 2012 Outpost Embedded, LLC
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

from Xlib.display import Display
from Xlib.ext import xinput


def print_hierarchy_changed_event(event):
    print('<deviceid=%s time=%s flags=%s info={' % (
        event.data.deviceid,
        event.data.time,
        event.data.flags,
        ))
    for info in event.data.info:
        print_info(info)
    print('}>')


def print_info(info):
    print('  <deviceid=%s attachment=%s type=%s enabled=%s flags=%s>' % (
        info.deviceid,
        info.attachment,
        info.type,
        info.enabled,
        info.flags,
        ))


def main(argv):
    display = Display()
    try:
        extension_info = display.query_extension('XInputExtension')
        xinput_major = extension_info.major_opcode

        version_info = display.xinput_query_version()
        print('Found XInput version %u.%u' % (
          version_info.major_version,
          version_info.minor_version,
        ))

        screen = display.screen()
        screen.root.xinput_select_events([
          (xinput.AllDevices, xinput.HierarchyChangedMask),
        ])

        while True:
            event = display.next_event()
            if (
              event.type == display.extension_event.GenericEvent
              and event.extension == xinput_major
              and event.evtype == 11
            ):
                print_hierarchy_changed_event(event)

    finally:
        display.close()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
