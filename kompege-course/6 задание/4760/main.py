from turtle import *

tracer(0)
screensize(200, 200)
s = 30
for _ in range(14):
    for _ in range(3):
        fd(3*s); rt(90)
    left(180)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(3, 'violet')

mainloop()