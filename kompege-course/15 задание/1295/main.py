def f(x):
    P = 17 <= x <= 54
    Q = 37 <= x <= 83
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

ox = [dx for x in [17, 54, 37, 83] for dx in [x - 0.001, x, x + 0.001]]
m = []
for a1 in ox:
    for a2 in ox:
        if a2>a1 and all(f(x)==1 for x in range(1, 10000)):
            m.append(a2-a1)
print(round(min(m)))