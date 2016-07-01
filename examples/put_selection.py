#!/usr/bin/env python
#
# examples/put_selection.py -- demonstrate putting selections
# (equivalent to copying to the clipboard)
#
#	Copyright (C) 2013 Peter Liljenberg <peter.liljenberg@gmail.com>
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

import sys
import os

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib import X, display, Xutil, Xatom
from Xlib.protocol import event


# This script does not implement fancy stuff like INCR or MULTIPLE, so
# put a hard limit on the amount of data we allow sending this way
MAX_SIZE = 50000


def log(msg, *args):
    sys.stderr.write(msg.format(*args) + '\n')

def error(msg, *args):
    log(msg, *args)
    sys.exit(1)


def main():
    if len(sys.argv) < 3:
        sys.exit('usage: {0} SELECTION TYPE [FILE [TYPE [FILE...]]]\n\n'
                 'SELECTION is typically PRIMARY, SECONDARY or CLIPBOARD.\n'
                 'If FILE is omitted, stdin is read.\n'
                 'Multiple type/file combos can be specified.\n'
                 .format(sys.argv[0]))

    args = sys.argv[1:]

    d = display.Display()

    sel_name = args[0]
    del args[0]
    sel_atom = d.get_atom(sel_name)

    # map type atom -> data
    types = {}

    while args:
        type_atom = d.get_atom(args[0])
        del args[0]

        if args:
            f = open(args[0], 'rb')
            del args[0]
        else:
            f = sys.stdin

        # Limit selection size to avoid implementing INCR
        data = f.read(MAX_SIZE)
        f.close()

        if len(data) >= MAX_SIZE:
            log('too much data: {0} bytes, max is {1} bytes', len(data), MAX_SIZE)
            error('INCR support not implemented to put larger files')

        types[type_atom] = data


    targets_atom = d.get_atom('TARGETS')


    # We must have a window to own a selection
    w = d.screen().root.create_window(
        0, 0, 10, 10, 0, X.CopyFromParent)

    # And to grab the selection we must have a timestamp, get one with
    # a property notify when we're anyway setting wm_name
    w.change_attributes(event_mask = X.PropertyChangeMask)
    w.set_wm_name(os.path.basename(sys.argv[0]))

    e = d.next_event()
    sel_time = e.time
    w.change_attributes(event_mask = 0)

    # Grab the selection and make sure we actually got it
    w.set_selection_owner(sel_atom, sel_time)
    if d.get_selection_owner(sel_atom) != w:
        log('could not take ownership of {0}', sel_name)
        return

    log('took ownership of selection {0}', sel_name)

    # The event loop, waiting for and processing requests
    while True:
        e = d.next_event()

        if (e.type == X.SelectionRequest
            and e.owner == w
            and e.selection == sel_atom):

            client = e.requestor

            if e.property == X.NONE:
                log('request from obsolete client!')
                client_prop = e.target # per ICCCM recommendation
            else:
                client_prop = e.property

            target_name = d.get_atom_name(e.target)

            log('got request for {0}, dest {1} on 0x{2:08x} {3}',
                target_name, d.get_atom_name(client_prop),
                client.id, client.get_wm_name())

            # Is the client asking for which types we support?
            if e.target == targets_atom:
                # Then respond with TARGETS and the type
                prop_value = [targets_atom] + types.keys()
                prop_type = Xatom.ATOM
                prop_format = 32

            # Request for the offered type
            elif e.target in types:
                prop_value = types[e.target]
                prop_type = e.target
                prop_format = 8

            # Something else, tell client they can't get it
            else:
                log('refusing conversion to {0}', target_name)
                client_prop = X.NONE

            # Put the data on the dest window, if possible
            if client_prop != X.NONE:
                client.change_property(
                    client_prop, prop_type, prop_format, prop_value)

            # And always send a selection notification
            ev = event.SelectionNotify(
                time = e.time,
                requestor = e.requestor,
                selection = e.selection,
                target = e.target,
                property = client_prop)

            client.send_event(ev)

            # Done!

        elif (e.type == X.SelectionClear
              and e.window == w
              and e.atom == sel_atom):
            log('lost ownership of selection {0}', sel_name)
            return

        # A proper owner would also look for PropertyNotify here on
        # the selector's windows to implement INCR and waiting for
        # acknowledgement that the client has finished copying.


if __name__ == '__main__':
    main()
