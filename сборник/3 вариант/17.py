nums = [int(i) for i in open('17.txt')]

trs = [
    [nums[ind], nums[ind + 1], nums[ind + 2]] for ind in range(len(nums)-2)
]

mn = min(i for i in nums if abs(i)%1000==500)

ans = []

for tr in trs:
    if all(abs(num)%2!=0 for num in tr):
        if sum(tr)>mn:
            ans.append(tr)

print(
    len(ans), min(sum(tr) for tr in ans)
)