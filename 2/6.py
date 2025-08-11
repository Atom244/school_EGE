# https://education.yandex.ru/ege/task/b8cff36c-8515-44c7-a164-9614e0c139b5

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = w and (x == (z <= y))
                if int(F) == 1:
                    print(y, w, z, x, int(F))
