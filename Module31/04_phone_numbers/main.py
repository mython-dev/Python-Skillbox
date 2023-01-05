# TODO здесь писать код

import re

string = ['9999999999', '999999-999', '99999x9999']

true = 'всё в порядке.'

false = 'не подходит.'

if len(string[0]) == 10:
    print('Первый номер:', true)
else:
    print('Первый номер:', false)

if re.findall(r'[8-9]\d{9}', str(string[1])):
    print('Второй номер:', true)
else:
    print('Второй номер:', false)

if string[2].isdigit() == True:
    print('Третий номер:',true)
else:
    print('Третий номер:', false)
