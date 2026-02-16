for k, r in enumerate(open('9')):
    k += 1
    nums = [int(i) for i in r.split()]
    n3 = [n for n in nums if nums.count(n)==3]
    n1 = [n for n in nums if nums.count(n) == 1]
    if len(set(n3))==1 and len(set(n1))==4:
        if sum(n1)>sum(n3):
            print(k, nums)