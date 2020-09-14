#!/usr/bin/python
#
# examples/dpms.py -- DPMS usage examples.
#
#    Copyright (C) 2020 Thiago Kenji Okada <thiagokokada@gmail.com>
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

import random
import time

from Xlib import display
from Xlib.ext import dpms


class DPMSExamples(object):
    def __init__(self):
        self.d = display.Display()

        capable = self.d.dpms_capable()
        assert capable, 'DPMS is not supported in your system'

        self.initial_info = self.d.dpms_info()
        self.initial_timeouts = self.d.dpms_get_timeouts()

        # Making sure that DPMS is enable for this examples
        self.d.dpms_enable()
        self.d.sync()

    def print_dpms(self):
        current_info = self.d.dpms_info()
        print('\nDPMS state: {}\nPower level: {}'.format(current_info.state,
                                                         current_info.power_level))
        current_timeouts = self.d.dpms_get_timeouts()
        print('Standby: {}, Suspend: {}, Off: {}\n'.format(current_timeouts.standby_timeout,
                                                           current_timeouts.suspend_timeout,
                                                           current_timeouts.off_timeout))

    def toggle_dpms(self):
        current_info = self.d.dpms_info()
        if current_info.state:
            self.d.dpms_disable()
        else:
            self.d.dpms_enable()

        self.d.sync()

    def restore(self):
        print('Restoring DPMS configuration')
        self.d.dpms_set_timeouts(self.initial_timeouts.standby_timeout,
                                 self.initial_timeouts.suspend_timeout,
                                 self.initial_timeouts.off_timeout)
        if self.initial_info.state:
            self.d.dpms_enable()
        else:
            self.d.dpms_disable()

        self.d.sync()

        self.print_dpms()

    def set_random_timeouts(self):
        # Can be any number greater than 0
        # Using 10 just to not turnoff the screen suddenly
        standby_timeout = random.randint(10, 600)
        # Shouldn't be smaller than standby_timeout
        suspend_timeout = random.randint(standby_timeout, 600)
        # Shouldn't be smaller than standby_timeout or suspend_timeout
        off_timeout = random.randint(suspend_timeout, 600)
        self.d.dpms_set_timeouts(standby_timeout, suspend_timeout, off_timeout)
        self.d.sync()

    def turn_off_display(self):
        self.d.dpms_force_level(dpms.DPMSModeOff)
        self.d.sync()

    def turn_on_display(self):
        self.d.dpms_force_level(dpms.DPMSModeOn)
        self.d.sync()


def main():
    try:
        examples = DPMSExamples()

        print('Initial state')
        examples.print_dpms()

        print('Setting random timeouts')
        examples.set_random_timeouts()
        examples.print_dpms()

        print('The next example will turn-off your screen, press Ctrl-C to cancel.')
        time.sleep(2)
        examples.turn_off_display()

        print('Turning it on again...')
        time.sleep(2)
        examples.turn_on_display()

        print()

        print('Toggle DPMS')
        examples.toggle_dpms()
        examples.print_dpms()

        print('Toggle it again')
        examples.toggle_dpms()
        examples.print_dpms()
    finally:
        examples.restore()


if __name__ == '__main__':
    main()
