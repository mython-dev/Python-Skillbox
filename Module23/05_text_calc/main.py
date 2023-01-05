# TODO здесь писать код


def num_calc():

    num = [ ]
    with open('calc.txt', 'r') as file:
        for line in file.readlines():
            try:
                num.append(eval(line))
            except:
                if input('Обнаружена ошибка:' + line + 'Хотите исправить? ') == 'да':
                    line = input('Введите исправленную строку: ')


            print(sum(num))

num_calc()