# https://education.yandex.ru/ege/task/285d3aa4-19eb-4b9e-99cf-2f5219cc6027
for a in range(2):
    for b in range(2):
        for c in range(2):
            F = b == a or c <= b and b == (a or (c <= b))
            if int(F) == 1:
                print(a, c, b, int(F))

# Не обращай внимания на порядок, в котором идут нули и единицы в таблице. Для решения задачи важно только их количество в строчках или столбцах.
