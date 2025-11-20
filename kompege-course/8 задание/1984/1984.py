from itertools import *
count = 0
for i in permutations('ИГРОК'):
    stroke = ''.join(i)
    if stroke[0] != 'К' and 'РОК' not in stroke:
        count+=1
        print(stroke)
print(count)