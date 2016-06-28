|Build Status| |codecov.io| |Code Health|

The Python X Library
====================

Copyright
~~~~~~~~~

The main part of the code is

::

    Copyright (C) 2000-2002  Peter Liljenberg

Some contributed code is copyrighted by `the
contributors <https://github.com/python-xlib/python-xlib/graphs/contributors>`__,
in these cases that is indicated in the source files in question.

The Python X Library is released under LGPL v2.1 or later (since 2016),
see the file LICENSE for details. 0.15rc1 and before were released under
GPL v2.

Requirements
~~~~~~~~~~~~

The Python X Library requires Python 2.7 or newer. It has been tested to
various extents with Python 2.7 and 3.3 through 3.5.

Installation
~~~~~~~~~~~~

The Python Xlib uses the standard setuptools package, to install run
this command:

::

    python setup.py install

See the command help for details: ``python setup.py install -h``.

Alternatively, you can run programs from the distribution directory, or
change the module path in programs.

There's a simple example program, implemented twice using both the
high-level interface and the low-level protocol.

Introduction
~~~~~~~~~~~~

The Python X Library is intended to be a fully functional X client
library for Python programs. It is written entirely in Python, in
contrast to earlier X libraries for Python (the ancient X extension and
the newer plxlib) which were interfaces to the C Xlib.

This is possible to do since X client programs communicate with the X
server via the X protocol. The communication takes place over TCP/IP,
Unix sockets, DECnet or any other streaming network protocol. The C Xlib
is merely an interface to this protocol, providing functions suitable
for a C environment.

There are three advantages of implementing a pure Python library:

-  Integration: The library can make use of the wonderful object system
   in Python, providing an easy-to-use class hierarchy.

-  Portability: The library will be usable on (almost) any computer
   which have Python installed. A C interface could be problematic to
   port to non-Unix systems, such as MS Windows or OpenVMS.

-  Maintainability: It is much easier to develop and debug native Python
   modules than modules written in C.

Project status
~~~~~~~~~~~~~~

The low-level protocol is complete, implementing client-side X11R6. The
high-level object oriented interface is also fully functional. It is
possible to write client applications with the library. Currently, the
only real application using Python Xlib is the window manager PLWM,
starting with version 2.0.

There is a resource database implementation, ICCCM support and a
framework for adding X extension code. Several extensions have been
implemented; (RECORD, SHAPE, Xinerama, Composite, RANDR, and XTEST)
patches for additions are very welcome.

There are most likely still bugs, but the library is at least stable
enough to run PLWM. A continuously bigger part of the library is covered
by regression tests, improving stability.

The documentation is still quite rudimentary, but should be of some help
for people programming with the Xlib. X beginners should first find some
general texts on X. A very good starting point is
http://www.rahul.net/kenton/xsites.html

See the file TODO for a detailed list of what is missing, approximately
ordered by importance.

Contact information
~~~~~~~~~~~~~~~~~~~

Author email: Peter Liljenberg petli@ctrl-c.liu.se

Mailing list: http://sourceforge.net/mail/?group\_id=10350

The Python X Library is a SourceForged project (currently migrating to
GitHub). The project page is
http://sourceforge.net/projects/python-xlib/. Source is available from
that page as zip archive and from the `releases
list <https://github.com/python-xlib/python-xlib/releases>`__.

There isn't any real web page yet, only a derivative of this file. It is
located at http://python-xlib.sourceforge.net/. It now also features the
documentation for downloading or browsing.

.. |Build Status| image:: https://travis-ci.org/python-xlib/python-xlib.svg?branch=master
   :target: https://travis-ci.org/python-xlib/python-xlib
.. |codecov.io| image:: https://codecov.io/github/python-xlib/python-xlib/coverage.svg?branch=master
   :target: https://codecov.io/github/python-xlib/python-xlib?branch=master
.. |Code Health| image:: https://landscape.io/github/python-xlib/python-xlib/master/landscape.svg?style=flat
   :target: https://landscape.io/github/python-xlib/python-xlib/master
