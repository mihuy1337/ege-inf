from turtle import *

screensize(2000, 2000)
tracer(0)
s = 30
lt(90)

rt(90)
for _ in range(3): fd(15*s); rt(90); fd(20*s); rt(90)
up()
fd(7*s); rt(90); fd(13*s); lt(90)
down()
for _ in range(2): fd(10*s); lt(90); fd(17*s); lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(4, 'green')
        
