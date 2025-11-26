def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

ox = [dx for x in [25, 64, 40, 115] for dx in [x - 0.001, x, x + 0.001]]
m = []
for a1 in ox:
    for a2 in ox:
        if a2>a1:
            if all(f(x)==1 for x in range(0, 10000)):
                m = m + [a2-a1]
print(min(m))