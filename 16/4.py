# https://education.yandex.ru/ege/task/c2de1849-f600-4507-8972-bf4117c7fc31
# ошибка условия - ответ 82664462 хотя реальный ответ 82664463
import sys
from functools import lru_cache

sys.setrecursionlimit(3000)

@lru_cache(None)
def F(n):
    if n == 41:
        return 41
    elif n > 41 and n % 2 == 0:
        return F(n - 1) - n
    elif n > 41 and n % 2 != 0:
        return n * F(n - 2)

for i in range(1, 9090):
    F(i)

a = F(9094)
b = F(9089)

print(a / b)
