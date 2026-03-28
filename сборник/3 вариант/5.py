for k in range(1000, 10000):
    nums = [int(i) for i in str(k)]
    s = sum(nums)
    m = max(nums)
    n = min(nums)
    p1 = s-m
    p2 = s-n
    l = str(p1)+str(p2)
    if int(l)==1318:
        print(k, l)
