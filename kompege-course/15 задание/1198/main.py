def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = a1 <= x <= a2
    return (B <= A) and ((not C) or A)

ox = [dx for x in [18, 52, 16, 41] for dx in [x - 0.001, x, x + 0.001]]
m=[]
for a1 in ox:
    for a2 in ox:
        if a2 > a1 and all(f(x)==1 for x in range(1, 10000)):
            m.append(a2 - a1)

print(round(min(m)))