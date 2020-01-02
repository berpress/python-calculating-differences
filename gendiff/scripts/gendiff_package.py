import argparse

from formatters.float import get_format
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    dict_1, dict_2, diff = generate_diff(args.first_file, args.second_file)
    print(get_format(dict_1, dict_2, diff))


if __name__ == '__main__':
    main()
