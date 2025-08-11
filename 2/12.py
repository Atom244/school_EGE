# https://education.yandex.ru/ege/task/dae0ce42-122c-4ae5-b157-f8e47d13594a

for w in range(2):
    for x in range(2):
        for y in range(2):
            for u in range(2):
                F = (not ((y <= w) == x)) and u
                if int(F) == 1:
                    print(u, x, w, y, int(F))
