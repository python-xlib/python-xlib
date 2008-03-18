# Make postscript documentation for Python Xlib

include ../src/defs

python-xlib.ps: python-xlib.dvi
	dvips -o python-xlib.ps python-xlib.dvi

python-xlib.dvi: $(SRCS)
	if test -f python-xlib.aux; then \
           cp python-xlib.aux python-xlib.auxtmp; \
        else touch python-xlib.auxtmp; fi

	texi2dvi -b $(TOPSRC)
# If xref has changed, rebuild again to catch them
	cmp python-xlib.aux python-xlib.auxtmp || texi2dvi -b $(TOPSRC)

clean:
	rm -f python-xlib.*
