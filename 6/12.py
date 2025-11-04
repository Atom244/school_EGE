from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 60

for i in range(3):
    fd(7 * s)
    rt(90)
fd(8 * s)

for j in range(3):
    lt(90)
    fd(5 * s)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 43