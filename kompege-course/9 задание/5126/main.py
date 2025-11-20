f = open('txt')
k=0
for stroke in f:
    nums = sorted([int(num) for num in stroke.split()])
    nums1 = [i for i in nums if nums.count(i) == 3]
    nums2 = [i for i in nums if nums.count(i) == 1]
    if len(nums1) == 3 and len(nums2) == 3:
        if sum(nums2)/len(nums2) <= sum(nums1):
            print(nums, nums1, nums2)
            k+=1
print(k)