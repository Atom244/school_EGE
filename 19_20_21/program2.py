# число ходов до победы п1в2п3в4п5в6п7в8 и тд 0=win
from functools import lru_cache


def moves(s):
    return s+2, s+4, s*2

@lru_cache(None)
def game(s):
    if s >= 125: return 0
    if any(game(i)==0 for i in moves(s)): return 1
    if all(game(i)==1 for i in moves(s)): return 2
    if any(game(i)==2 for i in moves(s)): return 3
    if all(game(i) in [1, 3] for i in moves(s)): return 4

print(19,[s for s in range(1,125) if game(s)==2])
print(19,[s for s in range(1,125) if game(s)==3])
print(19,[s for s in range(1,125) if game(s)==4])