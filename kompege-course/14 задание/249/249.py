def cc3(x):
    a = []
    while x>0:
        a = [x%3] + a
        x //= 3
    return ''.join([str(i) for i in a])

for x in range(21, 30):
    if 20 < x < 30 and cc3(x)[-2:]=='11':
        print(x)