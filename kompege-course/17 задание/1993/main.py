nums = [int(i) for i in open('17_1993 (1).txt')]

pars = [[nums[ind], nums[ind + 1]] for ind in range(len(nums) - 1)]

sort_pars = []

for par in pars:
    if abs(sum(par))%3==0 and abs(sum(par))%6!=0:
        if abs(par[0]*par[1])%10==8:
            sort_pars.append(par)

print(len(sort_pars), max([sum(par) for par in sort_pars]))
