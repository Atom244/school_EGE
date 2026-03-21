from itertools import *

tab = '347 3456 1245 1237 236 25 14'.split()
pic ='ba bc ac ad cd ce df de fg fe eg'.split()

print(*range(1,8))

for var in permutations('abcdefg'):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x,y in pic):
        print(*var)