nums = [int(i) for i in open('17_2310.txt')]

on4 = [i for i in nums if i%10==4]
sm = min(on4)+max(on4)
pars = [
    [nums[ind], nums[ind + 1]] for ind in range(len(nums)-1)
]

print(
    len([par for par in pars if sum(par)<sm]),
    max(sum(par) for par in pars if sum(par)<sm)
)