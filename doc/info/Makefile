# Make info documentation for Python Xlib
#
# $Id: Makefile,v 1.2 2002-07-16 20:48:59 petli Exp $

include ../src/defs

python-xlib.info: $(SRCS)
	makeinfo --force --no-split -P $(SRCDIR) $(TOPSRC)

clean:
	rm -f python-xlib.info