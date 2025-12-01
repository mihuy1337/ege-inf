# from itertools import product, permutations
#
#
# def f(w, x, y, z):
#     return (x <= y) and (y<=z) and (z<=w)
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = (
#         (a1, 0, 1, a2),
#         (a3, 1, a4, 0),
#         (a5, 0, 1, a6)
#     )
#
#     if len(set(table))==len(table):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, r))) for r in table]==[1,1,1]:
#                 print(''.join(p))
from ipaddress import ip_network
from itertools import product, repeat
# def cc3(n):
#     k = []
#     while n>0:
#         k = [n%3] + k
#         n = n//3
#     return ''.join([str(i) for i in k])
# mn = []
# for n in range(10, 10000):
#     n_3 = cc3(n)
#     n_3 = n_3 + n_3[-3:] if n%4==0 else '1'+n_3+'20'
#     r = int(n_3, 3)
#     if r>423:
#         mn.append(r)
# print(min(mn), mn)

from turtle import *

# screensize(2000, 2000)
# tracer(0)
# s = 30
#
# for _ in range(9):
#     fd(27*s); rt(90); fd(30*s); rt(90)
# up()
# fd(3*s); rt(90); fd(6*s); lt(90)
# down()
# for _ in range(9):
#     fd(77*s); rt(90); fd(66*s); rt(90)
#
#
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*s, y*s)
#         dot(4, 'green')
# mainloop()
# from math import *
# for n in range(1, 10000):
#     i = ceil(log2(n))
#     if 32*1024*i == 28*1024*8:
#         print(n)

# for num, word in enumerate(product(sorted('досж'), repeat=6)):
#     if 'жс' == ''.join(word[:2]):
#         print(num+1, ''.join(word))
# k=0
# for row in open('9'):
#     nums = [int(num) for num in row.split()]
#     povt = [i for i in nums if nums.count(i)==3]
#     ne_povt = [i for i in nums if nums.count(i)==1]
#     if len(set(povt))==1 and len(ne_povt)==1:
#         if povt[0]%2!=0 and ne_povt[0]%2==0:
#             print(nums)
#             k+=1
#
# print(k)
# from math import *
# for dop in range(1, 10000):
#     n = ceil(15*ceil(log2(12))/8)
#     if (n+dop)*20 == 300:
#         print(dop)
# k=0
# for ip in ip_network('101.157.240.0/255.255.252.0', 0):
#     nums_bits = [bin(int(i))[2:] for i in str(ip).split('.')]
#     if nums_bits[0].count('1')+nums_bits[1].count('1') > \
#             nums_bits[2].count('1')+nums_bits[3].count('1'):
#         print(nums_bits)
#         k += 1
# print(k)

# print(bin(8**1023 + 2**1024 - 3)[2:].count('1'))

# def div(n, m):
#     return n//m
#
# def f(x):
#     return (div(x, 50) > 3) or (not (div(x, 13) > 3)) or (div(x, a) > 6)
#
# for a in range(1, 10000):
#     if all(f(x)==1 for x in range(1, 10000)):
#         print(a)

# from functools import *
#
# @lru_cache(None)
# def f(n):
#     return 1 if n == 1 else (n + 1) * f(n - 1)
#
# for i in range(1, 5038): f(i)
#
# print(f(5037)/f(5034))

# nums = [int(i) for i in open('17')]
# pars = [[nums[i], nums[i+1]] for i in range(0, len(nums) - 1)]
# pars_sort = [i for i in pars if sum(i)%3==0 and sum(i)%6!=0 and abs(i[0]*i[1])%10==8]
#
# pars_sum = [sum(i) for i in pars]
#
# print(len(pars_sort), max(pars_sum))