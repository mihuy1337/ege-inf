from math import dist
from turtle import *

def t(cls, k=10):
    tracer(0)
    up()
    for cl in cls:
        for x, y in cl:
            goto(x*k, y*k)
            dot(8, 'black')
    mainloop()

cla = [[], []]

for s in open('27A_25446.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x>20: pass
    elif y>10: cla[0].append([x, y])
    else: cla[1].append([x, y])
clb = [[], [], []]
for s in open('27B_25446.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if y>25 or y<0: pass
    elif x>24: clb[0].append([x, y])
    elif y>16: clb[1].append([x, y])
    else: clb[2].append([x, y])

def c(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

px = max(c(cla[0])[0], c(cla[1])[0])
py = max(c(cla[0])[1], c(cla[1])[1])

q1 = dist(
    c(clb[1]), c(clb[0])
)
q2 = max(dist(c(cl), d) for cl in clb for d in cl)
print(int(px*10000), int(py*10000))
print(int(q1*10000), int(q2*10000))