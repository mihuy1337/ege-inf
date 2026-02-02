def to3(n):
    k = ''
    while n:
        k = str(n%3) + k
        n = n//3
    return k

m = set()

def f(curr, end, step=0):
    if curr>end: return 0
    if curr==end and step!=15: return 0
    if curr==end and step==15: return 1
    if curr<end:
        return f(curr*2, end)+f(curr*2+1, end)

for n in range(1, 1000):
    if f(1, n)==15:
        m.add(to3(n))
print(len(m))

## неправильно