from functools import lru_cache


@lru_cache(None)
def f(curr, end):
    if curr>end: return 0
    if curr==end: return 1
    return f(curr+1, end)\
        +f(int(str(curr)[0] + str(curr)[1:][::-1]) if int(str(curr)[-1])>int(str(curr)[-2]) else curr, end)

print(f(101, 154))