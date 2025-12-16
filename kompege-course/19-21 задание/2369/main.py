def game(s1, s2, s3, m):
    if s1 + s2 + s3 >= 73: return m % 2 == 0
    if m == 0: return 0
    h = [
        game(s1 + 3, s2, s3, m - 1), game(s1 + 13, s2 , s3, m - 1), game(s1 + 23, s2, s3, m - 1),
        game(s1, s2 + 3, s3, m - 1), game(s1, s2 + 13, s3, m - 1), game(s1, s2 + 23, s3, m - 1),
        game(s1, s2, s3 + 3, m - 1), game(s1, s2, s3 + 13, m - 1), game(s1, s2, s3 + 23, m - 1),
    ]

    return any(h) if (m-1)%2==0 else all(h)
#all на any
print(
    '19)', [s for s in range(1, 24) if game(2, s, s*2, 2)]
)
print(
    '20)', [s for s in range(1, 24) if not game(2, s, s*2, 1) and game(2, s, s*2, 3)]
)
print(
    '21)', [s for s in range(1, 24) if game(2, s, s*2, 4) and not game(2, s, s*2, 2)]
)