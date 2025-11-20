k = 0

for s in open('txt'):
    nums = sorted([int(i) for i in s.split()])
    if (max(nums)<nums[0]+nums[1]+nums[2]) and len(set(nums)) == 3:
        k += 1

print(k)