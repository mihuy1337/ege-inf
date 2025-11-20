for n in range(1, 10000):
    b = bin(n)[2:]
    summa = sum([int(i) for i in b])
    b = b + str(summa%2)
    summa = sum([int(i) for i in b])
    b = b + str(summa % 2)
    if int(b, 2)>80:
        print(n, int(b, 2))

# for n in range(1, 100):
#     b = bin(n)[2:]
#     if b.count('1')%2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#
#     if b.count('1')%2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#
#     r = int(b, 2)
#     if r>80:
#         print(n, r)
