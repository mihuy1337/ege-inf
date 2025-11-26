def to11(n):
    k = []
    while n>0:
        k = [n%11] + k
        n = n//11
    return k
#
# print(len(
#     to27(2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561)
# ))
#
# print(len(
#     [i for i in to27(2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561) if i > 9]
# ))
# import string
# for x in string.printable[:29]:
#     arif = int(f'923{x}874', 29) + int(f'524{x}6152', 29)
#     if arif%28==0: print(arif/28)

for x in range(0, 3000 + 1):
    cc11 = to11(9*11**210 + 8*11**150 - x)
    if cc11.count(0) == 60:
        print(x)