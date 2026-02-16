from math import *

for dlina in range(1, 10000):
    i = ceil(log2(10 + 70))
    v = ceil(dlina*i/8)
    if 1_234_564*v > 24*1024*1024:
        print(dlina)