# $Id: icccm.py,v 1.1 2000-09-22 11:37:51 petli Exp $
#
# Xlib.xobject.icccm -- ICCCM structures 
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

from Xlib import X, Xutil
from Xlib.protocol import rq

Aspect = rq.Struct( rq.Int32('num'), rq.Int32('denum') )

WMNormalHints = rq.Struct( rq.Card32('flags'),
			   rq.Pad(16),
			   rq.Int32('min_width'),
			   rq.Int32('min_height'),
			   rq.Int32('max_width'),
			   rq.Int32('max_height'),
			   rq.Int32('width_inc'),
			   rq.Int32('height_inc'),
			   rq.Object('min_aspect', Aspect),
			   rq.Object('max_aspect', Aspect),
			   rq.Int32('base_width'),
			   rq.Int32('base_height'),
			   rq.Int32('win_gravity'),
			   )

WMHints = rq.Struct( rq.Card32('flags'),
		     rq.Card32('input'),
		     rq.Set('initial_state', 4,
			    ( Xutil.NormalState, Xutil.IconicState )),
		     rq.Pixmap('icon_pixmap'),
		     rq.Window('icon_window'),
		     rq.Int32('icon_x'),
		     rq.Int32('icon_y'),
		     rq.Pixmap('icon_mask'),
		     rq.Window('window_group'),
		     )

WMState = rq.Struct( rq.Set('state', 4,
			    ( Xutil.WithdrawnState,
			      Xutil.NormalState,
			      Xutil.IconicState )),
		     rq.Window('icon', ( X.NONE, )),
		     )

		     
WMIconSize = rq.Struct( rq.Card32('min_width'),
			rq.Card32('min_height'),
			rq.Card32('max_width'),
			rq.Card32('max_height'),
			rq.Card32('width_inc'),
			rq.Card32('height_inc'),
			)
			
