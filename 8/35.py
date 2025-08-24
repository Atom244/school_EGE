from itertools import *

k = 0
for x in product(sorted("ЛЕМУР"), repeat=4):
    s = "".join(x)
    k += 1
    if s[0] == "Л":
        print(k, s)
        break
# 126