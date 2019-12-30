import json
import os
from pathlib import Path
import yaml


def get_data_file(path):
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    patch = Path('my_file.mp3').suffix
    if patch == '.json':
        return json.load(open(path))
    return yaml.load(open(path), Loader=yaml.Loader)


def get_diff_data(first_data, second_data):
    set_first = set(first_data.keys())
    set_second = set(second_data.keys())
    diff_left = set_first - set_second
    diff_right = set_second - set_first
    diff_intersection = set_first & set_second
    data = list(diff_left) + list(diff_right) + list(diff_intersection)
    data_dict = {}
    for item in data:
        if first_data.get(item) is None:
            data_dict[("+", item)] = second_data[item]
        elif first_data.get(item) == second_data.get(item):
            data_dict[('', item)] = second_data[item]
        elif second_data.get(item) is None:
            data_dict[("-", item)] = first_data[item]
        else:
            data_dict[("+", item)] = first_data[item]
            data_dict[("-", item)] = second_data[item]
    return data_dict
