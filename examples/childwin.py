#!/usr/bin/python
#
# examples/childwin.py -- demonstrate child windows.
#
#	Copyright (C) 2008 David Bronke <whitelynx@gmail.com>
#	Copyright (C) 2002 Peter Liljenberg <petli@ctrl-c.liu.se>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA

# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib import X, display, Xutil

# Application window
class Window(object):
	def __init__(self, display):
		self.d = display

		# Find which screen to open the window on
		self.screen = self.d.screen()

		# background pattern
		bgsize = 20

		bgpm = self.screen.root.create_pixmap(
			bgsize,
			bgsize,
			self.screen.root_depth
			)

		bggc = self.screen.root.create_gc(
			foreground=self.screen.black_pixel,
			background=self.screen.black_pixel
			)

		bgpm.fill_rectangle(bggc, 0, 0, bgsize, bgsize)

		bggc.change(foreground=self.screen.white_pixel)

		bgpm.arc(bggc, -bgsize // 2, 0, bgsize, bgsize, 0, 360 * 64)
		bgpm.arc(bggc, bgsize // 2, 0, bgsize, bgsize, 0, 360 * 64)
		bgpm.arc(bggc, 0, -bgsize // 2, bgsize, bgsize, 0, 360 * 64)
		bgpm.arc(bggc, 0, bgsize // 2, bgsize, bgsize, 0, 360 * 64)

		# Actual window
		self.window = self.screen.root.create_window(
			100, 100, 400, 300, 0,
			self.screen.root_depth,
			X.InputOutput,
			X.CopyFromParent,

			# special attribute values
			background_pixmap=bgpm,
			event_mask=(
				X.StructureNotifyMask |
				X.ButtonReleaseMask
				),
			colormap=X.CopyFromParent
			)

		# Set some WM info

		self.WM_DELETE_WINDOW = self.d.intern_atom('WM_DELETE_WINDOW')
		self.WM_PROTOCOLS = self.d.intern_atom('WM_PROTOCOLS')

		self.window.set_wm_name('Xlib example: childwin.py')
		self.window.set_wm_icon_name('childwin.py')
		self.window.set_wm_class('childwin', 'XlibExample')

		self.window.set_wm_protocols([self.WM_DELETE_WINDOW])
		self.window.set_wm_hints(
			flags=Xutil.StateHint,
			initial_state=Xutil.NormalState
			)

		self.window.set_wm_normal_hints(
			flags=(Xutil.PPosition | Xutil.PSize | Xutil.PMinSize),
			min_width=50,
			min_height=50
			)

		# Map the window, making it visible
		self.window.map()

		# Child window
		(self.childWidth, self.childHeight) = (20, 20)
		self.childWindow = self.window.create_window(
			20, 20, self.childWidth, self.childHeight, 0,
			self.screen.root_depth,
			X.CopyFromParent,
			X.CopyFromParent,

			# special attribute values
			background_pixel=self.screen.white_pixel,
			colormap=X.CopyFromParent,
			)
		self.childWindow.map()


	# Main loop, handling events
	def loop(self):
		current = None
		while 1:
			e = self.d.next_event()

			# Window has been destroyed, quit
			if e.type == X.DestroyNotify:
				sys.exit(0)

			# Button released, add or subtract
			elif e.type == X.ButtonRelease:
				if e.detail == 1:
					print("Moving child window.")
					self.childWindow.configure(
						x=e.event_x - self.childWidth // 2,
						y=e.event_y - self.childHeight // 2
						)
					self.d.flush()

			# Somebody wants to tell us something
			elif e.type == X.ClientMessage:
				if e.client_type == self.WM_PROTOCOLS:
					fmt, data = e.data
					if fmt == 32 and data[0] == self.WM_DELETE_WINDOW:
						sys.exit(0)


if __name__ == '__main__':
	Window(display.Display()).loop()
