from turtle import *

tracer(0)

screensize(5000, 5000)
s = 90



for i in range(8):
    fd(10 * s)
    rt(45)
    fd(10 * s)
    rt(135)

for i in range(4):
    fd(4 * s)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 98