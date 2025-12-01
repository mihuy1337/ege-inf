nums = [int(i) for i in open('17_2017.txt')]
m = []
for num in nums:
    if hex(num)[2:][-1]=='b':
        if num%7==0 and num%6!=0 and num%13!=0 and num%19!=0:
            m.append(num)
print(sum(m), len(m))