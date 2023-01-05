# TODO здесь писать код


import os
 
path = r'/Users/mython'
size = 0
path, dirs, files = next(os.walk(path))
for f in files:
    fp = os.path.join(path, f)
    size += os.path.getsize(fp)

print(path) 
print('Размер каталога (в Кб): ', size / 1024)
print('Количество подкаталогов: ', len(dirs))
print('Количество файлов: ', len(files))