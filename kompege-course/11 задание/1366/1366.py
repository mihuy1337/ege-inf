from math import ceil, log2

for N in range(2, 10000):
    i = ceil(log2(N))
    ves = ceil(80*i/8)
    if 1200*ves <= 150*1024:
        print(N)
