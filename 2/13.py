# https://education.yandex.ru/ege/task/dae0ce42-122c-4ae5-b157-f8e47d13594a

for x in range(2):
    for y in range(2):
        for w in range(2):

            F = (x <= y) and (w or (not w))

            print(w, x, y, int(F))
