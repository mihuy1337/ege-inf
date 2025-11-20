from math import *

for N in range(2, 10000):
    i = ceil(log2(N))
    ves = ceil(261*i/8)
    if 252_500*ves >= 31*1024*1024:
        print(N)
        break