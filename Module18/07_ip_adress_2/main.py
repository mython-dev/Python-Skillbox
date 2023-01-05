# TODO здесь писать код


def msg(m,s):
    if m==0 : return "IP-адрес корректен"
    if m==1 : return s+"не целое число"
    if m==2 : return "Адрес - это четыре числа, разделённые точками"

def fnk(t):
    if -1<int(t)<256: return 0
    if not t.isdigit(): return 1
    return 2

ls=input().split('.')
s=''
for s in ls:
    k=fnk(s)
    if k!=0 : break
print (msg(k,s))