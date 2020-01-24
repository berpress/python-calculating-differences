def get_plain_diff(data):
    tt = get_diff(data)
    f = open("plain-h.txt", "w")
    f.write(tt)
    f.close()
    return get_diff(data)


def get_diff(t, path=()):
    text = ""
    for k, v in t.items():
        new_path = path + (k,)
        if isinstance(v, dict):
            text += get_diff(v, path=new_path)
        else:
            if v[0] != 'same':
                path_str = '{}'.format('.'.join(new_path))
                text += "Property {}".format(path_str)
                if v[0] == 'add':
                    text += " was added with value: "
                    if isinstance(v[1], dict):
                        text += "'complex value'"
                    else:
                        text += f"{v[1]}"
                if v[0] == 'remove':
                    text += " was removed"
                if v[0] == 'modified':
                    text += " was changed. From '{}' to '{}'".format(v[1],
                                                                     v[2])
                text += '\n'
    return text




