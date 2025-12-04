from functools import *

@lru_cache(None)
def f(n):
    return g(n - 1) - g(n - 5)
@lru_cache(None)
def g(n):
    if n<=25: return 2*(n+1)
    if n>25: return g(n - 4) + n

for i in range(20, 150775): f(i)

print(f(150774))
