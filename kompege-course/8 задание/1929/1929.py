from itertools import *
c=0
for i in permutations('дейкстра', 6):
    if i.count('й') == 1:
        if (i[-1] != 'й') and (i[i.index('й')+1] in 'дйкстр'):
            c+=1
            print(''.join(i))
print(c)