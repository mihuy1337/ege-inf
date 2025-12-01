from math import *

for n in range(1, 10000):
    i = ceil(log2(n))
    v = ceil(248*i/8)
    if v*75_600 > 16*1024*1024:
        print(n)