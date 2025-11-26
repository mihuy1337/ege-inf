m = []

for n in range(4, 1000):
    n_bin = bin(n)[2:]
    if n%3==0: r_bin = n_bin + n_bin[-3] + n_bin[-2] + n_bin[-1]
    else: r_bin = n_bin + bin((n%3)*3)[2:]
    print(n, n_bin, r_bin, int(r_bin, 2))
    if int(r_bin, 2) >= 200:
        m.append(n)

print(min(m))