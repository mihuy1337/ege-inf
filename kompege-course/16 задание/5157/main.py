from functools import *
from sys import setrecursionlimit

setrecursionlimit(14000)
@lru_cache(1000000)
def f(n):
    if n >= 10_000: return n
    if n < 10_000 and n%3==0: return n + f(n//3)
    if n < 10_000 and n % 3 != 0: return 2*n + f(n + 3)

for i in range(10000, 47, -1): f(i)

print(f(999) - f(46))