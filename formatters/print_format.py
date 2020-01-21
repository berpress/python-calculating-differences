def get_text_diff(diff):
    text = '{\n'
    space_count = 2
    for key, value in diff.items():
        item = diff[key]
        space = " " * space_count
        if isinstance(item, dict):
            text += "{0}{1}: ".format(space, key)
            text += get_text_diff(item)
        else:
            diff_property = item[0]
            if diff_property == 'add':
                text += get_text_dict("+", key, item[1], space)
            elif diff_property == 'same':
                text += get_text_dict(" ", key, item[1], space)
            elif diff_property == 'remove':
                text += get_text_dict("-", key, item[1], space)
            elif diff_property == 'modified':
                before, after = item[1:]
                text += f"{space} +{key}: {before}"
                text += '\n'
                text += f"{space} -{key}: {after}"
                text += '\n'
            text += space
    text += '}\n'
    return text


def get_text_dict(status, key, item, space):
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
