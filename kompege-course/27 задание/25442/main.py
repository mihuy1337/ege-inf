from math import dist
from turtle import *

def t(cls):
    tracer(0)
    k=20
    for cl in cls:
        for x, y in cl:
            goto(x*k, y*k)
            dot(3, 'green')
    mainloop()

cla = [[], []]

for s in open('27A_25442.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x>30: pass
    elif y>10: cla[0].append([x, y])
    else: cla[1].append([x, y])

clb = [[], [], []]
for s in open('27B_25442.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x<0 or y<0 or x>44: pass
    elif y>16: clb[0].append([x, y])
    elif x>24: clb[1].append([x, y])
    else: clb[2].append([x, y])

def c(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

p1 = dist(c(cla[0]), c(cla[1]))
p2 = max(dist(c(cl), p) for cl in cla for p in cl)
print(int(p1*10000), int(p2*10000))

q1 = min(
    dist(c(clb[0]), c(clb[1])),
    dist(c(clb[1]), c(clb[2])),
    dist(c(clb[0]), c(clb[2]))
)

q2 = max(
    dist(c(clb[0]), c(clb[1])),
    dist(c(clb[1]), c(clb[2])),
    dist(c(clb[0]), c(clb[2]))
)
print(int(q1*10000), int(q2*10000))