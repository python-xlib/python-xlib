# $Id: display.py,v 1.3 2000-08-08 09:47:45 petli Exp $
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

# Xlib.xobjects modules
import xobject.resource
import xobject.drawable
import xobject.fontable
import xobject.colormap
import xobject.cursor

class _BaseDisplay(protocol.display.Display):
    resource_classes = {
	'resource': xobject.resource.Resource,
	'drawable': xobject.drawable.Drawable,
	'window': xobject.drawable.Window,
	'pixmap': xobject.drawable.Pixmap,
	'font': xobject.fontable.Font,
	'gc': xobject.fontable.GC,
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
	return self.display.next_event()

    def pending_events(self):
	return self.display.pending_events()

    ###
    ### display information retrieval
    ###

    def screen(self, sno = None):
	if sno is None
	    return self.display.info.roots[self.display.default_screen]
	else:
	    return self.display.info.roots[sno]
					   
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

    def get_selection_owner(self, selection):
	r = request.GetSelectionOwner(display = self.display,
				      selection = selection)
	return r.owner

    def send_event(self, destination, event, propagate = 0, event_mask = 0):
	request.SendEvent(display = self.display,
			  propagate = propagate,
			  destination = destination,
			  event_mask = event_mask,
			  event = event)

    def ungrab_pointer(self, time):
	request.UngrabPointer(display = self.display,
			      time = time)
	
    def change_active_pointer_grab(self, event_mask, cursor, time):
	request.ChangeActivePointerGrab(display = self.display,
					cursor = cursor,
					time = time,
					event_mask = event_mask)
	
    def ungrab_keyboard(self, time):
	request.UngrabKeyboard(display = self.display,
			       time = time)

    def allow_events(self, mode, time):
	request.AllowEvents(display = self.display,
			    mode = mode,
			    time = time)

    def grab_server(self):
	request.GrabServer(display = self.display)

    def ungrab_server(self):
	request.UngrabServer(display = self.display)

    def warp_pointer(self, x, y, src_window = 0, src_x = 0, src_y = 0,
		     src_width = 0, src_height = 0):

	request.WarpPointer(display = self.display,
			    src_window = src_window,
			    dst_window = X.NONE,
			    src_x = src_x,
			    src_y = src_y,
			    src_width = src_width,
			    src_height = src_height,
			    dst_x = x,
			    dst_y = y)

    def set_input_focus(self, focus, revert_to, time):
	request.SetInputFocus(display = self.display,
			      revert_to = revert_to,
			      focus = focus,
			      time = time)

    def get_input_focus(self):
	return request.GetInputFocus(display = self.display)

    def query_keymap(self):
	r = request.QueryKeymap(display = self.display)
	return r.map

    def open_font(self, name):
	fid = self.display.allocate_resource_id()
	request.OpenFont(display = self.display,
			 fid = fid,
			 name = name)

	return fontable.Font(self.display, fid, owner = 1)

    def list_fonts(self, pattern, max_names):
	r = request.ListFonts(display = self.display,
			      max_names = max_names,
			      pattern = pattern)
	return r.fonts

    def list_fonts_with_info(self, pattern, max_names):
	return request.ListFontsWithInfo(display = self.display,
					 max_names = max_names,
					 pattern = pattern)

    def set_font_path(self, path):
	request.SetFontPath(display = self.display,
			    path = path)

    def get_font_path(self):
	r = request.GetFontPath(display = self.display)
	return r.paths

    def query_extension(self, name):
	r = request.QueryExtension(display = self.display,
				   name = name)
	if r.present:
	    return r
	else:
	    return None
	
    def list_extensions(self):
	r = request.ListExtensions(display = self.display)
	return r.names

    def change_keyboard_mapping(self, first_keycode, keysyms):
	request.ChangeKeyboardMapping(display = self.display,
				      first_keycode = first_keycode,
				      keysyms = keysyms)

    def get_keyboard_mapping(self, first_keycode, count):
	r = request.GetKeyboardMapping(display = self.display,
				       first_keycode = first_keycode,
				       count = count)
	return r.keysyms

    def change_keyboard_control(self, **keys):
	request.ChangeKeyboardControl(display = self.display,
				      attrs = keys)

    def get_keyboard_control(self):
	return request.GetKeyboardControl(display = self.display)
    
    def bell(self, percent = 0):
	request.Bell(display = self.display,
		     percent = percent)
	
    def change_pointer_control(self, accel = None, threshold = None):

	if accel is None:
	    do_accel = 0
	    accel_num = 0
	    accel_denum = 0
	else:
	    do_accel = 1
	    accel_num, accel_denum = accel

	if threshold is None:
	    do_threshold = 0
	else:
	    do_threshold = 1

	request.ChangePointerControl(display = self.display,
				     do_accel = do_accel,
				     do_thres = do_threshold,
				     accel_num = accel_num,
				     accel_denum = accel_denum,
				     threshold = threshold)

    def get_pointer_control(self):
	return request.GetPointerControl(display = self.display)

    def set_screen_saver(self, timeout, interval, prefer_blank, allow_exposures):
	request.SetScreenSaver(display = self.display,
			       timeout = timeout,
			       interval = interval,
			       prefer_blank = prefer_blank,
			       allow_exposures = allow_exposures)

    def get_screen_saver(self):
	return request.GetScreenSaver(display = self.display)

    def change_hosts(self, mode, host_family, host):
	request.ChangeHosts(display = self.display,
			    mode = mode,
			    host_family = host_family,
			    host = host)

    def list_hosts(self):
	return request.ListHosts(display = self.display)
    
    def set_access_control(self, mode):
	request.SetAccessControl(display = self.display,
				 mode = mode)

    def set_close_down_mode(self, mode):
	request.SetCloseDownMode(display = self.display,
				 mode = mode)
	
    def force_screen_saver(self, mode):
	request.ForceScreenSaver(display = self.display,
				 mode = mode)
    
    def set_pointer_mapping(self, map):
	r = request.SetPointerMapping(display = self.display,
				      map = map)
	return r.status

    def get_pointer_mapping(self):
	r = request.GetPointerMapping(display = self.display)
	return r.map

    def set_modifier_mapping(self, keycodes):
	r = request.SetModifierMapping(display = self.display,
				       keycodes = keycodes)
	return r.status

    def get_modifier_mapping(self):
	r = request.GetModifierMapping(display = self.display)
	return r.keycodes

    def no_operation(self):
	request.NoOperation(self)
	
