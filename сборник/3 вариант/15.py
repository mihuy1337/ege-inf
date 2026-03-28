def f(a, x, y):
    return (105 != y+2*x) or (a>x) or (a>y)

for a in range(0, 1000):
    if all(f(a, x, y)==1 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)