nums = [int(i) for i in open('17_2238.txt')]

trs = [
    [nums[ind], nums[ind + 1], nums[ind + 2]] for ind in range(len(nums) - 2)
]
sr = sum(nums)/len(nums)
m = []
for tr in trs:
    if sum(num > sr for num in tr)>=2:
        m.append(tr)

print(
    len(m),
    max(sum(tr) for tr in m)
)