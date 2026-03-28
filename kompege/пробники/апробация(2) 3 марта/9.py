k=0

for r in open('9'):
    nums = sorted([int(i) for i in r.split()])
    if len(set(nums))==len(nums):
        if (max(nums) + min(nums))*2 == sum(nums[1:len(nums)-1]):
            print(nums)
            k += 1

print(k)