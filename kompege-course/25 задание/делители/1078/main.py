def div(n):
    ds = set()
    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            ds |= {d, n//d}
    return sorted(ds)

for n in range(1204300, 1204380+1):
    s = sum(i for i in div(n) if i%2==0 and i!=n)
    if s!=0 and s%10==0:
        print(n, s)
