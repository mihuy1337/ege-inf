from turtle import *

tracer(0)
screensize(2000, 2000)
s = 25

for _ in range(4):
    fd(19*s); lt(180); backward(10*s); rt(90)
up()
backward(5*s); lt(90); fd(4*s); rt(90)
down()
for _ in range(2):
    fd(15*s); lt(90); fd(8*s); lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(4, 'green')
mainloop()