k=0

for s in open('txt'):
    nums = sorted([int(i) for i in s.split()])
    if (max(nums)**3 >= 2*nums[0]*nums[1]*nums[2])\
        and all(i>10 for i in nums):
        k+=1

print(k)