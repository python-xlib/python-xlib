XK_blank = 0x9df
XK_soliddiamond = 0x9e0
XK_checkerboard = 0x9e1
XK_ht = 0x9e2
XK_ff = 0x9e3
XK_cr = 0x9e4
XK_lf = 0x9e5
XK_nl = 0x9e8
XK_vt = 0x9e9
XK_lowrightcorner = 0x9ea
XK_uprightcorner = 0x9eb
XK_upleftcorner = 0x9ec
XK_lowleftcorner = 0x9ed
XK_crossinglines = 0x9ee
XK_horizlinescan1 = 0x9ef
XK_horizlinescan3 = 0x9f0
XK_horizlinescan5 = 0x9f1
XK_horizlinescan7 = 0x9f2
XK_horizlinescan9 = 0x9f3
XK_leftt = 0x9f4
XK_rightt = 0x9f5
XK_bott = 0x9f6
XK_topt = 0x9f7
XK_vertbar = 0x9f8

from Xlib.XK import _load_keysyms_into_XK
_load_keysyms_into_XK(__name__)