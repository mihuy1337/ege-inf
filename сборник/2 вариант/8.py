from itertools import *

for n, w in enumerate(product(sorted('стрела'), repeat=5), 1):
    w = ''.join(w)
    if (n%2!=0) and (w[0] not in 'аст') and ('ее' not in w) and (w.count('е')==2):
        print(n, w)
