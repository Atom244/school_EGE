from itertools import *

comb = []
for l in 0,1,2,3:
    for p in product('02468',repeat=l):
        comb.append(''.join(p))

ans = []
for a1 in '13579':
    for a2 in '13579':
        for a in comb:
            n = int(f'20{a1}{a2}22{a}')
            if n > 10**10:
                break
            if n % 10980 == 0:
                ans.append(n)

for x in sorted(ans):
    print(x,x//10980)