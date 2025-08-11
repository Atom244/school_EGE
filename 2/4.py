# https://education.yandex.ru/ege/task/b25eae9f-10c8-4e3d-8a9c-baf4a08a1e32

for c in range(2):
    for a in range(2):
        for t in range(2):
            for s in range(2):
                F = ((not c) <= (not a)) or not (t <= s) or c
                if int(F) == 0:
                    print(t, c, s, a, int(F))