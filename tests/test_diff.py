from gendiff.gendiff import generate_diff
from tests.fixtures.test_result import FLOAT_RES


def test_float_json_file():
    first_file = 'tests/fixtures/json/first.json'
    second_file = 'tests/fixtures/json/second.json'
    res = FLOAT_RES
    assert res == generate_diff(first_file, second_file)


def test_float_yaml_file():
    first_file = 'tests/fixtures/yaml/after.yml'
    second_file = 'tests/fixtures/yaml/before.yml'
    res = FLOAT_RES
    assert res == generate_diff(first_file, second_file)