nums = [int(num) for num in open('17.txt')]

trs = [[nums[ind], nums[ind+1], nums[ind+2]] for ind in range(0, len(nums)-2)]
mi = min(x for x in nums if 10<=abs(x)<=99)
ma = max(x for x in nums if 10<=abs(x)<=99)
ans = []

for tr in trs:
    if sum(10<=abs(x)<=99 for x in tr)>=2:
        if sum(tr)>ma+mi:
            ans.append(tr)
print(
    len(ans), max(sum(tr) for tr in ans)
)