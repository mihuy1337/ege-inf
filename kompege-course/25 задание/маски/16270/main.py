from itertools import *
from fnmatch import *

for a1, a2, a3 in product('0123456789', repeat=3):
    n = f'12{a1}345{a2}67089{a3}'
    if fnmatch(n, '12?345?67089?') and int(n)%206==0:
        print(n, int(n)//206)