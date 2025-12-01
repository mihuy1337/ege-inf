nums = [int(i) for i in open('17_2015.txt')]

s_nums = [i for i in nums if (i%10==5 or i%10==7)\
          and (i%9!=0 and i%11!=0)]

print(len(s_nums), max(s_nums)+min(s_nums))