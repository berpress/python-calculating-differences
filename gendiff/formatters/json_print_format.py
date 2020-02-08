def get_dict_diff(diff):
    text = "{"
    text += get_diff(diff)
    text += "}"
    return text


ADDED = '+'
SAME = ' '
REMOVED = '-'


def get_diff(diff, space=" "):
    diff_text = '{0}{1}'.format("", '\n')
    for key, value in diff.items():
        item = diff[key]
        if isinstance(item, dict):
            diff_lines = get_diff(item, space * 2)
            diff_text = \
                '{0}{1}{2}: {{{3}{4}}}{5}'.format(
                    diff_text, space, key, diff_lines, space, '\n')
        else:
            diff_property = item[0]
            if diff_property == 'add':
                add_lines = get_diff_format(ADDED, key, item[1], space)
                diff_text = '{0}{1}'.format(diff_text, add_lines)
            elif diff_property == 'same':
                same_lines = get_diff_format(SAME, key, item[1], space)
                diff_text = '{}{}'.format(diff_text, same_lines)
            elif diff_property == 'remove':
                remove_lines = get_diff_format(REMOVED, key, item[1], space)
                diff_text = '{0}{1}'.format(diff_text, remove_lines)
            elif diff_property == 'modified':
                before, after = item[1:]
                before_lines = f"{space}+{key}: {before}"
                after_lines = f"{space}-{key}: {after}"
                diff_text = '{0}{1}{2}{3}{4}'.format(diff_text,
                                                     before_lines,
                                                     '\n', after_lines, '\n')
    return diff_text


def get_diff_format(status, key, item, space):
    if isinstance(item, dict):
        k = list(item.keys())[0]
        diff_text = "{0}{1}{2}: ".format(space, status, key)
        diff_text += '{\n'
        diff_text += "{0}{1}: {2}\n".format(space * 2, k, item[k])
        diff_text += space
        diff_text += '}'
    else:
        diff_text = f"{space}{status}{key}: {item}"
    diff_text += '\n'
    return diff_text
