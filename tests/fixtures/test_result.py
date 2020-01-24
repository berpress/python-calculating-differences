FLOAT_RES = "Property group3 was added with value: 'complex value\nProperty " \
            "group2 was removed\nProperty group1.baz was changed. From 'bas' " \
            "to 'bars'\nProperty common.setting4 was added with value: blah " \
            "blah\nProperty common.setting5 was added with value: " \
            "'complex value'\nProperty common.setting6 was removed\nProperty " \
            "common.setting2 was removed"

NOT_FLOAT_RES = (
    {'add': {'group3'}, 'removed': {'group2'}, 'modified': {
        'group1': {'add': set(), 'removed': set(),
                   'modified': {'baz': ('bas', 'bars')}, 'same': {'foo'}},
        'common': {'add': set(), 'removed': set(), 'modified': {
            'setting5': {'add': set(), 'removed': set(),
                         'modified': {'key': ('value', 'value5')},
                         'same': set()}}, 'same': {'setting1'}}},
     'same': set()}
)

NOT_FLOAT_YAML = (
    {'add': set(), 'removed': set(), 'modified': {
        'test1': {'add': set(), 'removed': set(), 'modified': {
            'a': {'add': set(), 'removed': set(), 'modified': {
                'a1': {'add': set(), 'removed': set(), 'modified': {
                    'a2': {'add': set(), 'removed': set(),
                           'modified': {'c3': (0, 2), 'b3': (4, 0)},
                           'same': {'a3'}}}, 'same': set()}}, 'same': set()}},
                  'same': set()}}, 'same': set()}

)
