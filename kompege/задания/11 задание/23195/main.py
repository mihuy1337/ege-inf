from math import *

for n in range(1, 10000):
    i = ceil(log2(n))
    v = ceil(172*i/8)
    if v*356_984 >= 54*1024*1024:
        print(n)