# $Id: rdb.py,v 1.1 2000-08-11 15:03:23 petli Exp $
#
# Xlib.rdb -- X resource database implementation
#
#    Copyright (C) 2000 Peter Liljenberg <petli@ctrl-c.liu.se>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import string
import types
import re

comment_re = re.compile(r'^\s*!')
resource_spec_re = re.compile(r'^\s*([-_a-zA-Z0-9?.*]+)\s*:\s*(.*?)\s*$')
value_escape_re = re.compile('\\\\([ \tn\\]|[0-7]{3,3})')
resource_parts_re = re.compile(r'([.*]+)')

NAME_MATCH = 0
CLASS_MATCH = 2
WILD_MATCH = 4
NO_MATCH = 6

TIGHT_NAME = 0
LOOSE_NAME = 1
TIGHT_CLASS = 2
LOOSE_NAME = 3
TIGHT_WILD = 4
LOOSE_WILD = 5


class ResourceDB:
    def __init__(self, file = None, string = None, resources = None):
	self.db = {}
	if file is not None:
	    self.insert_file(file)
	if string is not None:
	    self.insert_string(string)
	if resources is not None:
	    self.insert_resources(resources)

    def insert_file(self, file):
	if type(file) is types.StringType:
	    file = open(file, 'r')

	self.insert_string(file.read())
	
    def insert_string(self, data):
	# First split string into lines

	lines = string.split(data, '\n')

	while lines:
	    line = lines[0]
	    del lines[0]

	    # Skip empty line
	    if not line:
		continue

	    # Skip comments
	    if comment_re.match(line):
		continue
	    
	    # Handle continued lines
	    while line[-1] == '\\':
		if lines:
		    line = line[:-1] + lines[0]
		    del lines[0]
		else:
		    line = line[:-1]
		    break

	    # Split line into resource and value
	    m = resource_spec_re.match(line)

	    # Bad line, just ignore it silently
	    if not m:
		continue

	    res, value = m.group(1, 2)
	    
	    # Convert all escape sequences in value
	    splits = value_escape_re.split(value)

	    for i in range(1, len(splits), 2):
		s = splits[i]
		if len(s) == 3:
		    splits[i] = chr(string.atoi(s, 8))
		elif s == 'n':
		    splits[i] = '\n'

	    value = string.join(splits, '')

	    self.insert(res, value)

    def insert_resources(self, resources):
	for res, value in resources:
	    self.insert(res, value)

    def insert(self, resource, value):

	# Split res into components and bindings
	parts = resource_parts_re.split(resource)

	# If the last part is empty, this is an invalid resource
	# which we simply ignore
	if parts[-1] == '':
	    return
	
	db = self.db
	for i in range(1, len(parts), 2):
	    
	    # Create a new mapping/value group
	    if not db.has_key(parts[i - 1]):
		db[parts[i - 1]] = ({}, {})

	    # Use second mapping if a loose binding, first otherwise
	    if '*' in parts[i]:
		db = db[parts[i - 1]][1]
	    else:
		db = db[parts[i - 1]][0]

	# Insert value into the derived db
	if db.has_key(parts[-1]):
	    db[parts[-1]] = db[parts[-1]][:2] + (value, )
	else:
	    db[parts[-1]] = ({}, {}, value)


    def __getitem__(self, (name, cls)):

	# Split name and class into their parts

	namep = string.split(name, '.')
	clsp = string.split(cls, '.')

	# It is an error for name and class to have different number
	# of parts

	if len(namep) != len(clsp):
	    raise ValueError('Different number of parts in resource name/class: %s/%s' % (name, cls))

	# We maintain a list of parts mapping groups, and iterate
	# until we either find a matching value, or run out of
	# mappings

	loosedbs = []
	groups = []
	
	# Precedence order: name -> class -> ? -> empty string
	
	if self.db.has_key(namep[0]):
	    groups.append(self.db[namep[0]])

	elif self.db.has_key(clsp[0]):
	    groups.append(self.db[clsp[0]])

	elif self.db.has_key('?'):
	    groups.append(self.db['?'])

	# Special case for resources which begins with a loose
	# binding, e.g. '*foo.bar'
	if self.db.has_key(''):
	    loosedbs.append(self.db[''][1])

	# No match, raise KeyError
	if not groups and not loosedbs:
	    raise KeyError((name, cls))


	# Iterate over each name/class component
	# until we find a single value

	for i in range(1, len(namep)):

	    print 'component:', namep[i], clsp[i]
	    print 'groups:   ', groups
	    print 'loosedbs: ', loosedbs
	    print
	    
	    # For each component, we choose among the mappings
	    # by applying these rules in order:
	    
	    # Rule 1: If the current group contains a match for the
	    # name, class or '?', we drop all previously found loose
	    # binding mappings.

	    # Rule 2: A matching name has precedence over a matching
	    # class, which in turn has precedence over '?'.

	    # Rule 3: Tight bindings have precedence over loose
	    # bindings.

	    best = NO_MATCH
	    ngs = []

	    for part, score in ((namep[i], NAME_MATCH),
				(clsp[i], CLASS_MATCH),
				('?', WILD_MATCH)):

		for group in groups:
		    # Match in tight binding
		    if group[0].has_key(part) and score <= best:
			if score == best:
			    ngs.append(group[0][part])
			else:
			    ngs = [group[0][part]]
			    best = score

		    # Match in loose binding
		    elif group[1].has_key(part) and score + 1 <= best:
			if score + 1 == best:
			    ngs.append(group[1][part])
			else:
			    ngs = [group[1][part]]
			    best = score + 1

		# Short cut when we have found a match
		if ngs:
		    break
		

	    # Found component, so use rule 1 to drop all
	    # loose binding mappings

	    if ngs:
		groups = ngs
#		del loosedbs[:]
	    
	    # No match in direct groups, check previous loose bindings
	    # instead.

	    else:
		for part, score in ((namep[i], NAME_MATCH),
				    (clsp[i], CLASS_MATCH),
				    ('?', WILD_MATCH)):
		    for db in loosedbs:
			if db.has_key(part):
			    ngs.append(db[part])

		    # Shortcut when there have been matches
		    if ngs:
			break

		# Ah, some matches.  Use them for the next iteration
		# of the mapping and drop all loose binding mappings

		if ngs:
		    groups = ngs
#		    del loosedbs[:]

		# No matches, augment loose binding mappings with
		# those from old groups
		else:
		    for group in groups:
			loosedbs.append(group[1])
		    groups = ()
		
	# Now groups should contain at least one item with a value.
	# (There should only be one, hopefully...  Either way, return
	# the first in the list.)
	
	for group in groups:
	    if len(group) == 3:
		return group[2]

	# Nothing found, raise KeyError
	raise KeyError((name, cls))
	
