# from itertools import *
#
# def f(u, w, x, y, z):
#     return ((z <= w) and (y == ( not(x) ) )) <= (u == (y or z))
#
# for t1, t2, t3, t4, t5, t6, t7, t8 in product([0, 1], repeat=8):
#     table = (
#         (0, t1, 0, 0, 0),
#         (0, t2, t3, 0, 0),
#         (t4, 0, 0, 0, t5),
#         (0, 0, t6, t7, t8)
#     )
#
#     if len(table)==len(set(table)):
#         for stolbs in permutations('uwxyz'):
#             if [f(**dict(zip(stolbs, row))) for row in table] == [0, 0, 0, 0]:
#                 print(''.join(stolbs))

# for n in range(1, 10000):
#     n_bin = bin(n)[2:]
#     if n%2==0:
#         r = '1' + n_bin + str(n_bin.count('1')%2)
#     else:
#         r = n_bin + '0' + str(n_bin.count('1')%2)
#     r_des = int(r, 2)
#     print(n, n_bin, r, r_des)
#     if r_des>100:
#         print(n)

# from turtle import *
#
# screensize(2000, 2000)
# s = 20
# tracer(0)
#
# for x in range(100, 1, -1):
#     for _ in range(4): fd(x*s); rt(90); fd(48*s); rt(90)
#     up()
#     fd(27*s); rt(90); fd(24*s); lt(90)
#     down()
#     for _ in range(4): fd(29*s); rt(90); backward(18*s); rt(90)
# up()
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         goto(x*s, y*s)
#         dot(5, 'green')
# mainloop()

from math import log2, ceil

# for i in range(10000):
#     v = 800*600*i
#     if 700*1024*8 >= v:
#         print(2**i)

# from itertools import permutations
# k = 0
# for kod in permutations('калий'):
#     kod = ''.join(kod)
#     if kod[0] != 'й' and 'иа' not in kod:
#         print(kod)
#         k += 1
# print(k)

f = open('9')
k = 0
for row in f:
    nums = sorted([int(num) for num in row.split()])
    # if len(set(nums)) == 4:
    #     print(nums, nums[1:5])
    if (len(set(nums)) == 4) and ((nums[0]**2 + nums[-1]**2) >= (nums[0]**2 + nums[-1]**2) >= (nums[1]**2 + nums[2]**2 + nums[3]**2 + nums[4]**2)**2):
        k += 1
print(k)
#
# print(k)
# from math import *
# for dop in range(1, 10000):
#     i = ceil(log2(12))
#     v = ceil(11*i/8)
#     if (v + dop)*50 == 700:
#         print(dop)

# from ipaddress import *
#
# for mask in range(32):
#     net = ip_network(f'153.202.16.37/{mask}', 0)
#     if f'153.202.16.32/{mask}' == str(net):
#         byts = str(net.netmask).split('.')
#         summ = int(byts[-1])+int(byts[-2])
#         print(net, byts, summ)

# def to36(n):
#     k = []
#     while n>0:
#         k = [n%36] + k
#         n //= 36
#     return k
# k=0
# ss = to36(30*36**231 + 18*6**101 - 3*36**45 - 2357)
# for num in ss:
#     if num%5 == 0 or num%3 == 0:
#         if (num%5 != 0 and num%3 == 0) or (num%5 == 0 and num%3 != 0):
#             k += 1
#             print(num)
# print(k)
# print(to36(30*36**231 + 18*6**101 - 3*36**45 - 2357))

# def dele(n, m):
#     return n%m==0
#
# for x in range(10000):
#     for a in range(10000):
#         if (dele(x, 2) <= (not(dele(x, 13))) or (x + a >= 1000))==1:
#             print(a)
#             break
