from  itertools import *

comb = []
for p in product('13579',repeat=3):
    comb.append(''.join(p))


ans = []
for a1 in '0123456789':
    for a2 in comb:
        n = int(f'71{a2}39{a1}28')
        if n%2024==0:
            ans.append(n)
for x in sorted(ans):
    print(x,x//2024)