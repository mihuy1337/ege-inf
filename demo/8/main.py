from itertools import *
c=0
for word in product(sorted('строка'), repeat=5):
    c += 1
    if word[0] not in 'аст' and word.count('о')==2:
        print(c, ''.join(word))
print(c)