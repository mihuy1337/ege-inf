from functools import *

@lru_cache(2200)
def f(n):
    if n == 1: return 1
    if n > 1: return n*f(n - 1)

for n in range(1, 2024): f(n)


print(f(2023)/f(2020))