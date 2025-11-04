from turtle import *

tracer(0)
screensize(5000, 5000)
s = 60

for i in range(15):
    fd(7 * s)
    rt(30)
    fd(8 * s)
    rt(150)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 28