def fact(n):
    ds = []
    d = 2
    while d**2 <= n:
        while n % d == 0:
            ds.append(d)
            n = n // d
        d += 1
    if n > 1:
        ds.append(n)
    return ds

for n in range(5_700_001, 5_700_000 + 1_000_000):
    d = set(fact(n))
    m = max(d) + min(d) if len(d) else 0
    if m > 70_000 and int(m**0.5)**2 == m:
        print(n, m)
