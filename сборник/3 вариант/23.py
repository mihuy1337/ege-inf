def f(curr, end):
    if curr<end or curr==8: return 0
    if curr==end: return 1
    return f(curr-1, end)+f(curr-4, end)+f(curr//2, end)

print(f(30, 12)*f(12, 4))