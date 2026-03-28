from itertools import *
from string import printable

k = 0
for w in product(printable[:7], repeat=5):
    w = ''.join(w)
    if w[0]!='0':
        if w.count('0')==1 and w.count('1')<=2:
            k += 1
            print(w)
print(k)