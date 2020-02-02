def get_dict_diff(diff):
    text = "{"
    text += get_diff(diff)
    text += "}"
    return text


def get_diff(diff,  space=" "):
    text = ''
    text += "\n"
    for key, value in diff.items():
        item = diff[key]
        if isinstance(item, dict):
            text += "{0}{1}: ".format(space, key)
            text += "{"
            text += get_diff(item, space * 2)
            text += space
            text += "}"
            text += '\n'
        else:
            diff_property = item[0]
            if diff_property == 'add':
                text += get_diff_format("+", key, item[1], space)
            elif diff_property == 'same':
                text += get_diff_format(" ", key, item[1], space)
            elif diff_property == 'remove':
                text += get_diff_format("-", key, item[1], space)
            elif diff_property == 'modified':
                before, after = item[1:]
                text += f"{space}+{key}: {before}"
                text += '\n'
                text += f"{space}-{key}: {after}"
                text += '\n'
    return text


def get_diff_format(status, key, item, space):
    if isinstance(item, dict):
        k = list(item.keys())[0]
        text = "{0}{1}{2}: ".format(space, status, key)
        text += '{\n'
        text += "{0}{1}: {2}\n".format(space * 2, k, item[k])
        text += space
        text += '}'
    else:
        text = f"{space}{status}{key}: {item}"
    text += '\n'
    return text
