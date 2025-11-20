from turtle import *

screensize(2000, 2000)
s = 50
tracer(0)

for _ in range(15): fd(7*s); rt(30); fd(8*s); rt(150)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(5, 'red')

mainloop()