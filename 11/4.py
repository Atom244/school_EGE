from math import *

kod = 26 + 26
char = ceil(log2(kod))
pas = ceil( 7*char/8 )
user = pas + 12

for k in range(2, 1000):
    if user * k <= 2048:
        print(k)

# 113