from turtle import *

tracer(0)
screensize(8000, 8000)
s = 20

degree = 0

lines_count = 0

for i in range(100):
    lines_count += 1
    dot(7, 'red')
    fd(10*s)
    rt(30)
    degree += 30
    if degree == 360:
        break

up()

print(lines_count)

mainloop()
