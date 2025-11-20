from math import *

for dop in range(2, 10000):
    N = 510 + 10
    i = ceil(log2(N))
    ves = ceil(99*i/8)
    if 4322*(ves + dop) >= 543*1024:
        print(dop)
        break