from functools import *

@lru_cache(2000)
def f(n):
    if n == 1: return 1
    if n > 1: return n**2 + int(f(n - 1))
    return None

for i in range(1, 1001): f(i)

print(f(1000) - f(997))