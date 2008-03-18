# Top-level makefile for Python Xlib documentation

FORMATS = info ps html

all: $(FORMATS)

info::
	(cd info; make)

ps::
	(cd ps; make)

html::
	(cd html; make)

clean:
	for f in $(FORMATS); do (cd $$f; make clean); done
