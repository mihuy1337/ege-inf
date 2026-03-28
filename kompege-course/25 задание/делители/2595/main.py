def div(n):
    ds = set()
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            ds |= {d, n//d}
    return sorted(ds)

for n in range(400_000_001, 400_000_000 + 100000):
    divs = div(n)
    p = divs[0]*divs[1]*divs[2]*divs[3]*divs[4] if len(divs)>=5 else 0
    if p<=n and p%100==17:
        print(p, divs[4])

