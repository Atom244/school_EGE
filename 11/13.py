from math import *
lst = []
for dop in range(1, 1000):
    alph = 10 + 510
    char = ceil(log2(alph))
    idd = ceil(char*99/8)
    if (idd + dop) * 4322 >= 543 * 2**10:
        lst+=[dop]

print(min(lst))

# 5