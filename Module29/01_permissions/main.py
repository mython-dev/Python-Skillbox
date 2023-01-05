# TODO здесь писать код


import functools
from typing import Callable


def check_permission(user_name: str) -> Callable:
    """Декоратор для проверки прав пользователя.
    Возвращает ошибку или право доступа к функции"""


    ADMIN = ['admin']

    def check_permission_2(func: Callable) -> Callable:

        @functools.wraps(func)
    
        def wrapped(*args, **kwargs) -> Callable:
            try:
                if user_name in ADMIN:
                    return func(*args, **kwargs)
            except:
                print('У пользователя недостаточно прав, чтобы выполнить функцию {func_name}'.format(
        func_name=func.__name__))

        return wrapped

    return check_permission_2


@check_permission('user')
def delete_site():
    print('Удаляем сайт')


@check_permission('admin')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

