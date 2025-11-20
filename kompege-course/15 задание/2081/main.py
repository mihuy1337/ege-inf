from itertools import product


def f(x):
    p = set([i for i in product('01', repeat=8) if i[:2]=='11'])
    q = set([i for i in product('01', repeat=8) if i[-1]=='0'])
