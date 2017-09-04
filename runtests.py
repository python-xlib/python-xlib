#!/usr/bin/env python

# Python 2/3 compatibility.
from __future__ import print_function

import os
import signal
import subprocess
import sys
import tempfile
import textwrap

from pkg_resources import load_entry_point


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

def tests_run(display, authfile=None):
    pid = os.fork()
    if pid != 0:
        return pid
    if authfile is None:
        authfile = os.devnull
    os.environ['DISPLAY'] = display
    os.environ['XAUTHORITY'] = authfile
    cmd = [
        sys.executable,
        '-c', textwrap.dedent(
            '''
            from pkg_resources import load_entry_point
            sys.exit(load_entry_point(
                'nose', 'console_scripts', 'nosetests',
            )())
            '''
        ).lstrip(),
        '--exe', '--with-xunit', '--verbosity=3',
    ]
    has_custom_tests = False
    for arg in sys.argv[1:]:
        if not arg.startswith('-'):
            has_custom_tests = True
        cmd.append(arg)
    if not has_custom_tests:
        cmd.extend(('test/', 'examples/run_examples.py'))
    print('running tests: `{0}`'.format(' '.join(cmd)))
    sys.argv = cmd
    try:
        load_entry_point('nose', 'console_scripts', 'nosetests')()
    except SystemExit as err:
        code = err.code
    else:
        code = 0
    os._exit(code)


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
        tests_pid = tests_run(server_display, authfile=authfile.name)
        pid, status = os.waitpid(tests_pid, 0)
        assert pid == tests_pid
        sys.exit(status >> 8)

    except KeyboardInterrupt:
        sys.exit(1)

    finally:
        for func in reversed(cleanup_funcs):
            func()


if __name__ == '__main__':
    runtests()
