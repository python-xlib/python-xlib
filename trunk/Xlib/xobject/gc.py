# $Id: gc.py,v 1.1 2000-08-07 10:30:20 petli Exp $
#
# Xlib.xobject.gc -- graphic context object
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

from Xlib.protocol import request

import resource

class GC(resource.Resource):
    __gc__ = resource.Resource.__resource__
    __fontable__ = resource.Resource.__resource__

    def change(self, **keys):
	request.Request(display = self.display,
			attrs = keys)


    def copy(self, src_gc, mask):
	request.CopyGC(display = self.display,
		       src_gc = src_gc,
		       dst_gc = self.id,
		       mask = mask)

    def set_dashes(self, offset, dashes):
	request.SetDashes(display = self.display,
			  gc = self.id,
			  dash_offset = offset,
			  dashes = dashes)

    def set_clip_rectangles(self, x_origin, y_origin, rectangles, ordering):
	request.SetClipRectangles(display = self.display,
				  ordering = ordering,
				  gc = self.id,
				  x_origin = x_origin,
				  y_origin = y_origin,
				  rectangles = rectangles)
    def free(self):
	request.FreeGC(display = self.display,
		       gc = self.id)
	if self.owner:
	    self.display.free_resource_id(self.id)
	    self.id = None
	    self.owner = 0

    
