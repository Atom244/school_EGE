from itertools import *
k = 0
for x in product("КРСЛ","КРЕСЛО","КРЕСЛО","ЕО"):
    s = ''.join(x)
    k += 1
print(k)
# 288