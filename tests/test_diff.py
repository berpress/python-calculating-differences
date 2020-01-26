from formatters.plain_format import get_plain_diff
from formatters.print_format import get_dict_diff
from gendiff.gendiff import generate_diff
from tests.fixtures.test_diff import FLOAT_RES, NOT_FLOAT_RES, NOT_FLOAT_YAML


def test_flat_json_file():
    first_file = 'tests/fixtures/json/json_file/first.json'
    second_file = 'tests/fixtures/json/json_file/second.json'
    diff = generate_diff(first_file, second_file)
    f = open('fixtures/json/json_result/flat_diff.txt')
    data_file = f.read()
    assert data_file == get_dict_diff(diff)

#
# def test_float_yaml_file():
#     first_file = 'tests/fixtures/yaml/after.yml'
#     second_file = 'tests/fixtures/yaml/before.yml'
#     assert FLOAT_RES == generate_diff(first_file, second_file)


# def test_nested_flat_json_file():
#     first_file = 'fixtures/json/json_file/h_first.json'
#     second_file = 'fixtures/json/json_file/h_second.json'
#     diff = generate_diff(first_file, second_file)
#     f = open('fixtures/json/json_result/flat_nested_diff.txt')
#     data_file = f.read()
#     assert data_file == get_dict_diff(diff)


# def test_not_float_yaml_file():
#     first_file = 'tests/fixtures/yaml/before_nested.yml'
#     second_file = 'tests/fixtures/yaml/after_nested.yml'
#     assert NOT_FLOAT_YAML == generate_diff(first_file, second_file)
