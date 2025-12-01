nums = [int(i) for i in open('17_1994.txt')]

pars = [[nums[ind], nums[ind + 1]] for ind in range(len(nums) - 1)]
print(pars)
sort_pars = [par for par in pars if par[0]*par[1]>0\
             and abs(sum(par))%7==0]
print(sort_pars)

print(len(sort_pars), min([i[0]*i[1] for i in sort_pars]))