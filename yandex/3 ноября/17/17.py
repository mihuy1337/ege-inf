nums = [int(i) for i in open('17.txt')]

pars = [[nums[ind], nums[ind + 1]] for ind in range(len(nums) - 1)]
m = []
for par in pars:
    if any(1000<=num<=9999 for num in par):
        if sum(par)%min(num for num in nums if 100<=num<=999 and num%45==0):
            m.append(par)            
            

print(len(m), min(sum(par) for par in m))
