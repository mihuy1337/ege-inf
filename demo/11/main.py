from math import *

for n in range(1, 10000):
    i = ceil(log2(n))
    if 11*1024*1024*1024*8 <= 3_845_627*2783*i:
        print(n)