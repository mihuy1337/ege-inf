def game(s, m):
    if 36 <= s <= 60: return m % 2 == 0
    if s > 60: return m%2!=0
    if m == 0: return 0
    h = [
        game(s + 1, m - 1),
        game(s*2, m - 1),
        game(s*3, m - 1)
    ]
    return any(h) if (m-1)%2==0 else all(h)

print(
    '19)', [s for s in range(1, 35 + 1) if game(s, 2)]
)
print(
    '20)', [s for s in range(1, 35 + 1) if (not game(s, 1)) and game(s, 3)]
)

print(
    '21)', [s for s in range(1, 35 + 1) if (game(s, 2) or game(s, 4)) and (not game(s, 2))]
)