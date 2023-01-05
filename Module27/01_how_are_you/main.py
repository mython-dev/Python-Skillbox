# TODO здесь писать код

def decorator_function(func):
    def how_are_you():
        print('Как дела? Хорошо.')
        print('А у меня не очень! Ладно, держи свою функцию. {}'.format(func))
        func()
    return how_are_you()

@decorator_function
def hello_world():
    print('<Тут что-то происходит...>')
hello_world()

