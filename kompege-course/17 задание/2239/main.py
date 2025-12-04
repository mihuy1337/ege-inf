nums = [int(i) for i in open('17_2239.txt')]

pars = [
    [nums[ind], nums[ind + 1]] for ind in range(len(nums)-1)
]
mx = max(i for i in nums if i%19==0)
sort_pars = [par for par in pars\
             if any(num>mx for num in par)]

print(
    len(sort_pars),
    min(sum(par) for par in sort_pars)
)