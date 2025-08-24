from itertools import *

k = 0
for x in product(sorted("МАРИЯ"), repeat=4):
    s = ''.join(x)
    k += 1
    if k == 211:
        print(k, s)
# ИРМА