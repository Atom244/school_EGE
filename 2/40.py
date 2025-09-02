from itertools import *

def f(x,y,z,w):
    return (x == y) <= (z == w)

table = [(0,0,0,1),
         (1,1,1,0)]
k = 0
for p in permutations('xyzw'):
    if [f(**dict(zip(p,row))) for row in table] == [0,0]:
        k += 1
        print(p)
print(k)