# Make postscript documentation for Python Xlib
#
# $Id: Makefile,v 1.1 2000-09-22 11:37:51 petli Exp $

include ../src/defs

python-xlib.ps: $(SRCS)
	texi2dvi -b $(TOPSRC)
	dvips -o python-xlib.ps python-xlib.dvi

clean:
	rm -f python-xlib.*