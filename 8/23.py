from itertools import *

k = 0
for x in permutations("ИГРОК"):
    s = ''.join(x)
    if s[0] != "К" and "РОК" not in s:
        k += 1
print(k)
# 90