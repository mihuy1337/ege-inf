def f(x, y):
    a = 3 <= x <= 60
    b = x in {i for i in range(2, 177) if 177%i==0}
    c = x in {i for i in range(2, y) if y%i==0}
    return c <= (a and (not b))
m = []
for y in range(2, 10000):
    if all(f(x, y)==1 for x in range(2, 1000)):
        m.append(y)
print(max(m))
