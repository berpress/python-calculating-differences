FLOAT_RES = (
    {'add': {'verbose'}, 'removed': {'proxy'},
     'modified': {'timeout': (50, 20)}, 'same': {'host'}}
)

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
