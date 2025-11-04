from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 60

def vec(x, y):
    goto(xcor() + x * s, ycor() + y * s)

for i in range(2):
    vec(6,2)
    vec(0,-2)

for i in range(3):
    vec(2,-1)
    vec(-2,-1)

for i in range(6):
    vec(-2, 1)




up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 54