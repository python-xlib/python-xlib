# Xlib.xobject.colormap -- colormap object
#
#    Copyright (C) 2000 Peter Liljenberg <petli@ctrl-c.liu.se>
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

from Xlib import error
from Xlib.protocol import request

from . import resource

import re

try:
    from typing import TYPE_CHECKING, TypeVar, Optional
except ImportError:
    TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from Xlib.protocol import rq
    _T = TypeVar("_T")
    _ErrorHandler = Callable[[error.XError, Optional[rq.Request]], _T]

rgb_res = [
    re.compile(r'\Argb:([0-9a-fA-F]{1,4})/([0-9a-fA-F]{1,4})/([0-9a-fA-F]{1,4})\Z'),
    re.compile(r'\A#([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])\Z'),
    re.compile(r'\A#([0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F])\Z'),
    re.compile(r'\A#([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F])\Z'),
    re.compile(r'\A#([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F])\Z'),
    ]

class Colormap(resource.Resource):
    __colormap__ = resource.Resource.__resource__

    def free(self, onerror = None):
        # type: (_ErrorHandler[object] | None) -> None
        request.FreeColormap(display = self.display,
                             onerror = onerror,
                             cmap = self.id)

        self.display.free_resource_id(self.id)

    def copy_colormap_and_free(self, scr_cmap):
        # type: (int) -> Colormap
        mid = self.display.allocate_resource_id()
        request.CopyColormapAndFree(display = self.display,
                                    mid = mid,
                                    src_cmap = src_cmap)

        cls = self.display.get_resource_class('colormap', Colormap)
        return cls(self.display, mid, owner = 1)

    def install_colormap(self, onerror = None):
        # type: (_ErrorHandler[object] | None) -> None
        request.InstallColormap(display = self.display,
                                onerror = onerror,
                                cmap = self.id)

    def uninstall_colormap(self, onerror = None):
        # type: (_ErrorHandler[object] | None) -> None
        request.UninstallColormap(display = self.display,
                                  onerror = onerror,
                                  cmap = self.id)

    def alloc_color(self, red, green, blue):
        return request.AllocColor(display = self.display,
                                  cmap = self.id,
                                  red = red,
                                  green = green,
                                  blue = blue)

    def alloc_named_color(self, name):
        # type: (str) -> request.AllocColor | request.AllocNamedColor | None
        for r in rgb_res:
            m = r.match(name)
            if m:
                rs = m.group(1)
                r = int(rs + '0' * (4 - len(rs)), 16)

                gs = m.group(2)
                g = int(gs + '0' * (4 - len(gs)), 16)

                bs = m.group(3)
                b = int(bs + '0' * (4 - len(bs)), 16)

                return self.alloc_color(r, g, b)

        try:
            return request.AllocNamedColor(display = self.display,
                                           cmap = self.id,
                                           name = name)
        except error.BadName:
            return None

    def alloc_color_cells(self, contiguous, colors, planes):
        # type: (bool, int, int) -> request.AllocColorCells
        return request.AllocColorCells(display = self.display,
                                       contiguous = contiguous,
                                       cmap = self.id,
                                       colors = colors,
                                       planes = planes)

    def alloc_color_planes(self, contiguous, colors, red, green, blue):
        # type: (bool, int, int, int, int) -> request.AllocColorPlanes
        return request.AllocColorPlanes(display = self.display,
                                        contiguous = contiguous,
                                        cmap = self.id,
                                        colors = colors,
                                        red = red,
                                        green = green,
                                        blue = blue)

    def free_colors(self, pixels, plane_mask, onerror = None):
        # type: (Sequence[int], int, _ErrorHandler[object] | None) -> None
        request.FreeColors(display = self.display,
                           onerror = onerror,
                           cmap = self.id,
                           plane_mask = plane_mask,
                           pixels = pixels)

    def store_colors(self, items, onerror = None):
        # type: (dict[str, int], _ErrorHandler[object] | None) -> None
        request.StoreColors(display = self.display,
                            onerror = onerror,
                            cmap = self.id,
                            items = items)

    def store_named_color(self, name, pixel, flags, onerror = None):
        # type: (str, int, int, _ErrorHandler[object] | None) -> None
        request.StoreNamedColor(display = self.display,
                                onerror = onerror,
                                flags = flags,
                                cmap = self.id,
                                pixel = pixel,
                                name = name)

    def query_colors(self, pixels):
        # type: (Sequence[int]) -> rq.Struct
        r = request.QueryColors(display = self.display,
                                cmap = self.id,
                                pixels = pixels)
        return r.colors

    def lookup_color(self, name):
        # type: (str) -> request.LookupColor
        return request.LookupColor(display = self.display,
                                   cmap = self.id,
                                   name = name)
