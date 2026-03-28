ans = []

for n in 1, 3, 5, 7, 9:
    for h in 0, 2, 4, 6, 8:
        num = int(f'{h}{n}{h}{h}{n}{h}{n}77')
        if num%7777==0 and num<=10**9:
            ans.append(num)

for a in ans:
    print(a, a//7777)