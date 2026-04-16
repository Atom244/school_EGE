from itertools import *

comb = []
for l in 0,1,2:
    for p in product('13579',repeat=l):
        comb.append(''.join(p))

ans = []
for a1 in comb:
    for a2 in comb:
        for a3 in '02468':
            n = int(f'1{a1}2{a3}3{a2}45')
            if n>10**8:
                break
            if n%153==0:
                ans.append(n)

for x in sorted(ans):
    print(x,x//153)