# https://education.yandex.ru/ege/task/768a7194-db18-4b74-ac4a-43d063659eb9
import sys
from functools import lru_cache
sys.setrecursionlimit(5000)

@lru_cache(None)
def F(n):
    if n >= 2024:
        return 1
    else:
        return F(n + 2) + F(n + 4)


lst = []
for i in range(1, 2025):
    lst.append(F(i))

set_lst = set(lst)

print(len(set_lst))
