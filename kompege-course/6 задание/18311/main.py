from turtle import *

tracer(0)
screensize(2000, 2000)
s = 40

for _ in range(5): fd(15*s); lt(90); fd(25*s); lt(90)
up()
fd(4*s); lt(90); fd(12*s); lt(90)
down()
for _ in range(6): fd(38*s); rt(90); fd(22*s); rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(5, 'red')

mainloop()