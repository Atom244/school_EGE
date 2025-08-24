from itertools import *

k = 0
for x in product("КРОТ", repeat=6):
    s = ''.join(x)
    if s.count("О") == 1:
        print(s)
        k += 1

print(k)

# 1458