from math import *

for length in range(1, 10000):
    i = ceil(log2(52 + 500))
    v = ceil(length*i/8)
    if v*45_877 > 49*1024*1024:
        print(length)
