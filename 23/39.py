from functools import lru_cache

@lru_cache(None)
def f(c,e,nechet):
    if c > e: return 0
    if c == e: return nechet == 1
    return f(c+1,e,nechet + 1 if (c+1)%2!= 0 else nechet) + f(c+2,e,nechet + 1 if (c+2)%2!= 0 else nechet) + f(c*2,e,nechet + 1 if (c*2)%2!= 0 else nechet)

print(f(2,40, 0))