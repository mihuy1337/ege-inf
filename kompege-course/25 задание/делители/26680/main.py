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

def p(n): return n>1 and all(n%d!=0 for d in range(2, int(n**0.5)+1))

for n in range(5_000_001, 5_000_000+1000000, 2):
    d = [i for i in fact(n) if i%2!=0]
    if len(set(d))==2 and len(d)==2 and d[0]*d[1]==n:
        if p(max(d)-min(d)):
            print(n, max(d))