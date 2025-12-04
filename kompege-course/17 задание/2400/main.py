nums = [int(i) for i in open('17_2400.txt')]

pars = [
    [nums[ind], nums[ind + 1]] for ind in range(len(nums)-1)
]

sort_pars = [par for par in pars if sum(par)>=100 and any(i<0 for i in par)]

print(
    len(sort_pars),
    max(i[0]*i[1] for i in sort_pars)
)