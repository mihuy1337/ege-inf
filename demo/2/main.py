from itertools import *

def f(w, x, y, z):
    return (x or y) and (not (y==z)) and (not w)

for t1, t2, t3, t4 in product([0, 1], repeat=4):
    table = (
        (1, t1, 1, t2),
        (0, 1, t3, 0),
        (t4, 1, 1, 0)
    )
    if len(table)==len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, row))) for row in table]==[1,1,1]:
                print(''.join(p))
# zyxw