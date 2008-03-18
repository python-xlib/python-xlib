# Make info documentation for Python Xlib

include ../src/defs

python-xlib.info: $(SRCS)
	makeinfo --force --no-split -P $(SRCDIR) $(TOPSRC)

clean:
	rm -f python-xlib.info
