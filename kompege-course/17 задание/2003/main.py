nums = [int(i) for i in open('17_2003.txt')]

s_nums = [i for i in nums if i%3==0\
          and i%17!=0 and i%7!=0 and i%19!=0 and i%27!=0]

print(len(s_nums), max(s_nums))