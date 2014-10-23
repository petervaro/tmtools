#!/usr/bin/env python3
## INFO ########################################################################
##                                                                            ##
##                                  tmtools                                   ##
##                                  =======                                   ##
##                                                                            ##
##             tmLanguage, tmTheme, tmPreferences, etc. generator             ##
##                       Version: 1.0.00.019 (20141023)                       ##
##                                                                            ##
##                               File: setup.py                               ##
##                                                                            ##
##            For more information about the project, please visit            ##
##                  <https://github.com/petervaro/tmtools>.                   ##
##                       Copyright (C) 2014 Peter Varo                        ##
##                                                                            ##
##  This program is free software: you can redistribute it and/or modify it   ##
##   under the terms of the GNU General Public License as published by the    ##
##       Free Software Foundation, either version 3 of the License, or        ##
##                    (at your option) any later version.                     ##
##                                                                            ##
##    This program is distributed in the hope that it will be useful, but     ##
##         WITHOUT ANY WARRANTY; without even the implied warranty of         ##
##            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.            ##
##            See the GNU General Public License for more details.            ##
##                                                                            ##
##     You should have received a copy of the GNU General Public License      ##
##     along with this program, most likely a file in the root directory,     ##
##        called 'LICENSE'. If not, see <http://www.gnu.org/licenses>.        ##
##                                                                            ##
######################################################################## INFO ##

# Import python modules
from distutils.core import setup

# Install tmtools
if __name__ == '__main__':
    # Get current version number
    with open('VERSION', encoding='utf-8') as file:
        VERSION = '.'.join(version.read().split('.')[:-1])

    # Get license information
    with open('LICENSE', encoding='utf-8') as file:
        LICENSE = file.read()

    # Get license information
    with open('README', encoding='utf-8') as file:
        README = file.read()

    setup(name='tmtools',
          version=VERSION,
          license=LICENSE,
          description='tmLanguage, tmTheme, tmPreferences, etc. generator',
          long_description=README,
          author='Peter Varo',
          author_email='petervaro@sketchandprototype.com',
          url='https://github.com/petervaro/tmtools',
          platforms='Any',
          packages=['tmtools'])
