def f(curr, end):
    if curr>end: return 0
    if curr==end: return 1
    return f(curr+1, end)+f(curr*1.5, end) \
            if curr%2==0 else f(curr+1, end)

print(f(1, 20))