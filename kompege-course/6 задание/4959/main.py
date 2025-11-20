from turtle import *

screensize(1000, 1000)

s = 40
tracer(0)

fd(9*s); rt(90)
for _ in range(2): fd(3*s); rt(90); fd(3*s); rt(270)
for _ in range(2): fd(3*s); rt(90)
fd(9*s)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(3, 'green')

mainloop()