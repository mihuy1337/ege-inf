def to14(n):
    k = []
    while n:
        k = [n%14] + k
        n = n//14
    return k

num = 4*2187**2101 + 729**2000 - 5*243**2100 + 81**2200 - 3*27**2250 - 26244

print(
    len([i for i in to14(num) if i>9])
)