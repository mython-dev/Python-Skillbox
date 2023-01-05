# TODO здесь писать код

def f(x):
    for a in x:
        try:
            b = int(a)
            if b != a: return x
        except: return x
    a = list(x)
    a.sort()
    return tuple(a)
u= (6, 5, 4, 3, 2, 1)
v = (1, 2, 3.14, 4, 5, 6)
w = (4, '*', -1)
print(*f(u)); print(*f(v)); print(*f(w))