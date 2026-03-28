def f(n):
    ds = []
    d = 2
    while d**2<=n:
        while n%d==0:
            ds.append(d)
            n = n//d
        d+=1
    if n>1: ds.append(n)
    return ds

for n in range(2_700_034, 2_700_034+100000, 100):
    d = f(n)
    if any(d.count(i)>=5 for i in d):
        print(n, min(i for i in d if d.count(i)>=5))