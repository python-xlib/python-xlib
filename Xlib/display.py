# $Id: display.py,v 1.1 2000-08-02 09:39:24 petli Exp $
#
# Xlib.display -- high level display object
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


# Xlib modules
import error

# Xlib.protocol modules
import protocol.display
from protocol import request


class Display:
    def __init__(self, display = None):
	self.display = protocol.display.Display(display)
	self.resource_ids = {}
	self.last_resource_id = 0

    def fileno(self):
	return self.display.fileno()

    def close(self):
	self.display.close()


    ###
    ### X requests
    ###

    def intern_atom(self, name, only_if_exists = 0):
	r = request.InternAtom(display = self.display,
			       name = name,
			       only_if_exists = only_if_exists)
	return r.atom

    def get_atom_name(self, atom):
	r = request.GetAtomName(display = self.display,
				atom = atom)
	return r.name
			       
    def bell(self, percent = 0):
	request.Bell(display = self.display,
		     percent = percent)
	
    ###
    ### Private interface
    ###
	
    def allocate_resource_id(self):
	"""id = d.allocate_resource_id()

	Allocate a new X resource id number ID.

	Raises ResourceIDError if there are no free resource ids.
	"""

	i = self.last_resource_id
	while self.resource_ids.has_key(i):
	    i = i + 1
	    if i > self.display.info.resource_id_mask:
		i = 0
	    if i == self.last_resource_id:
		raise error.ResourceIDError('out of resource ids')

	self.resource_ids[i] = None
	self.last_resource_id = i
	return self.info.resource_id_base | i

    def free_resource_id(self, rid):
	"""d.free_resource_id(rid)

	Free resource id RID.

	Raises ResourceIDError if RID is not allocated.
	"""

	i = rid & self.display.info.resource_id_mask

	# Attempting to free a resource id outside our range
	if rid - i != self.display.info.resource_id_base:
	    raise error.ResourceIDError('resource id 0x%08x is not in our range' % rid)
	
	try:
	    del self.resource_ids[i]
	except KeyError:
	    raise error.ResourceIDError('resouce id 0x%08x is not allocated' % rid)

    
