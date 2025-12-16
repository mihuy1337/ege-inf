def game(s1, s2, m):
    if s1 + s2 >= 77: return m % 2 ==0
    if m == 0: return 0
    h = [
        game(s1 + 1, s2, m - 1), game(s1*2, s2, m - 1),
        game(s1, s2 + 1, m - 1), game(s1, s2*2, m - 1)
    ]

    return any(h) if (m-1)%2==0 else all(h)

#тут all меняется на any
print(
    '19)', [s for s in range(1, 70) if game(7, s, 2)]
)

print(
    '20)', [s for s in range(1, 70) if game(7, s, 3) and not game(7, s, 1)]
)

print(
    '21)', [s for s in range(1, 70) if (game(7, s, 2) or game(7, s, 4)) and not game(7, s, 2)]
)