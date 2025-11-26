from functools import *
@lru_cache(None)
def f(n):
    return 2 * (g(n - 3) + 8)
@lru_cache(None)
def g(n):
    return 2*n if n < 10 else g(n - 2) + 1

for i in range(10, 15_549): f(i)

print(f(15_548))