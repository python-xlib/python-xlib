#!/usr/bin/env python

# Python 2/3 compatibility.
from __future__ import print_function

import os
import signal
import subprocess
import sys
import tempfile
import unittest


class SigException(BaseException):
    def __init__(self, signum):
        super(SigException, self).__init__()
        self.signum = signum

def xsession_sighandler(signum, frame):
    raise SigException(signum)

def xserver_start(display, executable='Xvfb', authfile=None):
    pid = os.fork()
    if pid != 0:
        return pid
    if authfile is None:
        authfile = os.devnull
    # This will make the xserver send us a SIGUSR1 when ready.
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)
    cmd = [
        executable,
        '-auth', authfile,
        '-noreset',
        display,
    ]
    print('starting xserver: `{0}`'.format(' '.join(cmd)))
    os.execlp(cmd[0], *cmd)

def tests_run(display, authfile=None, test_names=()):
    # Run in this process (not a fork) so `coverage run runtests.py` sees the tests.
    if authfile is None:
        authfile = os.devnull
    os.environ['DISPLAY'] = display
    os.environ['XAUTHORITY'] = authfile
    loader = unittest.TestLoader()
    if test_names:
        print('running tests: `{0}`'.format(' '.join(test_names)))
        suite = loader.loadTestsFromNames(test_names)
    else:
        print('running tests: `test/`, `examples/run_examples.py`')
        suite = unittest.TestSuite((
            loader.discover('test', top_level_dir='.'),
            # `examples` is not a package, so it is its own top level directory.
            loader.discover('examples', pattern='run_examples.py', top_level_dir='examples'),
        ))
    return unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()


def runtests():

    cleanup_funcs = []

    try:
        if hasattr(sys, 'pypy_version_info'):
            server_display = ':8'
        else:
            server_display = ':9'
        server_display += ''.join(str(n) for n in sys.version_info[:3])

        # Setup a temporary authentication file.
        cookie = subprocess.check_output('mcookie').strip()
        authfile = tempfile.NamedTemporaryFile(delete=False)
        cleanup_funcs.append(lambda: os.unlink(authfile.name))
        authfile.close()
        subprocess.check_call((
            'xauth',
            '-f', authfile.name,
            'add', server_display, '.', cookie,
        ))

        # Setup signal handler to wait for xserver to be ready.
        signal.signal(signal.SIGUSR1, xsession_sighandler)

        # Start xserver.
        server_pid = xserver_start(server_display, authfile=authfile.name)
        cleanup_funcs.append(lambda: os.waitpid(server_pid, 0))
        cleanup_funcs.append(lambda: os.kill(server_pid, signal.SIGTERM))

        # Give the server 3 seconds to start.
        signal.alarm(3)

        # Wait for server to be ready.
        try:
            signal.pause()
        except SigException as err:
            assert signal.SIGUSR1 == err.signum
            signal.alarm(0)

        # Run tests.
        success = tests_run(server_display, authfile=authfile.name, test_names=sys.argv[1:])
        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        sys.exit(1)

    finally:
        for func in reversed(cleanup_funcs):
            func()


if __name__ == '__main__':
    runtests()
