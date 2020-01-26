import argparse

from formatters.plain_format import get_plain_diff
from formatters.print_format import get_dict_diff
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    if args.format == 'plain':
        tt = get_plain_diff(diff)
        f = open("../../tests/fixtures/json/json_result/flat_text_diff.txt",
                 "w")
        f.write(tt)
        f.close()
        print(get_plain_diff(diff))

    else:
        print(get_dict_diff(diff))


if __name__ == '__main__':
    main()
