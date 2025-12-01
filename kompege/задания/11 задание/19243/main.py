from math import *

for n in range(1, 1000):
    i = ceil(log2(n))
    v = ceil(377*i/8)
    if v*23155 > 5536*1024:
        print(n)