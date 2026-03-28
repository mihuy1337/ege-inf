def div(n):
    ds = set()
    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            ds |= {d, n//d}
    return sorted(ds)

for n in range(500001, 500000+1000):
    div8 = [i for i in div(n) if i%10==8 and i!=8 and i!=n]
    if div8:
        print(n, min(div8))
