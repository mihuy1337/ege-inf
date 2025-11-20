def f(x):
    return (x&107==0) <= ((x&55!=0)<=(x&a!=0))
m = []
for a in range(1, 10000):
    if all(f(x)==1 for x in range(1, 10000)):
        m.append(a)

print(min(m))