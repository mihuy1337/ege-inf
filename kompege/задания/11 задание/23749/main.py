from math import *

for n in range(1, 10000):
    i = ceil(log2(n))
    v = ceil(2783*i/8)
    if v*3_845_627 >= 11*1024*1024*1024:
        print(n)