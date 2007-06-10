#!/usr/bin/env python

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import Xlib.rdb

import unittest

resources = """
! Single component

single: name
Single: class
?: wild

! name vs class vs ?

p.first.second: n.n
p.first.Second: n.c
p.first.?: n.w

p.First.second: c.n
p.First.Second: c.c
p.First.?: c.w

p.?.second: w.n
p.?.Second: w.c
p.?.?: w.w

! Tight over loose bindings

b.tight.match: tight
b.tight*match: bad
b.loose*match: loose

! skip matches

s.*end: default
s.foo*end: default foo
s.foo.bar.end: bar foo

! Multiple skip matches

ss.*mid*end: default
ss.foo*mid*end: default foo
ss.foo*mid.bar*end: bar foo

! First component unbound

*fie.fum: skipfirst
fie.fum: matchtwo
feh.fie.fum: matchfirst
"""

queries = (
    # Single component
    ('single', 'Single', 'name'),
    ('noname', 'Single', 'class'),
    ('noname', 'Noclass', 'wild'),

    # Name vs class vs ?

    ('p.first.second', 'P.First.Second', 'n.n'),
    ('p.first.noname', 'P.First.Second', 'n.c'),
    ('p.first.noname', 'P.First.Noclass', 'n.w'),

    ('p.noname.second', 'P.First.Second', 'c.n'),
    ('p.noname.noname', 'P.First.Second', 'c.c'),
    ('p.noname.noname', 'P.First.Noclass', 'c.w'),

    ('p.noname.second', 'P.Noclass.Second', 'w.n'),
    ('p.noname.noname', 'P.Noclass.Second', 'w.c'),
    ('p.noname.noname', 'P.Noclass.Noclass', 'w.w'),

    # Tight over loose bindings

    ('b.tight.match', 'B.Tight.Match', 'tight'),
    ('b.loose.match', 'B.Loose.Match', 'loose'),

    # skip matches

    ('s.bar.end', 'S.Bar.End', 'default'),
    ('s.foo.bar.end', 'S.Foo.Bar.End', 'bar foo'),
    ('s.foo.gazonk.end', 'S.Foo.Gazonk.End', 'default foo'),

    # Multiple skip matches

    ('ss.x.mid.x.end', 'Ss.X.Mid.X.End', 'default'),
    ('ss.foo.x.mid.x.end', 'Ss.Foo.X.Mid.X.End', 'default foo'),
    ('ss.foo.x.mid.bar.x.end', 'Ss.Foo.X.Mid.Bar.X.End', 'bar foo'),
    ('ss.foo.mid.x.mid.bar.x.end', 'Ss.Foo.Mid.X.Mid.Bar.X.End', 'default foo'),
    ('ss.foo.x.mid.x.mid.bar.x.end', 'Ss.Foo.X.Mid.X.Mid.Bar.X.End', 'default foo'),

    # First component unbound
    ('fie.fum', 'Fie.Fum', 'matchtwo'),
    ('noname.fie.fum', 'Noclass.Fie.Fum', 'skipfirst'),
    ('feh.fie.fum', 'Feh.Fie.Fum', 'matchfirst'),
    )

resource_set1 = (
    ('foo.bar', 1,),
    ('foo.bar.gazonk', 2),
    ('*bar*gazonk', 3),
    )

resource_set2 = (
    ('foo.bar', 10,),     # Changing the value of an item
    ('foo.bar.whee', 11), # Adding entries to existing component
    ('foo.bar*whoho', 12),
    ('foo.fie', 13),      # Copy new resources
    ('foo.fie*fum', 14),
    ('*foo.bar', 15),
    )

class TestRDB(unittest.TestCase):
    def testParseAndQuery(self):
        # Test string parsing and querying
        db = Xlib.rdb.ResourceDB(string = resources)
        for name, cls, value in queries:
            try:
                v = db[name, cls]
            except KeyError:
                raise AssertionError('Value not found for %s/%s:\n    expected %s' % (name, cls, value))

            if v != value:
                raise AssertionError('Value mismatch for %s/%s:\n    expected %s, got %s' % (name, cls, value, v))


    def testUpdate(self):
        # Test update.  An update should have the same result as
        # inserting all the resource entries in the manually

        db1 = Xlib.rdb.ResourceDB()
        db2 = Xlib.rdb.ResourceDB()
        db3 = Xlib.rdb.ResourceDB()

        db1.insert_resources(resource_set1)
        db2.insert_resources(resource_set2)

        db1.update(db2)

        db3.insert_resources(resource_set1)
        db3.insert_resources(resource_set2)

        assert db1.db == db3.db


if __name__ == '__main__':
    unittest.main()
