#a = [1, 5, 3]
#b = [1, 5, 1, 5]
#c = [1, 3, 1, 5, 3, 3]
#for i in b:
    #a.append(i)
#t = 0
#for i in a:
    #if i == 5:
        t += 1
#print(t)
#d = []
#for i in a:
    #if i != 5:
        #d.append(i)
#for i in c:
    #d.append(i)
#t = 0
#for i in d:
    #if i == 3:
        #t += 1
#print(t)
#print(d)

# TODO переписать программу

# Задача 1. Страшный код

one = [1, 5, 3]
two = [1, 5, 1, 5]
three = [1, 3, 1, 5, 3, 3]

one.extend(two)
number_of_digits_five = one.count(5)
print(number_of_digits_five)
for _ in range(number_of_digits_five):
    one.remove(5)

one.extend(three)
number_of_digits_three = one.count(3)
print(number_of_digits_three)
print(one)