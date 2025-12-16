def game(s1, s2, m):
    if s1 + s2 >= 59: return m%2==0
    if m == 0: return 0
    h = [
        game(s1 + 1, s2, m - 1),
        game(s1*2, s2, m - 1),
        game(s1, s2 + 1, m - 1),
        game(s1, s2*2, m - 1)
    ]

    return any(h) if (m-1)%2==0 else all(h)

print(
    '19)', [s for s in range(1, 54) if game(5, s, 1)]
)

print(
    '20)', [s for s in range(1, 54) if not game(5, s, 1) and game(5, s, 3)]
)

print(
    '21)', [s for s in range(1, 54) if game(5, s, 4) and not game(5, s, 2)]
)