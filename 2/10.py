# https://education.yandex.ru/ege/task/7a1cd054-b366-41c5-b596-99e0d45835fd

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (y == (not w)) <= ((not (w and (x == (x or (w <= z))))))
                if int(F) == 1:
                    print(y, z, w, x, int(F))
