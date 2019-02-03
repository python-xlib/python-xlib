# Distutils script for python-xlib

from setuptools import setup

import Xlib


setup(
    name='python-xlib',
    version=Xlib.__version_string__,

    description='Python X Library',
    download_url='https://github.com/python-xlib/python-xlib/releases',
    url='https://github.com/python-xlib/python-xlib',
    license='LGPLv2+',

    author='Peter Liljenberg',
    author_email='petli@ctrl-c.liu.se',

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

    keywords='xlib x11 x windows',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
    ],
)
