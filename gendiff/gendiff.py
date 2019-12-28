import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(first_file, second_file):
    first = get_data_file(first_file)
    second = get_data_file(second_file)
    data_diff = get_diff_data(first, second)
    print(data_diff)


def get_data_file(path):
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    return json.load(open(path))


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
            data_dict[(None, item)] = second_data[item]
        elif second_data.get(item) is None:
            data_dict[("-", item)] = first_data[item]
        else:
            data_dict[("+", item)] = first_data[item]
            data_dict[("-", item)] = second_data[item]
    return data_dict


if __name__ == '__main__':
    main()
