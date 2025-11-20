from itertools import *
count=0
for i in product('AB123', repeat=8):
    s = ''.join(i).replace('B', 'A')
    if s.count('A') == 2:
        print(s)
        count+=1

print(count)