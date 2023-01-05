# TODO здесь писать код

import re

numbers_txt = open('numbers.txt', 'r')
answer_txt = open('answer.txt', 'a')
summ = 0

numbers = numbers_txt.read() 
numbers = re.findall(r'[+-]?\d+', numbers) 
numbers = [int(x) for x in numbers]

for x in numbers:
    summ += x

answer_txt.write(str(summ))
numbers_txt.close()
answer_txt.close()