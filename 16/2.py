# https://education.yandex.ru/ege/task/9178fe45-2340-4140-a4af-eb341dee3d78
import sys
from functools import lru_cache

sys.setrecursionlimit(2500)

@lru_cache(None)
def F(n):
    if n <= 1:
        return 42
    elif n > 1 and n % 2 == 0:
        return F(n-2) + F(n-3) + n
    else:
        return F(n - 1) + F(n - 3) - n

for i in range(100):
    F(i)

print(F(99))
