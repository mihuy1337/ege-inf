def f(curr, end):
    if curr>end: return 0
    if curr==end: return 1
    return f(curr+2, end)+f(curr+4, end)+f(curr+5, end)

for n in range(31, 1000):
    if f(31, n)==1001:
        print(n)
        break