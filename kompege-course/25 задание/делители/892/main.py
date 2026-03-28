def div(num):
    ds = set()
    for d in range(1, int(num**0.5) + 1):
        if num%d==0:
            ds |= {d, num//d}
    return sorted(ds)

for i in range(154026, 154044):
    d = div(i)
    if len(d)==4:
        print(*d[-2:])