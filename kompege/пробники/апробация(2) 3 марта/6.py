from turtle import *

screensize(2000, 2000)
s = 30
tracer(0)

for _ in range(2):
    fd(1*s); lt(270); fd(16*s); rt(90)
up()
bk(4*s); rt(90); fd(10*s); lt(90)
down()
for _ in range(2):
    fd(17*s); rt(90); fd(7*s); rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(4, 'green')

mainloop()