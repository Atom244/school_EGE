from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n >= 2 and n%2==0:
        return f(n/2) + 1
    if n >= 2 and n%2!=0:
        return f(n-1) + n

for k in range(1,10000):
    if f(k) == 19:
        print(k)
