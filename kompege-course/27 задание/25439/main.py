from math import dist

clA = [[], []]

for s in open('27A_25439.txt'):
    x, y = [float(c) for c in s.replace(',', '.').split()]
    if y>25 or x>20: pass
    elif y>15: clA[0].append([x, y])
    else: clA[1].append([x, y])


clB = [[], [], []]
for s in open('27B_25439.txt'):
    x, y = [float(c) for c in s.replace(',', '.').split()]
    if x < -2 or x>0: pass
    elif y>5: clB[0].append([x, y])
    elif x<-1.25 and y<5: clB[1].append([x, y])
    else: clB[2].append([x, y])

def center(cl):
    for p in cl:
        m = []
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

x0, y0 = center(clA[0])
x1, y1 = center(clA[1])
print(int(min(x0,x1)*10000), int(min(y0,y1)*10000))

q1 = min([len(clB[0]), len(clB[1]), len(clB[2])])
q2 = max([len(clB[0]), len(clB[1]), len(clB[2])])
print(q1, q2)
