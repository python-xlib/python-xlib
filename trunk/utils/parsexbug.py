#!/usr/bin/python

class BugFile:
    def __init__(self, file):
	self.file = file
	self.cbuf = self.sbuf = ''

    def read_client(self, bytes):
	while len(self.cbuf) < bytes and self.file:
	    self.read_next()

	d = self.cbuf[:bytes]
	self.cbuf = self.cbuf[bytes:]

	return d

    def read_server(self, bytes):
	while len(self.sbuf) < bytes and self.file:
	    self.read_next()

	d = self.sbuf[:bytes]
	self.sbuf = self.sbuf[bytes:]

	return d

    def read_next(self):
	line = self.file.readline()
	if line == '':
	    self.file = None
	    return
	
	src = line[0]
	length = int(line[1:-1])
	data = self.file.read(length)
	if src == 'C':
	    self.cbuf = self.cbuf + data
	elif src == 'S':
	    self.sbuf = self.sbuf + data
	else:
	    raise ValueError('Bad control line: %s' % line)

