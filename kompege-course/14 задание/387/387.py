def cc(n, a):
    x = []
    while n>0:
        x = [n%a] + x
        n = n//a
    return x

print(sum(cc(51*7**12-7**3-22, 7)))