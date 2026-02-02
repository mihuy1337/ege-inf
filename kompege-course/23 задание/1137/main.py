def f(curr: int, end: int):
    if curr>end: return 0
    if curr==end: return 1
    return f(curr+1, end)\
        +f(int(f'{curr:b}1', 2), end)\
        +f(int(f'{curr:b}0', 2), end)

print(f(int('100', 2), int('11101', 2)))