
def cc(n, a):
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = ''
    while n>0:
        x = alf[n%a] + x
        n //= a
    return x

print(cc(6*144**26 + 11*12**75 - 48, 12), cc(6*144**26 + 11*12**75 - 48, 12).count('B'))
