def cc(n, a):
    x = []
    while n>0:
        x = x + [n%a]
        n = n//a
    return x

print(cc(2*27**7+3**10-9, 3).count(0))