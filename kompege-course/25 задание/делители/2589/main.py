def div(n):
    ds = set()
    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            ds |= {d, n//d}
    return sorted(ds)

for n in range(300001, 300001+1000):
    div3 = [i for i in div(n) if i%3==0 and i!=n]
    if len(div3)==5:
        print(n, max(div3))