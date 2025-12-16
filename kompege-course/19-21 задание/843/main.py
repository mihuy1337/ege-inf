def game(s1, s2, m):
    if s2+s1 <= 20: return m%2==0
    if m == 0: return 0
    h = [
        game(s1 - 1, s2, m - 1), game(s1/2 if s1%2==0 else (s1+1)/2, s2, m - 1),
        game(s1, s2 - 1, m - 1), game(s1, s2 / 2 if s2 % 2 == 0 else (s2 + 1) / 2, m - 1)
    ]
    return any(h) if (m-1)%2==0 else all(h)

print(
    '19)', [s for s in range(11, 1000) if game(10, s, 2)]
)
print(
    '20)', [s for s in range(11, 1000) if not game(10, s, 1) and game(10, s, 3)]
)
print(
    '21)', [s for s in range(11, 1000) if game(10, s, 4) and not game(10, s, 2)]
)