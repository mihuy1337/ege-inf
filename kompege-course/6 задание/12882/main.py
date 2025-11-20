from turtle import *

screensize(2000, 2000)
tracer(0)
s = 40

lt(255)
for _ in range(3):
    lt(30)
    for _ in range(4):
        fd(10*s); left(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(5, 'red')
mainloop()