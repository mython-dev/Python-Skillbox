# TODO здесь писать код


def checking_array(checking_list):
    return [i for i, v in enumerate(checking_list)if checking_num(i)]

k= 0

def checking_num(i_num):


    for i in range(2, i_num // 2 + 1):
        if i_num % i == 0:
            k = k + 1
        if k <= 0:
            return True
        else:
            return False

s = input('Введите текст: ').split()

i_list = checking_array(s)
print(i_list)