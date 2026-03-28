from string import printable
mx = []
for x in printable[:22]:
    n = int(f'12313{x}57', 22) + int(f'1{x}34561', 22)
    print(n/21)