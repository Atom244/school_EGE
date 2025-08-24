from itertools import *

k = 0
for x in permutations("АБИКОЛУН"):
    s = "".join(x)
    s = s.replace("Б", "К").replace("Л", "К").replace("Н", "К")\
        .replace("А", "О").replace("И", "О").replace("У", "О")
    if "КК" not in s and "ОО" not in s:
        k += 1
print(k)
# 1152