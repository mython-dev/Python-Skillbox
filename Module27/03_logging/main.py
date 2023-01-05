# TODO здесь писать код

from datetime import *

def logging(func):
    def wrapper():
        try:
            print(f'{func.__name} - {func.__doc__}')
            func()
        except Exception as e:
            e = f'{datetime.now().strftime("%d.%m.%Y %H:%M: %S")} - {func.__name__} - {e}'
            with open('log.txt', 'a+', encoding='utf-8') as f:
                f.write(e)

    return wrapper

@logging

def test_func():
    print(Error)

test_func()