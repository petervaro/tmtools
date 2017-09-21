#!/usr/bin/env python3
## INFO ##
## INFO ##

# Import python modules
from itertools import count


#------------------------------------------------------------------------------#
def generate_comments(scope,
                      line_comments  = (),
                      block_comments = (),
                      **kwargs):
    index  = count()
    values = []

    # If language has line comments
    for line_comment, i in zip(line_comments, index):
        values.append({'name' : f'TM_COMMENT_START{f"_{i + 1}" if i else ""}',
                       'value': line_comment + ' '})

    # If langauge has block comments
    for (start_comment, close_comment), i in zip(block_comments, index):
        suffix = f'_{i + 1}' if i else ''
        values.append({'name' : f'TM_COMMENT_START{suffix}',
                       'value': start_comment + ' '})
        values.append({'name' : f'TM_COMMENT_END{suffix}',
                       'value': ' ' + close_comment})

    # Return the new plist
    return {'name' : 'Comments',
            'scope': f'source.{scope}',
            'settings': {'shellVariables': values}}
