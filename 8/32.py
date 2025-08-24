from itertools import *

k = 0
for x in permutations("ДЕЙКСТРА", 6):
    s = "".join(x)
    if s.count("Й") == 1 and any(sub in s for sub in ["ЙД", "ЙК", "ЙС", "ЙТ","ЙР"]):
        k += 1
print(k)
# 9000