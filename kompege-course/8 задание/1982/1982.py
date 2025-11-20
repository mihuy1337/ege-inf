from itertools import *
count = 0
for i in product('ЛОДКА', repeat=4):
    if i.count('О') >= 2:
        print(''.join(i))
        count+=1

print(count)