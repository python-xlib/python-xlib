# $Id: display.py,v 1.2 2000-08-07 10:30:19 petli Exp $
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

# Xlib.xoobjects modules
import xobject.resource
import xobject.drawable
import xobject.font
import xobject.gc
import xobject.colormap
import xobject.cursor

class _BaseDisplay(protocol.display.Display):
    resource_classes = {
	'resource': xobject.resource.Resource,
	'drawable': xobject.drawable.Drawable,
	'window': xobject.drawable.Window,
	'pixmap': xobject.drawable.Pixmap,
	'font': xobject.font.Font,
	'gc': xobject.gc.GC,
	'colormap': xobject.colormap.Colormap,
	'cursor': xobject.cursor.Cursor,
	}

class Display:
    def __init__(self, display = None):
	self.display = _BaseDisplay(display)

    def fileno(self):
	return self.display.fileno()

    def close(self):
	self.display.close()

    def flush(self):
	self.display.flush()

    def next_event(self):
	self.display.next_event()

    def pending_events(self):
	self.display.pending_events()
				
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
	
