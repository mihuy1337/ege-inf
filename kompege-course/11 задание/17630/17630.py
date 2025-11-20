from math import log2, ceil

for l in range(1000):
     i = ceil(log2(10+26+450))
     ves = ceil(i*l/8)
     if ves >= 213*1024/708:
         print(l)
         break