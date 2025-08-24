from itertools import *

k = 0
for x in permutations("01234567", 5):
    s = "".join(x)
    if "1" not in s and s[0] != '0':
        s = s.replace("2", "0").replace("4", "0").replace("6", "0")\
            .replace("1", "3").replace("5", "3").replace("7", "3")
        if "00" not in s and "33" not in s:
            k += 1
print(k)
# 180