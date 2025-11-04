from turtle import *

tracer(0)

screensize(5000, 5000)
s = 60

for i in range(3):
    down()
    for j in range(2):
        fd(7 * s)
        rt(90)
        fd(7 * s)
        rt(90)
    up()
    fd(6 * s)
    rt(90)
    fd(6 * s)
    lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

mainloop()
# 76
# https://vkvideo.ru/video-205865487_456240451