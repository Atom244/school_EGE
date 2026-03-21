from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n-1)-2*g(n-1)

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    return f(n-1)+g(n-1)+n

print(sum([int(s) for s in str(g(36))]))