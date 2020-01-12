def get_text_diff(d1, d2, data):
    text = '{\n'
    for v in data['add']:
        text += get_print_data(v, d2[v], '+')
        text += '\n'
    for v in data['removed']:
        text += get_print_data(v, d1[v], '-')
        text += '\n'
    for v in data['same']:
        text += f' {get_print_data(v, d1[v])}'
        text += '\n'
    for v1 in data['modified']:
        if isinstance(data['modified'][v1], dict):
            text += 3 * ' '
            text += f'{v1}:\n'
            text += 3 * ' '
            text += get_text_diff(d1[v1], d2[v1], data['modified'][v1])
        else:
            text += 3 * ' '
            text += get_print_data(v1, d2[v1], '+')
            text += '\n'
            text += 3 * ' '
            text += get_print_data(v1, d1[v1], '-')
            text += "\n"
            text += '}\n'
            return text
    text += '}\n'
    return text


def get_print_data(key, value, option=''):
    text = ''
    text += 3 * ' '
    if isinstance(value, bool):
        value = str(value).lower()
    text += f'{option} {key}: ' + f'{value}'
    return text


