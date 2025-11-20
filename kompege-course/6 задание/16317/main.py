from turtle import *
from typing import get_origin

screensize(4000, 4000)
s = 30
tracer(0)

for _ in range(2): fd(21*s); rt(90); fd(27*s); rt(90)
up()
fd(9*s); rt(90); fd(10*s); lt(90)
down()
for _ in range(2): fd(86*s); rt(90); fd(47*s); rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*s, y*s)
        dot(5, 'red')
mainloop()