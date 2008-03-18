# Make HTML documentation for Python Xlib

include ../src/defs

python-xlib_toc.html: $(SRCS)
	./texi2html -splitnode -menu $(TOPSRC)
	ln -sf python-xlib_toc.html index.html

clean:
	rm -f *.html
