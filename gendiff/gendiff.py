from gendiff.parsers import get_data_file, get_diff_data


def generate_diff(first_file, second_file):
    first = get_data_file(first_file)
    second = get_data_file(second_file)
    data_diff = get_diff_data(first, second)
    return first, second, data_diff
