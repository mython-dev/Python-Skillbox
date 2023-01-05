# TODO здесь писать код

ls = input('Введите текст: ').split(' ')
max_len = max([len(x) for x in ls])
print([x for x in ls if len(x) == max_len])
