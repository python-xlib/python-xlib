# Distutils script for python-xlib
#
# Metadata lives here rather than in a `[project]` table of pyproject.toml
# because that table (PEP 621) needs setuptools>=61, which needs Python>=3.7.
# Once Python 2.7 and 3.3 to 3.6 support is dropped, it can all move to
# pyproject.toml (`version` as dynamic, read from `Xlib.__version_string__`),
# and this file can be deleted.

import io

from setuptools import setup

from Xlib import __version_string__

with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()


setup(
    name='python-xlib',
    version=__version_string__,
    description='Python X Library',
    long_description=long_description,
    download_url='https://github.com/python-xlib/python-xlib/releases',
    url='https://github.com/python-xlib/python-xlib',
    license='LGPLv2+',
    author='Peter Liljenberg',
    author_email='petli@ctrl-c.liu.se',
    keywords=['windows', 'x', 'x11', 'xlib'],
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
    ],
    install_requires=['six>=1.10.0'],
    packages=[
        'Xlib',
        'Xlib.ext',
        'Xlib.keysymdef',
        'Xlib.protocol',
        'Xlib.support',
        'Xlib.xobject'
    ],
    options={'bdist_wheel': {'universal': '1'}},
)
