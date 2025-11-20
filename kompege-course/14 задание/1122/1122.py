def cc(n, a):
    x = []
    while n>0:
        x = [n%a] + x
        n //= a
    return x

for x in range(100000):
    if sum(cc(36**17-6**x+71, 6)) == 61:
        print(x)
        break