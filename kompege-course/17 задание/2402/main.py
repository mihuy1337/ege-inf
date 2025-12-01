nums = [int(i) for i in open('17_2402.txt')]

trpls = [[nums[ind - 1], nums[ind], nums[ind + 1]] for ind in range(1, len(nums) - 1)]

def to3(n):
    k = []
    while n>0:
        k = [n%3] + k
        n = n // 3
    return ''.join([str(k) for k in k])
sort_trpls = []
for t in trpls:
    if any(to3(num)[-1]=='2' for num in t):
        sort_trpls.append(t)

print(
    len(sort_trpls),
    sum([min(t) for t in sort_trpls])
)