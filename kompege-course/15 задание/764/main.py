def dele(n, m):
    return n%m==0

def f(x):
    return (dele(x, 15) and (not dele(x, 21))) <= (not dele(x, a)) or (not x, 15)
m = []
for a in range(1, 10000):
    if all(f(x)==1 for x in range(1, 10000)):
        m.append(a)
print(min(m))
