# $Id: XK.py,v 1.5 2005-02-06 02:32:34 calroc99 Exp $
#
# Xlib.XK -- X keysym defs
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

from X import NoSymbol

def string_to_keysym(str):
    '''Given the name of a keysym as a string, return its numeric code.
    Don't include the 'XK_' prefix. Just use the base, i.e. 'Delete'
    instead of 'XK_Delete'.'''
    return globals().get('XK_' + str, NoSymbol)

def load_keysym_group(group):
    '''Given a group name such as 'latin1' or 'katakana' load the keysyms
    defined in module 'Xlib.keysymdef.group-name' into this XK module.'''
    if '.' in group:
	raise ValueError('invalid keysym group name: %s' % group)

    G = globals() #Get a reference to XK.__dict__ a.k.a. globals

    #Import just the keysyms module.
    mod = __import__('Xlib.keysymdef.%s' % group, G, locals(), [group])

    #Extract names of just the keysyms.
    keysyms = [n for n in dir(mod) if n[:3] == 'XK_']

    #Copy the named keysyms into XK.__dict__
    for keysym in keysyms:
        ## k = mod.__dict__[keysym]; assert k == int(k) #probably too much.
        G[keysym] = mod.__dict__[keysym]

def _load_keysyms_into_XK(mod):
    '''keysym definition modules need no longer call Xlib.XK._load_keysyms_into_XK().
    You should remove any calls to that function from your keysym modules.'''
    pass

# Always import miscellany and latin1 keysyms
import Xlib.keysymdef.miscellany
import Xlib.keysymdef.latin1


def keysym_to_string(keysym):
    # ISO latin 1, LSB is the code
    if keysym & 0xff00 == 0:
	return chr(keysym & 0xff)

    if keysym in [XK_BackSpace, XK_Tab, XK_Clear, XK_Return,
		  XK_Pause, XK_Scroll_Lock, XK_Escape, XK_Delete]:
	return chr(keysym & 0xff)

    # We should be able to do these things quite automatically
    # for latin2, latin3, etc, in Python 2.0 using the Unicode,
    # but that will have to wait.

    return None
