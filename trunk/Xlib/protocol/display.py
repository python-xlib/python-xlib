# $Id: display.py,v 1.3 2000-08-08 09:47:45 petli Exp $
#
# Xlib.protocol.display -- core display communication
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

# Standard modules
import sys
import os
import select
import string
import struct
import socket
import re
import fcntl
import FCNTL

# Xlib modules
from Xlib import error

# Xlib.protocol modules
import rq
import event

display_re = re.compile(r'^([-a-zA-Z0-9._]*):([0-9]+)(\.([0-9]+))?$')

class Display:
    resource_classes = {}
    
    def __init__(self, display = None):
	# Use $DISPLAY if display isn't provided
	if display is None:
	    display = os.environ.get('DISPLAY', '')

	m = display_re.match(display)
	if not m:
	    raise error.DisplayNameError(display)

	self.display_name = display
	host = m.group(1)
	dno = int(m.group(2))
	screen = m.group(4)
	if screen:
	    self.default_screen = int(screen)
	else:
	    self.default_screen = 0

	try:
	    # If hostname (or IP) is provided, use TCP socket
	    if host:
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((host, 6000 + dno))

	    # Else use Unix socket
	    else:
		self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		self.socket.connect('/tmp/.X11-unix/X%d' % dno)
	except socket.error, val:
	    raise error.DisplayConnectionError(display, str(val))

	# Make sure that the connection isn't inherited in child processes
	fcntl.fcntl(self.socket.fileno(), FCNTL.F_SETFD, FCNTL.FD_CLOEXEC)

	# Find authorization cookie
	authorization = ('', '')
	try:
	    # We could parse .Xauthority, but xauth is simpler
	    # although more inefficient
	    data = os.popen('xauth list %s 2>/dev/null' % self.display_name).read()

	    # If there's a cookie, it is of the format
	    #      DISPLAY SCHEME COOKIE
	    # We're interested in the two last parts for the
	    # connection establishment
	    lines = string.split(data, '\n')
	    if len(lines) >= 1:
		parts = string.split(lines[0], None, 2)
		if len(parts) == 3:
		    scheme = parts[1]
		    hexauth = parts[2]
		    auth = ''
		    
		    # Translate hexcode into binary
		    for i in range(0, len(hexauth), 2):
			auth = auth + chr(string.atoi(hexauth[i:i+2], 16))
			
		    authorization = (scheme, auth)
		    
	except os.error:
	    pass
	
	# Internal structures for communication
	self.request_serial = 1

	self.socket_error = None
	
	self.event_queue = []
	self.request_queue = []
	self.sent_requests = []
	self.request_length = 0
	
	self.data_send = ''
	self.data_recv = ''

	# Use an default error handler, one which just prints the error
	self.error_handler = None
	
	# Figure out which endianess the hardware uses
	self.big_endian = struct.unpack('BB', struct.pack('H', 0x0100))[0]

	if self.big_endian:
	    order = 0x42
	else:
	    order = 0x6c
	    
	# Send connection setup
	r = ConnectionSetupRequest(self,
				   byte_order = order,
				   protocol_major = 11,
				   protocol_minor = 0,
				   auth_prot_name = authorization[0],
				   auth_prot_data = authorization[1])

	# Did connection fail?
	if r.status != 1:
	    raise error.DisplayConnectionError(self.display_name, r.reason)

	# Set up remaining info structures
	self.info = r

	self.default_screen = max(self.default_screen, len(self.info.roots) - 1)

	self.resource_ids = {}
	self.last_resource_id = 0

	
    #
    # Public interface
    #
    
    def fileno(self):
	if self.socket_error:
	    raise self.socket_error
	
	return self.socket.fileno()
    
    def next_event(self):
	if self.socket_error:
	    raise self.socket_error

	if not self.event_queue:
	    self.send_and_recv(event = 1)
	
	event = self.event_queue[0]
	del self.event_queue[0]
	return event

    def pending_events(self):
	if self.socket_error:
	    raise self.socket_error

	return len(self.event_queue)
    
    def flush(self):
	if self.socket_error:
	    raise self.socket_error

	if self.request_queue:
	    self.send_and_recv(flush = 1)
	    
    def close(self):
	if self.socket_error:
	    raise self.socket_error

	self.close_internal('client')

    def set_error_handler(self, handler):
	self.error_handler = handler


    def allocate_resource_id(self):
	"""id = d.allocate_resource_id()

	Allocate a new X resource id number ID.

	Raises ResourceIDError if there are no free resource ids.
	"""

	i = self.last_resource_id
	while self.resource_ids.has_key(i):
	    i = i + 1
	    if i > self.info.resource_id_mask:
		i = 0
	    if i == self.last_resource_id:
		raise error.ResourceIDError('out of resource ids')

	self.resource_ids[i] = None
	self.last_resource_id = i
	return self.info.resource_id_base | i

    def free_resource_id(self, rid):
	"""d.free_resource_id(rid)

	Free resource id RID.  Attempts to free a resource id which
	isn't allocated by us are ignored.
	"""

	i = rid & self.info.resource_id_mask

	# Attempting to free a resource id outside our range
	if rid - i != self.info.resource_id_base:
	    return None
	
	try:
	    del self.resource_ids[i]
	except KeyError:
	    pass

    

    def get_resource_class(self, class_name):
	"""class = d.get_resource_class(class_name)

	Return the class to be used for X resource objects of type
	CLASS_NAME, or None if no such class is set.
	"""

	return self.resource_classes.get(class_name, None)
    
    #
    # Private functions
    #

    def send_request(self, request, wait_for_response):
	if self.socket_error:
	    raise self.socket_error

	request._serial = self.request_serial
	self.request_serial = (self.request_serial + 1) % 65536
	self.request_queue.append(request, wait_for_response)

	if len(self.request_queue) > 10:
	    self.flush()
	    

    def close_internal(self, whom):
	# Clear out data structures
	self.request_queue = None
	self.sent_requests = None
	self.event_queue = None
	self.data_send = None
	self.data_recv = None

	# Close the connection
	self.socket.close()

	# Set a connection closed indicator
	self.socket_error = error.ConnectionClosedError(whom)
	
	
    def send_and_recv(self, flush = None, event = None, request = None):

	# Translate all queued requests into binary form for sending.
	for req, wait in self.request_queue:
	    self.data_send = self.data_send + req._binary
	    if wait:
		self.sent_requests.append(req)
		
	del self.request_queue[:]

	# Loop, recieving and sending data.

	# Timeout is set to None initially to block until there is
	# something to recieve or send.
	timeout = None
	
	while 1:

	    # Wait for socket to be ready for sending data (if any)
	    # and recieving data (always).
	    if self.data_send:
		writeset = [self.socket]
	    else:
		writeset = []

	    try:
		rs, ws, es = select.select([self.socket], writeset, [], timeout)

	    # Ignore errors caused by a signal recieved while blocking.
	    # All other errors are re-raised.
	    except select.error, err:
		if err[0] != errno.EINTR:
		    raise err
		continue

	    # Socket is ready for sending data, send as much as possible.
	    if ws:
		try:
		    i = self.socket.send(self.data_send)
		except socket.error, err:
		    self.close_internal('server: %s' % err[1])
		    raise self.socket_error
		
		self.data_send = self.data_send[i:]

	    # There is data to read.  Do so and parse recieved data.
	    gotreq = 0
	    if rs:
		try:
		    recv = self.socket.recv(2048)
		except socket.error, err:
		    self.close_internal('server: %s' % err[1])
		    raise self.socket_error

		if not recv:
		    # Clear up, set a connection closed indicator and raise it
		    self.close_internal('server')
		    raise self.socket_error
		
		self.data_recv = self.data_recv + recv
		gotreq = self.parse_response(request)
		
	    # We have recieved or sent all that we had to and is just
	    # trying to do some bonus recieving and sending.
	    if timeout is not None:
		# If that failed: quit the loop
		if not rs and not ws:
		    return

		# Otherwise, make another pass
		else:
		    continue
	    

	    # There are three different end of send-recv-loop conditions.
	    # However, we don't leave the loop immediately, instead we
	    # try to send and recieve any data that might be left.  We
	    # do this by giving a timeout of 0 to select to poll
	    # the socket.

	    # When flushing: all requests have been sent
	    if flush and not self.data_send:
		timeout = 0

	    # When waiting for an event: an event has been read
	    if event and self.event_queue:
		timeout = 0

	    # When processing a certain request: got its reply
	    if request is not None and gotreq:
		timeout = 0

	    # Else there's still data which must be sent,
	    # so loop around to another blocking select
    

    def parse_response(self, request):
	"""Internal method.

	Parse data recieved from server.  If REQUEST is not None
	true is returned if the request with that serial number
	was recieved, otherwise false is returned.

	If REQUEST is -1, we're parsing the server connection setup
	response.
	"""

	if request == -1:
	    return self.parse_connection_setup()

	# Parse ordinary server response
	gotreq = 0
	while 1:
	    # Are we're waiting for additional data for a request response?
	    if self.request_length:
		if len(self.data_recv) < self.request_length:
		    return gotreq
		else:
		    gotreq = self.parse_request_response(request) or gotreq


	    # Every response is at least 32 bytes long, so don't bother
	    # until we have recieved that much
	    if len(self.data_recv) < 32:
		return gotreq

	    # Check the first byte to find out what kind of response it is
	    rtype = ord(self.data_recv[0])

	    # Error resposne
	    if rtype == 0:
		gotreq = self.parse_error_response(request) or gotreq

	    # Request response
	    elif rtype == 1:
		# Set reply length, and loop around to see if
		# we have got the full response
		rlen = int(struct.unpack('=L', self.data_recv[4:8])[0])
		self.request_length = 32 + rlen * 4

	    # Else event response
	    else:
		self.parse_event_response(rtype)


    def parse_error_response(self, request):
	# Code is second byte
	code = ord(self.data_recv[1])

	# Fetch error class
	estruct = error.xerror_class.get(code, error.XError)
	
	e = estruct(self, self.data_recv[:32])
	self.data_recv = self.data_recv[32:]

	# print 'recv Error:', e

	req = self.get_waiting_request(e.sequence_number)
	
	# Error for a request whose response we are waiting for,
	# or which have an error handler
	if req:
	    req._set_error(e)
	    return request == e.sequence_number

	# Else call the error handler
	else:
	    if self.error_handler:
		rq.call_error_handler(self.error_handler, e)
	    else:
		self.default_error_handler(e)
		
	    return 0


    def default_error_handler(self, err):
	sys.stderr.write('X protocol error:\n%s\n' % err)
	    

    def parse_request_response(self, request):
	req = self.get_waiting_replyrequest()

	# Sequence number is always data[2:4]
	# Do sanity check before trying to parse the data
	sno = struct.unpack('=H', self.data_recv[2:4])[0]
	if sno != req._serial:
	    raise RuntimeError("Expected reply for request %s, but got %s.  Can't happen!"
			       % (req._serial, sno))
	
	req._parse_response(self.data_recv[:self.request_length])
	# print 'recv Request:', req
	
	self.data_recv = self.data_recv[self.request_length:]
	self.request_length = 0
	
	return req.sequence_number == request
	

    def parse_event_response(self, etype):
	estruct = event.event_class.get(etype, event.AnyEvent)

	e = estruct(display = self, binarydata = self.data_recv[:32])
	self.data_recv = self.data_recv[32:]

	# Drop all requests having an error handler,
	# but which obviously succeded
	self.get_waiting_request(e.sequence_number)
	
	# print 'recv Event:', e
	
	self.event_queue.append(e)


    def get_waiting_request(self, sno):
	if not self.sent_requests:
	    return None

	# Normalize sequence numbers, even if they have wrapped.
	# This ensures that
	#   sno <= last_serial
	# and
	#   self.sent_requests[0]._serial <= last_serial
	
	if self.sent_requests[0]._serial > self.request_serial:
	    last_serial = self.request_serial + 65536
	    if sno < self.request_serial:
		sno = sno + 65536
	    
	else:
	    last_serial = self.request_serial
	    if sno > self.request_serial:
		sno = sno - 65536

	# No matching events at all
	if sno < self.sent_requests[0]._serial:
	    return None

	# Find last req <= sno
	req = None
	reqpos = len(self.sent_requests)
	adj = 0
	last = 0
	
	for i in range(0, len(self.sent_requests)):
	    rno = self.sent_requests[i]._serial + adj

	    # Did serial numbers just wrap around?
	    if rno < last:
		adj = 65536
		rno = rno + adj

	    last = rno
		
	    if sno == rno:
		req = self.sent_requests[i]
		reqpos = i + 1
		break
	    elif sno < rno:
		req = None
		reqpos = i
		break

	# Delete all request such as req <= sno
	del self.sent_requests[:reqpos]

	return req
	
    def get_waiting_replyrequest(self):
	for i in range(0, len(self.sent_requests)):
	    if hasattr(self.sent_requests[i], '_reply'):
		req = self.sent_requests[i]
		del self.sent_requests[:i + 1]
		return req

	# Reply for an unknown request?  No, that can't happen.
	else:
	    raise RuntimeError("Request reply to unknown request.  Can't happen!")
	
    def parse_connection_setup(self):
	"""Internal function used to parse connection setup response.
	"""

	# Only the ConnectionSetupRequest has been sent so far
	r = self.sent_requests[0]

	while 1:
	    # print 'data_send:', repr(self.data_send)
	    # print 'data_recv:', repr(self.data_recv)
	    
	    if r._data:
		alen = r._data['additional_length'] * 4
		    
		# The full response haven't arrived yet
		if len(self.data_recv) < alen:
		    return 0

		# Connection failed or further authentication is needed.
		# Set reason to the reason string
		if r._data['status'] != 1:
		    r._data['reason'] = self.data_recv[:r._data['reason_length']]

		# Else connection succeeded, parse the reply
		else:
		    x, d = r._success_reply.parse_binary(self.data_recv[:alen],
							 self, rawdict = 1)
		    r._data.update(x)

		del self.sent_requests[0]
		
		self.data_recv = self.data_recv[alen:]
		
		return 1

	    else:
		# The base reply is 8 bytes long
		if len(self.data_recv) < 8:
		    return 0

		r._data, d = r._reply.parse_binary(self.data_recv[:8],
						   self, rawdict = 1)
		self.data_recv = self.data_recv[8:]

		# Loop around to see if we have got the additional data
		# already


PixmapFormat = rq.Struct( rq.Card8('depth'),
			  rq.Card8('bits_per_pixel'),
			  rq.Card8('scanline_pad'),
			  rq.Pad(5)
			  )

VisualType = rq.Struct ( rq.Card32('visual_id'),
			 rq.Card8('class'),
			 rq.Card8('bits_per_rgb_value'),
			 rq.Card16('colormap_entries'),
			 rq.Card32('red_mask'),
			 rq.Card32('green_mask'),
			 rq.Card32('blue_mask'),
			 rq.Pad(4)
			 )
			
Depth = rq.Struct( rq.Card8('depth'),
		   rq.Pad(1),
		   rq.LengthOf('visuals', 2),
		   rq.Pad(4),
		   rq.List('visuals', VisualType)
		   )

Screen = rq.Struct( rq.Window('root'),
		    rq.Colormap('default_colormap'),
		    rq.Card32('white_pixel'),
		    rq.Card32('black_pixel'),
		    rq.Card32('current_input_mask'),
		    rq.Card16('width_in_pixels'),
		    rq.Card16('height_in_pixels'),
		    rq.Card16('width_in_mms'),
		    rq.Card16('height_in_mms'),
		    rq.Card16('min_installed_maps'),
		    rq.Card16('max_installed_maps'),
		    rq.Card32('root_visual'),
		    rq.Card8('backing_store'),
		    rq.Card8('save_unders'),
		    rq.Card8('root_depth'),
		    rq.LengthOf('allowed_depths', 1),
		    rq.List('allowed_depths', Depth)
		    )

		    
class ConnectionSetupRequest(rq.GetAttrData):
    _request = rq.Struct( rq.Set('byte_order', 1, (0x42, 0x6c)),
			  rq.Pad(1),
			  rq.Card16('protocol_major'),
			  rq.Card16('protocol_minor'),
			  rq.LengthOf('auth_prot_name', 2),
			  rq.LengthOf('auth_prot_data', 2),
			  rq.Pad(2),
			  rq.String8('auth_prot_name'),
			  rq.String8('auth_prot_data') )
    
    _reply = rq.Struct ( rq.Card8('status'),
			 rq.Card8('reason_length'),
			 rq.Card16('protocol_major'),
			 rq.Card16('protocol_minor'),
			 rq.Card16('additional_length') )

    _success_reply = rq.Struct( rq.Card32('release_number'),
				rq.Card32('resource_id_base'),
				rq.Card32('resource_id_mask'),
				rq.Card32('motion_buffer_size'),
				rq.LengthOf('vendor', 2),
				rq.Card16('max_request_length'),
				rq.LengthOf('roots', 1),
				rq.LengthOf('pixmap_formats', 1),
				rq.Card8('image_byte_order'),
				rq.Card8('bitmap_format_bit_order'),
				rq.Card8('bitmap_format_scanline_unit'),
				rq.Card8('bitmap_format_scanline_pad'),
				rq.Card8('min_keycode'),
				rq.Card8('max_keycode'),
				rq.Pad(4),
				rq.String8('vendor'),
				rq.List('pixmap_formats', PixmapFormat),
				rq.List('roots', Screen),
				)
    
			       
    def __init__(self, display, *args, **keys):
	self._binary = self._request.build_from_args(args, keys)
	self._data = None
	display.request_queue.append((self, 1))
	display.send_and_recv(request = -1)



