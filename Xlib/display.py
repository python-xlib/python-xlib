# $Id: display.py,v 1.14 2001-01-11 15:13:05 petli Exp $
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

# Python modules
import new

# Xlib modules
import error
import ext
import X

# Xlib.protocol modules
import protocol.display
from protocol import request, event

# Xlib.xobjects modules
import xobject.resource
import xobject.drawable
import xobject.fontable
import xobject.colormap
import xobject.cursor

_resource_baseclasses = {
    'resource': xobject.resource.Resource,
    'drawable': xobject.drawable.Drawable,
    'window': xobject.drawable.Window,
    'pixmap': xobject.drawable.Pixmap,
    'fontable': xobject.fontable.Fontable,
    'font': xobject.fontable.Font,
    'gc': xobject.fontable.GC,
    'colormap': xobject.colormap.Colormap,
    'cursor': xobject.cursor.Cursor,
    }

_resource_hierarchy = {
    'resource': ('drawable', 'window', 'pixmap',
		 'fontable', 'font', 'gc',
		 'colormap', 'cursor'),
    'drawable': ('window', 'pixmap'),
    'fontable': ('font', 'gc')
    }
    
class _BaseDisplay(protocol.display.Display):
    resource_classes = _resource_baseclasses.copy()

    # Implement a cache of atom names, used by Window objects when
    # dealing with some ICCCM properties not defined in Xlib.Xatom
    
    def __init__(self, *args, **keys):
	apply(protocol.display.Display.__init__, (self, ) + args, keys)
	self._atom_cache = {}

    def get_atom(self, atomname):
	if not self._atom_cache.has_key(atomname):
	    r = request.InternAtom(display = self, name = atomname, only_if_exists = 0)
	    self._atom_cache[atomname] = r.atom
	    
	return self._atom_cache[atomname]

	
class Display:
    def __init__(self, display = None):
	self.display = _BaseDisplay(display)

	# Create the keymap cache
	self._keymap_codes = [()] * 256
	self._keymap_syms = {}
	self._update_keymap(self.display.info.min_keycode,
			    (self.display.info.max_keycode
			     - self.display.info.min_keycode + 1))
	
	# Find all supported extensions
	self.extensions = []
	self.class_extension_dicts = {}
	self.display_extension_methods = {}
	
	exts = self.list_extensions()

	# Go through all extension modules
	for extname, modname in ext.__extensions__:
	    if extname in exts:
		
		# Import the module and fetch it
		__import__('Xlib.ext.' + modname)
		mod = getattr(ext, modname)

		info = self.query_extension(extname)
		self.display.set_extension_major(extname, info.major_opcode)
		
		# Call initialiasation function
		mod.init(self, info)

		self.extensions.append(extname)

		
	# Finalize extensions by creating new classes
	for type, dict in self.class_extension_dicts.items():
	    origcls = self.display.resource_classes[type]
	    self.display.resource_classes[type] = new.classobj(origcls.__name__,
							       (origcls,),
							       dict)

	# Problem: we have already created some objects without the
	# extensions: the screen roots and default colormaps.
	# Fix that by reinstantiating them.
	for screen in self.display.info.roots:
	    screen.root = self.display.resource_classes['window'](self.display, screen.root.id)
	    screen.default_colormap = self.display.resource_classes['colormap'](self.display, screen.default_colormap.id)
	    
	
    def get_display_name(self):
	return self.display.get_display_name()

    def fileno(self):
	return self.display.fileno()

    def close(self):
	self.display.close()

    def set_error_handler(self, handler):
	self.display.set_error_handler(handler)

    def flush(self):
	self.display.flush()

    def sync(self):
	# Do a light-weight replyrequest to sync.  There must
	# be a better way to do it...
	self.get_pointer_control()
	
    def next_event(self):
	return self.display.next_event()

    def pending_events(self):
	return self.display.pending_events()

    def has_extension(self, extension):
	return extension in self.extensions
    
    def create_resource_object(self, type, id):
	return self.display.resource_classes[type](self.display, id)

    # We need this to handle display extension methods
    def __getattr__(self, attr):
	try:
	    function = self.display_extension_methods[attr]
	    return new.instancemethod(function, self, self.__class__)
	except KeyError:
	    raise AttributeError(attr)
	
    ###
    ### display information retrieval
    ###

    def screen(self, sno = None):
	if sno is None:
	    return self.display.info.roots[self.display.default_screen]
	else:
	    return self.display.info.roots[sno]

    def screen_count(self):
	return len(self.display.info.roots)

    def get_default_screen(self):
	return self.display.get_default_screen()
    
    ###
    ### Extension module interface
    ###

    def extension_add_method(self, object, name, function):
	"""extension_add_method(object, name, function)

	Add an X extension module method.  OBJECT is the type of
	object to add the function to, a string from this list:

	    display
	    resource
	    drawable
	    window
	    pixmap
	    fontable
	    font
	    gc
	    colormap
	    cursor

	NAME is the name of the method, a string.  FUNCTION is a
	normal function whose first argument is a 'self'.
	"""

	if object == 'display':
	    if hasattr(self, name):
		raise error.MethodOverrideError('attempting to replace display method: %s' % name)

	    self.display_extension_methods[name] = function

	else:
	    types = (object, ) + _resource_hierarchy.get(object, ())
	    for type in types:
		cls = _resource_baseclasses[type]
		if hasattr(cls, name):
		    raise error.MethodOverrideError('attempting to replace %s method: %s' % (type, name))

		method = new.instancemethod(function, None, cls)
		
		# Maybe should check extension overrides too
		try:
		    self.class_extension_dicts[type][name] = method
		except KeyError:
		    self.class_extension_dicts[type] = { name: method }
	    
    def add_extension_event(self, code, evt):
	"""add_extension_event(code, evt)

	Add an extension event.  CODE is the numeric code, and EVT is
	the event class.
	"""
	
	self.display.add_extension_event(code, evt)

    def add_extension_error(self, code, err):
	"""add_extension_error(code, err)

	Add an extension error.  CODE is the numeric code, and ERR is
	the error class.
	"""
	
	self.display.add_extension_error(code, err)

    ###
    ### keymap cache implementation
    ###

    # The keycode->keysym map is stored in a list with 256 elements.
    # Each element represents a keycode, and the tuple elements are
    # the keysyms bound to the key.

    # The keysym->keycode map is stored in a mapping, where the keys
    # are keysyms.  The values are a sorted list of tuples with two
    # elements each: (index, keycode)
    # keycode is the code for a key to which this keysym is bound, and
    # index is the keysyms index in the map for that keycode.

    def keycode_to_keysym(self, keycode, index):
	try:
	    return self._keymap_codes[keycode][index]
	except IndexError:
	    return X.NoSymbol

    def keysym_to_keycode(self, keysym):
	try:
	    return self._keymap_syms[keysym][0][1]
	except (KeyError, IndexError):
	    return 0

    def keysym_to_keycodes(self, keysym):
	try:
	    # Copy the map list, reversing the arguments
	    return map(lambda x: (x[1], x[0]), self._keymap_syms[keysym])
	except KeyError:
	    return []
    
    def refresh_keyboard_mapping(self, evt):
	if isinstance(evt, event.MappingNotify):
	    self._update_keymap(evt.first_keycode, evt.count)
	else:
	    raise TypeError('expected a MappingNotify event')
	
    def _update_keymap(self, first_keycode, count):
	"""Internal function, called to refresh the keymap cache.
	"""

	# Delete all sym->code maps for the changed codes
	
	lastcode = first_keycode + count
	for keysym, codes in self._keymap_syms.items():
	    i = 0
	    while i < len(codes):
		code = codes[i][1]
		if code >= first_keycode and code < lastcode:
		    del codes[i]
		else:
		    i = i + 1

	# Get the new keyboard mapping
	keysyms = self.get_keyboard_mapping(first_keycode, count)

	# Replace code->sym map with the new map
	self._keymap_codes[first_keycode:lastcode] = keysyms

	# Update sym->code map
	code = first_keycode
	for syms in keysyms:
	    index = 0
	    for sym in syms:
		if sym != X.NoSymbol:
		    if self._keymap_syms.has_key(sym):
			symcodes = self._keymap_syms[sym]
			symcodes.append((index, code))
			symcodes.sort()
		    else:
			self._keymap_syms[sym] = [(index, code)]
			
		index = index + 1
	    code = code + 1

	
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

    def send_event(self, destination, event, propagate = 0, event_mask = 0,
		   onerror = None):

	request.SendEvent(display = self.display,
			  onerror = onerror,
			  propagate = propagate,
			  destination = destination,
			  event_mask = event_mask,
			  event = event)

    def ungrab_pointer(self, time, onerror = None):
	request.UngrabPointer(display = self.display,
			      onerror = onerror,
			      time = time)
	
    def change_active_pointer_grab(self, event_mask, cursor, time, onerror = None):
	request.ChangeActivePointerGrab(display = self.display,
					onerror = onerror,
					cursor = cursor,
					time = time,
					event_mask = event_mask)
	
    def ungrab_keyboard(self, time, onerror = None):
	request.UngrabKeyboard(display = self.display,
			       onerror = onerror,
			       time = time)

    def allow_events(self, mode, time, onerror = None):
	request.AllowEvents(display = self.display,
			    onerror = onerror,
			    mode = mode,
			    time = time)

    def grab_server(self, onerror = None):
	request.GrabServer(display = self.display,
			   onerror = onerror)

    def ungrab_server(self, onerror = None):
	request.UngrabServer(display = self.display,
			     onerror = onerror)

    def warp_pointer(self, x, y, src_window = 0, src_x = 0, src_y = 0,
		     src_width = 0, src_height = 0, onerror = None):

	request.WarpPointer(display = self.display,
			    onerror = onerror,
			    src_window = src_window,
			    dst_window = X.NONE,
			    src_x = src_x,
			    src_y = src_y,
			    src_width = src_width,
			    src_height = src_height,
			    dst_x = x,
			    dst_y = y)

    def set_input_focus(self, focus, revert_to, time, onerror = None):
	request.SetInputFocus(display = self.display,
			      onerror = onerror,
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
	ec = error.CatchError(error.BadName)

	request.OpenFont(display = self.display,
			 onerror = ec,
			 fid = fid,
			 name = name)
	self.sync()

	if ec.get_error():
	    self.display.free_resource_id(fid)
	    return None
	else:
	    cls = self.display.get_resource_class('font', xobject.fontable.Font)
	    return cls(self.display, fid, owner = 1)

    def list_fonts(self, pattern, max_names):
	r = request.ListFonts(display = self.display,
			      max_names = max_names,
			      pattern = pattern)
	return r.fonts

    def list_fonts_with_info(self, pattern, max_names):
	return request.ListFontsWithInfo(display = self.display,
					 max_names = max_names,
					 pattern = pattern)

    def set_font_path(self, path, onerror = None):
	request.SetFontPath(display = self.display,
			    onerror = onerror,
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

    def change_keyboard_mapping(self, first_keycode, keysyms, onerror = None):
	request.ChangeKeyboardMapping(display = self.display,
				      onerror = onerror,
				      first_keycode = first_keycode,
				      keysyms = keysyms)

    def get_keyboard_mapping(self, first_keycode, count):
	r = request.GetKeyboardMapping(display = self.display,
				       first_keycode = first_keycode,
				       count = count)
	return r.keysyms

    def change_keyboard_control(self, onerror = None, **keys):
	request.ChangeKeyboardControl(display = self.display,
				      onerror = onerror,
				      attrs = keys)

    def get_keyboard_control(self):
	return request.GetKeyboardControl(display = self.display)
    
    def bell(self, percent = 0, onerror = None):
	request.Bell(display = self.display,
		     onerror = onerror,
		     percent = percent)
	
    def change_pointer_control(self, accel = None, threshold = None, onerror = None):

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
				     onerror = onerror,
				     do_accel = do_accel,
				     do_thres = do_threshold,
				     accel_num = accel_num,
				     accel_denum = accel_denum,
				     threshold = threshold)

    def get_pointer_control(self):
	return request.GetPointerControl(display = self.display)

    def set_screen_saver(self, timeout, interval, prefer_blank, allow_exposures, onerror = None):
	request.SetScreenSaver(display = self.display,
			       onerror = onerror,
			       timeout = timeout,
			       interval = interval,
			       prefer_blank = prefer_blank,
			       allow_exposures = allow_exposures)

    def get_screen_saver(self):
	return request.GetScreenSaver(display = self.display)

    def change_hosts(self, mode, host_family, host, onerror = None):
	request.ChangeHosts(display = self.display,
			    onerror = onerror,
			    mode = mode,
			    host_family = host_family,
			    host = host)

    def list_hosts(self):
	return request.ListHosts(display = self.display)
    
    def set_access_control(self, mode, onerror = None):
	request.SetAccessControl(display = self.display,
				 onerror = onerror,
				 mode = mode)

    def set_close_down_mode(self, mode, onerror = None):
	request.SetCloseDownMode(display = self.display,
				 onerror = onerror,
				 mode = mode)
	
    def force_screen_saver(self, mode, onerror = None):
	request.ForceScreenSaver(display = self.display,
				 onerror = onerror,
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

    def no_operation(self, onerror = None):
	request.NoOperation(display = self.display,
			    onerror = onerror)
	
