def two(n):
    n = [i for i in str(n)]
    for i, r in enumerate(n):
        if r=='9': break
        else: n[i]= str(int(r)+1)
    return int(''.join(n))

def f(curr: int, end: int):
    if curr>end: return 0
    if curr==end: return 1
    return f(curr+1, end)+f(two(curr), end)

print(f(25, 51))
