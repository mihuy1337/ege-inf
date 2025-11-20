def cc10(x, n):
    x = str(x)[::-1]
    s = 0
    for m in range(len(x)):
        s = s + int(x[m]) * n**m
    return s


for n in range(1, 10000):
    if cc10(103, n) == cc10(97, n + 2):
        print(n)