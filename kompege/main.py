# from itertools import permutations
#
#
# def f(x, y, z):
#     return x <= y and z
#
# table = [
#     [0, 1, 0],
#     [1, 1, 0]
# ]
#
# for i in permutations('xyz'):
#     if [f(*dict(zip(i, row))) for row in table] == [0, 0]:
#         print(i)
# m = []
# for n in range(1, 1000):
#     r = bin(n)[2:]
#
#     if sum([int(i) for i in r])%2 == 0:
#         r = '10' + r
#     else: r = '11' + r
#
#     if sum([int(i) for i in r])%2 != 0:
#         r = r + '11'
#     else: r = r + '00'
#
#     if int(r, 2) < 860:
#         m.append(r)
#
# print(m)
# print(len(m))


# from turtle import *
#
# screensize(1000, 1000)
# tracer(0)
# left(90)
# s = 50
#
# for _ in range(19): fd(8*s); rt(110); fd(8*s); rt(70)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*s, y*s)
#         dot(4, 'green')
#
# mainloop()

# v1 = 2560*1440*22
# v2 = 1920*108*20
# print('v1', v1)
# print('v2', v2)
#
# razn_kb = (v1 - v2)/8/1024
#
# print(razn_kb*130)
# from itertools import*
# m = []
# for word in product('катер', repeat=3):
#     if word.count('р')>=2:
#         m.append(''.join(word))
# print(m)
# print(len(m))

# k = 0
# for s in open('9'):
#     nums = [int(i) for i in s.split()]
#     if sum(nums)==360:
#         if nums[0]==nums[2] and nums[1]==nums[3]:
#             k+=1
#             print(nums)
# print(k)
# from math import *
# i = ceil(log2(10000))
# v1 = (3000*i)/8
# print(v1)
# v2_20  = (v1*(2**20))/1024
#
# print(v2_20)

# from ipaddress import *
#
# print(ip_network('156.132.15.138/255.255.252.0', 0))
# k = 0
# for ip in ip_network('156.132.15.138/255.255.252.0', 0):
#     print(ip)
#     k += 1
#     if str(ip) == '156.132.15.138':
#         break
#         print(ip)
# print(k)

# def to(n, m):
#     k = []
#     while n>0:
#         k = [n%m] + k
#         n = n // m
#     return k
#
# for m in range(2, 10000):
#     if len(to(50, m)) == 2:
#         print(m)
#         print(to(50, m))
#         break

def f(x):
    P = 16 <= x <= 84
    Q = 27 <= x <= 43
    A = a1 <= x <= a2
    return (A <= P) or Q

ox = [dx for x in [16, 84, 27, 43] for dx in [x - 0.001, x, x + 0.001]]
m = []
for a1 in ox:
    for a2 in ox:
        if a2>a1 and all(f(x)==1 for x in ox):
            m.append(a2-a1)
print(m)

print(round(max(m)))