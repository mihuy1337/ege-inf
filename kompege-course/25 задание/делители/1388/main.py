def div(n):
    ds = set()
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            ds |= {n//d, d}
    return sorted(ds)


for i in range(150000, 151000):
    divs = div(i)
    s = sum(divs) if len(divs) else 0
    if s%13==10:
        print(i, s)
