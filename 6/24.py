from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 60

def vec(x, y):
    goto(xcor() + x * s, ycor() + y * s)

for i in range(5):
    vec(5,4)
    vec(4,-4)
    vec(-7,-2)
    vec(-2,2)




up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 27