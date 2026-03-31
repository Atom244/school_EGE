from functools import lru_cache

@lru_cache(None)
def f(c,e):
    if c > e: return 0
    if c == e: return 1
    return f(c+1,e) + f(c+2,e) + f(c*4,e)

print(f(1,13))