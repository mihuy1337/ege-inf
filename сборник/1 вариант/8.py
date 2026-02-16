from itertools import *

for n, w in enumerate(product(sorted('стрела'), repeat=5)):
    n = n + 1
    w = ''.join(w)
    if n%2==0:
        if w[0] not in 'аст':
            if ('лл' not in w) and (w.count('л')==2):
                print(n, w)