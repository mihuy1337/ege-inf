def cc4(n):
    a = []
    while n>0:
        a = a + [n%4]
        n = n//4
    return a

print(cc4(3*16**8-4**5+30).count(3))