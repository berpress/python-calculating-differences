def get_plain_diff(data):
    return get_diff(data)


def get_diff(t, path=()):
    text = ""
    for k, v in t.items():
        new_path = path + (k,)
        if isinstance(v, dict):
            text = '{0}{1}'.format(text, get_diff(v, path=new_path))
        else:
            if len(v) == 2:
                status, value = v
            else:
                status, value, value_2 = v
            if status != 'same':
                path_str = '{}'.format('.'.join(new_path))
                text += "Property {}".format(path_str)
                if status == 'add':
                    text += " was added with value: "
                    if isinstance(value, dict):
                        text += "'complex value'"
                    else:
                        text += f"{value}"
                if status == 'remove':
                    text += " was removed"
                if status == 'modified':
                    text += " was changed. From '{}' to '{}'".format(value,
                                                                     value_2)
                text += '\n'
    return text




