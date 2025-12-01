nums = [int(i) for i in open('17_1999.txt')]

trpls = [
    [
        nums[ind - 1], nums[ind], nums[ind + 1]
    ] for ind in range(1, len(nums) - 1)
]
sort_trpls = []
for trpl in trpls:
    if any(num%12==0 for num in trpl):
        if all(num%3==0 for num in trpl):
            sort_trpls.append(trpl)

print(
    len(sort_trpls),
    min([sum(trpl)/len(trpl) for trpl in sort_trpls])
)
