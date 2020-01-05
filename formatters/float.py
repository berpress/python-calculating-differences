def get_format(d1, d2, data):
    string = '{\n'
    for v in data['add']:
        string += get_print_data(v, d2[v], '+')
        string += '\n'
    for v in data['removed']:
        string += get_print_data(v, d1[v], '-')
        string += '\n'
    for v in data['same']:
        string += f' {get_print_data(v, d1[v])}'
        string += '\n'
    for v1 in data['modified']:
        if isinstance(data['modified'][v1], dict):
            get_format(d1[v1], d2[v1], data['modified'][v1])
        else:
            string += get_print_data(v1, d2[v1], '+')
            string += '\n'
            string += get_print_data(v1, d1[v1], '-')
            string += '\n'
    string += '}\n'
    return string


def get_print_data(key, value, option=''):
    string = ''
    string += 3*' '
    if isinstance(value, bool):
        value = str(value).lower()
    string += f'{option} {key}: {value}'
    return string
