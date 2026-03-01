from functools import lru_cache
from itertools import *

@lru_cache(None)
def f(n):
    if n==1: return 15
    if n>=2: return 2*f(n-1)-n

for i in range(2, 2026): f(i)

print(
    (f(2025)-f(2023)-1)/(2**2022)
)
