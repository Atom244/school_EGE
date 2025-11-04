from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 35

for i in range(2):
    fd(24 * s)
    rt(90)
    fd(10 * s)
    rt(90)
fd(3 * s)
lt(90)
fd(13 * s)
rt(90)
for i in range(2):
    fd(9 * s)
    rt(90)
    fd(32 * s)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 120