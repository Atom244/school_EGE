# https://education.yandex.ru/ege/task/1f39750d-897a-4bd0-a261-4233cd2cdca4

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and y) or ((z == y) and w)
                print(w, y, x, z, int(F))
