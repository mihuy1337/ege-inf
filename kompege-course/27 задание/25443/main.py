from math import dist
from turtle import *

def t(cls):
    up()
    tracer(0)
    k = 10
    for cl in cls:
        for x, y in cl:
            goto(x*k, y*k)
            dot(8, 'purple')
    mainloop()

cla = [[], []]

for s in open('27A_25443.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if x<-4 or y<-15: pass
    elif y>16: cla[0].append([x, y])
    else: cla[1].append([x, y])
clb = [[], [], []]
for s in open('27B_25443.txt'):
    x, y = [float(i) for i in s.replace(',', '.').split()]
    if y<-18 or y>24: pass
    elif x > 20: clb[0].append([x, y])
    elif y>12: clb[1].append([x, y])
    else: clb[2].append([x, y])

def c(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

p1 = dist(c(cla[0]), c(cla[1]))
p2 = max(dist(c(cl), d) for cl in cla for d in cl)

qx = (c(clb[0])[0] + c(clb[1])[0] + c(clb[2])[0])/3
qy = (c(clb[0])[1] + c(clb[1])[1] + c(clb[2])[1])/3

print(int(p1*10000), int(p2*10000))
print(int(qx*10000), int(qy*10000))