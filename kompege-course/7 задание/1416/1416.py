from math import *

for N in range(2, 10000):
    i = ceil(log2(N))
    mb = 3900*2160*i/(8*1024*1024)
    if mb <= 13:
        print(N)