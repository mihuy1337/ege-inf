from math import *

for dlina in range(1, 10000):
    i = ceil(log2(10 + 50))
    v = ceil(dlina*i/8)
    if 1_567_123*v > 20*1024*1024:
        print(dlina)