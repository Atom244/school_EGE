# https://education.yandex.ru/ege/task/d326e2e1-9711-4d6e-9d1e-6aa0da23e13c
from functools import lru_cache
import sys

sys.setrecursionlimit(6000) # преодоление лимита рекурсии

@lru_cache(None)
def F(n):
    if n <= 12:
        return 1
    if n > 12:
        return F(n - 1) + n - 2

for i in range(1, 900): # кэширование чисел? ИЛИ for i in range(1, 2025 - макс число в условии)
    F(i)

print(F(2024) - F(2020))
