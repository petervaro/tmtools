#!/usr/bin/env python3
## INFO ########################################################################
##                                                                            ##
##                                  tmtools                                   ##
##                                  =======                                   ##
##                                                                            ##
##             tmLanguage, tmTheme, tmPreferences, etc. generator             ##
##                       Version: 1.0.00.094 (20141110)                       ##
##                                                                            ##
##                         File: tmtools/buildsys.py                          ##
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

#------------------------------------------------------------------------------#
def generate_buildsys(scope, build, run=None, rebuild=None,
                      rebuild_and_run=None, **kwargs):
    # Commands and their names
    options = {'Run': run,
               'Rebuild': rebuild,
               'Rebuild and Run': rebuild_and_run}

    # Basic build system
    buildsys = {'cmd': build,
                'shell': True,
                'selector': 'source.{}'.format(scope)}

    # Construct command variants
    variants = []
    for name, command in options.items():
        if command:
            variants.append({'name': name,
                             'cmd': command,
                             'shell': True})
    # If there wre variants
    if variants:
        buildsys['variants'] = variants

    # Return new plist
    return buildsys
