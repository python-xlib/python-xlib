# Make HTML documentation for Python Xlib
#
# $Id: Makefile,v 1.1 2000-09-22 11:37:51 petli Exp $

include ../src/defs

python-xlib_toc.html: $(SRCS)
	texi2html -splitnode -menu $(TOPSRC)
	ln -sf python-xlib_toc.html index.html

clean:
	rm -f *.html