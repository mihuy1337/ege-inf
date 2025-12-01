nums = [int(i) for i in open('17_2013.txt')]
m = []
for num in nums:
    if num%10==2 or num%10==7:
        if num%3==0 and num%11==0:
            m.append(num)

print(len(m), min(m))