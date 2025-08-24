from itertools import *

k = 0
for x in product(sorted("МАРИЯ"), repeat=4):
    s = ''.join(x)
    k += 1
    if s == "АРИЯ":
        print(k, s)
# 85