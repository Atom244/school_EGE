from math import *

for n in range(1, 1000):
    kod = 10 + 52 + 458
    char = ceil(log2(kod))
    num = ceil(n * char / 8)
    if num * 862 <= 276 * 2**10:
        print(n)

# 261