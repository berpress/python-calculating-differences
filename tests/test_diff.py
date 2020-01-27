from formatters.plain_format import get_plain_diff
from formatters.print_format import get_dict_diff
from gendiff.gendiff import generate_diff
import os

TEST_FILES_JSON = 'tests/fixtures/json/json_file/'
TEST_FILES_YAML = 'tests/fixtures/json/yaml_file/'


def test_flat_json_file():
    first_file = os.path.join(TEST_FILES_JSON, "first.json")
    second_file = os.path.join(TEST_FILES_JSON, "second.json")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/json/json_result/flat_diff.txt')
    data_file = f.read()
    assert data_file == get_dict_diff(diff)


def test_text_json_file():
    first_file = os.path.join(TEST_FILES_JSON, "first.json")
    second_file = os.path.join(TEST_FILES_JSON, "second.json")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/json/json_result/flat_text_diff.txt')
    data_file = f.read()
    assert data_file == get_plain_diff(diff)


# def test_float_yaml_file():
#     first_file = 'tests/fixtures/yaml/after.yml'
#     second_file = 'tests/fixtures/yaml/before.yml'
#     assert FLOAT_RES == generate_diff(first_file, second_file)


def test_nested_flat_json_file():
    first_file = os.path.join(TEST_FILES_JSON, "h_first.json")
    second_file = os.path.join(TEST_FILES_JSON, "h_second.json")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/json/json_result/flat_nested_diff.txt')
    data_file = f.read()
    assert data_file == get_dict_diff(diff)


def test_nested_text_json_file():
    first_file = os.path.join(TEST_FILES_JSON, "h_first.json")
    second_file = os.path.join(TEST_FILES_JSON, "h_second.json")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/json/json_result/flat_text_nested_diff.txt')
    data_file = f.read()
    assert data_file == get_plain_diff(diff)

# def test_not_float_yaml_file():
#     first_file = 'tests/fixtures/yaml/before_nested.yml'
#     second_file = 'tests/fixtures/yaml/after_nested.yml'
#     assert NOT_FLOAT_YAML == generate_diff(first_file, second_file)
