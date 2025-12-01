nums = [int(i) for i in open('17_2016.txt')]
m = []
for num in nums:
    if num%13==7:
        if num%7 != 0 and num%11 != 0:
            m.append(num)

print(max(m)-min(m), len(m))