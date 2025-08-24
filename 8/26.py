from itertools import *

k = 0
for x in product("01234", repeat=6):
    s = "".join(x)
    if s[0] != '0' and s[0] != '1' and s[-1] != '3' and s[-1] != '4':
        k += 1
print(k)
# 5625