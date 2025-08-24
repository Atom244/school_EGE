from itertools import *

k = 0
for x in set(product("AB123", repeat=8)):
    s = "".join(x)
    if s.count("A") + s.count("B") == 2:
        k += 1
print(k)
# 81648