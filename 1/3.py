from itertools import *

tab = '245 135 26 156 124 34'.split()
pic ='bc ba cd df fa de fe ae '.split()

print(*range(1,7))

for var in permutations('abcdef'):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x,y in pic):
        print(*var)