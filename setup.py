# Distutils script for python-xlib

from importlib.metadata import version
from setuptools import (__version__ as setuptools_version, setup)


# Check setuptools is recent enough to support `setup.cfg`.
installed_version = version('setuptools')
setuptools_require = '30.3.0'
assert setuptools_version >= setuptools_require, 'setuptools >= {} is required'.format(setuptools_require)


setup(
    install_requires=['six>=1.10.0'],
    setup_requires=['setuptools-scm'],
    packages=[
        'Xlib',
        'Xlib.ext',
        'Xlib.keysymdef',
        'Xlib.protocol',
        'Xlib.support',
        'Xlib.xobject'
    ],
)
