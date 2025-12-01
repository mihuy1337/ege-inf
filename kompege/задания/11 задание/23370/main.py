from math import *

for l in range(1, 10000):
    i = ceil(log2(10 + 17))
    v = ceil(l*i/8)
    if v*7_564_230 > 31*1024*1024:
        print(l)