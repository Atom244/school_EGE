from itertools import *

k = 0
for x in product("WXYZ", "ABC", "ABC", "ABC", "ABC", "WXYZ"):
    s = ''.join(x)
    k += 1
print(k)
# 1296