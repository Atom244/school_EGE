from math import *

for n in range(1, 1000):
    kod = 10 + 26*2 + 450
    char = ceil(log2(kod))
    idd = ceil(char*n/8)
    if idd * 708 >= 213 * 2**10:
        print(n) 

# 274