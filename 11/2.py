from math import *

kod = 10 + 26 + 26
char = ceil(log2(kod))
pas = ceil((10 * char) / 8)

user = 870 / 30

print(user - pas)