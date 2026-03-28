def div(n):
    ds = set()
    for d in range(2, int(n**0.5)+1):
        if n%d==0: ds |= {d, n//d}
    return sorted(ds)

for n in range(106732567, 152673836+1):
    d = div(n)
    if len(d)==3:
        print(n, max(d))