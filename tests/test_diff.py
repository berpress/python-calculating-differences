import pytest
from collections import OrderedDict

from gendiff.formatters.json_format import get_json_diff
from gendiff.formatters.plain_format import get_plain_diff
from gendiff.formatters.json_print_format import get_dict_diff
from gendiff.gendiff import generate_diff
import os

TEST_FILES = 'tests/fixtures/files/'
RESULT_FILE = 'tests/fixtures/results/'


def sort_dict(item: dict):
    return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in
            sorted(item.items())}


@pytest.mark.parametrize('file_type', [
    'json',
    'yml',
])
def test_flat_diff(file_type):
    first_file_path = os.path.join(TEST_FILES, f'first.{file_type}')
    second_file_path = os.path.join(TEST_FILES, f'second.{file_type}')
    diff = generate_diff(first_file_path, second_file_path)
    diff = OrderedDict(sorted(diff.items()))
    with open(os.path.join(RESULT_FILE, "flat_diff.txt")) as f:
        data_file = f.read()
    assert data_file == get_dict_diff(diff), "Данные не совпадают"


@pytest.mark.parametrize('file_type', [
    'json',
    'yml',
])
def test_flat_text_diff(file_type):
    first_file_path = os.path.join(TEST_FILES, f'first.{file_type}')
    second_file_path = os.path.join(TEST_FILES, f'second.{file_type}')
    diff = generate_diff(first_file_path, second_file_path)
    diff = sort_dict(diff)
    with open(os.path.join(RESULT_FILE, "flat_text_diff.txt")) as f:
        data_file = f.read()
    assert data_file == get_plain_diff(diff), "Данные не совпадают"


@pytest.mark.parametrize('file_type', [
    'json',
    'yml',
])
def test_nested_flat_file(file_type):
    first_file_path = os.path.join(TEST_FILES, f'first_nested.{file_type}')
    second_file_path = os.path.join(TEST_FILES, f'second_nested.{file_type}')
    diff = generate_diff(first_file_path, second_file_path)
    diff = sort_dict(diff)
    with open(os.path.join(RESULT_FILE, "flat_nested_diff.txt")) as f:
        data_file = f.read()
    assert data_file == get_dict_diff(diff), "Данные не совпадают"


@pytest.mark.parametrize('file_type', [
    'json',
    'yml',
])
def test_nested_text_flat_file(file_type):
    first_file_path = os.path.join(TEST_FILES, f'first_nested.{file_type}')
    second_file_path = os.path.join(TEST_FILES, f'second_nested.{file_type}')
    diff = generate_diff(first_file_path, second_file_path)
    diff = sort_dict(diff)
    with open(os.path.join(RESULT_FILE, "flat_text_nested_diff.txt")) as f:
        data_file = f.read()
    assert data_file == get_plain_diff(diff), "Данные не совпадают"


@pytest.mark.parametrize('file_type', [
    'json',
    'yml',
])
def test_nested_json_file(file_type):
    first_file_path = os.path.join(TEST_FILES, f'first_nested.{file_type}')
    second_file_path = os.path.join(TEST_FILES, f'second_nested.{file_type}')
    diff = generate_diff(first_file_path, second_file_path)
    diff = sort_dict(diff)
    with open(os.path.join(RESULT_FILE, "json_nested")) as f:
        data_file = f.read()
    assert data_file == get_json_diff(diff), "Данные не совпадают"
