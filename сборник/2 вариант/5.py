m = []
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n%3==0:
        r2 = n2 + n2[-3:]
    else:
        r2 = n2 + bin((n%3-1)*3)[2:]
    r = int(r2, 2)
    if r<416: m.append(r)
print(max(m))
