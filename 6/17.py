from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 40


for i in range(2):
    fd(21*s)
    rt(90)
    fd(27 * s)
    rt(90)
up()
fd(9 * s)
rt(90)
fd(10 * s)
lt(90)
down()
for i in range(2):
    fd(86 * s)
    rt(90)
    fd(47 * s)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 234