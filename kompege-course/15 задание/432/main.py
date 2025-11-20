def dele(x, a):
    return x%a==0

def f(x):
    return ((not dele(x, 84)) or (not dele(x, 90))) <= (not dele(x, a))

m = []

for a in range(1, 10000):
    if all(f(x)==1 for x in range(1, 10000)):
        m = m + [a]

print(min(m))

