for k, l in enumerate(open('9'), 1):
    nums = [int(i) for i in l.split()]
    n4 = [i for i in nums if nums.count(i)==4]
    n1 = [i for i in nums if nums.count(i)==1]
    if len(set(n4))==1 and len(set(n1))==3:
        if sum(n1)<sum(n4):
            print(k, nums)