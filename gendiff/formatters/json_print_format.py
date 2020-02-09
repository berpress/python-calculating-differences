def get_dict_diff(diff):
    text = "{"
    text += get_diff(diff)
    text += "}"
    return text


ADDED = '+'
SAME = ' '
REMOVED = '-'


def get_diff(diff, space=" "):
    diff_list_text = ['\n']
    for key, value in diff.items():
        item = diff[key]
        if isinstance(item, dict):
            diff_lines = get_diff(item, space * 2)
            diff_text = \
                '{0}{1}: {{{2}{3}}}{4}'.format(space, key, diff_lines, space,
                                               '\n')
            diff_list_text.append(diff_text)
        else:
            diff_property = item[0]
            if diff_property == 'add':
                add_lines = get_diff_format(ADDED, key, item[1], space)
                diff_list_text.append(add_lines)
            elif diff_property == 'same':
                same_lines = get_diff_format(SAME, key, item[1], space)
                diff_list_text.append(same_lines)
            elif diff_property == 'remove':
                remove_lines = get_diff_format(REMOVED, key, item[1], space)
                diff_list_text.append(remove_lines)
            elif diff_property == 'modified':
                before, after = item[1:]
                before_lines = f"{space}+{key}: {before}"
                after_lines = f"{space}-{key}: {after}"
                diff_list_text.append(before_lines)
                diff_list_text.append('\n')
                diff_list_text.append(after_lines)
                diff_list_text.append('\n')
    return ''.join(diff_list_text)


def get_diff_format(status, key, item, space):
    list_text = []
    if isinstance(item, dict):
        k = list(item.keys())[0]
        diff_text = "{0}{1}{2}: ".format(space, status, key)
        list_text.append(diff_text)
        list_text.append('{\n')
        list_text.append("{0}{1}: {2}\n".format(space * 2, k, item[k]))
        list_text.append(space)
        list_text.append('}')
    else:
        list_text.append(f"{space}{status}{key}: {item}")
    list_text.append('\n')
    return "".join(list_text)
