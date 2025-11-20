def cc10(x, n):
    x = str(x)[::-1]
    s = 0
    for i in range(len(x)):
        s = s + int(x[i]) * n**i
    return s

for n in range(1, 10000):
    if cc10(21, n)*cc10(13, n)==cc10(313, n):
        print(n)