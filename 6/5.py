from turtle import *

tracer(0)
screensize(8000, 8000)
s = 20
for i in range(100):
    dot(7, 'red')
    fd(10*s)
    rt(8)

up()


mainloop()
# черепашка делает повторы через 360 градусов так что ответ 360/8=45 отрезков