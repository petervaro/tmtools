#!/usr/bin/env python3
## INFO ##
## INFO ##

# Import python modules
from itertools import count


#------------------------------------------------------------------------------#
def generate_comments(scope,
                      comments=()):
    values = []
    for i, comment in enumerate(comments):
        if not isinstance(comment, dict):
            raise DeprecationWarning('Comment description should be a `dict`')

        suffix = f'_{i + 1}' if i else ''
        values.append({'name' : 'TM_COMMENT_START' + suffix,
                       'value': comment['begin'] + ' '})

        try:
            values.append({'name' : 'TM_COMMENT_END' + suffix,
                           'value': ' ' + comment['end']})
        except KeyError:
            pass

        try:
            values.append({'name' : 'TM_COMMENT_DISABLE_INDENT' + suffix,
                           'value': comment['disable_indent']})
        except KeyError:
            pass

    # Return the new plist
    return {'name' : 'Comments',
            'scope': f'source.{scope}',
            'settings': {'shellVariables': values}}
