from turtle import *

tracer(0)
screensize(5000, 5000)
s = 80

for i in range(16):
    lt(36)
    fd(4 * s)
    lt(36)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 31