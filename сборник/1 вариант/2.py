from itertools import *

def f(w, x, y, z):
    return x <= (not((y<=z) and (z == (not w))))

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (0, a1, a2, 0),
        (a4, 1, 1, a3),
        (a5, 1, 0, 0)
    ]

    if len(set(table))==3:
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, i))) for i in table]==[0,0,0]:
                print(''.join(p))