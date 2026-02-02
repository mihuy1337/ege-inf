from functools import *

@lru_cache(None)
def f(n):
    if n >= 10_000: return n
    if n < 10_000 and n%3==0: return n + f(n//3)
    if n < 10_000 and n % 3 != 0: return 2*n + f(n + 3)

for i in range(1, 10000): f(i)

print(f(999) - f(46))