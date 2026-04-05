# обощенный program2
from functools import lru_cache


def moves(s):
    return s+2, s+4, s*2

@lru_cache(None)
def game(s):
    if s >= 125: return 0
    m = [game(i) for i in moves(s)]
    m0 = [i for i in m if i%2==0]
    if len(m0)>0: return min(m0)+1
    else: return max(m)+1

print(19,[s for s in range(1,125) if game(s)==2])
print(19,[s for s in range(1,125) if game(s)==3])
print(19,[s for s in range(1,125) if game(s)==4])