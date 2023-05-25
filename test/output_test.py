import os
from pathlib import Path
import subprocess


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

    actual_output = subprocess.check_output(['python', python_path])
    assert expected_output == actual_output.decode('utf-8')


def test_ch01_outputs():
    output_verification('ch01/hello_world')


def test_ch02_strings_outputs():
    output_verification('ch02/hello_world')
    output_verification('ch02/hello_world_typed')
    output_verification('ch02/message_comparison')
    output_verification('ch02/quoted_strings')
    output_verification('ch02/upper_method')
    output_verification('ch02/lower_method')
    output_verification('ch02/title_method')
    output_verification('ch02/f_strings')
    output_verification('ch02/f_strings2')
    output_verification('ch02/whitespace')
    output_verification('ch02/strip')
    output_verification('ch02/removeprefix')


def test_ch02_numbers_outputs():
    output_verification('ch02/integers')
    output_verification('ch02/integers2')


def test_ch02_type_checking_output():
    output_verification('ch02/typechecking')

