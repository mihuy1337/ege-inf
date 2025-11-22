def f(x, y):
    return (2*x + y != 70) or (x < y) or (a < x)
m = []
for a in range(2000, 1, -1):
    if all(f(x, y)==1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        m = m + [a]
print(max(m))