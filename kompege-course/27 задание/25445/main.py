from math import dist
from turtle import *

def t(cls, k=10):
    tracer(0)
    up()
    for cl in cls:
        for x, y in cl:
            goto(x*k, y*k)
            dot(8, 'green')
    mainloop()
cla = [[], []]
for s in open('27A_25445.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x<-5 or y<-5: pass
    elif y>5: cla[0].append([x, y])
    else: cla[1].append([x, y])

clb = [[], [], []]
for s in open('27B_25445.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if y>30 or y<0: pass
    elif y>16: clb[0].append([x, y])
    elif x>25: clb[1].append([x, y])
    else: clb[2].append([x, y])

def c(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

px = abs(
    c(cla[0])[0] - c(cla[1])[0]
)
py = abs(
    c(cla[0])[1] - c(cla[1])[1]
)
qx = (
   c(clb[0])[0] +  c(clb[1])[0] + c(clb[2])[0]
)/3
qy = (
   c(clb[0])[1] +  c(clb[1])[1] + c(clb[2])[1]
)/3

print(int(px*10000), int(py*10000))
print(int(qx*10000), int(qy*10000))