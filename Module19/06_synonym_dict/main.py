# TODO здесь писать код


count_input = int(input('Введите количество пар слов: '))
synonims = dict()
for i in range(1, count_input + 1):
    couples = input(f'{i} пара: ').split(' - ')
for couple in couples[:1]:
    synonims[couple] = couples[1]
word = input('Введите слово: ').title()
for synonim in synonims:
    if word == synonim.title():
        print(f'Синоним: {synonims[synonim]}')
        break
    elif word == synonims[synonim].title():
        print(f'Синоним: {synonim}')
    break
else:
    print('Такого слова в словаре нет')