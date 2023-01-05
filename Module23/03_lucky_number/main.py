# TODO здесь писать код


from random import random

file = open('out_file.txt', 'w')

sum = 0

while True:
    n = float(input('Введите число: '))

    if random() < 0.13:
        print('Неудача!')
        break

    sum += n
    file.write(str(n) + '\n')

    if sum >= 777:
        print('успех!')
        break
