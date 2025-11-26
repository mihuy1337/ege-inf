from turtle import *

screensize(2000, 1000)
s=40
tracer(0)

for _ in range(2): fd(14*s); lt(270); backward(12*s); rt(90)
up()
fd(9*s); rt(90); backward(7*s); lt(90)
down()
for _ in range(2): fd(13*s); rt(90); fd(6*s); rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(4, 'green')
mainloop()






















