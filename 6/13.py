from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 60

for i in range(5):
    fd(15 * s)
    lt(90)
    fd(25 * s)
    lt(90)
up()
fd(4 * s)
lt(90)
fd(12 * s)
lt(90)
down()

for j in range(6):
    fd(38 * s)
    rt(90)
    fd(22 * s)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 34