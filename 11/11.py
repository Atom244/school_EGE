from math import *

for alph in range(1, 10000):
    char =  ceil(log2(alph))
    idd = ceil(char*80/8)

    if idd * 1200 <= 150 * 2**10:
        print(alph)

# 4096