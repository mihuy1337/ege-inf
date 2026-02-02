from functools import lru_cache


@lru_cache(None)
def f(curr, end):
    if curr>end or curr==6: return 0
    if curr==end: return 1
    return f(curr+2, end)+f(curr*3, end)

print(
    f(1, 25)*f(25, 63)
)