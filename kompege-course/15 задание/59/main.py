def dele(n, m):
    return n%m==0

def f(x):
    return (dele(x, a) and dele(x, 24) and (not dele(x, 16))) <= (not dele(x, a))
m = []
for a in range(1, 1000):
    if all(f(x)==1 for x in range(1, 1000)):
        m.append(a)

print(min(m))