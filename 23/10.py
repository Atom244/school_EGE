# с подсчётом шагов (минимальное)
from functools import lru_cache

@lru_cache(None)
def f(curr, end, step):
    if curr > end: return 10**8
    if curr == end: return step
    if curr < end: return min(f(curr+1, end, step+1), f(curr+5, end, step+1), f(curr*3, end, step+1))

print(f(1,227, 0))