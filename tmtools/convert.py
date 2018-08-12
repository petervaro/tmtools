#!/usr/bin/env python3
## INFO ##
## INFO ##

# Import python modules
import json
import plistlib
from os import makedirs
from copy import deepcopy
from itertools import cycle
from collections import OrderedDict
from os.path import join, expanduser

# Import user modules
from tmtools.comments import generate_comments
from tmtools.buildsys import generate_buildsys

# Module level constants
THEME_EXT = '.tmTheme'
LANG_EXT  = '.tmLanguage'
PREF_EXT  = '.tmPreferences'
BUILD_EXT = '.sublime-build'
NAME_KEYS = 'name', 'contentName', 'scopeName'


#------------------------------------------------------------------------------#
def _combinator(iterable1, iterable2):
    # Create 'OrderedSet's
    i1 = tuple(OrderedDict.fromkeys(iterable1))
    i2 = tuple(OrderedDict.fromkeys(iterable2))
    # Decide which one to repeat
    if len(i1) < len(i2):
        i1 = cycle(i1)
    else:
        i2 = cycle(i2)
    # Iterate through the values
    for value1, value2 in zip(i1, i2):
        yield value1, value2



#------------------------------------------------------------------------------#
def _replacer(data, name, scope):
    # If data is not the preferred container type
    if not isinstance(data, (dict, list)):
        if isinstance(data, (int, str)):
            return
        else:
            raise TypeError("tmtools' abstractions can operate only "
                            'on dict, list, int and str objects')
    # If data is a dictionary
    try:
        for key, value in list(data.items()):
            # If key is one of the name-keys
            if key in NAME_KEYS:
                data[key] = value.format(NAME=name, SCOPE=scope)
                continue
            # Convert integer dictionary keys into string literals
            if isinstance(key, int):
                data[str(key)] = data.pop(key)
            # Recursion on sub-data
            _replacer(value, name, scope)
    # If data is a list
    except AttributeError:
        for item in data:
            # Recursion on sub-data
            _replacer(item, name, scope)


#------------------------------------------------------------------------------#
def _formatter(data, name):
    # If data is not the preferred container type
    if not isinstance(data, (dict, list)):
        return
    # If data is a dictionary
    try:
        for key, value in data.items():
            # If key is one of the name-keys
            if key in NAME_KEYS:
                data[key] = value.format(NAME=name)
            # If key is not a name-key
            else:
                # If value is a color-object
                try:
                    data[key] = value.to_hex()
                except AttributeError:
                    # Recursion on sub-data
                    _formatter(value, name)
    # If data is a list
    except AttributeError:
        for item in data:
            # Recursion on sub-data
            _formatter(item, name)



#------------------------------------------------------------------------------#
class TMFile:

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, name,
                       file=None,
                       path=None,
                       scope='',
                       test_name=None,
                       test_file=None,
                       test_path=None,
                       comments={},
                       buildsys={}):
        # Store static values
        self._name      = name
        self._file      = file or name
        self._path      = path or os.getcwd()
        self._scope     = scope
        self._test_name = test_name or name
        self._test_file = test_file or self._test_name
        self._test_path = test_path or self._path
        self._comments  = comments
        self._buildsys  = buildsys
        # Create empty definitions
        self._definition = self._test_definition = {}


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # TODO: Add "Automatically Generated, Don't Change" label to files
    def write(self, kind,
                    extension):
        # If write comments-tmpreferences too
        comments = self._comments
        if comments:
            comment_name = f'Comments({self._name}){PREF_EXT}'
            preference = generate_comments(self._scope, comments)
        # If write build-systems too
        buildsys = self._buildsys
        if buildsys:
            buildsys_name = self._name + BUILD_EXT
            buildsys.setdefault(
                'build',
                'printf \'There is no "build" command defined\n\'')
            system = generate_buildsys(self._scope, **buildsys)
        # Write work and/or test files to path(s)
        definitions = self._definition, self._test_definition
        paths_names = _combinator((self._path, self._test_path),
                                  (self._file, self._test_file))
        for definition, (file_path, file_name) in zip(definitions, paths_names):
            # Create dirs if they don't exist
            real_path = expanduser(file_path)
            makedirs(real_path, exist_ok=True)
            # Create full path to file
            full_path = join(real_path, file_name + extension)
            # Write out the property-list file
            with open(full_path, 'w+b') as file:
                plistlib.dump(definition, file)
                print(f'{kind} dictionary has been converted and placed:',
                      f'\t{full_path!r}',
                      sep='\n')
            if comments:
                full_path = join(real_path, comment_name)
                with open(full_path, 'w+b') as file:
                    plistlib.dump(preference, file)
                    print('Comments preference has been converted and placed:',
                          f'\t{full_path!r}',
                          sep='\n')
            if buildsys:
                full_path = join(real_path, buildsys_name)
                with open(full_path, 'w') as file:
                    json.dump(system, file, indent=4)
                    print('Build system has been converted and placed:',
                          f'\t{full_path!r}',
                          sep='\n')



#------------------------------------------------------------------------------#
class Language(TMFile):

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def from_dict(self, definition):
        # If patterns is a dictionary or it does not exist
        try:
            patterns = definition.get('patterns', {})
            definition['patterns'] = [patterns[key] for key in sorted(patterns)]
        # If patterns is not a dictionary
        except TypeError:
            # If patterns is not a list
            if not isinstance(definition['patterns'], list):
                definition['patterns'] = []

        # If test-file is different than the working one
        if self._name != self._test_name:
            self._test_definition = test_definition = deepcopy(definition)
            _replacer(test_definition, self._test_name, self._scope)
        # If test-file is identical with the working one
        else:
            self._test_definition = definition

        # Format and store definition
        _replacer(definition, self._name, self._scope)
        self._definition = definition


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def write(self):
        # Call parent's method
        super().write('Syntax', LANG_EXT)



#------------------------------------------------------------------------------#
class Theme(TMFile):

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def from_dict(self, definition):
        # If test-file is different than the working one
        if self._name != self._test_name:
            self._test_definition = test_definition = deepcopy(definition)
            _formatter(test_definition, self._test_name)
        # If test-file is identical with the working one
        else:
            self._test_definition = definition

        # Format and store definition
        _formatter(definition, self._name)
        self._definition = definition


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def write(self, css=False):
        # Call parent's method
        super().write('Style', THEME_EXT)
        # If CSS output needed
        if css:
            pass
