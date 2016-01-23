#!/usr/bin/env python

from __future__ import print_function
import sys, os
import string
import unittest
import struct
import array

import coverage

testfolder = os.path.abspath(os.path.dirname(__file__))
package_root = os.path.abspath(os.path.join(testfolder, ".."))
sys.path.append(package_root)

# needs to be called before importing the modules
cov = coverage.coverage(branch = True, omit = os.path.join(package_root, 'examples', '*.py'))
cov.start()

from Xlib.protocol import request, rq, event
import Xlib.protocol.event

def is_big_endian():
    return struct.unpack('BB', struct.pack('H', 0x0100))[0] != 0

def run_tests():
    if is_big_endian():
        excludes = ['test_events_le', 'test_requests_le', ]
    else:
        excludes = ['test_events_be', 'test_requests_be', ]

    suite = unittest.TestSuite()

    sys.path.append(testfolder)

    for root, dirs, files in os.walk(testfolder):
        test_modules = [
            file.replace('.py', '') for file in files if
                file.startswith('test_') and
                file.endswith('.py')]

        test_modules = [mod for mod in test_modules if mod.lower() not in excludes]
        print('test_modules:')
        print(test_modules)
        for mod in test_modules:

            imported_mod = __import__(mod, globals(), locals())

            suite.addTests(
                unittest.defaultTestLoader.loadTestsFromModule(imported_mod))

    unittest.TextTestRunner(verbosity=3).run(suite)
    cov.stop()
    #print(cov.analysis())
    print(cov.report())
    cov.html_report(
        directory = os.path.join(package_root, "Coverage_report"),
        omit = [os.path.join(package_root, 'examples', '*.py'),
                os.path.join(package_root, 'utils', '*.py'),
                os.path.join(package_root, 'test', '*.py'), ]
        )


if __name__ == '__main__':
    run_tests()