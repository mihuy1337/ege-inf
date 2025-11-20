k = 0

for s in open('txt'):
    nums = sorted([int(i) for i in s.split()])
    if nums[0]+nums[3] < nums[1]+nums[2]:
        k+=1

print(k)