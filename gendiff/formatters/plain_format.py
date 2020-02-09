def get_plain_diff(data):
    return get_diff(data)


def get_diff(t, path=()):
    diff_list_text = []
    for k, v in t.items():
        new_path = path + (k,)
        if isinstance(v, dict):
            diff_list_text.append(get_diff(v, path=new_path))
        else:
            if len(v) == 2:
                status, value = v
            else:
                status, value, value_2 = v
            if status != 'same':
                path_str = '{}'.format('.'.join(new_path))
                diff_list_text.append("Property {}".format(path_str))
                if status == 'add':
                    diff_list_text.append(" was added with value: ")
                    if isinstance(value, dict):
                        diff_list_text.append( "'complex value'")
                    else:
                        diff_list_text.append(str(value))
                if status == 'remove':
                    diff_list_text.append( " was removed")
                if status == 'modified':
                    diff_list_text.append(" was changed. From '{}' to '{}'"
                                     .format(value, value_2))
                diff_list_text.append('\n')
    return "".join(diff_list_text)




