# Xlib.xobject.cursor -- cursor object
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

from Xlib.protocol import request

from . import resource

try:
    from typing import TYPE_CHECKING, TypeVar, Optional
except ImportError:
    TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing_extensions import TypeAlias
    from Xlib.error import XError
    from Xlib.protocol.rq import Request
    _T = TypeVar("_T")
    _ErrorHandler:  TypeAlias = Callable[[XError, Optional[Request]], _T]

class Cursor(resource.Resource):
    __cursor__ = resource.Resource.__resource__

    def free(self, onerror = None):
        # type: (_ErrorHandler[object] | None) -> None
        request.FreeCursor(display = self.display,
                           onerror = onerror,
                           cursor = self.id)
        self.display.free_resource_id(self.id)

    def recolor(self, foreground, background, onerror=None):
        # type: (tuple[int, int, int], tuple[int, int, int],  _ErrorHandler[object] | None) -> None
        fore_red, fore_green, fore_blue = foreground
        back_red, back_green, back_blue = background

        request.RecolorCursor(display = self.display,
                              onerror = onerror,
                              cursor = self.id,
                              fore_red = fore_red,
                              fore_green = fore_green,
                              fore_blue = fore_blue,
                              back_red = back_red,
                              back_green = back_green,
                              back_blue = back_blue)
