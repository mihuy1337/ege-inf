def f(n):
    ds = []
    d = 2
    while d**2<=n:
        while n%d==0:
            ds.append(d)
            n = n//d
        d+=1
    if n>1: ds.append(n)
    return sorted(ds)

for n in range(987654321, 987654321-100000, -1):
    d = f(n)
    if len(d)==13 and ('1' in str(sum(d))):
        print(n, max(d))