#!/usr/bin/env python3
## INFO ##
## INFO ##

#------------------------------------------------------------------------------#
def generate_buildsys(scope,
                      build,
                      run=None,
                      rebuild=None,
                      rebuild_and_run=None,
                      **kwargs):
    # Basic build system
    buildsys = {'cmd': build,
                'shell': True,
                'selector': f'source.{scope}'}

    # Construct command variants
    variants = []
    for name, command in {'Run': run,
                          'Rebuild': rebuild,
                          'Rebuild and Run': rebuild_and_run}.items():
        if command:
            variants.append({'name': name,
                             'cmd': command,
                             'shell': True})
    # If there wre variants
    if variants:
        buildsys['variants'] = variants

    # Return new plist
    return buildsys
