from itertools import *

c=0

for a in permutations('вайфу', 4):
    i = ''.join(a)
    if (i[0] != 'й') and ('фв' not in i) and ('вф' not in i):
        print(''.join(i))
        c += 1
print(c)