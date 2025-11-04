from turtle import *

scale = 20

tracer(0)
left(90)
screensize(900,900)


up()


down()

for i in range(2):
    forward(10 * scale)
    right(90)
    forward(18 * scale)
    right(90)

up()

forward(5 * scale)
right(90)
forward(14 * scale)
left(90)

down()
for i in range(2):
    forward(17 * scale)
    right(90)
    forward(7 * scale)
    right(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scale, y * scale)
        dot(5, 'black')

mainloop()

# 30