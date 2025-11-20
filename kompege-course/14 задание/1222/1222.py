def cc(n, a):
    x = []
    while n>0:
        x = [n%a] + x
        n //= a
    return x
x1 = cc(5*216**1156 - 4*36**1147 + 6**1153 - 875, 6)
x2 = cc(5*216**1156 - 4*36**1147 + 6**1153 - 875, 6)
print(x1.count(5) - x2.count(0))