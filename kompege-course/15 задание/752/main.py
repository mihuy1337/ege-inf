def f(x):
    C = x in {3, 6, 9, 12}
    V = x in {1, 2, 3, 4, 5, 6}
    A = x in a
    return (not ((not A) and C)) or (not V)

a = set()

for x in range(1, 10000):
    if f(x)==0:
        a.add(x)

print(len(a))