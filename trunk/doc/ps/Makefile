# Make postscript documentation for Python Xlib
#
# $Id: Makefile,v 1.2 2001-11-30 10:38:06 petli Exp $

include ../src/defs

python-xlib.ps: python-xlib.dvi
	dvips -o python-xlib.ps python-xlib.dvi

python-xlib.dvi: $(SRCS)
	cp python-xlib.aux python-xlib.auxtmp
	texi2dvi -b $(TOPSRC)
# If xref has changed, rebuild again to catch them
	cmp python-xlib.aux python-xlib.auxtmp || texi2dvi -b $(TOPSRC)

clean:
	rm -f python-xlib.*