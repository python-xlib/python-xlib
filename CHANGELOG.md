NEWS for Python X Library

Version 0.25
============

Bug Fixes
---------

- fix increasing memory usage on display instantiation

NV-CONTROL extension
--------------------

- add first implementation by Roberto Leinardi (@leinardi)

---
Version 0.24
============

Bug Fixes
---------

- fix protocol handling: correctly support explicit Unix
  connections and fix support fox macOS
- improve Python 3 support: fix events sub-code handling
  and possible crashes when unpacking text data
- add support for error handlers to the Composite extension

Misc
----

- fix `xfixes` example
- fix a bunch of typos in the code / documentation

---
Version 0.23
============

Bug Fixes
---------

- fix strings decoding: use Latin-1

---
Version 0.22
============

Bug Fixes
---------

- fix `Display.change_pointer_control` implementation
- fix `Drawable.put_pil_image` implementation

---
Version 0.21
============

Bug Fixes
---------

- fix use under Windows Subsystem for Linux: when DISPLAY does not
  specify a protocol, and the implicit Unix socket connection fails,
  fallback to TCP (mimicking XCB's behavior).

Misc
----

- don't bundle a copy of texi2html to build the HTML documentation,
  but use the currently installed version instead.

---
Version 0.20
============

Bug Fixes
---------

- fix unclosed file in Xauth implementation
- fix support for `Window.set_wm_transient_for`
- fix support for `Drawable.put_image` / `Drawable.get_image`
- use ASCII for decoding strings in Python 3 (same as Python 2)
- fix Python 3 warnings about `array.tostring()` (deprecated)

Misc
----

Improve response processing performance: reduce the number of
`socket.recv` calls needed to receive a full response.

---
Version 0.19
============

Bug Fixes
---------

- don't throw an exception if `$XAUTHFILE` / `~/.Xauthority` is missing
- fix authentication work-around for SSH forwarding under Python 3
- improve `$DISPLAY` handling: support optional protocol prefix, and
  correctly handle `unix:0.0` as `:0.0`

---
Version 0.18
============

Bug Fixes
---------

- fix Python 3 buffer abstraction
- fix interrupted select handling for Python 3.3/3.4
- fix Unix socket support when only an abstract address is available

---
Version 0.17
============

Bug Fixes
---------

- fix Xauth handling when using Python 2 and DISPLAY contains a remote IP
- fix String16 request field handling when using Python 3
- fix RECORD extension and example when using Python 3
- fix handling of properties: use byte strings for all X11 8-bits
  strings, as not all of them are text properties (the window
  getters/setters for `wm_name`, `wm_icon_name`, `wm_class`, and
  `wm_client_machine` still return/expect Unicode strings)

API Changes
-----------

Core:

- new window getter/setter for text properties: `get_full_text_property`
  and `change_text_property`; with automatic conversion to/from Unicode
  when the property type encoding is supported (`STRING` and
  `UTF8_STRING`)

Composite extension:

-   support for `GetOverlayWindow` request

---
Version 0.16
============

Licensing
---------

The project is now licensed under the GNU Lesser General Public License
v2.1 or later (see the LICENSE file for details).

Compatibility
-------------

Support for Python versions older than 2.7 has been dropped. Support for
Python 3 (3.3, 3.4 and 3.5) has been added. Note that Python-Xlib now
depends on the six package (>=1.10) for combined Python 2 / 3 support.

API Changes
-----------

With the change of license, and no way to contact the original author of
the SHAPE extension, the code had to be rewritten from scratch. This
resulted in a few minor API changes (see [examples/shapewin.py](examples/shapewin.py)).

Partial support for the SECURITY. XInput, and XFIXES extensions has been
added.

Bug Fixes
---------

- fix RECORD extension
- fixed OS X socket path
- fix handling of generic events
- fix handling of KeymapNotify events
- several fixes for the RandR extension

---
Version 0.15rc1 - 14 Nov 2009
=============================

Improved support for newer versions of Mac OS X, a couple of new
extensions, and several bugfixes.

Composite extension
-------------------

Support for the composite extension, used to implement a composition
manager (added for plcm work in plwm).

By itself this extension is not very useful, it is intended to be used
together with the DAMAGE and XFIXES extensions. Typically you would also
need RENDER or glX or some similar method of creating fancy graphics.

XF86 special function keysyms
-----------------------------

Keysym definitions for special function keys found on modern keyboards,
e.g. raise and lower volume, start specific applications, etc. Have a
look in [Xlib/keysymdef/xf86.py](Xlib/keysymdef/xf86.py) to see what
there are and experiment with xev to see what your keyboard generates.
These definitions aren't brought in by default, so you must do this
after importing `Xlib.XK`:

```python
Xlib.XK.load_keysym_group('xf86')
```

RANDR extension
---------------

The RANDR extension complements XINERAMA as a way of getting data about
the physical screens making up a virtual screen in X. An example of
usage can be found in [examples/xrandr.py](examples/xrandr.py).

---
Version 0.14 - 1 Oct 2007 (trialed as 0.14rc1 on 10 Jun 2007)
=============================================================

A couple of new extensions, a Python 2.5 fix and a couple of aliases
(`Display.get_atom()` now uses the internal cache and added
`Window.raise_window()`). Tabs converted to spaces (SF id: 1559082).

RECORD extension (SF id: 1538663)
---------------------------------

Alex Badea contributed a RECORD extension module, allowing Python Xlib
programs to capture mouse and keyboard events (or all other core or
extension events) easily. A demo is in the examples directory. See
<http://refspecs.freestandards.org/X11/recordlib.pdf> for more
information.

XINERAMA extension
------------------

Mike Meyer contributed a Xinerama extension module, allowing Python Xlib
programs to interrogate the X server about positions and sizes of
multiple screens. Specifications are a bit tricky to find -
<http://sourceforge.net/projects/xinerama/> has some older specs and the
source code of the xorg project (libs & server code) has "definitive"
information.

Python 2.5 fix (SF id: 1623900)
-------------------------------

Bugfix to correct handling of XAuthority file parsing under Python 2.5
causing failed authentication.

---
Version 0.13 - 6 Aug 2006 (trialed as 0.13pre1 on 22 Jul 2006)
==============================================================

A small release to incorporate a number of minor corrections and bug
fixes, including small changes to keysym handling, `.Xauthority`
parsing, several fixes to sending/receiving/flushing data, addition of
`WithdrawnState` to `WMHints`. petli completed documentation for
`Display` objects.

---
Version 0.12 - 29 Mar 2002
==========================

SHAPE extension
---------------

Jeffrey Boser contributed a SHAPE extension module, allowing Python Xlib
programs to use shaped windows. Take a look at examples/shapewin.py for
ideas on how to use it. For more information on shaped windows, see
<http://ftp.x.org/pub/R6.6/xc/doc/hardcopy/Xext/shape.PS.gz>

Python 2.2 fix
--------------

In Python 2.2 `FCNTL.FD_CLOEXEC` has disappeared and `FCNTL` on the whole
is deprecated, so that had to be dealt with to make the Xlib work with
that version.

---
Version 0.11 - 23 Feb 2002
==========================

Regression tests for the protocol definition
--------------------------------------------

Regressions tests have been created for all requests, replies and
events. The tests use PyUnit, and the old resource database test has
been updated to use it too.

A lot of protocol bugfixes
--------------------------

The bugs discovered by the regression tests have been fixed.
Additionally, a subtle bug in the core engine which could cause a
"can't happen"-error has also been found and fixed.

---
Version 0.10 - 16 Dec 2001
==========================

Event bugfix
------------

The xlib failed to parse the type code of events sent from other clients
using `SendEvent`. This has been fixed, adding the field `send_event' to
all event objects.

Event documentation
-------------------

The section "Event Types" in the manual has been written, detailing
all event types in the core protocol. The manual is now ten pages
thicker.

Basic support for GetImage/PutImage
-----------------------------------

The Drawable methods `put_image()` and `get_image()` have been
implemented, but handling image data is still up to the user. There is
however, thanks to Ilpo Nyyssönen, a trivial method `put_pil_image()`
that will work on some combinations of image and drawable depth. It's
not perfect, but it's a start.

---
Version 0.9 - 4 Dec 2001
========================

Documentation improved
----------------------

The documentation has been augmented with a chapter about event
handling, and a chapter listing all X objects and their methods provided
by the library. They are not described in any detail, though.

Keysym handling improved
------------------------

The module `Xlib.XK`, which listed all keysyms, have been split up into
several sub-modules providing different sets of keysyms. By importing
`Xlib.XK` only the miscellany and latin1 sets are loaded, thus removing
some unnecessary clutter.

`Xlib.display.Display` has two new methods (`lookup_string()` and
`rebind_string()`) for translating keysyms into characters.

Small changes to library interface
----------------------------------

The order of the `Xlib.display.Display` method `send_event()` parameters
`event_mask` and propagate has changed.

Some of the class names in `Xlib.protocol.event` have changed, to have
the same name as the corresponding event type constant.

A few bugfixes
--------------

If a display has more than one screen, the default screen was always set
to the highest numbered one, irrespective of what the user specified in
`$DISPLAY`.

Some response attributes in `Xlib.protocol.request` accidentally included
a comma.

---
Version 0.8 - 12 Jan 2001
=========================

Uses distutils
--------------

Python Xlib now uses distutils to make installation and distribution
building easier.

Tested with Python 2.0
----------------------

A few incompatibilities with Python 2.0 has been fixed.

---
Version 0.7 - 8 Jan 2001
========================

Fixed the 64-bit platform fix.
------------------------------

As it turns out, the attempted fix for 64-bit platforms in v0.6 didn't
really work. Close study of structmodules.c gave the answer why, and now
it really should work. Yeah.

Optimizations of core protocol engine
-------------------------------------

Python Xlib is now at least 25% faster after the core of the protocol
engine has been rewritten. This is some quite cute code: tailor-made
methods are generated for all structures, resulting in a 650% speed-up
in generating binary data, and a 75% speed-up in parsing binary data.

Interested Python hackers are recommended to take a look at the Struct
class in `Xlib/protocol/rq.py`.

---
Version 0.6 - 29 Dec 2000
=========================

Fix to make python-xlib work on 64-bytes architectures.
-------------------------------------------------------

The struct and array modules uses `sizeof(long)` to determine the number
of bytes used when representing the type code 'l'. On Intel and VAX,
this is 32 bits as expected. On Alpha, it's 64 bits. python-xlib now
probes how large each type code is to avoid this problem.

---
Version 0.5 - 28 Dec 2000
=========================

- Functions implemented to get and set all ICCCM WM properties on Window
  objects.

- Keymap cache implemented, with external `Xlib.display.Display` methods
  `keycode_to_keysym`, `keysym_to_keycode`, `keysym_to_keycodes` and
  `refresh_keyboard_mapping`.

- Two utils for debugging X traffic implemented. `utils/tcpbug.py`
  forwards a TCP connection and outputs the communication between the
  client and the server. This output can then be fed into
  `utils/parsexbug.py`, which will output all requests, responses,
  errors and events in a readable format.

---
Version 0.4 - 4 Oct 2000
========================

- Thread support completed, but not really stress-tested yet.

- A framework for handling different platforms has been implemented,
  together with generic Unix code and some simple VMS code.

- Some documentation has been written.

- The usual bunch of bugfixes.
