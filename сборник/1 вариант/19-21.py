def gm(s, m):
    if s<=60: return m%2==0
    if m==0: return 0
    h = [gm(s-3, m-1),gm(s-5, m-1),gm(s//4, m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print(19, [s for s in range(61, 10000) if not gm(s, 1) and gm(s, 2)])
print(20, [s for s in range(61, 10000) if not gm(s, 1) and gm(s, 3)])
print(21, [s for s in range(61, 10000) if not gm(s, 2) and gm(s, 4)])