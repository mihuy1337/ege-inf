nums = [int(i) for i in open('17_2309.txt')]

kr = lambda x: [i for i in nums if i%x==0]

if len(kr_11 := kr(11)) > len(kr_17 := kr(17)):
    print(len(kr_11), min(kr_11))
else:
    print(len(kr_17), max(kr_17))