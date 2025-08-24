from itertools import *

k = 0
for x in product("САЛО", repeat = 6):
    s = ''.join(x)
    if s.count("О") <= 3 and s.count("О") != 0:
        k += 1
print(k)
# 3213 ВНИМАНИЕ НА УСЛОВИЕ !!!!! 