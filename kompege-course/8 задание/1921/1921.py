from itertools import *
c=0
for number in product('0123456789', repeat=3):
    if number[0] != '0' and (int(number[0]) <= int(number[1]) <= int(number[2])):
        print(number)
        c+=1
print(c)