from math import *

for dop in range(10000):
    N = 999+10
    i = ceil(log2(N))
    ves = ceil(745*i/8)
    if 312*(ves+dop) <= 311*1024:
        print(dop*312) #В УСЛОВИИ НАПИСАНО ВСЕХ ПОЛЬЗОВАТЕЛЕЙ