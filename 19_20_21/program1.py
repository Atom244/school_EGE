from functools import lru_cache


def moves(s):
    return s+2, s+4, s*2

@lru_cache(None)
def game(s):
    if s >= 125: return 'w'
    if any(game(i)=='w' for i in moves(s)): return 'p1'
    if all(game(i)=='p1' for i in moves(s)): return 'v1'
    if any(game(i)=='v1' for i in moves(s)): return 'p2'
    if all(game(i) in ['p1', 'p2'] for i in moves(s)): return 'v2'

print(19,[s for s in range(1,125) if game(s)=='v1'])
print(19,[s for s in range(1,125) if game(s)=='p2'])
print(19,[s for s in range(1,125) if game(s)=='v2'])