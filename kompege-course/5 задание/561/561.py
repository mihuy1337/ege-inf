def cc(n):
    string = ''
    while n > 0:
        string += str(n % 3)
        n //= 3
    return string[::-1]
c = []
for n in range(3, 1000):
    b = cc(n)
    b = b + str(n%3)
    r = int(b, 3)
    if 100 <= r < 1000:
        print(r)

