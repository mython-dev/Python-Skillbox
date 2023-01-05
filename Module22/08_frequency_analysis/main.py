# TODO здесь писать код



import re
from collections import Counter
 
with open('text.txt') as infile,\
         open('text1.txt', 'w') as out:
    txt = infile.read()
    s = re.sub(r'[^\w\s]',' ',txt).split()
    words = [(v,k) for v, k in Counter(s).items()]
    words.sort(key = lambda x: (-x[1], x[0]))
    for w in words:
        print(*w, file = out)