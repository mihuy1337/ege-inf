for n in range(2, 1000):
    b = bin(n)[2:]
    b = b[::-1]
    b = b[1:] if b[0] == '0' else b
    r = int(b, 2)
    if r==13:
        print(n, r)