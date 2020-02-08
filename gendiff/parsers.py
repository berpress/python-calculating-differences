import json
import os
import yaml

ADDED = "add"
SAME = "same"
REMOVED = "remove"


def get_data_file(path):
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    _, file_type = os.path.splitext(path)
    if file_type == '.json':
        return json.load(open(path))
    elif file_type == '.yml':
        return yaml.load(open(path), Loader=yaml.Loader)
    else:
        raise Exception("Invalid format, run --help!")


def get_diff_data(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    intersect_keys = d1_keys & d2_keys
    removed = d1_keys - d2_keys
    added = d2_keys - d1_keys
    modified_dict = \
        {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    diff = {}

    for source, keys, status in (
            (d2, added, ADDED),
            (d1, same, SAME),
            (d1, removed, REMOVED),
    ):
        for key in keys:
            diff[key] = (status, source[key])
    for key in modified_dict:
        value_1, value_2 = modified_dict[key]
        if isinstance(value_1, dict) and isinstance(value_2, dict):
            diff[key] = get_diff_data(value_1, value_2)
        else:
            diff[key] = ('modified', value_1, value_2)
    return dict(sorted(diff.items()))
