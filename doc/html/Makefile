# Make HTML documentation for Python Xlib
#
# $Id: Makefile,v 1.2 2001-12-16 14:23:38 petli Exp $

include ../src/defs

python-xlib_toc.html: $(SRCS)
	./texi2html -splitnode -menu $(TOPSRC)
	ln -sf python-xlib_toc.html index.html

clean:
	rm -f *.html