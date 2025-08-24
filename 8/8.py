from itertools import *

k = 0


for x in product("БЕРКЛИЙ", repeat = 4):
    s = ''.join(x)
    if s[0] != "Й" and ('Е' in s or 'И' in s):
        print(s)
        k += 1

print(k)

# 1558