from itertools import *

k = 0
for x in product("КАТЕР", repeat = 3):
    s = ''.join(x)
    if s.count("Р") >= 2:
        print(s)
        k += 1
print(k)

# 13