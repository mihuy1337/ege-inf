from itertools import *
count=0
for i in product('вишня', repeat=6):
    if (i[0] != 'ш') and (i[-1] not in 'ия') and (i.count('в') <= 1):
        count+=1
print(count)