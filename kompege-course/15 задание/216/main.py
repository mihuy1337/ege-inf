def f(x):
    return ((x&26!=0) or (x&13 != 0)) <= ((x&29 == 0) <= (x&a != 0))
m = []
for a in range(1, 10000):
    if all(f(x)==1 for x in range(1, 10000)):
        m = m + [a]

print(min(m))