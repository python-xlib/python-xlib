#!/usr/bin/python
#
# examples/xfixes.py -- demonstrate the XFIXES extension
#
#    Copyright (C) 2011 Outpost Embedded, LLC
#      Forest Bond <forest.bond@rapidrollout.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


import sys, os
from optparse import OptionParser

# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Xlib.display import Display


def main(argv):
    parser = OptionParser()
    parser.add_option('--hide-cursor', action='store_true', default=False)
    parser.add_option('--show-cursor', action='store_true', default=False)

    opts, args = parser.parse_args(argv[1:])

    if opts.hide_cursor and opts.show_cursor:
        parser.error('--hide-cursor and --show-cursor cannot be combined')

    if not any((opts.hide_cursor, opts.show_cursor)):
        parser.error('specify --hide-cursor or --show-cursor')

    display = Display()

    if not display.has_extension('XFIXES'):
        if display.query_extension('XFIXES') is None:
            print >>sys.stderr, 'XFIXES extension not supported'
            return 1

    xfixes_version = display.xfixes_query_version()
    print >>sys.stderr, 'Found XFIXES version %s.%s' % (
      xfixes_version.major_version,
      xfixes_version.minor_version,
    )

    if opts.hide_cursor:
        display.screen().root.xfixes_hide_cursor()
    elif opts.show_cursor:
        display.screen().root.xfixes_hide_cursor()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
