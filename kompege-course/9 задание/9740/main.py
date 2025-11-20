f = open('txt')
k = 0
for s in f:
    line = [int(i) for i in s.split()]
    line_povt = [i for i in line if line.count(i) == 3]
    line_nepovt = [i for i in line if line.count(i) == 1]
    if len(line_povt) == 3 and len(line_nepovt) == 4:
        if sum(line_nepovt)/len(line_nepovt) <= line_povt[0]:
            k+=1
print(k)
