from string import *
print(printable[:23])
for x in printable[:23]:
    arif = int(f'324{x}72', 23) + int(f'45{x}562', 23)
    if arif%22==0:
        print(int(x, 23)//22)
