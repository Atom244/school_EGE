from itertools import *

k = 0
for x in product("ГЕПАРД", repeat=5):
    s = "".join(x)
    if s[0] != "А" and s[-1] != "Е" and s.count("Г") == 1:
        k += 1
print(k)
# 2200