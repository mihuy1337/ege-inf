from math import *
m = []
for k in range(6000, 100000):
    i = ceil(log2(10+1597+26))
    v = ceil(378*i/8)
    print(v)
    if v*k/(1024*1024) <= 154:
        m.append(k)
print(max(m))
