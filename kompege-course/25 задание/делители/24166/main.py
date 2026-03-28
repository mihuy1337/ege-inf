def fact(n):
    ds = []
    d = 2
    while d**2<=n:
        while n%d==0:
            ds.append(d)
            n = n//d
        d+=1
    if n>1: ds.append(n)
    return sorted(ds)

for n in range(7_305_678, 7_305_678+10000):
    d = fact(n)
    if len(d)==4 and str(sum(d)) == str(sum(d))[::-1]:
        print(n, sum(d))