from itertools import *

tab = '235 14 17 256 147 47 356'.split()
pic ='bd bf bc de ce cg ea fg ga'.split()

print(*range(1,8))

for var in permutations('abcdefg'):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x,y in pic):
        print(*var)