# TODO здесь писать код

from math import prod
 
floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]
 
numbers__ = prod(numbers) 
floats__ = list(map(lambda elem: round(elem ** 3, 3), floats))
names__ = list(filter(lambda name: len(name) > 4, names))
 
print(floats__,'\n',numbers__,'\n',names__)