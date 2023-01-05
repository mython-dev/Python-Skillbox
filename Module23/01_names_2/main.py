# TODO здесь писать код


with open('people.txt', encoding='UTF-8') as f:
    try:
        f = f.readlines()
        size = sum([len(i.strip()) for i in f])
        for x, i in enumerate(f, 1):
            if len(i.strip()) < 3:
                raise BaseException(f'Длина {x} строки меньше 3 символов')
    except BaseException as b:
        print(b)
    finally:
        print('Общее количество символов:', size)