from fnmatch import *

for n in range(0, 10**10, 7993):
    if fnmatch(f'{n}', '4*4736*1'):
        print(n, n//7993)