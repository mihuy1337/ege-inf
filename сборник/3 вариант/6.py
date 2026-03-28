from turtle import *

screensize(2000, 2000)
tracer(0)
s = 30

for _ in range(2):
    fd(9*s); rt(90); fd(5*s); rt(270)

bk(18*s); lt(90); fd(10*s); rt(90)

up()
fd(5*s); rt(90); fd(4*s); lt(90)
down()
for _ in range(4):
    fd(5*s); rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(4, 'green')
mainloop()