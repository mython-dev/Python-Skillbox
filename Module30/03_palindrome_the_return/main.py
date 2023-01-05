# TODO здесь писать код


from collections import Counter
 
can_be_poly = lambda s: len(s) % 2 == sum(x % 2 for x in Counter(s).values())

print(can_be_poly('abcba'), can_be_poly('abbbc'))
