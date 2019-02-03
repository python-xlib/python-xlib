#!/usr/bin/python
#
# examples/security.py -- demonstrate the SECURITY extension
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

import sys, os
from optparse import OptionParser

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib.display import Display
from Xlib.ext import security


def main(argv):
    parser = OptionParser()

    parser.add_option('--generate', action='store_true', default=False)
    parser.add_option('--proto', default='MIT-MAGIC-COOKIE-1')
    parser.add_option('--trusted', action='store_true', default=False)
    parser.add_option('--untrusted', action='store_true', default=False)

    parser.add_option('--revoke', action='store_true', default=False)

    opts, args = parser.parse_args(argv[1:])

    if opts.trusted and opts.untrusted:
        parser.error('--trusted and --untrusted cannot be combined')

    if not any((opts.generate, opts.revoke)):
        parser.error('specify --generate or --revoke')

    display = Display()

    if not display.has_extension('SECURITY'):
        if display.query_extension('SECURITY') is None:
            print('SECURITY extension not supported', file=sys.stderr)
            return 1

    security_version = display.security_query_version()
    print('SECURITY version %s.%s' % (
      security_version.major_version,
      security_version.minor_version,
    ), file=sys.stderr)

    if opts.generate:
        kwargs = {}
        if opts.trusted:
            kwargs['trust_level'] = security.SecurityClientTrusted
        elif opts.untrusted:
            kwargs['trust_level'] = security.SecurityClientUntrusted
        reply = display.security_generate_authorization(opts.proto, **kwargs)
        print(reply.authid)

    elif opts.revoke:
        for arg in args:
            authid = int(arg, 10)
            display.security_revoke_authorization(authid)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
