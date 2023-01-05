# TODO здесь писать код

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
 
    func.__invocation_count__ = 0
 
    def wrapper(*args, **kwargs):
        func.__invocation_count__ += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, func.__invocation_count__))
        return res
    return wrapper
