def div(n):
    ds = set()
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            ds |= {d, n//d}
    return sorted(ds)

for n in range(250200, 251200):
    divs = div(n)
    s = max(divs)+min(divs) if len(divs) else 0
    if s%123==17:
        print(n, s)