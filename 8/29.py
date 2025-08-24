from itertools import *

k = 0
for x in product("ABCD", repeat=4):
    s = "".join(x)
    if s[0]<=s[1]<=s[2]<=s[3]:
        k += 1
print(k)
# 35