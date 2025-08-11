# https://education.yandex.ru/ege/task/a0a0262b-ffa0-4fdb-a501-894d30e26aa9

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((1 == w) == (not ((w and x) or y))) <= z
                print(x, z, y, w, int(F))