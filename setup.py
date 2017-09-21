#!/usr/bin/env python3
## INFO ##
## INFO ##

# Import python modules
from distutils.core import setup

# Install tmtools
if __name__ == '__main__':
    # Get license information
    with open('README', encoding='utf-8') as file:
        README = file.read()

    setup(name='tmtools',
          version='1.1.0',
          license='GNU General Public License Version 3',
          description='tmLanguage, tmTheme, tmPreferences, etc. generator',
          long_description=README,
          author='Peter Varo',
          author_email='hello@petervaro.com',
          url='https://github.com/petervaro/tmtools',
          platforms='Any',
          packages=['tmtools'])
