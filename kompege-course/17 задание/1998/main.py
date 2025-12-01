nums = [int(i) for i in open('17_1998.txt')]

triples = [[nums[ind - 1], nums[ind], nums[ind + 1]] for ind in range(1, len(nums) - 1)]

sort_triple = [triple for triple in triples\
               if abs(triple[0]*triple[1]*triple[2])%7==0\
               and abs(sum(triple))%10==5]

print(len(sort_triple), max([sum(i) for i in sort_triple]))