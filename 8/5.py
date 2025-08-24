from itertools import *

k = 0

for i in range(4, 6+1):
    for x in product("АНИМЕ", repeat=i):
        s = ''.join(x)
        print(s)
        k += 1
print(k)

# АЛЬТЕРНАТИВА (ОТ КЕГЭ):
'''
k = 0

for x in product("АНИМЕ", repeat=4):
    s = ''.join(x)
    k += 1

for x in product("АНИМЕ", repeat=5):
    s = ''.join(x)
    k += 1

for x in product("АНИМЕ", repeat=6):
    s = ''.join(x)
    k += 1

print(k)
'''

# 19375