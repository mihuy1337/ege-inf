for n in range(21, 10000):
    n_bin = bin(n)[2:]
    r_bin = '11' + n_bin[2:] + '0'\
            if n%2==0\
            else n_bin + str(sum(int(i) for i in n_bin)%2)
    r = int(r_bin, 2)
    print(n, n_bin, r_bin, r)
    if r>154:
        print(n)
        break
