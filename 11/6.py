from math import *
m = []
for kod in range(1, 1000):
    char = ceil( log2(kod) )
    idd = ceil((char * 1231) / 8)

    if idd * 523872 >= 432 * 2**20:
        m+=[kod]

print(min(m))

# 33