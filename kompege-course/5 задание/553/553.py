c = 0

for n in range(1, 1000):
    b = bin(n)[2:]
    summa = sum([int(i) for i in b])
    b = b + str(summa % 2)
    summa = sum([int(i) for i in b])
    b = b + str(summa % 2)

    r = int(b, 2)

    if r<80:
        print(n, r)
        c += 1

print(c)
