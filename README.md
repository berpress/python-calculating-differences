[![Build Status](https://travis-ci.org/berpress/python-project-lvl2.svg?branch=master)](https://travis-ci.org/berpress/python-project-lvl2)
[![Maintainability](https://api.codeclimate.com/v1/badges/af20f096ba6001823e65/maintainability)](https://codeclimate.com/github/berpress/python-project-lvl2/maintainability)


### Вычислитель отличий

1. Установка 
``` sh
python3 -m pip install --user --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple litovsky-get-diff-file

```
2. Использование

    Утилита принимает на вход два обязательных парамметра - пути к файлам (first_file, second_file). Результат сравнения файлов может выводиться в разных форматах: например, plain ("плоский"), json ("JSON-подобный формат") или в json (сырые данные). На вход принимаются json и yaml файлы.
    По умолчанию разность файлов выводится в JSON-подобный формат, например 
    ``` sh
    gendiff first.json second.json
    ```
    Результат 
    ``` sh
    {
    host: hexlet.io
    + timeout: 20
    - timeout: 50
    - proxy: 123.234.53.22
    + verbose: true
    }
    ```
    Для вывода в плоский формат необходимо указать параметр --format plain
     ``` sh
    gendiff --format plain before.json after.json
    ```
    Результат 
    ``` sh
    Property 'common.setting2' was removed
    Property 'common.setting6' was removed
    Property 'common.setting4' was added with value: 'blah blah'
    Property 'common.setting5' was added with value: 'complex value'
    Property 'group1.baz' was changed. From 'bas' to 'bars'
    Property 'group2' was removed
    Property 'group3' was added with value: 'complex value'
    ```
    Для вывода в json формат необходимо указать параметр --format json
     ``` sh
    gendiff --format json before.json after.json
    ```
    Результат 
    ``` sh
    ('{"host": ["same", "hexlet.io"], "proxy": ["remove", "123.234.53.22"], '
    '"timeout": ["modified", 50, 20], "verbose": ["add", true]}')
    ```
