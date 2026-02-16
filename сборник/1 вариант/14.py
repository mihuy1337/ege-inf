def cc27(n):
    k = []
    while n:
        k = [n%27] + k
        n = n // 27
    return k

n = 3*2187**1801 + 729**2000 - 4*243**2100 + 81**2200 - 2*27**2400 - 13122

print(
    len([i for i in cc27(n) if i>8])
)