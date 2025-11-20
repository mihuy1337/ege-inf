def cc10(x, n):
    x = str(x)[::-1]
    s = 0
    for a in range(len(x)):
        s = s + int(x[a])*n**a
    return s

for i in range(10000000):
    if cc10(33, i + 4) - cc10(33, 4) == 33:
        print(i)