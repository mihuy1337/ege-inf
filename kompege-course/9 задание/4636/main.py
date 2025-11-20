k = 0

for s in open('txt'):
    nums = sorted([int(i) for i in s.split()])
    if (max(nums) - min(nums) >= 50) and (nums[1]*nums[2] <= 1000):
        k+=1

print(k)