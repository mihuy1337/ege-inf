from itertools import *
count = 0
for i in product('ПУЛЯ', repeat=6):
    if i.count('У') == 2:
        count+=1
        print(''.join(i))
print(count)