XK_leftcaret = 0xba3
XK_rightcaret = 0xba6
XK_downcaret = 0xba8
XK_upcaret = 0xba9
XK_overbar = 0xbc0
XK_downtack = 0xbc2
XK_upshoe = 0xbc3
XK_downstile = 0xbc4
XK_underbar = 0xbc6
XK_jot = 0xbca
XK_quad = 0xbcc
XK_uptack = 0xbce
XK_circle = 0xbcf
XK_upstile = 0xbd3
XK_downshoe = 0xbd6
XK_rightshoe = 0xbd8
XK_leftshoe = 0xbda
XK_lefttack = 0xbdc
XK_righttack = 0xbfc

from Xlib.XK import _load_keysyms_into_XK
_load_keysyms_into_XK(__name__)
