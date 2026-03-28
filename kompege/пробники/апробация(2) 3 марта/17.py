nums = [int(i) for i in open('17.txt')]

pars = [
    [nums[ind], nums[ind + 1]] for ind in range(0, len(nums)-1)
]

mx = max(i for i in nums if 1000<=abs(i)<=9999 and abs(i)%43==0)
ans = []
for p in pars:
    if any(1000<=abs(n)<=9999 for n in p):
        if sum(p)**2 < mx**2:
            ans.append(p)

print(
    len(ans), max(sum(par)**2 for par in ans)
)
