# https://education.yandex.ru/ege/task/c498e786-aabe-4366-99dc-113c59f3de18

for p1 in range(2):
    for p2 in range(2):
        for p3 in range(2):
            for p4 in range(2):
                F = (p3 <= p1) <= (p4 or not p2)
                if int(F) == 0:
                    print(p3, p1, p4, p2, int(F))

# answer: ywxz
# Не обращай внимания на порядок, в котором идут нули и единицы в таблице. Для решения задачи важно только их количество в строчках или столбцах.