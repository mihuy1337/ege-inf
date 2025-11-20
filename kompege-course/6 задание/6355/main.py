from turtle import *

screensize(2000, 2000)
s = 40
tracer(0)

for _ in range(3): fd(7*s); rt(90)
fd(8*s)
for _ in range(3): lt(90); fd(5*s)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(3, 'red')

mainloop()