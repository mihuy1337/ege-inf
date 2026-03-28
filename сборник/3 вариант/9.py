for r in open('9'):
    nums = [int(i) for i in r.split()]
    n2 = [i for i in nums if nums.count(i)==2]
    n1 = [i for i in nums if nums.count(i)==1]
    if len(n2+n1)==6 and len(set(n2))==2 and len(set(n1))==2:
        if sum(n1)<=sum(set(n2)):
            print(sum(nums), n2, n1)