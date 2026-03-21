from turtle import *

tracer(0)
screensize(5000,  5000)
s = 30

lt(90)


for i in range(2):
    fd(8 * s)
    rt(90)
    fd(18 * s)
    rt(90)
up()

fd(4 * s)
rt(90)
fd(10 * s)
lt(90)

down()

for i in range(2):
    fd(17 * s)
    rt(90)
    fd(7 * s)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()

# 275