# Top-level makefile for Python Xlib documentation
#
# $Id: Makefile,v 1.1 2000-09-22 11:37:51 petli Exp $

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
