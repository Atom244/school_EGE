from turtle import *


tracer(0)
left(90)
scale = 20
screensize(900,900)
for i in range(3):
    forward(5 * scale)
    right(90)
    forward(12 * scale)
    right(90)

up()

forward(3 * scale)
right(90)
forward(2 * scale)
right(90)

down()

for i in range(4):
    forward(5 * scale)
    right(90)
    forward(12 * scale)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * scale, y * scale)
        dot(5, 'black')

mainloop()

# 14
