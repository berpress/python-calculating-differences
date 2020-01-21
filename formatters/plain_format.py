def get_plain_diff(d1, d2, data):
    text = ''
    patch = ''
    print(data)
    if len(data['add']) > 0:
        text_add = ""
        for item in data['add']:
            patch += item
            text_add += "'{0}' was add with value:".format(item)
            if isinstance(d2[item], dict):
                text_add += ' complex value'
            else:
                text_add += " '{0}'".format(d2[item])
            text += "Property {0} \n".format(text_add)
            text_add = ''
    if len(data['removed']) > 0:
        text_add = ""
        for item in data['removed']:
            text_add += "'{0}' was removed".format(item)
        text += "Property {0} \n".format(text_add)
    if len(data['modified']) > 0:
        text_add = ""
        for key in data['modified']:
            item = data['modified'][key]
            patch += key
            if isinstance(item, dict):
                text_add += get_plain_diff(d1[key], d2[key], item)
            else:
                text_add += "Property '{0}' was changed.".format(patch)
                text_add += ' From {0} to {1}'.format(item[0], item[1])
        text += "{0} \n".format(text_add)
    return text


# def print_tree(t, path=()):
#     for k, v in t.items():
#         new_path = path + (k,)
#         if isinstance(v, dict):
#             print_tree(v, path=new_path)
#         else:
#             return (
#                 '{}: {}'.format(
#                     '.'.join(new_path),
#                     v,
#                 )
#             )

def print_tree(t, path=()):
    for k, v in t.items():
        new_path = path + (k,)
        if isinstance(v, dict):
            print_tree(v, path=new_path)
        else:
            print(
                '{}: {}'.format(
                    '.'.join(new_path),
                    v,
                )
            )

# def get_print_data(data, d, description):
#     text = ''
#     if isinstance(data['add'], dict):
#         pass
#     else:
#         for item in data['add']:
#             text += " '{0}' {1}".format(item, description)
#             if isinstance(d[item], dict):
#                 text += 'complex value'
#             else:
#                 text += " '{0}'".format(d[item])
#     text += "\n"
#     return text




