from turtle import *
s = 20
screensize(5000, 5000)
tracer(0)

for i in range(2):
    forward(5 * s)
    right(90)
    forward(11 * s)
    right(90)

up()

forward(-4 * s)
right(90)
forward(6 * s)
left(90)

down()

for i in range(2):
    forward(42 * s)
    right(90)
    forward(63 * s)
    right(90)

# коорд точки
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x * s, y * s)
        dot(3, 'red')
print(126*2 + 12+5 + 42 + 42 - 5)

mainloop()
