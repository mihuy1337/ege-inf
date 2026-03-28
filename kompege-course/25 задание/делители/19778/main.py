def div(n):
    ds = set()
    for d in range(2, int(n**0.5)+1):
        if n%d==0: ds |= {d, n//d}
    return ds

for n in range(9_500_001, 9_500_001+100000):
    divp = [i for i in div(n) if len(div(i))==0]
    f = sum(divp)//len(divp) if divp else 0
    if f!=0 and f%813==0:
        print(n, f)