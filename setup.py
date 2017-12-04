# Distutils script for python-xlib

from setuptools import setup


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
