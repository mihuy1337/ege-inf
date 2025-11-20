def mod(m, n):
    return m%n

def f(x):
    return ((mod(x, 4) != 3) or (mod(x, 6) != 1)) <= (mod(x, 36) != a)
m = []
for a in range(1, 10000):
    if all(f(x)==1 for x in range(1, 10000)):
        m.append(a)
print(min(m))