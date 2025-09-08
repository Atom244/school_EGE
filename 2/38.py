from itertools import *

def f(x,y,z,w):
    return (x == (not y)) <= ((x and w) == z) # само условие

for a1,a2,a3,a4,a5 in product([0,1], repeat=5): # перебор неизвестных в табличке(по их кол-ву)
    table = [(1,1,a1,a2),
             (1,1,a3,1),
             (a4,1,1,a5)]
    if len(table) == len(set(table)):# проверка на отстутствие дубликатов, если есть незвестные
        for p in permutations('xyzw'):# перебор самих букв, которые используются
            if [f(**dict(zip(p,row))) for row in table] == [0,0,0]: # в конце таблица с F
                print("ВОТ ТВОЙ ОТВЕТ, ПУПЕПЧИК:",*p)
