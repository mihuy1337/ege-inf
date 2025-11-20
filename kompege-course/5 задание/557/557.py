for n in range(10000):
    b = bin(n)[2:]
    b = b + b[-1]

    b = b + '0' if b.count('1')%2==0 else b + '1'
    b = b + '0' if b.count('1') % 2 == 0 else b + '1'

    r = int(b, 2)

    if r>144: print(n, r); break