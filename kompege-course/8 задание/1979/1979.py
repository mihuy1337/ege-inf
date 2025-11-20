from itertools import *
count = 0
for i in product('КРСЛ', 'КРЕСЛО', 'КРЕСЛО', 'ЕО'):
    count+=1

print(count)