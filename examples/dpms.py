#!/usr/bin/python
#
# examples/dpms.py -- DPMS usage examples.
#
#    Copyright (C) 2020 Thiago Kenji Okada<thiagokokada@gmail.com>
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

import time

from Xlib import display
from Xlib.ext import dpms


class DPMSExamples(object):
    def __init__(self):
        self.d = display.Display()
        # Making sure that DPMS is enabled
        self.d.dpms_enable()
        # For some reason, the call above needs another X11 call
        # to actually trigger it
        self.d.dpms_get_version()

    def dpms_info(self):
        capable = self.d.dpms_capable()
        timeouts = self.d.dpms_get_timeouts()

        return (capable, timeouts)

    def turn_off_display(self):
        self.d.dpms_force_level(dpms.DPMSModeOff)
        # For some reason, the call above needs another X11 call
        # to actually trigger it
        self.d.dpms_get_version()

    def turn_on_display(self):
        self.d.dpms_force_level(dpms.DPMSModeOn)
        # For some reason, the call above needs another X11 call
        # to actually trigger it
        self.d.dpms_get_version()


if __name__ == '__main__':
    examples = DPMSExamples()

    capable, timeouts = examples.dpms_info()

    assert capable, 'DPMS is not supported in your system'

    print('Current DPMS timeouts:')
    print('Standby: {}, Suspend: {}, Off: {}'.format(
        timeouts.standby_timeout,
        timeouts.suspend_timeout,
        timeouts.off_timeout
    ))

    print('\nThe next example will turn-off your screen, press Ctrl-C to cancel.')
    time.sleep(2)
    examples.turn_off_display()

    print('\nTurning it on again...')
    time.sleep(2)
    examples.turn_on_display()
