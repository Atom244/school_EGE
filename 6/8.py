from turtle import *

tracer(0)
screensize(5000, 5000)
s = 60

for i in range(14):
    for j in range(3):
        fd(3 * s)
        rt(90)
    lt(180)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')
mainloop()
# 28