nums = [int(i) for i in open('17.txt')]

trs = [
    [nums[ind], nums[ind+1], nums[ind+2]] for ind in range(0, len(nums)-2)
]

mn = min(i for i in nums if 100<=abs(i)<999)
mx = max(i for i in nums if 100<=abs(i)<999)
m = []
for tr in trs:
    if sum(100<=abs(i)<=999 for i in tr)>=2:
        if sum(tr)>mx+mn:
            m.append(tr)
print(
    len(m), max(sum(tr) for tr in m)
)