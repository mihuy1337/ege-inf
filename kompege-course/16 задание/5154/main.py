from functools import *
@lru_cache(3000)
def f(n):
    if n > 100_000: return n
    if n <= 100_000: return f(n + 1) + 5*n + 2

for i in range(100000, 3, -1): f(i)

print(f(3) - f(7))