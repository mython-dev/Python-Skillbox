# TODO здесь писать код


import os
 
 
def save_files(string):
    path = str(input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): '))
    name_file = str(input('Введите имя файла: '))
    r_path = path.replace(" ", "/")
    real_path = os.path.join(r_path, name_file)
    path = str('/Users/' + real_path) # <--  mac os
    check_file = os.path.exists(path)
    if check_file:
        print('Файл с таким именем уже существует!')
        ans_q = input('Вы действительно хотите перезаписать файл? ').lower()
        if ans_q == 'да' or ans_q == 'yes':
            f = open(path, 'w')
            f.write(string)
            print('Файл успешно перезаписан!')

    else:
        f = open(path, 'w')
        f.write(string)
        print('Файл успешно сохранён!')
 
 
save_files(str(input('Введите строку: ')))