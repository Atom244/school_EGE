from turtle import *

tracer(0)
screensize(5000, 5000)
s = 90

fd(9 * s)
rt(90)
for i in range(2):
    fd(3 * s)
    rt(90)
    fd(3 * s)
    rt(270)
for j in range(2):
    fd(3 * s)
    rt(90)
fd(9 * s)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')
mainloop()
# 73