from math import *

for dop in range(1, 1000):
    kod = 10 + 8190
    char = ceil( log2(kod) )
    num = ceil( char*303/8 )
    user = num + dop

    if 101*user <= 101 * 1024:
        print(dop)

# 493