nums = [int(i) for i in open('17_2401.txt')]

pars = [
    [nums[ind], nums[ind + 1]] for ind in range(len(nums)-1)
]

sort_pars = [par for par in pars\
             if (n := sum(abs(i) for i in par)) <= 200\
             and n >= 50]

print(
    len(sort_pars),
    min(min(i) for i in sort_pars)
)