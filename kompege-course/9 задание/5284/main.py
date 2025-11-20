f = open('txt')
k = 0
for s in f:
    l = sorted([int(i) for i in s.split()])
    l_3 = [i for i in l if l.count(i) == 3]
    l_razn = [i for i in l if l.count(i) == 1]
    if len(l_3) == 3 and len(l_razn) == 3:
        if (l[0]+l[-1])**2 > (l[1]**2 + l[2]**2 + l[3]**2 + l[4]**2):
            print(l, l_3, l_razn)
            k+=1
print(k)