from formatters.plain_format import get_plain_diff
from gendiff.gendiff import generate_diff
from tests.fixtures.test_result import FLOAT_RES, NOT_FLOAT_RES, NOT_FLOAT_YAML


def test_float_json_file():
    first_file = 'fixtures/json/first.json'
    second_file = 'fixtures/json/second.json'
    diff = generate_diff(first_file, second_file)
    assert FLOAT_RES == get_plain_diff(diff)


def test_float_yaml_file():
    first_file = 'tests/fixtures/yaml/after.yml'
    second_file = 'tests/fixtures/yaml/before.yml'
    assert FLOAT_RES == generate_diff(first_file, second_file)


def test_not_float_json_file():
    first_file = 'tests/fixtures/json/h_first.json'
    second_file = 'tests/fixtures/json/h_second.json'
    assert NOT_FLOAT_RES == generate_diff(first_file, second_file)


def test_not_float_yaml_file():
    first_file = 'tests/fixtures/yaml/before_nested.yml'
    second_file = 'tests/fixtures/yaml/after_nested.yml'
    assert NOT_FLOAT_YAML == generate_diff(first_file, second_file)
