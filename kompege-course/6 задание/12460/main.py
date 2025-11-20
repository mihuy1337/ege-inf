from turtle import *

screensize(2000, 2000)
tracer(0)
s = 40

for _ in range(3):
    down()
    for _ in range(2): fd(7*s); rt(90); fd(7*s); rt(90)
    up()
    fd(6*s); rt(90); fd(6*s); lt(90)

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(5, 'red')

mainloop()