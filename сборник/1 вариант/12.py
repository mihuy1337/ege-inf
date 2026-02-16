from itertools import product, repeat

commands = {
    (' ', 0): (' ', -1, 1),
    (' ', 1): (' ', 2, 1),

    ('1', 1): ('0', 2, 1),

    ('0', 1): ('1', -1, 1),
}

def mt(s):
    s = list(' ' + s + ' ')
    state = 0
    i = len(s) - 1
    while True:
        cmd = commands[(s[i], state)]
        state = cmd[2]
        if cmd[1]==2: break
        s[i] = cmd[0]
        i = i + cmd[1]
    return ''.join(s)

for n in product('01', repeat=520):
    if mt(''.join(n)).count('0')==125:
        print(n.count('0'))