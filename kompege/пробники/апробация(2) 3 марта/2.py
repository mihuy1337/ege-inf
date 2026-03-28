from itertools import *

def f(x, y, w, z):
    return ((not x) and y and (not w))\
            or ((not x) and y and (not z) and (not w))\
            or (x and y and z  and (not w))

for a1, a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):
    table = [
        (1, a1, a2, a3),
        (0, a4, 1, a5),
        (a6, 0, 0, a7)
    ]

    if len(set(table))==3:
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table]==[1,1,1]:
                print(''.join(p))