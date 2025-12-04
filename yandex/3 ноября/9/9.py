k = 0

for row in open('9.txt'):
    nums = sorted([int(num) for num in row.split()])
    if len(set(nums)) == len(nums):
        if (min(nums)+max(nums))/2 > (nums[1]+nums[2])/2:
            k += 1
            print(k, nums)
