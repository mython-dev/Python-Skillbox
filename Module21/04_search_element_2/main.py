# TODO здесь писать код

from math import inf
 

 
def foo(d, depth=1):
    if depth > max_depth:
        return


    for key in d:
        if key == find:
            return d[key]
        elif isinstance(d[key], dict):
            result = foo(d[key], depth + 1)
            if result:
                return result
 

 
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
 

ishem = input('Какой ключ ишем? ')
 
find = ishem
max_depth = inf
print(foo(site))
find = ishem
max_depth = 1
print(foo(site))