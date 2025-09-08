from itertools import *

def f(x,y,z):
    return (x <= y) and (y <= z) # само условие

table = [(1,0,0), # табличку переписать
         (1,0,1)]

for p in permutations('xyz'):# перебор самих букв, которые используются
    if [f(**dict(zip(p,row))) for row in table] == [0,1]: # в конце столбец с F
        print("ВОТ ТВОЙ ОТВЕТ, ПУПЕПЧИК:",*p)