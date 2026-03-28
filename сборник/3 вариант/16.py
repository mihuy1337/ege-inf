from functools import *

@lru_cache(None)
def f(n):
    if n<10: return n
    if n>=10: return f(n-15) + n**3

for i in range(10, 1001): f(i)

print(f(1000)-f(940))

