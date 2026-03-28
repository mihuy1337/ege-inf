from math import *

for dlina in range(1, 10000):
    i = ceil(log2(10 + 34 + 26))
    v = ceil(dlina*i/8)
    if 1142*v > 305*1024:
        print(dlina)
