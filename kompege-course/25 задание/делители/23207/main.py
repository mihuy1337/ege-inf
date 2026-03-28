# def div(n):
#     ds = set()
#     for d in range(2, int(n**0.5)+1):
#         if n%d==0: ds |= {d, n//d}
#     return sorted(ds)
#
# def p(n): return n>0 and all(n%d!=0 for d in range(2, int(n**0.5)+1))

def fact(n):
    ds = []
    d = 2
    while d**2<=n:
        while n%d==0:
            ds.append(d)
            n = n//d
        d+=1
    if n>1: ds.append(n)
    return sorted(ds)

for n in range(1_324_728, 1_325_727+100000):
    divs = fact(n)
    if len(divs)==2 and divs[0]*divs[1]==n and all(str(i).count('5')==1 for i in divs):
        print(n, max(divs))
    # if len(divs)==1 and divs[0]**2==n and str(divs[0]).count('5')==1:
    #     print(n, sorted(divs)[-1])