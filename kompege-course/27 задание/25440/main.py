from math import dist
from turtle import *

cla = [[], []]

for s in open('27A_25440.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x<-30 or y<-45: pass
    elif y>7: cla[0].append([x, y])
    else: cla[1].append([x, y])

k=50
def t(cl):
    tracer(0)
    up()
    for c in cl:
        for x, y in c:
            goto(x*k, y*k)
            dot(3, 'red')

clb = [[], [], []]
for s in open('27B_25440.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x<-2 or x>0: pass
    elif y>5: clb[0].append([x, y])
    elif x<-1: clb[1].append([x, y])
    else: clb[2].append([x, y])

def center(cl):
    m = []
    for p in cl:
        c = sum(dist(p, p1) for p1 in cl)
        m.append([c, p])
    return min(m)[1]

x0, y0 = center(cla[0])
x1, y1 = center(cla[1])
print(int(max(x0, x1)*10000), int(max(y0, y1)*10000))

qx = int(((center(clb[0])[0] + center(clb[1])[0] + center(clb[2])[0])/3)*10000)
qy = int(((center(clb[0])[1] + center(clb[1])[1] + center(clb[2])[1])/3)*10000)
print(abs(qx), qy)

