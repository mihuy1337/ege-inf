def cc(n, a):
    x = []
    while n>0:
        x = [n%a] + x
        n = n//a
    return x

print(len(set(cc(11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338, 15))))