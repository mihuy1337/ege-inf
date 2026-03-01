def c2(n):
    c2s = str(n)
    if int(c2s[1]) < int(c2s[2]):
        return int(c2s[0] + c2s[2] + c2s[1])
    else:
        return 0

def f(curr, end):
    if curr==end: return 1
    if curr>end: return 0
    c2s = str(curr)
    if curr<end:
        if int(c2s[1]) < int(c2s[2]):
            return f(curr+1, end)+f(int(c2s[0]+c2s[2]+c2s[1]), end)
        else: return f(curr+1, end)

print(f(110, 154))