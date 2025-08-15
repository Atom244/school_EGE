from math import *

for alph in range(1, 1000):
    char = ceil(log2(alph))
    idd = ceil(char*261/8)
    if idd * 252500 >= 31 * 2**20:
        print(alph)

# 9