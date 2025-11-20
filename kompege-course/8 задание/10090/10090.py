from itertools import *
count = 0
for i in permutations('01234567', 5):
    if i[0] != '0' and '1' not in i:
        s = ''.join(i).replace('0', 'ч')\
        .replace('2', 'ч')\
        .replace('4', 'ч')\
        .replace('6', 'ч')\
        .replace('1', 'н')\
        .replace('3', 'н')\
        .replace('5', 'н')\
        .replace('7', 'н')
        if ('нн' not in s) and ('чч' not in s):
            print(s, ''.join(i))
            count+=1
print(count)