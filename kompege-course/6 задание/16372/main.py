from turtle import *

screensize(4000, 4000)
tracer(0)
s = 20

for _ in range(2): fd(23*s); lt(90); backward(27*s); lt(90)
up()
backward(5*s); rt(90); fd(11*s); lt(90)
down()
for _ in range(2): fd(26*s); rt(90); fd(32*s); rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(5, 'red')
mainloop()