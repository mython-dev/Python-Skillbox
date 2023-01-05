# TODO здесь писать код


def can_make_pal(stri):
    d={}
    for a in stri:
        if d.get(a) is None:
            d[a]=1
        else:
            d[a]+=1
    n=len(d)
    e=0
    for a in d.values():
        if a%2==0: 
            e+=1
    return e==n or e==n-1
