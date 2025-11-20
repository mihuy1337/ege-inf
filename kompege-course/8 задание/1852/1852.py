from itertools import *
c=0
for i in product('гепард', repeat=5):
    if (i.count('г')==1) and (i[0] != 'а') and (i[-1] != 'е'):
        c+=1
print(c)