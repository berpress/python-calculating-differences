from gendiff.formatters.json_format import get_json_diff
from gendiff.formatters.plain_format import get_plain_diff
from gendiff.formatters.print_format import get_dict_diff
from gendiff.gendiff import generate_diff
import os

TEST_FILES_JSON = 'tests/fixtures/json/json_file/'
TEST_FILES_YAML = 'tests/fixtures/yaml/yaml_file/'


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


def test_flat_yaml_file():
    first_file = os.path.join(TEST_FILES_YAML, "after.yml")
    second_file = os.path.join(TEST_FILES_YAML, "before.yml")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/yaml/yaml_result/flat_diff.txt')
    data_file = f.read()
    assert data_file == get_dict_diff(diff)


def test_nested_flat_yaml_file():
    first_file = os.path.join(TEST_FILES_YAML, "after_nested.yml")
    second_file = os.path.join(TEST_FILES_YAML, "before_nested.yml")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/yaml/yaml_result/flat_nested_diff.txt')
    data_file = f.read()
    assert data_file == get_dict_diff(diff)


def test_text_yaml_file():
    first_file = os.path.join(TEST_FILES_YAML, "after.yml")
    second_file = os.path.join(TEST_FILES_YAML, "before.yml")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/yaml/yaml_result/flat_text_diff.txt')
    data_file = f.read()
    assert data_file == get_plain_diff(diff)


def test_nested_text_yaml_file():
    first_file = os.path.join(TEST_FILES_YAML, "after_nested.yml")
    second_file = os.path.join(TEST_FILES_YAML, "before_nested.yml")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/yaml/yaml_result/flat_text_nested_diff.txt')
    data_file = f.read()
    assert data_file == get_plain_diff(diff)


def test_nested_json_file():
    first_file = os.path.join(TEST_FILES_JSON, "h_first.json")
    second_file = os.path.join(TEST_FILES_JSON, "h_second.json")
    diff = generate_diff(first_file, second_file)
    f = open('tests/fixtures/json/print_json/json_nested')
    data_file = f.read()
    assert data_file == get_json_diff(diff)
