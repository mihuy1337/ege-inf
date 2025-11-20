from turtle import *

screensize(2000, 2000)
tracer(0)
s = 60

for _ in range(8):
    for _ in range(4):
        fd(5*s); rt(30); fd(6*s); rt(150)
    rt(60)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(3, 'red')

mainloop()