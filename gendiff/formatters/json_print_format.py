def get_dict_diff(diff):
    text = "{"
    text += get_diff(diff)
    text += "}"
    return text


def get_diff(diff,  space=" "):
    diff_text = ''
    diff_text += "\n"
    for key, value in diff.items():
        item = diff[key]
        if isinstance(item, dict):
            diff_text += "{0}{1}: ".format(space, key)
            diff_text += "{"
            diff_text += get_diff(item, space * 2)
            diff_text += space
            diff_text += "}"
            diff_text += '\n'
        else:
            diff_property = item[0]
            if diff_property == 'add':
                diff_text += get_diff_format("+", key, item[1], space)
            elif diff_property == 'same':
                diff_text += get_diff_format(" ", key, item[1], space)
            elif diff_property == 'remove':
                diff_text += get_diff_format("-", key, item[1], space)
            elif diff_property == 'modified':
                before, after = item[1:]
                diff_text += f"{space}+{key}: {before}"
                diff_text += '\n'
                diff_text += f"{space}-{key}: {after}"
                diff_text += '\n'
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
