def f(a, x):
    return (x%21==0) <= ((x%a!=0) <= (x%77!=0))

for a in range(1, 100000):
    if all(f(a, x)==1 for x in range(1, 100000)):
        print(a)