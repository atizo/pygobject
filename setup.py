#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# setup.py - distutils configuration for pygobject


'''Python Bindings for GObject.

PyGObject is a set of bindings for the glib, gobject and gio libraries.
It provides an object oriented interface that is slightly higher level than
the C one. It automatically does all the type casting and reference
counting that you would have to do normally with the C API. You can
find out more on the official homepage, http://www.pygtk.org/'''


import os
import sys

from distutils.core import setup
from distutils.command.install import install

MAJOR_VERSION = 2
MINOR_VERSION = 15
MICRO_VERSION = 1
VERSION       = '%d.%d.%d' % (MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

class PyGObjectBuildAndInstall(install):
    def run(self):
        os.system('sh autogen.sh --prefix=%s --disable-introspection && make && make install' % self.install_base)

if '--no-deps' in sys.argv:
    sys.argv.remove('--no-deps')

doclines = __doc__.split('\n')

setup(name='pygobject',
      url='http://www.pygtk.org/',
      version=VERSION,
      license='LGPL',
      maintainer='Johan Dahlin',
      maintainer_email='johan@gnome.org',
      description=doclines[0],
      long_description='\n'.join(doclines[2:]),
      provides=['codegen', 'gio', 'glib', 'gobject'],
      cmdclass={'install': PyGObjectBuildAndInstall,
                'develop': PyGObjectBuildAndInstall})
