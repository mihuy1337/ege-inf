from itertools import *
k=0
for num in product('0123456', repeat=6):
    num = ''.join(num)
    if num[0] in '246' and num.count('5')==2:
        k+=1
        print(k, num)
