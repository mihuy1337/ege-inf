def to14(n):
    k = []
    while n:
        k = [n%32] + k
        n = n//32
    return k

n = 5*512**1000 + 256**1001 - 128**1002 + 64**1003 - 7*32**1004 - 5120

print(
    len([i for i in to14(n) if i<=9])
)