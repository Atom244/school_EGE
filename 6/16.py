from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 60

lt(255)
for i in range(3):
    lt(30)
    for j in range(4):
        fd(10 * s)
        lt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 56