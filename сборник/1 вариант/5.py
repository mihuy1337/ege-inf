m = []

for n in range(1, 10000):
    n2 = f'{n:b}'
    if n%3==0:
        r2 = n2 + n2[-3:]
    else:
        r2 = n2 + f'{((n%3 + 1)*3):b}'
    r = int(r2, 2)
    if r<=416: m.append(r)

print(max(m))
