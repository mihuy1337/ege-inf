from itertools import *
count=0
for i in product('abcd', repeat=4):
    s = ''.join(i)
    if s[0]<=s[1]<=s[2]<=s[3]:
        count+=1
print(count)