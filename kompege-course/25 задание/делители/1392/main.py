def div(n):
    ds = set()
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            ds |= {d, n//d}
    return sorted(ds)

for n in range(550000, 551000):
    divs = div(n)
    f = sum(divs)//len(divs) if len(divs) else 0
    if f%31==13:
        print(n, f)