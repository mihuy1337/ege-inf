mn = []

for n in range(19, 10000):
    n2 = f'{n:b}'
    if n%2==0:
        r2 = '10' + n2
    else:
        r2 = '1' + n2 + '01'
    r = int(r2, 2)
    print(r)
    mn.append(r)

print(min(mn))