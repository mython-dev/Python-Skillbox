# TODO здесь писать код



import functools

def singleton(cls):
    """ Декоратор класса. Превращает класс в синглтон (может иметь только один инстанс) """
    functools.wraps(cls)

    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance  = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None

    return wrapper_singleton


@singleton

class Exapmle:
    pass

my_obj = Exapmle()

my_another_obj = Exapmle()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)



