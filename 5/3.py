from itertools import *

for n in range(100,1000):
    l = []
    for p in product(str(n), repeat=2):
        if p[0] != p[1] and p[0] != '0':
            s = ''.join(p)
            l.append(int(s))
    if l:
        r = max(l) - min(l)
        if r == 35:
            print(n, r)

# или как кабанов
'''
for n in range(100,1000):
    d = str(n)
    a = [d[0] + d[1], d[0] + d[2], d[1] + d[0], d[1] + d[2], d[2] + d[0], d[2] + d[1]]
    a = [int(x) for x in a if x[0] != '0']
    r = max(a) - min(a)
    if r == 35:
        print(n, r)
'''