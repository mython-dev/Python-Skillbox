# TODO здесь писать код


import collections

text = input('Введите текст: ').lower()

vocablary = dict()

sym_dict = dict()

print('Оригинальный словарь частот: ')

for sym  in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

for i_sym in sorted(sym_dict.keys()):
    print(i_sym, ':', sym_dict[i_sym])

for letter , serial_num in collections.Counter(text).items():
    vocablary.setdefault(serial_num,[]).append(letter)

print('Инвертированный словарь частот: ')

for i_vocabulary in vocablary:
    print(i_vocabulary, vocablary[i_vocabulary])
