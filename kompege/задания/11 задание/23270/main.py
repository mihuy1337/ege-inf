from math import *

for l in range(1, 10000):
    i = ceil(log2(10 + 27))
    v = ceil(l*i/8)
    if v*3548 > 12*1024:
        print(l)