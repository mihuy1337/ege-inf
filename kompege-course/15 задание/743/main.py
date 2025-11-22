def f(x):
    v = x in (1, 3, 5, 7, 9, 11)
    c = x in {3, 6, 9, 12}
    return (v <= (not c)) or (x in a)

a = set()

for x in range(1, 10000):
    if f(x)==0:
        print(x)
        a.add(x)

print(a)