def cc10(x, n):
    x = str(x)[::-1]
    s = 0
    for i in range(len(x)):
        s = s + int(x[i])*n**i
    return s

for n in range(1, 10000):
    if cc10(132, n)+cc10(13, 8) == cc10(124, n+1):
        print(n)