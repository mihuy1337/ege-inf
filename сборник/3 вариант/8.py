from itertools import *

for n, w in enumerate(product('авкмос', repeat=6), 1):
    w = ''.join(w)
    if n%2==0:
        if (w[0] not in 'авк'):
            if w.count('к')==2 and ('кк' not in w):
                print(n, w)