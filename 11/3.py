from math import *

kod = 4090 + 10
char = ceil(log2(kod))
v1 = ceil((101 * char) / 8)
v2048 = ceil((v1 * 2048) / 2**10)


print(char)
print(v2048)