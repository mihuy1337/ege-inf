from itertools import *
count = 0
for i in product('WXYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'WXYZ'):
    print(''.join(i))
    count+=1

print(count)