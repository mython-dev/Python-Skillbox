# TODO здесь писать код

import os
from collections.abc import Iterable
 
 
def strings_count(directory: str) -> Iterable[tuple]:
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            if os.path.join(root, file).endswith('.py'):
                curr_file = open(os.path.join(root, file), 'r', encoding='utf-8')
                for line in curr_file.readlines():
                    if line == '\n' or line.startswith('"') or line.startswith('#'):
                        continue
                    else:
                        count += 1
                yield os.path.join(root, file), count
 
 
for element in strings_count('..'):
    print('Файл "{}": строк кода - {}'.format(element[0], element[1]))