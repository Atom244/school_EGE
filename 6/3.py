
# просто рисунки

from turtle import *
import random
colormode(255)

tracer(20)
left(90)
scale = 20

for i in range(700):
    color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    forward(i)
    right(i)


mainloop()