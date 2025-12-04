from itertools import *

def f(w, y, z, x):
    return (not (y<=w)) or (x<=z)

for t1, t2, t3, t4 in product([0, 1], repeat=4):
    table = [(1, 1, 0, t1), (t2, 1, t3, 0),
             (1, 1, 0, t4)]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table]==[0,0,0]:
                print(''.join(p)) 
