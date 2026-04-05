from functools import lru_cache

@lru_cache(None)
def f(s,m):
    if m < 0: return 0
    if s >= 65: return m%2 == 0
    if m%2 != 0:
        return any([f(s + 1,m-1), f(s + 2, m-1), f(s*3,m-1)])
    if m%2 == 0:
        return all([f(s + 1, m - 1), f(s + 2, m - 1), f(s * 3, m - 1)])

print([s for s in range(1,65) if f(s,2)])
print([s for s in range(1,65) if (not f(s,1)) and f(s,3)])