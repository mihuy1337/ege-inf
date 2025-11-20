def cc(n, a):
    x = []
    while n>0:
        x = [n%a] + x
        n = n//a
    return x

for x in range(10000):
    if cc(125**200-5**x+74, 5).count(4)==100:
        print(x)
        break