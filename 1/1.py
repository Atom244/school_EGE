from itertools import *

tab = '56 378 26 68 17 134 258 247'.split() # цифры по табам
pic ='cf ca cb fd ab ag be ed dh gh'.split() # все пути

print(*range(1,9))

for var in permutations('abcdefgh'):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x,y in pic):
        print(*var)

