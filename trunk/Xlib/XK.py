# $Id: XK.py,v 1.4 2001-01-19 18:59:37 petli Exp $
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
    return globals().get('XK_' + str, NoSymbol)

def load_keysym_group(group):
    if '.' in group:
	raise ValueError('invalid keysym group name: %s' % group)

    # Try to import the corresponding package.  This will
    # finally result in the package calling _load_keysyms_into_XK
    __import__('Xlib.keysymdef.%s' % group, globals(), locals())

def _load_keysyms_into_XK(mod):
    # I reckon that this is the fastest way to import all
    # keysyms into this modules global dict.
    # To have some kind of security, check that we're only
    # loading something out of Xlib.keysymdef

    if mod[:15] ==  'Xlib.keysymdef.':
	exec 'from %s import *' % mod in globals()


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
