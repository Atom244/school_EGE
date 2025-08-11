# https://education.yandex.ru/ege/task/4820b374-36df-4864-912e-ac63edcbab34

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (not ((((((w and x) == x) or 1) <= z) or (not x)) and y))
                if int(F) == 0:
                    print(y, x, z, w, int(F))
