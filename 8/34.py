from itertools import *

k = 0
for x in set(permutations("МИМИКРИЯ")):
    s = "".join(x)
    k += 1
print(k)
# 3360
