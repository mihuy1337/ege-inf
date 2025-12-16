command = {
    (' ', 0): (' ', 1, 1),
    (' ', 1): (' ', 2, 1),
    ('1', 1): ('0', 1, 1),
    ('0', 1): ('1', 1, 1)
}

def mt(s):
    s = list(' ' + s + ' ')
    q = 0
    i = 0
    while True:
        cmd = command[(s[i], q)]
        s[i] = cmd[0]
        if cmd[1]==2: break
        i += cmd[1]
        q = cmd[2]
    return ''.join(s)

print(
    int(mt(f'{400:b}'), 2)
)
