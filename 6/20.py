from turtle import *

tracer(0)
lt(90)
screensize(5000, 5000)
s = 40

for i in range(2):
    fd(23 * s)
    lt(90)
    bk(27 * s)
    lt(90)

up()

bk(5 * s)
rt(90)
fd(11 * s)
lt(90)
down()

for i in range(2):
    fd(26 * s)
    rt(90)
    fd(32 * s)
    rt(90)



up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 1189