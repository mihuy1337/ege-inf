def f(x):
    b = x in b_del
    c = x in c_del
    a = 7<=x<=26
    return c <= (a and (not b))
b_del = [i for i in range(2, 77) if 77%i==0]
for y in range(1, 10000):
    c_del = [i for i in range(2, y) if y%i==0]
    if len(c_del)!=0:
        if all(f(x)==1 for x in range(1, 10000)):
            print(y)