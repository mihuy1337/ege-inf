from math import *

for n in range(1, 1000):
    i = ceil(log2(n))
    v = ceil(261*i/8)
    if v*252_500 > 31*1024*1024:
        print(n)