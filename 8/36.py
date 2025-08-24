from itertools import *

k = 0
l = 0
for x in product(sorted("АЛГОРИТМ"), repeat=4):
    s = "".join(x)
    k += 1
    if s[-2] == "И" and s [-1] == "М":
        l = k
print(l)
# 4053