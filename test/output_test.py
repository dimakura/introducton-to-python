import os
import re
from pathlib import Path
import subprocess


def remove_project_dir(string):
    regex = r'File "[\S]+/([\S]+.py)"'
    return re.sub(regex, r'File "\1"', string)


def output_verification(filename: str):
    """Runs file and checks its output."""
    dirname = 'listings'
    python_path = str(Path(dirname, filename).with_suffix('.py'))
    output_path = str(Path(dirname, filename).with_suffix('.out'))
    assert os.path.exists(python_path), f'File {python_path} does not exist.'

    if os.path.exists(output_path):
        with open(output_path, 'r') as f:
            expected_output = f.read()
    else:
        expected_output = ''

    try:
        actual_output = subprocess.check_output(['python', python_path], stderr=subprocess.STDOUT).decode('utf-8')
    except subprocess.CalledProcessError as e:
        full_output = e.output.decode('utf-8')
        actual_output = remove_project_dir(full_output)

    assert expected_output == actual_output


def test_getting_started_outputs():
    output_verification('getting-started/hello_world')


def test_variables_and_types_outputs():
    # string
    output_verification('variables-and-types/hello_world')
    output_verification('variables-and-types/message_comparison')
    output_verification('variables-and-types/quoted_strings')
    output_verification('variables-and-types/upper_method')
    output_verification('variables-and-types/lower_method')
    output_verification('variables-and-types/title_method')
    output_verification('variables-and-types/f_strings')
    output_verification('variables-and-types/f_strings2')
    output_verification('variables-and-types/whitespace')
    output_verification('variables-and-types/strip')
    output_verification('variables-and-types/removeprefix')

    # numbers
    output_verification('variables-and-types/integers')
    output_verification('variables-and-types/integers2')

    # types
    output_verification('variables-and-types/typechecking')    


def test_list_outputs():
    output_verification('lists/days')
    output_verification('lists/days_typed')
    output_verification('lists/add')
    output_verification('lists/pop')
    output_verification('lists/remove')
    output_verification('lists/clear')
    output_verification('lists/del')
    output_verification('lists/del_list')
    output_verification('lists/len')
    output_verification('lists/sorting')
    output_verification('lists/reverse')
    output_verification('lists/modify')


def test_if_outputs():
    output_verification('if-statement/vote')
    output_verification('if-statement/strings')
    output_verification('if-statement/numbers')
    output_verification('if-statement/simple-if')
    output_verification('if-statement/if-else')
    output_verification('if-statement/if-elif-else')
    output_verification('if-statement/list')


def test_loops_output():
    output_verification('loops/animals')
    output_verification('loops/squares')
    output_verification('loops/sum')
    output_verification('loops/min-max')
    output_verification('loops/built-in')
    output_verification('loops/while-loop')


def test_collections_output():
    output_verification('collections/tuples')
    output_verification('collections/tuples2')
    output_verification('collections/dictionaries')
    output_verification('collections/dictionary_loop')
    output_verification('collections/dictionary_change')
    output_verification('collections/sets')
