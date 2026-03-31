from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return n
    if n > 1:
        return n * f(n-1)
for i in range(1,2024):
    f(i)
print(f(2023)/f(2020))