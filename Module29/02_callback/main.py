# TODO здесь писать код



import functools
from typing import Callable, Dict, Any

app: Dict[str, callable] = dict()

def callback (route: str) -> Callable:
    """ Декоратор функции обратного вызова """

    def decorator_callback (func: Callable) -> Callable:
        app [route] = func

        @functools.wraps (func)
        
        def wrapper (*args, **kwargs) -> Any:

            return func(*args, **kwargs)
            
        return wrapper
    return decorator_callback
           
           
@callback('//')

def example() -> str:

    print("Пример функции, которая возвращает ответ сервера")
    return 'OK'


route = app.get('//')
if route:
    response = route
    print ('OTBeT:', response)
else:
    print ('Такого пути нет')
