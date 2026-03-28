def div(n):
    ds = set()
    for d in range(1, int(n**0.5)+1):
        if n%d==0: ds |= {d, n%d}
    return sorted(ds)

for n in range(55_000_000, 60_000_001):
    d = [i for i in div(n) if i%2!=0]
    if len(d)==5:
        print(n, max(d))
