def f(curr, end):
    if curr>end: return 0
    if curr==11 or curr==18: return 0
    if curr==end: return 1
    return f(curr+1, end)+f(curr+2, end)+f(curr*3, end)

print(f(4, 8)*f(8, 23))