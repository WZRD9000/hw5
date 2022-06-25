from victory import date_to_str
from main import separator
from filemanager import copy_file_or_directory, author_info
import os


def test_date_to_str():
    assert date_to_str('01.01.2001') == 'первое января 2001 года'


def test_separator():
    assert separator(5) == '*****'


def test_copy_file_or_directory():
    copy_file_or_directory('test_filemanager.py', 'copy_test_filemanager.py')
    os.remove('copy_test_filemanager.py')


def test_author_info():
    assert author_info() == 'Leonid Orlov'