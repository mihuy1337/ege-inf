def f(x):
    return (x%a!=0) <= ((x%48!=0) or (x%35!=0))

for a in range(1, 100000):
    if all(f(x)==1 for x in range(1, 100000)):
        print(a)
