# $Id: drawable.py,v 1.1 2000-08-07 10:30:20 petli Exp $
#
# Xlib.xobject.drawable -- drawable objects (window and pixmap)
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

from Xlib import X
from Xlib.protocol import request

# Other X resource objects
import resource
import colormap
import cursor
import gc

class Drawable(resource.Resource):
    __drawable__ = resource.Resource.__resource__

    def get_geometry(self):
	return request.GetGeometry(display = self.display,
				   drawable = self)

    def create_pixmap(self, width, height, depth):
	pid = self.display.allocate_resource_id()
	request.CreatePixmap(display = self.display,
			     depth = depth,
			     pid = pid,
			     drawable = self.id,
			     width = width,
			     height = height)
	
	return Pixmap(self.display, pid, owner = 1)

    def create_gc(self, **keys):
	cid = self.display.allocate_resource_id()
	request.CreateGC(display = self.display,
			 cid = cid,
			 drawable = self.id,
			 attrs = keys)

	return gc.GC(self.display, cid, owner = 1)
    
    def copy_area(self, gc, src_drawable, src_x, src_y, width, height, dst_x, dst_y):
	request.CopyArea(display = self.display,
			 src_drawable = src_drawable,
			 dst_drawable = self.id,
			 gc = gc,
			 src_x = src_x,
			 src_y = src_y,
			 dst_x = dst_x,
			 dst_y = dst_y,
			 width = width,
			 height = height)

    def copy_plane(self, gc, src_drawable, src_x, src_y, width, height,
		   dst_x, dst_y, bit_plane):
	request.CopyArea(display = self.display,
			 src_drawable = src_drawable,
			 dst_drawable = self.id,
			 gc = gc,
			 src_x = src_x,
			 src_y = src_y,
			 dst_x = dst_x,
			 dst_y = dst_y,
			 width = width,
			 height = height,
			 bit_plane = bit_plane)

    def poly_point(self, gc, coord_mode, points):
	request.PolyPoint(display = self.display,
			  coord_mode = coord_mode,
			  drawable = self.id,
			  gc = gc,
			  points = points)

    def poly_line(self, gc, coord_mode, points):
	request.PolyLine(display = self.display,
			 coord_mode = coord_mode,
			 drawable = self.id,
			 gc = gc,
			 points = points)

    def poly_segment(self, gc, segments):
	request.PolySegment(display = self.display,
			    drawable = self.id,
			    gc = gc,
			    segments = segments)
	
    def poly_rectangle(self, gc, rectangles):
	request.PolyRectangle(display = self.display,
			      drawable = self.id,
			      gc = gc,
			      rectangles = rectangles)

    def poly_arc(self, gc, arcs):
	request.PolyArc(display = self.display,
			drawable = self.id,
			gc = gc,
			arcs = arcs)

    def fill_poly(self, gc, shape, coord_mode, points):
	request.FillPoly(display = self.display,
			 shape = shape,
			 coord_mode = coord_mode,
			 drawable = self.id,
			 gc = gc,
			 points = points)

    def poly_fill_rectangle(self, gc, rectangles):
	request.PolyFillRectangle(display = self.display,
				  drawable = self.id,
				  gc = gc,
				  rectangles = rectangles)

    def poly_fill_arc(self, gc, arcs):
	request.PolyFillArc(display = self.display,
			    drawable = self.id,
			    gc = gc,
			    arcs = arcs)

    ### FIXME: fix pixmap uploading first
    def put_image(self):
	pass

    def get_image(self):
	pass

    def poly_text(self, gc, x, y, items):
	request.PolyText8(display = self.display,
			  drawable = self.id,
			  gc = gc,
			  x = x,
			  y = y,
			  items = items)
    
    def poly_text_16(self, gc, x, y, items):
	request.PolyText16(display = self.display,
			   drawable = self.id,
			   gc = gc,
			   x = x,
			   y = y,
			   items = items)
    
    def image_text(self, gc, x, y, string):
	request.ImageText8(display = self.display,
			   drawable = self.id,
			   gc = gc,
			   x = x,
			   y = y,
			   string = string)

    def image_text_16(self, gc, x, y, string):
	request.ImageText16(display = self.display,
			    drawable = self.id,
			    gc = gc,
			    x = x,
			    y = y,
			    string = string)

    def query_best_size(self, item_class, width, height):
	return request.QueryBestSize(display = self.display,
				     item_class = item_class,
				     drawable = self.id,
				     width = width,
				     height = height)
				     
class Window(Drawable):
    __window__ = resource.Resource.__resource__

    def create_window(self, x, y, width, height, border_width, depth,
		      window_class =  X.CopyFromParent,
		      visual = X.CopyFromParent,
		      **keys):
	
	wid = self.display.allocate_resource_id()
	request.CreateWindow(display = self.display,
			     depth = depth,
			     wid = wid,
			     parent = self.id,
			     x = x,
			     y = y,
			     width = width,
			     height = height,
			     border_width = border_width,
			     window_class = window_class,
			     visual = visual,
			     attrs = keys)
	return Window(self.display, wid, owner = 1)

    def change_attributes(self, **keys):
	request.ChangeWindowAttributes(display = self.display,
				       window = self.id,
				       attrs = keys)
    	
    def get_attributes(self):
	return request.GetWindowAttributes(display = self.display,
					   window = self.id)

    def destroy(self):
	request.DestroyWindow(display = self.display,
			      window = self.id)
	if self.owner:
	    self.display.free_resource_id(self.id)
	    self.id = None
	    self.owner = 0

    def destroy_sub_windows(self):
	request.DestroySubWindows(display = self.display,
				  window = self.id)


    def change_save_set(self, mode):
	request.ChangeSaveSet(display = self.display,
			      mode = mode,
			      window = self.id)

    def reparent_window(self, parent, x, y):
	request.ReparentWindow(display = self.display,
			       window = self.id,
			       parent = parent,
			       x = x,
			       y = y)

    def map(self):
	request.MapWindow(display = self.display,
			  window = self.id)

    def map_sub_windows(self):
	request.MapSubWindows(display = self.display,
			      window = self.id)

    def unmap(self):
	request.UnmapWindow(display = self.display,
			    window = self.id)
    
    def unmap_sub_windows(self):
	request.UnmapSubWindows(display = self.display,
				window = self.id)

    def configure(self, **keys):
	request.ConfigureWindow(display = self.display,
				window = self.id,
				attrs = keys)

    def circulate(self, direction):
	request.CirculateWindow(display = self.display,
				direction = direction,
				window = self.id)

    def query_tree(self):
	return request.QueryTree(display = self.display,
				 window = self.id)


    def change_property(self, property, type, data, mode = X.PropModeReplace):
	request.ChangeProperty(display = self.display,
			       mode = mode,
			       window = self.id,
			       property = property,
			       type = type,
			       data = data)

    def delete_property(self, property):
	request.DeleteProperty(display = self.display,
			       window = self.id,
			       property = property)

    def get_property(self, property, type, offset, length, delete = 0):
	r = request.GetProperty(display = self.display,
				delete = delete,
				window = self.id,
				property = property,
				type = type,
				long_offset = offset,
				long_length = length)

	if r.property_type:
	    return r
	else:
	    return None

    def list_properties(self):
	r = request.ListProperties(display = self.display,
				   window = self.id)
	return r.atoms

    def set_selection_owner(self, selection, time):
	request.SetSelectionOwner(display = self.display,
				  window = self.id,
				  selection = selection,
				  time = time)

    def convert_selection(self, selection, target, property, time):
	request.ConvertSelection(display = self.display,
				 requestor = self.id,
				 selection = selection,
				 target = target,
				 property = property,
				 time = time)

    def send_event(self, event, propagate = 0, event_mask = 0):
	request.SendEvent(display = self.display,
			  propagate = propagate,
			  destination = self.id,
			  event_mask = event_mask,
			  event = event)

    def grab_pointer(self, owner_events, event_mask,
		     pointer_mode, keyboard_mode,
		     confine_to, cursor, time):

	r = request.GrabPointer(display = self.display,
				owner_events = owner_events,
				grab_window = self.id,
				event_mask = event_mask,
				pointer_mode = pointer_mode,
				keyboard_mode = keyboard_mode,
				confine_to = confine_to,
				cursor = cursor,
				time = time)
	return r.status

    def grab_button(self, button, modifiers, owner_events, event_mask,
		    pointer_mode, keyboard_mode,
		    confine_to, cursor):
	
	request.GrabPointer(display = self.display,
			    owner_events = owner_events,
			    grab_window = self.id,
			    event_mask = event_mask,
			    pointer_mode = pointer_mode,
			    keyboard_mode = keyboard_mode,
			    confine_to = confine_to,
			    button = button,
			    modifiers = modifiers)

    def ungrab_button(self, button, modifiers):
	request.UngrabButton(display = self.display,
			     button = button,
			     grab_window = self.id,
			     modifiers = modifiers)


    def grab_keyboard(self, owner_events, pointer_mode, keyboard_mode, time):
	r = request.GrabKeyboard(display = self.display,
				 owner_events = owner_events,
				 grab_window = self.id,
				 time = time,
				 pointer_mode = pointer_mode,
				 keyboard_mode = keyboard_mode)

	return r.status

    def grab_key(self, key, modifiers, owner_events, pointer_mode, keyboard_mode):
	request.GrabKey(display = self.display,
			owner_events = owner_events,
			grab_window = self.id,
			modifiers = modifiers,
			key = key,
			pointer_mode = pointer_mode,
			keyboard_mode = keyboard_mode)

    def ungrab_key(self, key, modifiers):
	request.UngrabKey(display = self.display,
			  key = key,
			  grab_window = self.id,
			  modifiers = modifiers)

    def query_pointer(self):
	return request.QueryPointer(display = self.display,
				    window = self.id)

    def get_motion_events(self, start, stop):
	r = request.GetMotionEvents(display = self.display,
				    window = self.id,
				    start = start,
				    stop = stop)
	return r.events

    def translate_coords(self, src_window, src_x, src_y):
	return request.TranslateCoords(display = self.display,
				       src_wid = src_window,
				       dst_wid = self.id,
				       src_x = src_x,
				       src_y = src_y)

    ### FIXME: should exist as Display method to, for relative warps
    def warp_pointer(self, x, y, src_window = 0, src_x = 0, src_y = 0,
		     src_width = 0, src_height = 0):

	request.WarpPointer(display = self.display,
			    src_window = src_window,
			    dst_window = self.id,
			    src_x = src_x,
			    src_y = src_y,
			    src_width = src_width,
			    src_height = src_height,
			    dst_x = x,
			    dst_y = y)

    ### FIXME: as Display method too
    def set_input_focus(self, revert_to, time):
	request.SetInputFocus(display = self.display,
			      revert_to = revert_to,
			      focus = self.id,
			      time = time)

    def clear_area(self, x = 0, y = 0, width = 0, height = 0, exposures = 0):
	request.ClearArea(display = self.display,
			  exposures = exposures,
			  window = self.id,
			  x = x,
			  y = y,
			  width = width,
			  height = height)

    def create_colormap(self, visual, alloc):
	mid = self.display.allocate_resource_id()
	request.CreateColormap(display = self.display,
			       alloc = alloc,
			       mid = mid,
			       window = self.id,
			       visual = visual)
	return colormap.Colormap(self.display, mid, owner = 1)

    def list_installed_colormaps(self):
	r = request.ListInstalledColormaps(display = self.display,
					   window = self.id)
	return r.cmaps

    def rotate_properties(self, properties, delta):
	request.RotateProperties(display = self.display,
				 window = self.id,
				 delta = delta,
				 properties = properties)

class Pixmap(Drawable):
    __pixmap__ = resource.Resource.__resource__

    def free(self):
	request.FreePixmap(display = self.display,
			   pixmap = self.id)
	if self.owner:
	    self.display.free_resource_id(self.id)
	    self.id = None
	    self.owner = 0

    def create_cursor(self, mask,
		      (fore_red, fore_green, fore_blue),
		      (back_red, back_green, back_blue),
		      x, y):
	cid = self.display.allocate_resource_id()
	request.CreateCursor(display = self.display,
			     cid = cid,
			     source = self.id,
			     mask = mask,
			     fore_red = fore_red,
			     fore_green = fore_green,
			     fore_blue = fore_blue,
			     back_red = back_red,
			     back_green = back_green,
			     back_blue = back_blue,
			     x = x,
			     y = y)
	return cursor.Cursor(self.display, cid, owner = 1)

    
    
