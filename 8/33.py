from itertools import *

k = 0
for x in permutations("ВАЙФУ", 4):
    s = ''. join(x)
    if s[0] != "Й" and "ВФ" not in s and "ФВ" not in s:
        k += 1
print(k)
# 68