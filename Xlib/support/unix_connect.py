# $Id: unix_connect.py,v 1.1 2000-09-06 01:51:34 petli Exp $
#
# Xlib.support.unix_connect -- Unix-type display connection functions
#
#    Copyright (C) 2000 Peter Liljenberg <petli@ctrl-c.liu.se>
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

import re
import string
import os
import socket
import fcntl
import FCNTL

from Xlib import error

display_re = re.compile(r'^([-a-zA-Z0-9._]*):([0-9]+)(\.([0-9]+))?$')

def get_display(display):
    # Use $DISPLAY if display isn't provided
    if display is None:
	display = os.environ.get('DISPLAY', '')

    m = display_re.match(display)
    if not m:
	raise error.DisplayNameError(display)

    name = display
    host = m.group(1)
    dno = int(m.group(2))
    screen = m.group(4)
    if screen:
	screen = int(screen)
    else:
	screen = 0

    return name, host, dno, screen


def get_socket(dname, host, dno):
    try:
	# If hostname (or IP) is provided, use TCP socket
	if host:
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    s.connect((host, 6000 + dno))

	# Else use Unix socket
	else:
	    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	    s.connect('/tmp/.X11-unix/X%d' % dno)
    except socket.error, val:
	raise error.DisplayConnectionError(dname, str(val))

    # Make sure that the connection isn't inherited in child processes
    fcntl.fcntl(s.fileno(), FCNTL.F_SETFD, FCNTL.FD_CLOEXEC)

    return s


def get_auth(dname, host, dno):
    # Find authorization cookie
    auth_name = auth_data = ''
    
    try:
	# We could parse .Xauthority, but xauth is simpler
	# although more inefficient
	data = os.popen('xauth list %s 2>/dev/null' % dname).read()

	# If there's a cookie, it is of the format
	#      DISPLAY SCHEME COOKIE
	# We're interested in the two last parts for the
	# connection establishment
	lines = string.split(data, '\n')
	if len(lines) >= 1:
	    parts = string.split(lines[0], None, 2)
	    if len(parts) == 3:
		auth_name = parts[1]
		hexauth = parts[2]
		auth = ''

		# Translate hexcode into binary
		for i in range(0, len(hexauth), 2):
		    auth = auth + chr(string.atoi(hexauth[i:i+2], 16))

		auth_data = auth
    except os.error:
	pass

    return auth_name, auth_data
    
