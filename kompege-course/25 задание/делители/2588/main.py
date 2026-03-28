def div(n):
    ds = set()
    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            ds |= {d, n//d}
    return sorted(ds)

for n in range(190201, 190260+1):
    div2 = [i for i in div(n) if i%2==0]
    if len(div2)==4:
        print(*div2[-2:][::-1])