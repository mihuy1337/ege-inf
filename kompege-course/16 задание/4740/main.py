from functools import *
from math import factorial


@lru_cache(None)
def f(n):
    if n >= 5000: return factorial(n)
    if 1 <= n < 5000: return 2 * f(n + 1)//(n+1)


for i in range(5000, 4, -1): f(i)

print(1000*f(7)/f(4))
