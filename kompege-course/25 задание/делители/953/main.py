def fact(n):
    ds = []
    d = 2
    while d**2<=n:
        while n%d==0:
            ds.append(d)
            n = n // d
        d += 1
    if n>1: ds.append(n)
    return ds

for n in range(499999, 450000, -1):
    s = sum({i for i in fact(n) if i!=n})
    if s!=0 and s%10==0:
        print(n, s)
