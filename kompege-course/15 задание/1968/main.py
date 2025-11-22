def f(x):
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))

ox = [dx for x in [17, 58, 29, 80] for dx in [x - 0.001, x, x + 0.001]]
m = []
for a1 in ox:
    for a2 in ox:
        if a2>a1 and all(f(x) for x in range(1, 10000)):
            m.append(a2 - a1)
print(min(m))