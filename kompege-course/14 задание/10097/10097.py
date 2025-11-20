def cc(n, a):
    x = []
    while n>0:
        x = [n%a] + x
        n = n//a
    return x

print(cc(3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024, 25).count(0))