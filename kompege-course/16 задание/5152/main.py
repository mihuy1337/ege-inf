from functools import *
@lru_cache(None)
def f(n):
    return 2 if n == 1 else 2*f(n - 1)

for i in range(1, 1901): f(i)

print(
    f(1900)/(2**1890)
)