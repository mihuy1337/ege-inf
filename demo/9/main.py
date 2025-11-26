k = 0

for line in open('9'):
    k += 1
    nums = [int(num) for num in line.split()]
    povt = [x for x in nums if nums.count(x)==3]
    ne_povt = [x for x in nums if nums.count(x)==1]
    if len(set(povt))==1 and len(set(ne_povt))==4:
        if sum(ne_povt)/len(ne_povt) <= povt[0]:
            print(k)
