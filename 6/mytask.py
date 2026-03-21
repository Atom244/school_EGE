from turtle import *
tracer(0)
screensize(5000, 5000)
s = 60

def vec(x, y):
    goto(xcor() + x * s, ycor() + y * s)
vec(0,2)
vec(2,0)
vec(1,5)
vec(3,0)
vec(1,-5)
vec(2,0)
vec(0, -2)


up()

goto(0,0)
lt(90)
fd(2 * s)
rt(90)
down()
fd(7 * s)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 34