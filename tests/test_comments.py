## INFO ##
## INFO ##

# Import pytest modules
from pytest import raises

# Import tmtools modules
from tmtools.comments import generate_comments


#------------------------------------------------------------------------------#
def test_empty():
    expected = {'name'    : 'Comments',
                'scope'   : 'source.empty',
                'settings': {'shellVariables': []}}
    assert generate_comments('empty') == expected


#------------------------------------------------------------------------------#
def test_invalid():
    with raises(TypeError):
        generate_comments('invalid1', line_comments=None)

    with raises(TypeError):
        generate_comments('invalid2', block_comments=None)

    with raises(TypeError):
        generate_comments('invalid4', block_comments=(None,))


#------------------------------------------------------------------------------#
def test_line_only():
    expected = {'name'    : 'Comments',
                'scope'   : 'source.line_only',
                'settings': {'shellVariables': [{'name': 'TM_COMMENT_START',
                                                 'value': '-- '}]}}
    assert generate_comments('line_only', line_comments=('--',)) == expected


#------------------------------------------------------------------------------#
def test_block_only():
    expected = {'name'    : 'Comments',
                'scope'   : 'source.block_only',
                'settings': {'shellVariables': [{'name': 'TM_COMMENT_START',
                                                 'value': '/* '},
                                                {'name': 'TM_COMMENT_END',
                                                 'value': ' */'}]}}
    assert generate_comments('block_only',
                             block_comments=(('/*', '*/'),)) == expected


#------------------------------------------------------------------------------#
def test_both_line_and_block():
    expected = {'name'    : 'Comments',
                'scope'   : 'source.both_line_and_block',
                'settings': {'shellVariables': [{'name': 'TM_COMMENT_START',
                                                 'value': '// '},
                                                {'name': 'TM_COMMENT_START_2',
                                                 'value': '/* '},
                                                {'name': 'TM_COMMENT_END_2',
                                                 'value': ' */'}]}}
    assert generate_comments('both_line_and_block',
                             line_comments=('//',),
                             block_comments=(('/*', '*/'),)) == expected


#------------------------------------------------------------------------------#
def test_multi_line_and_block():
    expected = {'name'    : 'Comments',
                'scope'   : 'source.both_line_and_block',
                'settings': {'shellVariables': [{'name': 'TM_COMMENT_START',
                                                 'value': '// '},
                                                {'name': 'TM_COMMENT_START_2',
                                                 'value': '/// '},
                                                {'name': 'TM_COMMENT_START_3',
                                                 'value': '/* '},
                                                {'name': 'TM_COMMENT_END_3',
                                                 'value': ' */'},
                                                {'name': 'TM_COMMENT_START_4',
                                                 'value': '/+ '},
                                                {'name': 'TM_COMMENT_END_4',
                                                 'value': ' +/'}]}}
    assert generate_comments('both_line_and_block',
                             line_comments=('//', '///'),
                             block_comments=(('/*', '*/'),
                                             ('/+', '+/'))) == expected
