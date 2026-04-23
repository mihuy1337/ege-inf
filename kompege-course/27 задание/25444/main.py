from itertools import permutations, repeat
from math import dist
from turtle import *

def t(cls):
    tracer(0)
    up()
    k=50
    for cl in cls:
        for x, y in cl:
            goto(x*k, y*k)
            dot(8, 'green')
    mainloop()

clA = [[], []]
for s in open('27A_25444.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x>15: pass
    elif y > 10: clA[0].append([x, y])
    else: clA[1].append([x, y])

clB = [[], [], []]
for s in open('27B_25444.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if y<3 or y>6: pass
    elif y>5: clB[0].append([x, y])
    elif x<-1: clB[1].append([x, y])
    else: clB[2].append([x, y])


def c(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

c0 = c(clA[0])
c1 = c(clA[1])
d1 = [dist(c0, p) for p in clA[1]]
d2 = [dist(c1, p) for p in clA[0]]
p1 = min(d1+d2)
p2 = max(d1+d2)
print(int(p1*10000), int(p2*10000))

q1 = min(dist(i[0], i[1]) for i in permutations([c(clB[0]), c(clB[1]), c(clB[2])], 2))
q2 = max(dist(i[0], i[1]) for i in permutations([c(clB[0]), c(clB[1]), c(clB[2])], 2))
print(int(q1*10000), int(q2*10000))