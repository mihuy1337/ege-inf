from math import *

for n in range(1, 10000):
    i = ceil(log2(n))
    v = ceil(23*i/8)
    if 3222444*v>=45*1024*1024:
        print(n)