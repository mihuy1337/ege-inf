from itertools import *

print(len([''.join(i) for i in list(product('САЛО', repeat=6)) if 1 <= i.count('О') <= 3]))