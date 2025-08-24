from itertools import *

k = 0
for x in product("КМ", "КУМА","КУМА","КУМА","УА"):
    s = ''.join(x)
    k += 1
print(k)

# 256