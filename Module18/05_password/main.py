# TODO здесь писать код


while True:
    p = list(input('Придумайте пароль: '))
    l = len(p)
    z = len(list(filter(lambda x: x.isupper(),p )))
    c = len (list(filter(lambda x: x.isdigit(), p )))
    if (1 >= 8) and (z >= 1) and (c >= 3):
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадежный.')