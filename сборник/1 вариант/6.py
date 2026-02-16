from turtle import *

tracer(0)
screensize(2000, 2000)
s = 30

for _ in range(4):
    fd(9*s)
    lt(180)
    bk(10*s)
    rt(90)

up()

bk(7*s)
lt(90)
fd(3*s)
rt(90)

down()

for _ in range(2):
    fd(17*s)
    lt(90)
    fd(20*s)
    lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(4, 'green')
mainloop()