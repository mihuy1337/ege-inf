from math import dist
from turtle import *

cla = [[], []]

for s in open('27A_25441.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x<0 or y<0: pass
    elif y>18: cla[0].append([x, y])
    else: cla[1].append([x, y])

def t(cls):
    tracer(0)
    k = 10
    up()
    for cl in cls:
        for x, y in cl:
            goto(x*k, y*k)
            dot(3, 'green')
    mainloop()
clb = [[], [], []]
for s in open('27B_25441.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x<-2 or x>0: pass
    elif y>5: clb[0].append([x, y])
    elif x<-1: clb[1].append([x, y])
    else: clb[2].append([x, y])

def c(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

x0, y0 = c(cla[0])
x1, y1 = c(cla[1])
print(
    int(abs(x0-x1)*10000), int(abs(y0-y1)*10000)
)

# print(len(clb[0]), len(clb[1]), len(clb[2]))
q1 = dist(
    c(clb[0]), c(clb[1])
)
# q2 = max(dist(c(cl), p) for cl in clb for p in cl )

q2 = []
for cl in clb:
    for p in cl:
        q2.append(dist(c(cl), p))
print(
    int(q1*10000), int(max(q2)*10000)
)